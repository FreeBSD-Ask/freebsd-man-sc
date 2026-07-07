# getsockopt(2)

`getsockopt` — 获取和设置套接字上的选项

## 名称

`getsockopt`, `setsockopt`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

```c
int
getsockopt(int s, int level, int optname, void * restrict optval,
    socklen_t * restrict optlen);

int
setsockopt(int s, int level, int optname, const void *optval,
    socklen_t optlen);
```

## 描述

`getsockopt()` 和 `setsockopt()` 系统调用操作与套接字关联的*选项*。选项可能存在于多个协议层；它们始终存在于最顶层的“socket”层。

操作套接字选项时，必须指定选项所在的层级和选项名称。要在套接字层操作选项，`level` 指定为 `SOL_SOCKET`。要在任何其他层操作选项，则需提供控制该选项的适当协议的协议号。例如，要指示某选项由 TCP 协议解释，应将 `level` 设置为 TCP 的协议号；参见 [getprotoent(3)](../man3/getprotoent.3.md)。

`optval` 和 `optlen` 参数用于访问 `setsockopt()` 的选项值。对于 `getsockopt()`，它们标识一个缓冲区，用于返回所请求选项的值。对于 `getsockopt()`，`optlen` 是一个值-结果参数，初始包含 `optval` 所指向缓冲区的大小，返回时修改为指示实际返回值的大小。如果不需提供或返回选项值，`optval` 可以为 NULL。

`optname` 参数和任何指定的选项都会不经解释地传递给相应的协议模块进行解释。头文件

`#include <sys/socket.h>`

包含套接字层选项的定义，如下所述。其他协议层的选项在格式和名称上各不相同；请查阅手册第 4 节中的相应条目。

大多数套接字层选项使用 `int` 参数作为 `optval`。对于 `setsockopt()`，该参数应为非零值以启用布尔选项，或为零以禁用该选项。`SO_LINGER` 使用 `struct linger` 参数，定义于

`#include <sys/socket.h>`

指定选项的期望状态和 linger 间隔（参见下文）。`SO_SNDTIMEO` 和 `SO_RCVTIMEO` 使用 `struct timeval` 参数，定义于

`#include <sys/time.h>`

以下选项在套接字层被识别。对于协议特定的选项，请参见协议手册页，例如 [ip(4)](../man4/ip.4.md) 或 [tcp(4)](../man4/tcp.4.md)。除另有说明外，每个选项都可以用 `getsockopt()` 检查并用 `setsockopt()` 设置。

| 选项 | 描述 |
| --- | --- |
| `SO_DEBUG` | 启用调试信息记录 |
| `SO_REUSEADDR` | 启用本地地址重用 |
| `SO_REUSEPORT` | 启用重复地址和端口绑定 |
| `SO_REUSEPORT_LB` | 启用带负载均衡的重复地址和端口绑定 |
| `SO_KEEPALIVE` | 启用保持连接活动 |
| `SO_DONTROUTE` | 启用外发消息的路由旁路 |
| `SO_LINGER` | 如果存在数据，则在关闭时延迟 |
| `SO_BROADCAST` | 启用发送广播消息的权限 |
| `SO_OOBINLINE` | 启用带内接收带外数据 |
| `SO_SNDBUF` | 设置输出缓冲区大小 |
| `SO_RCVBUF` | 设置输入缓冲区大小 |
| `SO_SNDLOWAT` | 设置输出最小计数 |
| `SO_RCVLOWAT` | 设置输入最小计数 |
| `SO_SNDTIMEO` | 设置输出超时值 |
| `SO_RCVTIMEO` | 设置输入超时值 |
| `SO_ACCEPTFILTER` | 在监听套接字上设置接受过滤器 |
| `SO_NOSIGPIPE` | 控制该套接字 `SIGPIPE` 信号的生成 |
| `SO_TIMESTAMP` | 启用接收带有数据报的时间戳 |
| `SO_BINTIME` | 启用接收带有数据报的时间戳 |
| `SO_ACCEPTCONN` | 获取套接字的监听状态（仅获取） |
| `SO_DOMAIN` | 获取套接字的域（仅获取） |
| `SO_TYPE` | 获取套接字的类型（仅获取） |
| `SO_PROTOCOL` | 获取套接字的协议号（仅获取） |
| `SO_PROTOTYPE` | Linux `SO_PROTOCOL` 的 SunOS 别名（仅获取） |
| `SO_ERROR` | 获取并清除套接字上的错误（仅获取） |
| `SO_RERROR` | 启用接收错误报告 |
| `SO_FIB` | 获取或设置套接字关联的 FIB（路由表） |

以下选项在 FreeBSD 中被识别：

| 选项 | 描述 |
| --- | --- |
| `SO_LABEL` | 获取套接字的 MAC 标签（仅获取） |
| `SO_PEERLABEL` | 获取套接字对端的 MAC 标签（仅获取） |
| `SO_LISTENQLIMIT` | 获取套接字的 backlog 上限（仅获取） |
| `SO_LISTENQLEN` | 获取套接字的完整队列长度（仅获取） |
| `SO_LISTENINCQLEN` | 获取套接字的不完整队列长度（仅获取） |
| `SO_USER_COOKIE` | 设置套接字的 'so_user_cookie' 值（uint32_t，仅设置） |
| `SO_TS_CLOCK` | 设置 `SO_TIMESTAMP` 返回时间戳的特定格式 |
| `SO_MAX_PACING_RATE` | 设置套接字的每秒最大传输速率（字节） |
| `SO_NO_OFFLOAD` | 禁用协议卸载 |
| `SO_NO_DDP` | 禁用直接数据放置卸载 |
| `SO_SPLICE` | 将两个套接字拼接在一起 |
| `SO_PASSRIGHTS` | 启用通过 unix(4) 套接字传递 `SCM_RIGHTS` |

`SO_DEBUG` 在底层协议模块中启用调试。

`SO_REUSEADDR` 指示在 [bind(2)](bind.2.md) 系统调用中验证所提供地址时使用的规则应允许重用本地地址。

`SO_REUSEPORT` 允许多个进程完全重复绑定，前提是它们都在绑定端口之前设置了 `SO_REUSEPORT`。此选项允许程序的多个实例各自接收发往绑定端口的 UDP/IP 多播或广播数据报。

`SO_REUSEPORT_LB` 允许多个套接字完全重复绑定，前提是它们都在绑定端口之前设置了 `SO_REUSEPORT_LB`。传入的 TCP 和 UDP 连接根据本地端口号以及外部 IP 地址和端口号的哈希函数分布到参与的监听套接字中。最多有 256 个套接字可以绑定到同一个负载均衡组。`PF_DIVERT` 套接字也可以绑定到组，详情请参见 [divert(4)](../man4/divert.4.md) 手册页。

`SO_KEEPALIVE` 启用在已连接套接字上周期性传输消息。如果连接方未能响应这些消息，则认为该连接已断开，当尝试发送数据时，使用该套接字的进程会通过 `SIGPIPE` 信号得到通知。

`SO_DONTROUTE` 指示外发消息应绕过标准路由设施。相反，消息根据目标地址的网络部分直接发送到适当的网络接口。

`SO_LINGER` 控制当未发送的消息排队在套接字上且执行 [close(2)](close.2.md) 时采取的操作。如果套接字承诺可靠的数据传输且设置了 `SO_LINGER`，系统将在 [close(2)](close.2.md) 尝试时阻塞进程，直到能够传输数据或决定无法传递信息（一个称为 linger 间隔的超时时间，以秒为单位在请求 `SO_LINGER` 时由 `setsockopt()` 系统调用指定）。如果禁用了 `SO_LINGER` 且发出了 [close(2)](close.2.md)，系统将以允许进程尽快继续的方式处理关闭。

`SO_BROADCAST` 选项请求在套接字上发送广播数据报的权限。在系统的早期版本中，广播是特权操作。

对于支持带外数据的协议，`SO_OOBINLINE` 选项请求带外数据在接收时放置在正常数据输入队列中；然后可以通过 [recv(2)](recv.2.md) 或 [read(2)](read.2.md) 调用在没有 `MSG_OOB` 标志的情况下访问。某些协议的行为始终如同设置了此选项。

`SO_SNDBUF` 和 `SO_RCVBUF` 是分别调整输出和输入缓冲区分配的正常缓冲区大小的选项。对于高容量连接可以增大缓冲区大小，或者减小以限制可能的传入数据积压。系统对这些值设置了绝对上限，可通过 [sysctl(3)](../man3/sysctl.3.md) MIB 变量“`kern.ipc.maxsockbuf`”访问。

`SO_SNDLOWAT` 是设置输出操作最小计数的选项。大多数输出操作处理调用提供的所有数据，将数据传递给协议进行传输并根据流控需要进行阻塞。非阻塞输出操作在流控允许的范围内处理尽可能多的数据而不会阻塞，但如果流控不允许处理低水位值或整个请求中较小者，则不会处理任何数据。测试套接字写入能力的 [select(2)](select.2.md) 操作仅在可以处理低水位标记数量时才返回 true。`SO_SNDLOWAT` 的默认值设置为便于网络效率的大小，通常为 1024。

`SO_RCVLOWAT` 是设置输入操作最小计数的选项。通常，接收调用将阻塞直到接收到任何（非零）数量的数据，然后返回可用数量或请求数量中较小者。`SO_RCVLOWAT` 的默认值为 1。如果将 `SO_RCVLOWAT` 设置为更大的值，阻塞接收调用通常会等待直到接收到低水位值或请求数量中较小者。如果发生错误、捕获到信号或接收队列中下一个数据类型与返回的类型不同，接收调用返回的数据可能仍少于低水位标记。

`SO_SNDTIMEO` 是设置输出操作超时值的选项。它接受一个 `struct timeval` 参数，包含用于限制输出操作完成等待的秒数和微秒数。如果发送操作已阻塞了这么长时间，则返回部分计数，或者如果未发送任何数据，则返回 `EWOULDBLOCK` 错误。在当前实现中，此计时器在每次将额外数据传递给协议时重新启动，这意味着该限制适用于大小从输出低水位到高水位之间的输出部分。

`SO_RCVTIMEO` 是设置输入操作超时值的选项。它接受一个 `struct timeval` 参数，包含用于限制输入操作完成等待的秒数和微秒数。在当前实现中，此计时器在每次协议接收到额外数据时重新启动，因此该限制实际上是一个非活动计时器。如果接收操作已阻塞了这么长时间而未接收到额外数据，则返回短计数，或者如果未接收到任何数据，则返回 `EWOULDBLOCK` 错误。

`SO_FIB` 可用于覆盖给定套接字的默认 FIB（路由表）。该值必须为 0 到 sysctl *net.fibs* 返回值减一之间。

`SO_USER_COOKIE` 可用于设置套接字中的 uint32_t `so_user_cookie` 字段。该值为 uint32_t，可在处理与套接字相关流量的内核代码中使用。该字段的默认值为 0。例如，该值可用作 `ipfw/dummynet` 中的 skipto 目标或管道编号。

`SO_ACCEPTFILTER` 在套接字上放置一个 [accept_filter(9)](../man9/accept_filter.9.md)，在传入连接被提供给 [accept(2)](accept.2.md) 之前，在监听流套接字上对其进行过滤。同样，在尝试安装过滤器之前，必须在该套接字上调用 [listen(2)](listen.2.md)，否则 `setsockopt()` 系统调用将失败。

```c
struct  accept_filter_arg {
        char    af_name[16];
        char    af_arg[256-16];
};
```

`optval` 参数应指向一个 `struct accept_filter_arg`，用于选择和配置 [accept_filter(9)](../man9/accept_filter.9.md)。`af_name` 参数应填入应用程序希望放置在监听套接字上的接受过滤器的名称。可选参数 `af_arg` 可传递给由 `af_name` 指定的接受过滤器，以在附加时提供额外的配置选项。传入 NULL 的 `optval` 将移除过滤器。

`SO_NOSIGPIPE` 选项控制当写入已连接但另一端已关闭的套接字时，通常发送的 `SIGPIPE` 信号的生成，此时返回 `EPIPE` 错误。

如果在 `SOCK_DGRAM` 套接字上启用了 `SO_TIMESTAMP` 或 `SO_BINTIME` 选项，[recvmsg(2)](recv.2.md) 调用可能返回数据报接收时间对应的时间戳。然而，也可能不会返回，例如由于资源不足。`msghdr` 结构中的 `msg_control` 字段指向一个缓冲区，其中包含一个 `cmsghdr` 结构，后跟 `SO_TIMESTAMP` 的 `struct timeval` 和 `SO_BINTIME` 的 `struct bintime`。默认情况下，TIMESTAMP 的 `cmsghdr` 字段具有以下值：

```c
     cmsg_len = CMSG_LEN(sizeof(struct timeval));
     cmsg_level = SOL_SOCKET;
     cmsg_type = SCM_TIMESTAMP;
```

对于 `SO_BINTIME`：

```c
     cmsg_len = CMSG_LEN(sizeof(struct bintime));
     cmsg_level = SOL_SOCKET;
     cmsg_type = SCM_BINTIME;
```

通过在 `SO_TIMESTAMP` 之后使用 `SO_TS_CLOCK`，可获得附加的时间戳类型，它请求返回特定的时间戳格式，而不是在启用 `SO_TIMESTAMP` 时返回 `SCM_TIMESTAMP`。FreeBSD 中识别以下 `SO_TS_CLOCK` 值：

| 选项 | 描述 |
| --- | --- |
| `SO_TS_REALTIME_MICRO` | 实时（`SCM_TIMESTAMP`，`struct timeval`），默认 |
| `SO_TS_BINTIME` | 实时（`SCM_BINTIME`，`struct bintime`） |
| `SO_TS_REALTIME` | 实时（`SCM_REALTIME`，`struct timespec`） |
| `SO_TS_MONOTONIC` | 单调时间（`SCM_MONOTONIC`，`struct timespec`） |

`SO_ACCEPTCONN`、`SO_TYPE`、`SO_PROTOCOL`（及其别名 `SO_PROTOTYPE`）和 `SO_ERROR` 是仅用于 `getsockopt()` 的选项。`SO_ACCEPTCONN` 返回套接字当前是否正在接受连接，即是否在该套接字上调用了 [listen(2)](listen.2.md) 系统调用。`SO_TYPE` 返回套接字的类型，例如 `SOCK_STREAM`；它对启动时继承套接字的服务器很有用。`SO_PROTOCOL` 返回 `AF_INET` 和 `AF_INET6` 地址族套接字的协议号。`SO_ERROR` 返回套接字上任何挂起的错误并清除错误状态。它可用于检查已连接数据报套接字上的异步错误或其他异步错误。`SO_RERROR` 指示接收缓冲区溢出应作为错误处理。过去，接收缓冲区溢出被忽略，程序无法知道是否因溢出而丢失了消息或消息被截断。由于程序过去并不期望得到接收溢出错误，因此此行为不是默认的。

`SO_LABEL` 返回套接字的 MAC 标签。`SO_PEERLABEL` 返回套接字对端的 MAC 标签。注意，你的内核必须编译有 MAC 支持。更多信息请参见 [mac(3)](../man3/mac.3.md)。

`SO_LISTENQLIMIT` 返回由 [listen(2)](listen.2.md) 设置的排队连接最大数量。`SO_LISTENQLEN` 返回未接受的完整连接数。`SO_LISTENINCQLEN` 返回未接受的不完整连接数。

`SO_MAX_PACING_RATE` 指示套接字和底层网络适配器层将传输速率限制为给定的无符号 32 位值（字节每秒）。

`SO_NO_OFFLOAD` 禁用对协议卸载的支持。目前，这阻止 TCP 套接字使用 TCP 卸载引擎。`SO_NO_DDP` 禁用对称为直接数据放置（DDP）的特定 TCP 卸载的支持。DDP 是 Chelsio 网络适配器支持的一种卸载，允许通过 [aio_read(2)](aio_read.2.md) 在用户提供的缓冲区中以零拷贝方式接收重组的 TCP 数据流。

当传递给 `setsockopt()` 时，`SO_SPLICE` 使用以下 `optval` 将两个套接字拼接在一起：

```c
struct so_splice {
	int sp_fd;
	off_t sp_max;
	struct timeval sp_idle;
};
```

在 `s` 上接收的数据将通过 `sp_fd` 中指定的套接字自动传输，无需用户空间任何干预。也就是说，数据将通过 `sp_fd` 传输，如同用户空间直接调用了 [send(2)](send.2.md)。拼接是单向操作；一对给定的套接字可以单向或双向拼接。目前仅连接的 [tcp(4)](../man4/tcp.4.md) 套接字可以拼接在一起。如果 `sp_max` 大于零，则套接字对在传输了该字节数后自动取消拼接。如果 `sp_idle` 非零，则自初次调用 `setsockopt()` 起经过指定时间后，套接字对自动取消拼接。如果 `sp_fd` 为 -1，则立即取消拼接套接字。成功的 [select(2)](select.2.md)、[poll(2)](poll.2.md) 或 [kqueue(2)](kqueue.2.md) 操作测试从源套接字读取的能力，表示拼接已终止且至少有一个字节可供读取。当其中一个套接字关闭时，拼接结束。

当传递给 `getsockopt()` 时，`SO_SPLICE` 选项返回一个 64 位整数，包含最近一次拼接传输的字节数。也就是说，当套接字被拼接时，返回的值是到目前为止拼接的字节数。取消拼接时，此值被保存并返回，直到套接字关闭或再次拼接。例如，如果一次拼接传输了 100 字节然后取消拼接，随后的 `getsockopt` 调用将返回 100，直到套接字再次被拼接。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getsockopt()` 和 `setsockopt()` 系统调用在以下情况下失败：

**[`EBADF`]** `s` 参数不是有效的描述符。

**[`ENOTSOCK`]** `s` 参数是文件，而非套接字。

**[`ENOPROTOOPT`]** 该选项在指定层级未知。

**[`EFAULT`]** `optval` 所指向的地址不在进程地址空间的有效部分。对于 `getsockopt()`，如果 `optlen` 不在进程地址空间的有效部分，也可能返回此错误。

**[`EINVAL`]** 试图在非监听套接字上安装 [accept_filter(9)](../man9/accept_filter.9.md)。

**[`ENOMEM`]** 服务该请求所需的内存分配失败。

`setsockopt()` 系统调用还可能返回以下错误：

**[`ENOBUFS`]** 系统中没有足够的资源来执行该操作。

## 参见

[ioctl(2)](ioctl.2.md), [listen(2)](listen.2.md), [recvmsg(2)](recv.2.md), [socket(2)](socket.2.md), [getprotoent(3)](../man3/getprotoent.3.md), [mac(3)](../man3/mac.3.md), [sysctl(3)](../man3/sysctl.3.md), [ip(4)](../man4/ip.4.md), [ip6(4)](../man4/ip6.4.md), [sctp(4)](../man4/sctp.4.md), [tcp(4)](../man4/tcp.4.md), [protocols(5)](../man5/protocols.5.md), [sysctl(8)](../man8/sysctl.8.md), [accept_filter(9)](../man9/accept_filter.9.md), [bintime(9)](../man9/bintime.9.md)

## 历史

`getsockopt()` 和 `setsockopt()` 系统调用出现于 4.2BSD。`SO_SPLICE` 选项起源于 OpenBSD 4.9，首次出现于 FreeBSD 14.3。FreeBSD 的实现旨在源代码兼容。

## 缺陷

若干套接字选项应在系统的较低层级处理。
