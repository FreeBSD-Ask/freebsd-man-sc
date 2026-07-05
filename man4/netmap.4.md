# netmap.4

`netmap` — 快速数据包 I/O 框架

## 名称

`netmap`

## 概要

`device netmap`

## 描述

`netmap` 是一个为用户空间和内核客户端以及虚拟机提供极快速、高效数据包 I/O 的框架。它运行于 FreeBSD、Linux 和某些 Windows 版本上，并支持多种 `netmap` 设备，包括

**`physical`** 用于访问网络接口的各个队列；

**`host`** 用于将数据包注入主机栈；

**`VALE`** 实现一个非常快速且模块化的内核内软件交换机/数据面；

**`netmap`** 一个共享内存数据包传输通道；

**`netmap`** 一种类似于 [bpf(4)](bpf.4.md) 的捕获流量的机制

所有这些 `netmap` 设备都可以通过相同的 API 互换访问，并且比标准 OS 机制（socket、bpf、tun/tap 接口、原生交换机、管道）至少快一个数量级。借助足够快的硬件（NIC、PCIe 总线、CPU），在受支持的 NIC 上使用 `netmap` 的数据包 I/O 在 10 Gbit/s NIC 上可达 1488 万包每秒（Mpps），且占用不到一个核心；在 40 Gbit/s NIC 上可达 35-40 Mpps（受硬件限制）；对于 VALE 端口每个核心约 20 Mpps；对于 `netmap` 管道则超过 100 Mpps。没有原生 `netmap` 支持的 NIC 仍可在模拟模式下使用 API，它使用未经修改的设备驱动程序，比 [bpf(4)](bpf.4.md) 或原始 socket 快 3-5 倍。

用户空间客户端可以动态地将 NIC 切换到 `netmap` 模式，并通过内存映射缓冲区发送和接收原始数据包。类似地，可以动态创建 `VALE` 交换机实例和端口、`netmap` 管道和 `netmap` 监视器，在进程、虚拟机、NIC 和主机栈之间提供高速数据包 I/O。

`netmap` 通过 ioctl(2) 支持非阻塞 I/O，并通过文件描述符和标准 OS 机制（如 select(2)、poll(2)、kqueue(2) 和 epoll(7)）支持同步和阻塞 I/O。所有类型的 `netmap` 设备和 `VALE` 交换机都由单个内核模块实现，该模块还通过标准驱动程序模拟 `VALE` API。为获得最佳性能，`VALE` 需要设备驱动程序中的原生支持。此类设备的列表位于本文档末尾。

在本（较长的）手册页的其余部分，我们记录了 `netmap` 和 `VALE` 架构、特性和用法的各个方面。

## 架构

`netmap` 通过*端口*支持原始数据包 I/O，端口可连接到物理接口*（NIC）*、主机栈或 `VALE` 交换机。端口使用预分配的环形缓冲区队列*（ring）*，这些队列位于 mmapped 区域中。NIC 或虚拟端口的每个发送/接收队列都有一个 ring。另一对 ring 连接到主机栈。

将文件描述符绑定到端口后，`netmap` 客户端可通过 ring 批量发送或接收数据包，并可能实现端口之间的零拷贝转发。

所有在 `netmap` 模式下操作的 NIC 使用同一内存区域，该区域可被所有拥有绑定到 NIC 的 `/dev/netmap` 文件描述符的进程访问。独立的 `VALE` 交换机和 `netmap` 端口默认使用独立的内存区域，但可独立配置为共享内存。

## 进入和退出 NETMAP 模式

以下章节描述了创建和控制 `netmap` 端口（包括 `VALE` 和 `netmap` 端口）的系统调用。更简单的高层函数在 Sx LIBRARIES 章节中描述。

端口和 ring 通过文件描述符创建和控制，文件描述符通过打开特殊设备创建：

```sh
fd = open("/dev/netmap");
```

然后通过以下调用绑定到特定端口：

```sh
ioctl(fd, NIOCREGIF, (struct nmreq *)arg);
```

`netmap` 有多种由 `struct nmreq` 参数控制的操作模式。`arg.nr_name` 指定 netmap 端口名，如下所示：

**`OS 网络接口名（例如 'em0'、'eth1'、...`** ）NIC 的数据路径与主机栈断开，文件描述符绑定到 NIC（一个或所有队列）或主机栈；

**`valeSSS:PPP`** 文件描述符绑定到 VALE 交换机 SSS 的端口 PPP。必要时会动态创建交换机实例和端口。SSS 和 PPP 都采用 [0-9a-zA-Z_]+ 形式，字符串不能超过 IFNAMSIZ 字符，且 PPP 不能是任何已存在 OS 网络接口的名称。

返回时，`arg` 指示共享内存区域的大小以及所有 `netmap` 数据结构的数量、大小和位置，可通过 mmap 内存访问这些结构：

```sh
char *mem = mmap(0, arg.nr_memsize, fd);
```

非阻塞 I/O 通过特殊的 ioctl(2) 完成，对文件描述符执行 select(2) 和 poll(2) 允许阻塞 I/O。

当 NIC 处于 `netmap` 模式时，OS 仍会认为接口处于 up 且运行状态。OS 为该 NIC 生成的数据包会进入一个 `netmap` ring，另一个 ring 用于将数据包发送到 OS 网络栈。对文件描述符执行 close(2) 会移除绑定，并将 NIC 返回到正常模式（将数据路径重新连接到主机栈），或销毁虚拟端口。

## 数据结构

mmapped 内存区域中的数据结构详见

`#include <sys/net/netmap.h>`

这是 `netmap` API 的最终权威参考。主要结构和字段如下所示：

```sh
struct netmap_if {
    ...
    const uint32_t   ni_flags;      /* 属性                       */
    ...
    const uint32_t   ni_tx_rings;   /* NIC 发送 ring              */
    const uint32_t   ni_rx_rings;   /* NIC 接收 ring              */
    uint32_t         ni_bufs_head;  /* 额外缓冲区链表的头         */
    ...
};
```

```sh
struct netmap_ring {
    ...
    const uint32_t num_slots;   /* 每个 ring 的槽位数            */
    const uint32_t nr_buf_size; /* 每个缓冲区的大小              */
    ...
    uint32_t       head;        /* (u) 用户拥有的第一个缓冲区    */
    uint32_t       cur;         /* (u) 唤醒位置                  */
    const uint32_t tail;        /* (k) 内核拥有的第一个缓冲区    */
    ...
    uint32_t       flags;
    struct timeval ts;          /* (k) 上次 rxsync() 的时间      */
    ...
    struct netmap_slot slot[0]; /* 槽位数组                      */
}
```

```sh
struct netmap_slot {
    uint32_t buf_idx;           /* 缓冲区索引                    */
    uint16_t len;               /* 数据包长度                    */
    uint16_t flags;             /* 缓冲区已更改等                */
    uint64_t ptr;               /* 间接缓冲区地址                */
};
```

**`struct netmap_if（每个接口一个`** ）指示可用 ring（`struct netmap_rings`）的数量及其在 mmapped 区域中的位置。tx 和 rx ring 的数量（`ni_tx_rings`、`ni_rx_rings`）通常取决于硬件。NIC 还有一对额外的 tx/rx ring 连接到主机栈。*NIOCREGIF* 还可请求在同一内存空间中分配额外的未绑定缓冲区，用作数据包的临时存储。额外缓冲区的数量在 `arg.nr_arg3` 字段中指定。成功时，内核将实际分配的额外缓冲区数量写回 `arg.nr_arg3`（如果内存空间耗尽，可能少于请求的数量）。`ni_bufs_head` 包含这些额外缓冲区中第一个的索引，它们以链表形式连接（每个缓冲区的第一个 uint32_t 是链表中下一个缓冲区的索引）。`0` 表示链表结束。应用程序可自由修改此链表并使用缓冲区（即将它们绑定到 netmap ring 的槽位）。关闭 netmap 文件描述符时，内核释放 `ni_bufs_head` 所指向链表中包含的缓冲区，无论这些缓冲区最初是否由内核在 *NIOCREGIF* 时提供。

**`struct netmap_ring（每个 ring 一个`** ）实现发送和接收 ring，带有读/写指针、元数据和一个描述缓冲区的*槽位*数组。

**`struct netmap_slot（每个缓冲区一个`** ）描述一个数据包缓冲区，通常由一个索引标识并驻留在 mmapped 区域中。

**`数据包缓冲区`** 内核分配的固定大小（通常 2 KB）数据包缓冲区。

`struct netmap_if` 在 mmapped 区域中的偏移量由 `NIOCREGIF` 返回结构中的 `nr_offset` 字段指示。从那里，所有其他对象都可通过相对引用（偏移量或索引）到达。以下文件中的宏和函数

`#include <net/netmap_user.h>`

帮助将它们转换为实际指针：

```sh
struct netmap_if *nifp = NETMAP_IF(mem, arg.nr_offset);
```

```sh
struct netmap_ring *txr = NETMAP_TXRING(nifp, ring_index);
```

```sh
struct netmap_ring *rxr = NETMAP_RXRING(nifp, ring_index);
```

```sh
char *buf = NETMAP_BUF(ring, buffer_index);
```

## RING、缓冲区和数据 I/O

`Ring` 是数据包的循环队列，具有三个索引/指针（`head`、`cur`、`tail`）；始终保留一个槽位为空。Ring 大小（`num_slots`）不应假定为 2 的幂。

`head` 是用户空间可用的第一个槽位；

`cur` 是唤醒点：当 `tail` 越过 `cur` 时，select/poll 将解除阻塞；

`tail` 是保留给内核的第一个槽位。

槽位索引*必须*只能向前移动；为方便起见，函数

```sh
nm_ring_next(ring, index)
```

返回按 ring 大小取模的下一个索引。

`head` 和 `cur` 仅由用户程序修改；`tail` 仅由内核修改。内核仅在执行 netmap 相关系统调用期间读/写 `struct netmap_ring` 槽位和缓冲区。唯一的例外是 `tail..head-1` 范围内明确分配给内核的槽位（和缓冲区）。

### 发送 RING

在发送 ring 上，执行 `netmap` 系统调用后，`head..tail-1` 范围内的槽位可用于发送。用户代码应顺序填充槽位，并将 `head` 和 `cur` 推进到准备好发送的槽位之后。如果用户代码在进一步发送之前需要更多槽位，可将 `cur` 进一步前移（参见 Sx SCATTER GATHER I/O）。

在下一次 NIOCTXSYNC/select()/poll() 时，到 `head-1` 为止的槽位被推送到端口，如果有更多槽位可用，`tail` 可能会前移。下面是 TX ring 演化的一个示例：

```sh
    系统调用后，cur 和 tail 之间的槽位是(a)可用的
              head=cur   tail
               |          |
               v          v
     TX  [.....aaaaaaaaaaa.............]
    用户创建新数据包以进行(T)传输
                head=cur tail
                    |     |
                    v     v
     TX  [.....TTTTTaaaaaa.............]
    NIOCTXSYNC/poll()/select() 发送数据包并报告新槽位
                head=cur      tail
                    |          |
                    v          v
     TX  [..........aaaaaaaaaaa........]
```

如果 ring 中没有空间，Fn select 和 Fn poll 将阻塞，即：

```sh
ring->cur == ring->tail
```

并在新槽位可用时返回。

高速应用程序可能希望通过在发出之前准备尽可能多的数据包来分摊系统调用的成本。

有待处理传输的发送 ring 满足：

```sh
ring->head != ring->tail + 1 (按 ring 大小取模)。
```

函数 `int nm_tx_pending(ring)` 实现此测试。

### 接收 RING

在接收 ring 上，执行 `netmap` 系统调用后，`head..tail-1` 范围内的槽位包含已接收的数据包。用户代码应处理它们，并将 `head` 和 `cur` 推进到要返回给内核的槽位之后。如果用户代码希望等待更多数据包而不将所有之前的槽位返回给内核，可将 `cur` 进一步前移。

在下一次 NIOCRXSYNC/select()/poll() 时，到 `head-1` 为止的槽位返回给内核以进行进一步接收，`tail` 可能会前移以报告新的传入数据包。

下面是 RX ring 演化的一个示例：

```sh
    系统调用后，有一些(h)持有和(R)接收的槽位
           head  cur     tail
            |     |       |
            v     v       v
     RX  [..hhhhhhRRRRRRRR..........]
    用户推进 head 和 cur，释放一些槽位并持有其他槽位
               head cur  tail
                 |  |     |
                 v  v     v
     RX  [..*****hhhRRRRRR...........]
    NICRXSYNC/poll()/select() 恢复槽位并报告新数据包
               head cur        tail
                 |  |           |
                 v  v           v
     RX  [.......hhhRRRRRRRRRRRR....]
```

## 槽位和数据包缓冲区

通常，数据包应存储在端口绑定到文件描述符时分配给槽位的 netmap 缓冲区中。一个数据包完全包含在单个缓冲区中。

以下标志影响槽位和缓冲区处理：

**NS_BUF_CHANGED** 当槽位中的 `buf_idx` 更改时*必须*使用。这可用于实现零拷贝转发，参见 Sx ZERO-COPY FORWARDING。

**NS_REPORT** 报告此缓冲区何时已传输。通常 `netmap` 批量通知发送完成，因此信号可能无限期延迟。此标志有助于检测数据包何时已发送以及文件描述符何时可关闭。

**NS_FORWARD** 当 ring 处于"透明"模式时，用户应用程序用此标志标记的数据包将在下一次系统调用时转发到另一端点，从而（以选择性方式）恢复 NIC 和主机栈之间的连接。

**NS_NO_LEARN** 告诉转发代码此数据包的源 MAC 地址不得用于学习桥接代码。

**NS_INDIRECT** 指示数据包的有效载荷位于用户提供的缓冲区中，其用户虚拟地址在槽位的 'ptr' 字段中。大小可达 65535 字节。这仅在 `VALE` 端口的发送 ring 上支持，有助于减少虚拟机互联中的数据复制。

**NS_MOREFRAG** 指示数据包以后续缓冲区继续；数据包中最后一个缓冲区必须清除此标志。

## 分散聚集 I/O

如果在除最后一个槽位之外的所有槽位中设置了 `NS_MOREFRAG` 标志，则数据包可跨越多个槽位。链的最大长度为 64 个缓冲区。这通常在连接虚拟机时与 `VALE` 端口一起使用，因为它们生成大型 TSO 段，这些段在到达物理设备之前不会被拆分。

注意：长度字段始终指单个分片；没有地方存储数据包的总长度。

在接收 ring 上，宏 `NS_RFRAGS(slot)` 指示此数据包的剩余槽位数，包括当前槽位。值大于 1 的槽位也设置了 NS_MOREFRAG。

## IOCTLS

`netmap` 使用两个 ioctl（NIOCTXSYNC、NIOCRXSYNC）进行非阻塞 I/O。它们不带参数。另外两个 ioctl（NIOCGINFO、NIOCREGIF）用于查询和配置端口，参数如下：

```sh
struct nmreq {
    char      nr_name[IFNAMSIZ]; /* (i) 端口名                     */
    uint32_t  nr_version;        /* (i) API 版本                   */
    uint32_t  nr_offset;         /* (o) mmap 区域中 nifp 的偏移量  */
    uint32_t  nr_memsize;        /* (o) mmap 区域的大小            */
    uint32_t  nr_tx_slots;       /* (i/o) 发送 ring 中的槽位数     */
    uint32_t  nr_rx_slots;       /* (i/o) 接收 ring 中的槽位数     */
    uint16_t  nr_tx_rings;       /* (i/o) 发送 ring 数             */
    uint16_t  nr_rx_rings;       /* (i/o) 接收 ring 数             */
    uint16_t  nr_ringid;         /* (i/o) 我们关心的 ring          */
    uint16_t  nr_cmd;            /* (i) 特殊命令                   */
    uint16_t  nr_arg1;           /* (i/o) 额外参数                 */
    uint16_t  nr_arg2;           /* (i/o) 额外参数                 */
    uint32_t  nr_arg3;           /* (i/o) 额外参数                 */
    uint32_t  nr_flags           /* (i/o) 打开模式                 */
    ...
};
```

通过 `/dev/netmap` 获取的文件描述符还支持网络设备支持的 ioctl，参见 [netintro(4)](netintro.4.md)。

**`nr_memsize`** 指示 `netmap` 内存区域的大小。处于 `netmap` 模式的 NIC 都共享同一内存区域，而 `VALE` 端口每个端口有独立的区域。

**`nr_tx_slots , nr_rx_slots`** 指示发送和接收 ring 的大小。

**`nr_tx_rings , nr_rx_rings`** 指示发送和接收 ring 的数量。ring 数量和大小都可在运行时使用接口特定的函数（例如 ethtool(8)）配置。

**NR_REG_ALL_NIC** netmap:foo（默认）所有硬件 ring 对

**NR_REG_SW** netmap:foo^ “主机 ring”，连接到主机栈。

**NR_REG_NIC_SW** netmap:foo* 所有硬件 ring 和主机 ring

**NR_REG_ONE_NIC** netmap:foo-i 仅第 i 个硬件 ring 对，编号在 `nr_ringid` 中；

**NR_REG_PIPE_MASTER** netmap:foo{i netmap 管道的主端，其标识符（i）在 `nr_ringid` 中；

**NR_REG_PIPE_SLAVE** netmap:foo}i netmap 管道的从端，其标识符（i）在 `nr_ringid` 中。管道的标识符应被视为管道名的一部分，不需要连续。返回时，管道将只有单个 ring 对，索引为 0，无论 `i` 的值如何。

**`NIOCGINFO`** 如果命名端口不支持 netmap，则返回 EINVAL。否则返回 0 和关于端口的（参考性）信息。注意，以下所有信息在接口实际进入 netmap 模式之前都可能发生变化。

**`NIOCREGIF`** 将 `nr_name` 命名的端口绑定到文件描述符。对于物理设备，这还会将其切换到 `netmap` 模式，将其与主机栈断开。多个文件描述符可绑定到同一端口，适当的同步留给用户。将文件描述符绑定到端口的推荐方法是使用函数 `nm_open(..)`（参见 Sx LIBRARIES），它解析名称以访问特定端口类型并启用功能。下面我们记录主要功能。`NIOCREGIF` 还可将文件描述符绑定到*netmap 管道*的一端，netmap 管道由两个交叉连接的 netmap 端口组成。netmap 管道共享父端口的同一内存空间，旨在启用主进程作为调度器向从进程分发的配置。为启用此功能，结构的 `nr_arg1` 字段可用作对内核的提示，指示我们期望使用多少管道，并在内存区域中预留额外空间。返回时，它给出与 NIOCGINFO 相同的信息，`nr_ringid` 和 `nr_flags` 指示通过文件描述符控制的 ring 的身份。`nr_flags` `nr_ringid` 选择通过此文件描述符控制哪些 ring。`nr_flags` 的可能值如下所示，连同应用程序库（如下面指示的 `nm_open`）可用于指示特定 ring 集合的命名方案。在下面的示例中，“netmap:foo”是任何有效的 netmap 端口名。默认情况下，poll(2) 或 select(2) 调用会推送发送 ring 上任何待处理的数据包，即使未指定写入事件。可通过将 `NETMAP_NO_TX_POLL` 或运算到写入 `nr_ringid` 的值来禁用此功能。使用此功能时，仅在调用 `ioctl(NIOCTXSYNC)` 或以写入事件（POLLOUT/wfdset）或满 ring 调用 `select()`/`poll()` 时才传输数据包。在将动态创建的虚拟接口注册到 `VALE` 交换机时，可使用 nr_tx_rings 和 nr_rx_rings 字段指定其所需的 ring 数（默认为 1，当前最多 16）。

**`NIOCTXSYNC`** 通知硬件有新数据包要发送，并更新可用于发送的槽位数。

**`NIOCRXSYNC`** 通知硬件已消耗的数据包，并请求新可用的数据包。

## SELECT、POLL、EPOLL、KQUEUE

对 `netmap` 文件描述符执行 select(2) 和 poll(2) 时，分别在请求写入（POLLOUT）和读取（POLLIN）事件时按 Sx 发送 RING 和 Sx 接收 RING 中所示处理 ring。两者在 ring 中无可用槽位（`ring->cur == ring->tail`）时都会阻塞。根据平台，还支持 epoll(7) 和 kqueue(2)。

发送 ring 中的数据包通常会在不请求写入事件的情况下被推送出去（并回收缓冲区）。向 *NIOCREGIF* 传递 `NETMAP_NO_TX_POLL` 标志可禁用此功能。默认情况下，仅在请求读取事件时才处理接收 ring。向 *NIOCREGIF* 传递 `NETMAP_DO_RX_POLL` 标志会更新接收 ring，即使没有读取事件。注意，在 epoll(7) 和 kqueue(2) 上，`NETMAP_NO_TX_POLL` 和 `NETMAP_DO_RX_POLL` 仅在为文件描述符发布某些事件时才有效。

## 库

`netmap` API 应直接使用，既因其简单性也为了与应用程序的高效集成。

为方便起见，

`#include <net/netmap_user.h>`

头文件提供了一些宏和函数，以简化创建文件描述符和使用 `netmap` 端口进行 I/O。这些函数松散地仿照 pcap(3) API，以便于将基于 libpcap 的应用程序移植到 `netmap`。要使用这些额外函数，程序应

```sh
#define NETMAP_WITH_LIBS
```

然后

```sh
#include <net/netmap_user.h>
```

提供以下函数：

**`ifname`** 是端口名，对于 NIC 为“netmap:PPP”形式，对于 `VALE` 端口为“valeSSS:PPP”形式。

**`req`** 为 NIOCREGIF ioctl 的参数提供初始值。nm_flags 和 nm_ringid 值会被解析 ifname 和 flags 时覆盖，其他字段可通过其他两个参数覆盖。

**`arg`** 指向 struct nm_desc，包含应覆盖默认值的参数（例如来自先前打开的文件描述符）。字段的使用如下所述

**`flags`** 可设置为以下标志的组合：`NETMAP_NO_TX_POLL`、`NETMAP_DO_RX_POLL`（复制到 nr_ringid）；`NM_OPEN_NO_MMAP`（如果 arg 指向同一内存区域，避免 mmap 并使用其中的值）；`NM_OPEN_IFNAME`（忽略 ifname 并使用 arg 中的值）；`NM_OPEN_ARG1`、`NM_OPEN_ARG2`、`NM_OPEN_ARG3`（使用 arg 中的字段）；`NM_OPEN_RING_CFG`（使用 arg 中的 ring 数量和大小）。

**`struct nm_desc * nm_open(const char *ifname, const struct nmreq *req, uint64_t flags, const struct nm_desc *arg`** ）类似于 pcap_open_live(3)，将文件描述符绑定到端口。

**`int nm_close(struct nm_desc *d`** ）关闭文件描述符，取消内存映射，释放资源。

**`int nm_inject(struct nm_desc *d, const void *buf, size_t size`** ）类似于 `pcap_inject()`，将数据包推送到 ring，成功时返回数据包大小，出错时返回 0；

**`int nm_dispatch(struct nm_desc *d, int cnt, nm_cb_t cb, u_char *arg`** ）类似于 `pcap_dispatch()`，对传入数据包应用回调

**`u_char * nm_nextpkt(struct nm_desc *d, struct nm_pkthdr *hdr`** ）类似于 `pcap_next()`，获取下一个数据包

## 支持的设备

`netmap` 原生支持以下设备：

在 FreeBSD 上：[cxgbe(4)](cxgbe.4.md), [em(4)](em.4.md), [iflib(4)](iflib.4.md)（提供 igb(4) [em(4)](em.4.md)），[ix(4)](ix.4.md), [ixl(4)](ixl.4.md), [re(4)](re.4.md), [vtnet(4)](vtnet.4.md)。

在 Linux 上：e1000、e1000e、i40e、igb、ixgbe、ixgbevf、r8169、virtio_net、vmxnet3。

没有原生支持的 NIC 仍可通过模拟在 `netmap` 模式下使用。性能低于原生 netmap 模式，但仍显著高于各种原始 socket 类型（bpf、PF_PACKET 等）。注意对于慢速设备（如 1 Gbit/s 及更慢的 NIC，或硬件无法维持线速的某些 10 Gbit/s NIC），模拟和原生模式可能具有相似或相同的吞吐量。

使用模拟时，tcpdump 等数据包嗅探程序可能会在 netmap 转移之前看到接收到的数据包。此行为并非有意为之，仅为模拟实现的副作用。注意，如果 netmap 应用程序随后将模拟适配器接收的数据包移动到主机 RX ring，嗅探器将再次截获这些数据包，因为数据包在被网络接口接收时即注入主机栈。

模拟也可用于具有原生 netmap 支持的设备，可用于测试或性能比较。sysctl 变量 `dev.netmap.admode` 全局控制 netmap 模式的实现方式。

## SYSCTL 变量和模块参数

`netmap` 和 `VALE` 操作的某些方面通过 FreeBSD 上的 sysctl 变量*（dev.netmap.\*）*和 Linux 上的模块参数*（/sys/module/netmap/parameters/\*）*控制：

**`dev.netmap.admode: 0`** 控制使用原生或模拟适配器模式。0 使用最佳可用选项；1 强制原生模式，如果不可用则失败；2 强制模拟，因此从不失败。

**`dev.netmap.generic_rings: 1`** 用于模拟 netmap 模式的 ring 数

**`dev.netmap.generic_ringsize: 1024`** 用于模拟 netmap 模式的 ring 大小

**`dev.netmap.generic_mit: 100000`** 控制模拟模式的中断合并

**`dev.netmap.fwd: 0`** 强制 NS_FORWARD 模式

**`dev.netmap.txsync_retry: 2`** `netmap` 刷新函数中的 txsync 循环数

**`dev.netmap.no_pendintr: 1`** 强制在系统调用时恢复发送缓冲区

**`dev.netmap.no_timestamp: 0`** 禁用 netmap ring 中时间戳的更新

**`dev.netmap.verbose: 0`** 详细的内核消息

**`dev.netmap.buf_num: 163840`**

**`dev.netmap.buf_size: 2048`**

**`dev.netmap.ring_num: 200`**

**`dev.netmap.ring_size: 36864`**

**`dev.netmap.if_num: 100`**

**`dev.netmap.if_size: 1024`** 全局内存区域中对象（netmap_if、netmap_ring、缓冲区）的大小和数量。唯一值得修改的参数是 `dev.netmap.buf_num`，因为它影响 netmap 使用的总内存量。

**`dev.netmap.buf_curr_num: 0`**

**`dev.netmap.buf_curr_size: 0`**

**`dev.netmap.ring_curr_num: 0`**

**`dev.netmap.ring_curr_size: 0`**

**`dev.netmap.if_curr_num: 0`**

**`dev.netmap.if_curr_size: 0`** 实际使用中的值。

**`dev.netmap.priv_buf_num: 4098`**

**`dev.netmap.priv_buf_size: 2048`**

**`dev.netmap.priv_ring_num: 4`**

**`dev.netmap.priv_ring_size: 20480`**

**`dev.netmap.priv_if_num: 2`**

**`dev.netmap.priv_if_size: 1024`** 私有内存区域中对象（netmap_if、netmap_ring、缓冲区）的大小和数量。每个 `VALE` 端口和每对 `netmap` 管道使用单独的内存区域。

**`dev.netmap.bridge_batch: 1024`** 通过 `VALE` 交换机移动数据包时使用的批量大小。大于 64 的值通常可保证良好的性能。

**`dev.netmap.max_bridges: 8`** 可创建的 `VALE` 交换机最大数量。此可调参数可在加载器时指定。

**`dev.netmap.ptnet_vnet_hdr: 1`** 允许 ptnet 设备使用 virtio-net 头部

**`dev.netmap.port_numa_affinity: 0`** 在 [numa(4)](numa.4.md) 系统上，尽可能从本地 NUMA 域为 netmap 端口分配内存。这可通过减少远程内存访问次数来提高性能。但是，当在附加到不同 NUMA 域的端口之间转发数据包时，这将阻止零拷贝转发优化，因此可能损害性能。注意，此设置必须在引导时作为加载器可调参数指定。

## 系统调用

`netmap` 使用 select(2)、poll(2)、epoll(7) 和 kqueue(2) 在发生重要事件时唤醒进程，并使用 mmap(2) 映射内存。ioctl(2) 用于配置端口和 `VALE` 交换机。

应用程序可能需要创建线程并将其绑定到特定核心以提高性能，使用标准 OS 原语，参见 [pthread(3)](../man3/pthread.3.md)。特别是 pthread_setaffinity_np(3) 可能有用。

## 实例

### 测试程序

`netmap` 附带一些可用于测试或简单应用的程序。参见 `netmap` 发行版中的 `examples/` 目录，或 FreeBSD 发行版中的 `tools/tools/netmap/` 目录。

pkt-gen(8) 是一个通用的流量源/接收器。

例如

```sh
pkt-gen -i ix0 -f tx -l 60
```

可以生成无限流的最小尺寸数据包，而

```sh
pkt-gen -i ix0 -f rx
```

是一个流量接收器。两者都打印流量统计信息，帮助监视系统的表现。

pkt-gen(8) 有许多选项可用于设置数据包大小、地址、速率，并使用多个发送/接收线程和核心。

[bridge(4)](bridge.4.md) 是另一个测试程序，它互联两个 `netmap` 端口。可用于接口之间的透明转发，如

```sh
bridge -i netmap:ix0 -i netmap:ix1
```

甚至使用 netmap 将 NIC 连接到主机栈

```sh
bridge -i netmap:ix0
```

### 使用原生 API

以下代码实现了一个流量生成器：

```sh
#include <net/netmap_user.h>
...
void sender(void)
{
    struct netmap_if *nifp;
    struct netmap_ring *ring;
    struct nmreq nmr;
    struct pollfd fds;
    fd = open("/dev/netmap", O_RDWR);
    bzero(&nmr, sizeof(nmr));
    strcpy(nmr.nr_name, "ix0");
    nmr.nm_version = NETMAP_API;
    ioctl(fd, NIOCREGIF, &nmr);
    p = mmap(0, nmr.nr_memsize, fd);
    nifp = NETMAP_IF(p, nmr.nr_offset);
    ring = NETMAP_TXRING(nifp, 0);
    fds.fd = fd;
    fds.events = POLLOUT;
    for (;;) {
	poll(&fds, 1, -1);
	while (!nm_ring_empty(ring)) {
	    i = ring->cur;
	    buf = NETMAP_BUF(ring, ring->slot[i].buf_index);
	    ... 在 buf 中准备数据包 ...
	    ring->slot[i].len = ... 数据包长度 ...
	    ring->head = ring->cur = nm_ring_next(ring, i);
	}
    }
}
```

### 辅助函数

可使用辅助函数实现一个简单的接收器：

```sh
#define NETMAP_WITH_LIBS
#include <net/netmap_user.h>
...
void receiver(void)
{
    struct nm_desc *d;
    struct pollfd fds;
    u_char *buf;
    struct nm_pkthdr h;
    ...
    d = nm_open("netmap:ix0", NULL, 0, 0);
    fds.fd = NETMAP_FD(d);
    fds.events = POLLIN;
    for (;;) {
	poll(&fds, 1, -1);
        while ( (buf = nm_nextpkt(d, &h)) )
	    consume_pkt(buf, h.len);
    }
    nm_close(d);
}
```

### 零拷贝转发

由于物理接口共享同一内存区域，可以通过交换缓冲区在端口之间进行数据包转发。发送 ring 中的缓冲区用于补充接收 ring：

```sh
    uint32_t tmp;
    struct netmap_slot *src, *dst;
    ...
    src = &src_ring->slot[rxr->cur];
    dst = &dst_ring->slot[txr->cur];
    tmp = dst->buf_idx;
    dst->buf_idx = src->buf_idx;
    dst->len = src->len;
    dst->flags = NS_BUF_CHANGED;
    src->buf_idx = tmp;
    src->flags = NS_BUF_CHANGED;
    rxr->head = rxr->cur = nm_ring_next(rxr, rxr->cur);
    txr->head = txr->cur = nm_ring_next(txr, txr->cur);
    ...
```

### 访问主机栈

主机栈在所有实际用途上只是一个常规的 ring 对，可使用 netmap API 访问（例如使用

```sh
nm_open("netmap:eth0^", ... ) ;
```

主机在 `netmap` 模式下要发送到接口的所有数据包最终进入 RX ring，而排队到 TX ring 的所有数据包都被发送到主机栈。

### VALE 交换机

测试 `VALE` 交换机性能的一个简单方法是将一个发送器和一个接收器附加到它，例如在两个不同的终端中运行：

```sh
pkt-gen -i vale1:a -f rx # 接收器
```

```sh
pkt-gen -i vale1:b -f tx # 发送器
```

通过简单地更改端口名，可使用相同示例测试 netmap 管道，例如：

```sh
pkt-gen -i vale2:x{3 -f rx # 主端上的接收器
```

```sh
pkt-gen -i vale2:x}3 -f tx # 从端上的发送器
```

以下命令将一个接口和主机栈附加到交换机：

```sh
valectl -h vale2:em0
```

附加到同一交换机的其他 `VALE` 客户端现在可以与网卡或主机通信。

## 参见

[vale(4)](vale.4.md), bridge(8), lb(8), nmreplay(8), pkt-gen(8), valectl(8)

`http://info.iet.unipi.it/~luigi/netmap/`

Luigi Rizzo, Revisiting network I/O APIs: the netmap framework, Communications of the ACM, 55 (3), pp.45-51, March 2012

Luigi Rizzo, netmap: a novel framework for fast packet I/O, Usenix ATC'12, June 2012, Boston

Luigi Rizzo, Giuseppe Lettieri, VALE, a switched ethernet for virtual machines, ACM CoNEXT'12, December 2012, Nice

Luigi Rizzo, Giuseppe Lettieri, Vincenzo Maffione, Speeding up packet I/O in virtual machines, ACM/IEEE ANCS'13, October 2013, San Jose

## 作者

`netmap` 框架最初由 Luigi Rizzo 于 2011 年在 Universita` di Pisa 设计和实现，并在 Matteo Landi、Gaetano Catalli、Giuseppe Lettieri 和 Vincenzo Maffione 的帮助下进一步扩展。

`netmap` 和 `VALE` 由欧洲委员会在 FP7 项目 CHANGE（257422）和 OPENLAB（287581）中资助。

## 注意事项

无论 CPU 和 OS 有多快，要在 10G 及更快的接口上达到线速，都需要具有足够性能的硬件。一些 NIC 在小数据包尺寸下无法维持线速。PCIe 或内存带宽不足也会导致性能下降。

低性能的另一个常见原因是链路上使用流量控制：慢速接收器会限制发送速度。运行高速实验时，请确保禁用流量控制。

### 特殊 NIC 功能

`netmap` 与某些 NIC 功能（如多队列、调度器、数据包过滤器）正交。

多个发送和接收 ring 原生支持，可使用普通 OS 工具（如 ethtool(8) 或设备特定的 sysctl 变量）配置。接收数据包转向（RPS）和传入流量过滤也是如此。

`netmap` *不使用*校验和卸载、TCP 分段卸载、加密、VLAN 封装/解封装等功能。使用 netmap 与主机栈交换数据包时，请确保禁用这些功能。
