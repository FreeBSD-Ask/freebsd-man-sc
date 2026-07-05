# bpf.4

`bpf` — Berkeley 数据包过滤器

## 名称

`bpf`

## 概要

`device bpf`

## 描述

Berkeley 数据包过滤器以协议无关的方式为数据链路层提供原始接口。网络上的所有数据包，甚至那些发往其他主机的数据包，都可以通过此机制访问。

数据包过滤器呈现为字符特殊设备 **/dev/bpf**。打开该设备后，必须使用 `BIOCSETIF` ioctl 将文件描述符绑定到特定的网络接口。一个给定接口可由多个监听者共享，每个描述符底层的过滤器将看到相同的数据包流。

每个 `bpf` 文件的每个打开实例都关联着一个用户可设置的包过滤器。当接口收到数据包时，所有在该接口上监听的文件描述符都会应用其过滤器。每个接受该数据包的描述符都会获得自己的副本。

通过写入 `bpf` 文件描述符可以将数据包发送到网络上。写入是无缓冲的，这意味着每次写入只能处理一个数据包。目前仅支持对以太网和 SLIP 链路的写入。

## 缓冲模式

`bpf` 设备通过应用程序提供的内存缓冲区向应用程序传递数据包数据。缓冲模式使用 `BIOCSETBUFMODE` ioctl 设置，使用 `BIOCGETBUFMODE` ioctl 读取。

### 缓冲读取模式

默认情况下，`bpf` 设备以 `BPF_BUFMODE_BUFFER` 模式运行，在此模式下，数据包数据通过 read(2) 系统调用从内核内存显式复制到用户内存。用户进程将声明一个固定缓冲区大小，该大小既用于调整内部缓冲区大小，也用于该文件上的所有 read(2) 操作。此大小通过 `BIOCGBLEN` ioctl 查询，通过 `BIOCSBLEN` ioctl 设置。注意，大于缓冲区大小的单个数据包必然会被截断。

### 零拷贝缓冲模式

`bpf` 设备还可以以 `BPF_BUFMODE_ZEROCOPY` 模式运行，在此模式下，数据包数据由内核直接写入两个用户内存缓冲区，避免系统调用和复制开销。缓冲区为固定（且相等）大小、页对齐，且为页大小的偶数倍。最大零拷贝缓冲区大小由 `BIOCGETZMAX` ioctl 返回。注意，大于缓冲区大小的单个数据包必然会被截断。

用户进程使用 `BIOCSETZBUF` ioctl 注册两个内存缓冲区，该 ioctl 接受一个指向 `struct bpf_zbuf` 的指针作为参数：

```sh
struct bpf_zbuf {
	void *bz_bufa;
	void *bz_bufb;
	size_t bz_buflen;
};
```

`bz_bufa` 是指向第一个将被填充的缓冲区的用户空间地址的指针，`bz_bufb` 是指向第二个缓冲区的指针。`bpf` 随后将在两个缓冲区之间循环，随着它们的填充和确认而切换。

每个缓冲区以一个固定长度的头部开始，用于保存缓冲区的同步和数据长度信息：

```sh
struct bpf_zbuf_header {
	volatile u_int  bzh_kernel_gen;	/* 内核生成号 */
	volatile u_int  bzh_kernel_len;	/* 缓冲区中数据的长度 */
	volatile u_int  bzh_user_gen;	/* 用户生成号 */
	/* ...为将来使用而填充... */
};
```

每个缓冲区的头部结构（包括所有填充）在使用 `BIOCSETZBUF` 配置之前应清零。缓冲区中的剩余空间将由内核用于存储数据包数据，其布局格式与缓冲读取模式相同。

内核和用户进程通过缓冲区头部遵循一个简单的确认协议来同步对缓冲区的访问：当头部生成号 `bzh_kernel_gen` 和 `bzh_user_gen` 持有相同的值时，内核拥有该缓冲区；当它们不同时，用户空间拥有该缓冲区。

当内核拥有缓冲区时，其内容不稳定且可能异步变化；当用户进程拥有缓冲区时，其内容稳定，且在被确认之前不会改变。

在注册缓冲区之前将缓冲区头部全部初始化为 0 的效果是将两个缓冲区的初始所有权分配给内核。内核通过修改 `bzh_kernel_gen` 来发出缓冲区已分配给用户空间的信号，用户空间通过将 `bzh_user_gen` 的值设置为 `bzh_kernel_gen` 的值来确认缓冲区并将其返回给内核。

为避免缓存和内存重排序效应，用户进程在检查和确认缓冲区时必须使用原子操作和内存屏障：

```sh
#include <machine/atomic.h>
/*
 * 将缓冲区的所有权返回给内核以供重用。
 */
static void
buffer_acknowledge(struct bpf_zbuf_header *bzh)
{
	atomic_store_rel_int(&bzh->bzh_user_gen, bzh->bzh_kernel_gen);
}
/*
 * 检查内核是否已将缓冲区分配给用户空间。
 * 如果用户空间拥有该缓冲区则返回 true，否则返回 false。
 */
static int
buffer_check(struct bpf_zbuf_header *bzh)
{
	return (bzh->bzh_user_gen !=
	    atomic_load_acq_int(&bzh->bzh_kernel_gen));
}
```

用户进程可使用 `BIOCROTZBUF` ioctl 强制将下一个缓冲区（如果有待处理数据）分配给用户空间。这允许用户进程在缓冲区未满之前检索部分填充缓冲区中的数据，例如在超时之后；进程必须使用头部生成号重新检查缓冲区所有权，因为如果没有数据存在，缓冲区将不会被分配给用户空间。

与缓冲读取模式一样，可使用 kqueue(2)、poll(2) 和 select(2) 来睡眠等待已完成缓冲区的可用性。当下一个缓冲区的所有权分配给用户空间时，它们将返回一个可读的文件描述符。

在当前实现中，内核可能将零个、一个或两个缓冲区分配给用户进程；然而，较早的实现维持了至多一次只能将一个缓冲区分配给用户进程的不变量。为确保进展和高性能，用户进程应尽快确认已完全处理的缓冲区，将其返回以供重用，且不应在持有另一个缓冲区时阻塞等待第二个缓冲区。

## IOCTLS

以下 ioctl(2) 命令码定义于

`#include <net/bpf.h>`

所有命令都需要这些头文件：

```sh
	#include <sys/types.h>
	#include <sys/time.h>
	#include <sys/ioctl.h>
	#include <net/bpf.h>
```

此外，`BIOCGETIF` 和 `BIOCSETIF` 需要

`#include <sys/socket.h>`

和

`#include <net/if.h>`

除 `FIONREAD` 外，以下命令可应用于任何打开的 `bpf` 文件。ioctl(2) 的（第三个）参数应是指向所示类型的指针。

`#include <net/bpf.h>`

```sh
struct bpf_dltlist {
	u_int bfl_len;
	u_int *bfl_list;
};
```

```sh
struct bpf_stat {
	u_int bs_recv;    /* 收到的数据包数 */
	u_int bs_drop;    /* 丢弃的数据包数 */
};
```

**`bs_recv`** 描述符自打开或重置以来收到的数据包数（包括自上次读取调用以来缓冲的任何数据包）；以及

**`bs_drop`** 被过滤器接受但由内核因缓冲区溢出而丢弃的数据包数（即应用程序的读取未能跟上数据包流量）。

```sh
struct bpf_program {
	u_int bf_len;
	struct bpf_insn *bf_insns;
};
```

```sh
struct bpf_version {
        u_short bv_major;
        u_short bv_minor;
};
```

`#include <net/bpf.h>`

**`BIOCGETIFLIST`** （`struct bpf_iflist`）返回可用监听点列表，稍后可使用 `BIOCSETIF` 附加。入口处 `bi_ubuf` 应指向用户提供的缓冲区。`bi_size` 应指定缓冲区长度，或为 0（如果该请求用于确定所需长度）。`bi_count` 可用于将输出限制为前 `count` 项，否则应为 0。返回时，如果缓冲区长度足以容纳所有所需条目，则所提供的缓冲区将以 NUL 结尾的可用监听点名称填充，并将 `bi_count` 设置为已复制名称的数量。否则返回 Er ENOSPC。

**`BIOCGBLEN`** （`u_int`）返回 `bpf` 文件读取所需的缓冲区长度。

**`BIOCSBLEN`** （`u_int`）设置 `bpf` 文件读取的缓冲区长度。在使用 `BIOCSETIF` 将文件附加到接口之前必须设置缓冲区。如果无法满足所请求的缓冲区大小，将设置并返回最接近的允许大小。如果传递给它的缓冲区不是此大小，read 调用将返回 Er EINVAL。

**`BIOCGDLT`** （`u_int`）返回所附加接口底层数据链路层的类型。如果未指定接口，则返回 Er EINVAL。以“`DLT_`”为前缀的设备类型定义于

**`BIOCGDLTLIST`** （`struct bpf_dltlist`）返回所附加接口底层数据链路层可用类型的数组：可用类型在 `bfl_list` 字段指向的数组中返回，而其以 u_int 为单位的长度由 `bfl_len` 字段提供。如果缓冲区空间不足，返回 Er ENOMEM；如果遇到错误地址，返回 Er EFAULT。返回时 `bfl_len` 字段被修改以指示返回数组的实际长度（以 u_int 为单位）。如果 `bfl_list` 为 `NULL`，则 `bfl_len` 字段被设置为指示所需数组长度（以 u_int 为单位）。

**`BIOCSDLT`** （`u_int`）更改所附加接口底层数据链路层的类型。如果未指定接口或指定类型对该接口不可用，则返回 Er EINVAL。

**`BIOCPROMISC`** 强制接口进入混杂模式。所有数据包（不仅仅是发往本地主机的那些）都会被处理。由于多个文件可在给定接口上监听，以非混杂方式打开其接口的监听者可能收到混杂方式接收的数据包。此问题可通过适当的过滤器解决。接口将保持混杂模式，直到所有以混杂方式监听的文件都被关闭。

**`BIOCFLUSH`** 刷新传入数据包缓冲区，并重置由 BIOCGSTATS 返回的统计信息。

**`BIOCGETIF`** （`struct ifreq`）返回文件正在监听的硬件接口的名称。名称在 `ifreq` 结构的 ifr_name 字段中返回。所有其他字段均未定义。

**`BIOCSETIF`** （`struct ifreq`）设置与文件关联的硬件接口。必须执行此命令才能读取任何数据包。使用 `ifreq` 结构的 `ifr_name` 字段按名称指示设备。此外，执行 `BIOCFLUSH` 的操作。

**`BIOCSRTIMEOUT`**

**`BIOCGRTIMEOUT`** （`struct timeval`）设置或获取读取超时参数。参数指定读取请求超时前等待的时间长度。此参数由 open(2) 初始化为零，表示无超时。

**`BIOCGSTATS`** （`struct bpf_stat`）返回以下数据包统计信息结构：字段为：

**`BIOCIMMEDIATE`** （`u_int`）根据参数的真值启用或禁用“立即模式”。启用立即模式时，读取在收到数据包后立即返回。否则，读取将阻塞直到内核缓冲区变满或发生超时。这对于 [rarpd(8)](../man8/rarpd.8.md) 等必须实时响应消息的程序很有用。新文件的默认值为关闭。

**`BIOCSETF`**

**`BIOCSETFNR`** （`struct bpf_program`）设置内核用于丢弃不感兴趣数据包的读取过滤程序。指令数组及其长度通过以下结构传入：过滤程序由 `bf_insns` 字段指向，其以“`struct bpf_insn`”为单位的长度由 `bf_len` 字段给出。有关过滤语言的解释，请参见 Sx FILTER MACHINE 节。`BIOCSETF` 和 `BIOCSETFNR` 之间唯一的区别是 `BIOCSETF` 执行 `BIOCFLUSH` 的操作，而 `BIOCSETFNR` 不执行。

**`BIOCSETWF`** （`struct bpf_program`）设置内核用于控制可将何种类型的数据包写入接口的写入过滤程序。有关 `bpf` 过滤程序的更多信息，请参见 `BIOCSETF` 命令。

**`BIOCVERSION`** （`struct bpf_version`）返回内核当前识别的过滤语言的主版本号和次版本号。在安装过滤器之前，应用程序必须检查当前版本是否与运行中的内核兼容。如果主版本号匹配且应用程序的次版本号小于或等于内核的次版本号，则版本号兼容。内核版本号在以下结构中返回：当前版本号由 `BPF_MAJOR_VERSION` 和 `BPF_MINOR_VERSION` 给出。不兼容的过滤器可能导致未定义行为（最可能是 Fn ioctl 返回错误或随意的包匹配）。

**`BIOCGRSIG`**

**`BIOCSRSIG`** （`u_int`）设置或获取接收信号。此信号将发送到由 `FIOSETOWN` 指定的进程或进程组。默认为 `SIGIO`。

**`BIOCSHDRCMPLT`**

**`BIOCGHDRCMPLT`** （`u_int`）设置或获取“header complete”标志的状态。如果链接层源地址应由接口输出例程自动填入，则设置为零。如果链接层源地址将按提供的那样写入到线路上，则设置为一。此标志默认初始化为零。

**`BIOCSSEESENT`**

**`BIOCGSEESENT`** （`u_int`）这些命令已过时，但为兼容性而保留。请改用 `BIOCSDIRECTION` 和 `BIOCGDIRECTION`。设置或获取决定接口上本地生成的数据包是否应由 BPF 返回的标志。设置为零以仅查看接口上的传入数据包。设置为一以查看接口上本地和远程生成的数据包。此标志默认初始化为一。

**`BIOCSDIRECTION`**

**`BIOCGDIRECTION`** （`u_int`）设置或获取决定接口上的传入、传出或所有数据包是否应由 BPF 返回的设置。设置为 `BPF_D_IN` 以仅查看接口上的传入数据包。设置为 `BPF_D_INOUT` 以查看接口上本地和远程生成的数据包。设置为 `BPF_D_OUT` 以仅查看接口上的传出数据包。此设置默认初始化为 `BPF_D_INOUT`。

**`BIOCSTSTAMP`**

**`BIOCGTSTAMP`** （`u_int`）设置或获取 BPF 返回的时间戳的格式和分辨率。设置为 `BPF_T_MICROTIME`、`BPF_T_MICROTIME_FAST`、`BPF_T_MICROTIME_MONOTONIC` 或 `BPF_T_MICROTIME_MONOTONIC_FAST` 以获取 64 位 `struct timeval` 格式的时间戳。设置为 `BPF_T_NANOTIME`、`BPF_T_NANOTIME_FAST`、`BPF_T_NANOTIME_MONOTONIC` 或 `BPF_T_NANOTIME_MONOTONIC_FAST` 以获取 64 位 `struct timespec` 格式的时间戳。设置为 `BPF_T_BINTIME`、`BPF_T_BINTIME_FAST`、`BPF_T_NANOTIME_MONOTONIC` 或 `BPF_T_BINTIME_MONOTONIC_FAST` 以获取 64 位 `struct bintime` 格式的时间戳。设置为 `BPF_T_NONE` 以忽略时间戳。所有 64 位时间戳格式都封装在 `struct bpf_ts` 中。`BPF_T_MICROTIME_FAST`、`BPF_T_NANOTIME_FAST`、`BPF_T_BINTIME_FAST`、`BPF_T_MICROTIME_MONOTONIC_FAST`、`BPF_T_NANOTIME_MONOTONIC_FAST` 和 `BPF_T_BINTIME_MONOTONIC_FAST` 是不带 _FAST 后缀的相应格式的类似版本，但不执行完整的时间计数器查询，因此其精度为一个定时器节拍。`BPF_T_MICROTIME_MONOTONIC`、`BPF_T_NANOTIME_MONOTONIC`、`BPF_T_BINTIME_MONOTONIC`、`BPF_T_MICROTIME_MONOTONIC_FAST`、`BPF_T_NANOTIME_MONOTONIC_FAST` 和 `BPF_T_BINTIME_MONOTONIC_FAST` 存储自内核引导以来经过的时间。此设置默认初始化为 `BPF_T_MICROTIME`。

**`BIOCFEEDBACK`** （`u_int`）设置数据包反馈模式。这允许在通过接口输出成功时将注入的数据包作为输入反馈给接口。当设置了 `BPF_D_INOUT` 方向时，注入的传出数据包不会被 BPF 返回以避免重复。此标志默认初始化为零。

**`BIOCLOCK`** 在 `bpf` 描述符上设置锁定标志。这防止执行可能更改设备底层操作参数的 ioctl 命令。

**`BIOCGETBUFMODE`**

**`BIOCSETBUFMODE`** （`u_int`）获取或设置当前 `bpf` 缓冲模式；可能的值为 `BPF_BUFMODE_BUFFER`（缓冲读取模式）和 `BPF_BUFMODE_ZBUF`（零拷贝缓冲模式）。

**`BIOCSETZBUF`** （`struct bpf_zbuf`）设置当前零拷贝缓冲区位置；只有在选择了零拷贝缓冲模式之后、在附加到接口之前才能设置缓冲区位置。缓冲区必须大小相同、页对齐，且大小为页的整数倍。必须填写 `bz_bufa`、`bz_bufb` 和 `bz_buflen` 三个字段。如果已为此设备设置了缓冲区，则 ioctl 将失败。

**`BIOCGETZMAX`** （`size_t`）获取允许的最大单个零拷贝缓冲区大小。由于零拷贝缓冲模式使用两个缓冲区，限制（实际上）是返回大小的两倍。由于零拷贝缓冲区消耗内核地址空间，建议保守选择缓冲区大小，尤其是在 32 位系统上使用多个 `bpf` 描述符时。

**`BIOCROTZBUF`** 强制将下一个缓冲区的所有权分配给用户空间（如果缓冲区中存在任何数据）。如果不存在数据，缓冲区将仍由内核拥有。这允许零拷贝缓冲的使用者实现超时并检索部分填充的缓冲区。为处理缓冲区中不存在数据因此未分配所有权的情况，用户进程必须对照 `bzh_user_gen` 检查 `bzh_kernel_gen`。

**`BIOCSETVLANPCP`** 将 VLAN PCP 位设置为所提供的值。

## 标准 IOCTLS

`bpf` 现在支持多个标准 ioctl(2)，允许用户对打开的 *bpf* 文件描述符进行异步和/或非阻塞 I/O。

**`FIONREAD`** （`int`）返回立即可读取的字节数。

**`SIOCGIFADDR`** （`struct ifreq`）返回与接口关联的地址。

**`FIONBIO`** （`int`）设置或清除非阻塞 I/O。如果 arg 为非零，则在无数据可用时执行 read(2) 将返回 -1 且 `errno` 将设置为 Er EAGAIN。如果 arg 为零，则禁用非阻塞 I/O。注意：设置此项会覆盖由 `BIOCSRTIMEOUT` 设置的超时。

**`FIOASYNC`** （`int`）启用或禁用异步 I/O。启用时（arg 为非零），当数据包到达时，由 `FIOSETOWN` 指定的进程或进程组将开始接收 `SIGIO`。注意，必须执行 `FIOSETOWN` 才能使其生效，因为系统不会为你默认设置。信号可通过 `BIOCSRSIG` 更改。

**`FIOSETOWN`**

**`FIOGETOWN`** （`int`）设置或获取在数据包可用时应接收 `SIGIO` 的进程或进程组（如果为负）。信号可使用 `BIOCSRSIG` 更改（参见上文）。

## BPF 头部

以下结构之一会前置于由 read(2) 返回或通过零拷贝缓冲区返回的每个数据包：

```sh
struct bpf_xhdr {
	struct bpf_ts	bh_tstamp;     /* 时间戳 */
	uint32_t	bh_caplen;     /* 捕获部分的长度 */
	uint32_t	bh_datalen;    /* 数据包的原始长度 */
	u_short		bh_hdrlen;     /* bpf 头部的长度（此结构
					  加对齐填充） */
};
struct bpf_hdr {
	struct timeval	bh_tstamp;     /* 时间戳 */
	uint32_t	bh_caplen;     /* 捕获部分的长度 */
	uint32_t	bh_datalen;    /* 数据包的原始长度 */
	u_short		bh_hdrlen;     /* bpf 头部的长度（此结构
					  加对齐填充） */
};
```

各字段的值以主机字节序存储，分别为：

**`bh_tstamp`** 数据包被数据包过滤器处理的时间。
**`bh_caplen`** 数据包捕获部分的长度。这是过滤器指定的截断量与数据包长度中的较小值。
**`bh_datalen`** 来自线路的数据包长度。此值独立于过滤器指定的截断量。
**`bh_hdrlen`** `bpf` 头部的长度，可能不等于 Fn sizeof struct bpf_xhdr 或 Fn sizeof struct bpf_hdr。

`bh_hdrlen` 字段的存在是为了考虑头部和链路层协议之间的填充。其目的是保证数据包数据结构的正确对齐，这在敏感对齐的体系结构上是必需的，并在许多其他体系结构上提高性能。数据包过滤器确保 `bpf_xhdr`、`bpf_hdr` 和网络层头部将是字对齐的。目前，出于向后兼容的原因，当时间戳设置为 `BPF_T_MICROTIME`、`BPF_T_MICROTIME_FAST`、`BPF_T_MICROTIME_MONOTONIC`、`BPF_T_MICROTIME_MONOTONIC_FAST` 或 `BPF_T_NONE` 时使用 `bpf_hdr`。否则使用 `bpf_xhdr`。然而，`bpf_hdr` 可能会在不久的将来被弃用。在对齐受限的机器上访问链路层协议字段时必须采取适当的预防措施。（这在以太网上不是问题，因为类型字段是位于偶数偏移量上的 short，地址可能以字节方式访问。）

此外，单个数据包会被填充，使每个数据包从字边界开始。这要求应用程序对如何从一个数据包前进到下一个数据包有所了解。宏 `BPF_WORDALIGN` 定义于

`#include <net/bpf.h>`

以促进此过程。它将其参数向上舍入到最近的字对齐值（其中一个字为 `BPF_ALIGNMENT` 字节宽）。

例如，如果“`p`”指向一个数据包的起始位置，此表达式将其前进到下一个数据包：

```sh
p = (char *)p + BPF_WORDALIGN(p->bh_hdrlen + p->bh_caplen)
```

为使对齐机制正常工作，传递给 read(2) 的缓冲区本身必须是字对齐的。malloc(3) 函数将始终返回对齐的缓冲区。

## 过滤器机器

过滤程序是一个指令数组，所有分支都向前定向，以 *return* 指令终止。每条指令对伪机器状态执行某种操作，该状态由累加器、索引寄存器、暂存存储器和隐式程序计数器组成。

以下结构定义了指令格式：

```sh
struct bpf_insn {
	u_short     code;
	u_char      jt;
	u_char      jf;
	bpf_u_int32 k;
};
```

`k` 字段在不同指令中以不同方式使用，`jt` 和 `jf` 字段被分支指令用作偏移量。操作码以半分层方式编码。有八类指令：`BPF_LD`、`BPF_LDX`、`BPF_ST`、`BPF_STX`、`BPF_ALU`、`BPF_JMP`、`BPF_RET` 和 `BPF_MISC`。各种其他模式和操作符位与类进行或运算以给出实际指令。类和模式定义于

`#include <net/bpf.h>`

以下是每个定义的 `bpf` 指令的语义。我们使用以下约定：A 是累加器，X 是索引寄存器，P[] 是数据包数据，M[] 是暂存存储器。P[i:n] 给出数据包中字节偏移“i”处的数据，解释为字（n=4）、无符号半字（n=2）或无符号字节（n=1）。M[i] 给出暂存存储器中第 i 个字，仅以字单位寻址。存储器的索引范围为 0 到 `BPF_MEMWORDS` - 1。`k`、`jt` 和 `jf` 是指令定义中的相应字段。“len”指数据包的长度。

```sh
BPF_LD+BPF_W+BPF_ABS	A <- P[k:4]
BPF_LD+BPF_H+BPF_ABS	A <- P[k:2]
BPF_LD+BPF_B+BPF_ABS	A <- P[k:1]
BPF_LD+BPF_W+BPF_IND	A <- P[X+k:4]
BPF_LD+BPF_H+BPF_IND	A <- P[X+k:2]
BPF_LD+BPF_B+BPF_IND	A <- P[X+k:1]
BPF_LD+BPF_W+BPF_LEN	A <- len
BPF_LD+BPF_IMM		A <- k
BPF_LD+BPF_MEM		A <- M[k]
```

```sh
BPF_LDX+BPF_W+BPF_IMM	X <- k
BPF_LDX+BPF_W+BPF_MEM	X <- M[k]
BPF_LDX+BPF_W+BPF_LEN	X <- len
BPF_LDX+BPF_B+BPF_MSH	X <- 4*(P[k:1]&0xf)
```

```sh
BPF_ST			M[k] <- A
```

```sh
BPF_STX			M[k] <- X
```

```sh
BPF_ALU+BPF_ADD+BPF_K	A <- A + k
BPF_ALU+BPF_SUB+BPF_K	A <- A - k
BPF_ALU+BPF_MUL+BPF_K	A <- A * k
BPF_ALU+BPF_DIV+BPF_K	A <- A / k
BPF_ALU+BPF_MOD+BPF_K	A <- A % k
BPF_ALU+BPF_AND+BPF_K	A <- A & k
BPF_ALU+BPF_OR+BPF_K	A <- A | k
BPF_ALU+BPF_XOR+BPF_K	A <- A ^ k
BPF_ALU+BPF_LSH+BPF_K	A <- A << k
BPF_ALU+BPF_RSH+BPF_K	A <- A >> k
BPF_ALU+BPF_ADD+BPF_X	A <- A + X
BPF_ALU+BPF_SUB+BPF_X	A <- A - X
BPF_ALU+BPF_MUL+BPF_X	A <- A * X
BPF_ALU+BPF_DIV+BPF_X	A <- A / X
BPF_ALU+BPF_MOD+BPF_X	A <- A % X
BPF_ALU+BPF_AND+BPF_X	A <- A & X
BPF_ALU+BPF_OR+BPF_X	A <- A | X
BPF_ALU+BPF_XOR+BPF_X	A <- A ^ X
BPF_ALU+BPF_LSH+BPF_X	A <- A << X
BPF_ALU+BPF_RSH+BPF_X	A <- A >> X
BPF_ALU+BPF_NEG		A <- -A
```

```sh
BPF_JMP+BPF_JA		pc += k
BPF_JMP+BPF_JGT+BPF_K	pc += (A > k) ? jt : jf
BPF_JMP+BPF_JGE+BPF_K	pc += (A >= k) ? jt : jf
BPF_JMP+BPF_JEQ+BPF_K	pc += (A == k) ? jt : jf
BPF_JMP+BPF_JSET+BPF_K	pc += (A & k) ? jt : jf
BPF_JMP+BPF_JGT+BPF_X	pc += (A > X) ? jt : jf
BPF_JMP+BPF_JGE+BPF_X	pc += (A >= X) ? jt : jf
BPF_JMP+BPF_JEQ+BPF_X	pc += (A == X) ? jt : jf
BPF_JMP+BPF_JSET+BPF_X	pc += (A & X) ? jt : jf
```

```sh
BPF_RET+BPF_A		accept A bytes
BPF_RET+BPF_K		accept k bytes
```

```sh
BPF_MISC+BPF_TAX	X <- A
BPF_MISC+BPF_TXA	A <- X
```

**`BPF_LD`** 这些指令将一个值复制到累加器中。源操作数的类型由“寻址模式”指定，可以是一个常量（`BPF_IMM`）、固定偏移处的数据包数据（`BPF_ABS`）、可变偏移处的数据包数据（`BPF_IND`）、数据包长度（`BPF_LEN`）或暂存存储器中的一个字（`BPF_MEM`）。对于 `BPF_IND` 和 `BPF_ABS`，数据大小必须指定为字（`BPF_W`）、半字（`BPF_H`）或字节（`BPF_B`）。所有已识别的 `BPF_LD` 指令的语义如下。

**`BPF_LDX`** 这些指令将一个值加载到索引寄存器中。注意，寻址模式比累加器加载更为受限，但包括 `BPF_MSH`，这是一种用于高效加载 IP 头部长度的技巧。

**`BPF_ST`** 此指令将累加器存储到暂存存储器中。我们不需要寻址模式，因为目标只有一种可能性。

**`BPF_STX`** 此指令将索引寄存器存储到暂存存储器中。

**`BPF_ALU`** alu 指令在累加器和索引寄存器或常量之间执行操作，并将结果存回累加器。对于二元操作，需要源模式（`BPF_K` 或 `BPF_X`）。

**`BPF_JMP`** 跳转指令改变控制流。条件跳转将累加器与常量（`BPF_K`）或索引寄存器（`BPF_X`）进行比较。如果结果为真（或非零），则采用真分支，否则采用假分支。跳转偏移量以 8 位编码，因此最长跳转为 256 条指令。然而，跳转始终（`BPF_JA`）操作码使用 32 位的 `k` 字段作为偏移量，允许任意远的目的地。所有条件都使用无符号比较约定。

**`BPF_RET`** 返回指令终止过滤程序并指定要接受的数据包量（即，它们返回截断量）。返回值为零表示应忽略该数据包。返回值可以是常量（`BPF_K`）或累加器（`BPF_A`）。

**`BPF_MISC`** 杂项类别是为不适合上述类别的任何内容以及可能需要添加的任何新指令而创建的。目前，这些是寄存器传输指令，将索引寄存器复制到累加器或反之亦然。

`bpf` 接口提供以下宏以促进数组初始化器：Fn BPF_STMT opcode operand 和 Fn BPF_JUMP opcode operand true_offset false_offset。

## SYSCTL 变量

一组 [sysctl(8)](../man8/sysctl.8.md) 变量控制 `bpf` 子系统的行为

**`net.bpf.optimize_writers`** : 0 各种程序使用 BPF 发送（但不接收）原始数据包（cdpd、lldpd、dhcpd、dhcp 中继等是此类程序的良好示例）。它们不需要传入数据包被发送给它们。启用此选项使新的 BPF 用户附加到只写接口列表，直到程序通过 Fn pcap_set_filter 显式指定读取过滤器。这消除了高速接口的性能下降。

**`net.bpf.stats`** : 用于检索常规统计信息的二进制接口。

**`net.bpf.zerocopy_enable`** : 0 允许将零拷贝用于 net BPF 读取器。谨慎使用。

**`net.bpf.maxinsns`** : 512 BPF 程序可包含的最大指令数。使用 [tcpdump(1)](../man1/tcpdump.1.md) `-d` 选项确定任何过滤器的近似指令数。

**`net.bpf.maxbufsize`** : 524288 为数据包缓冲区分配的最大缓冲区大小。

**`net.bpf.bufsize`** : 4096 为数据包缓冲区分配的默认缓冲区大小。

## 实例

以下过滤器取自反向 ARP 守护进程。它仅接受反向 ARP 请求。

```sh
struct bpf_insn insns[] = {
	BPF_STMT(BPF_LD+BPF_H+BPF_ABS, 12),
	BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, ETHERTYPE_REVARP, 0, 3),
	BPF_STMT(BPF_LD+BPF_H+BPF_ABS, 20),
	BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, ARPOP_REVREQUEST, 0, 1),
	BPF_STMT(BPF_RET+BPF_K, sizeof(struct ether_arp) +
		 sizeof(struct ether_header)),
	BPF_STMT(BPF_RET+BPF_K, 0),
};
```

此过滤器仅接受主机 128.3.112.15 和 128.3.112.35 之间的 IP 数据包。

```sh
struct bpf_insn insns[] = {
	BPF_STMT(BPF_LD+BPF_H+BPF_ABS, 12),
	BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, ETHERTYPE_IP, 0, 8),
	BPF_STMT(BPF_LD+BPF_W+BPF_ABS, 26),
	BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, 0x8003700f, 0, 2),
	BPF_STMT(BPF_LD+BPF_W+BPF_ABS, 30),
	BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, 0x80037023, 3, 4),
	BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, 0x80037023, 0, 3),
	BPF_STMT(BPF_LD+BPF_W+BPF_ABS, 30),
	BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, 0x8003700f, 0, 1),
	BPF_STMT(BPF_RET+BPF_K, (u_int)-1),
	BPF_STMT(BPF_RET+BPF_K, 0),
};
```

最后，此过滤器仅返回 TCP finger 数据包。我们必须解析 IP 头部以到达 TCP 头部。`BPF_JSET` 指令检查 IP 分片偏移是否为 0，以便我们确定拥有 TCP 头部。

```sh
struct bpf_insn insns[] = {
	BPF_STMT(BPF_LD+BPF_H+BPF_ABS, 12),
	BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, ETHERTYPE_IP, 0, 10),
	BPF_STMT(BPF_LD+BPF_B+BPF_ABS, 23),
	BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, IPPROTO_TCP, 0, 8),
	BPF_STMT(BPF_LD+BPF_H+BPF_ABS, 20),
	BPF_JUMP(BPF_JMP+BPF_JSET+BPF_K, 0x1fff, 6, 0),
	BPF_STMT(BPF_LDX+BPF_B+BPF_MSH, 14),
	BPF_STMT(BPF_LD+BPF_H+BPF_IND, 14),
	BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, 79, 2, 0),
	BPF_STMT(BPF_LD+BPF_H+BPF_IND, 16),
	BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, 79, 0, 1),
	BPF_STMT(BPF_RET+BPF_K, (u_int)-1),
	BPF_STMT(BPF_RET+BPF_K, 0),
};
```

## 参见

[tcpdump(1)](../man1/tcpdump.1.md), ioctl(2), kqueue(2), poll(2), select(2), [ng_bpf(4)](ng_bpf.4.md), [bpf(9)](../man9/bpf.9.md)

> McCanne, S., Jacobson V., "An efficient, extensible, and portable network monitor"。

## 历史

Enet 数据包过滤器于 1980 年由 Carnegie-Mellon 大学的 Mike Accetta 和 Rick Rashid 创建。Stanford 的 Jeffrey Mogul 将代码移植到 BSD，并从 1983 年起继续其开发。此后，它演变为 DEC 的 Ultrix 数据包过滤器、SunOS 4.1 下的 STREAMS NIT 模块以及 BPF。

## 作者

Lawrence Berkeley Laboratory 的 Steven McCanne 于 1990 年夏实现了 BPF。设计的很大一部分归功于 Van Jacobson。

零拷贝缓冲区的支持由 Robert N. M. Watson 在与 Seccuris Inc. 的合同下添加。

## 缺陷

读取缓冲区必须为固定大小（由 `BIOCGBLEN` ioctl 返回）。

未请求混杂模式的文件可能作为同一硬件接口上另一文件请求此模式的副作用而收到以混杂方式接收的数据包。这可以在内核中通过额外的处理开销来修复。然而，我们倾向于所有文件都必须假设接口处于混杂模式的模型，如果需要，必须利用过滤器来拒绝外来数据包。

观察到 `SEESENT`、`DIRECTION` 和 `FEEDBACK` 设置在某些接口类型上工作不正确，包括具有硬件回环而非软件回环的接口，以及点对点接口。它们似乎在广泛的以太网风格接口上运行正常。
