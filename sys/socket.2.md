# socket(2)

`socket` — 创建通信端点

## 名称

`socket`

## 库

Lb libc

## 概要

`#include <sys/socket.h>`

```c
int
socket(int domain, int type, int protocol);
```

## 描述

`socket()` 系统调用创建一个通信端点并返回一个描述符。

`domain` 参数指定进行通信的通信域；这将选择应使用的协议族。这些族定义于包含文件

`#include <sys/socket.h>`

当前可识别的格式有：

**`PF_LOCAL`** 主机内部协议（`PF_UNIX` 的别名）。

**`PF_UNIX`** 主机内部协议。参见 [unix(4)](../man4/unix.4.md)。

**`PF_INET`** Internet 版本 4 协议。参见 [icmp(4)](../man4/icmp.4.md), [igmp(4)](../man4/igmp.4.md), [ip(4)](../man4/ip.4.md), [sctp(4)](../man4/sctp.4.md), [tcp(4)](../man4/tcp.4.md), [udp(4)](../man4/udp.4.md), [udplite(4)](../man4/udplite.4.md)。

**`PF_INET6`** Internet 版本 6 协议。参见 [icmp6(4)](../man4/icmp6.4.md), [ip6(4)](../man4/ip6.4.md), [mld(4)](../man4/mld.4.md)。

**`PF_DIVERT`** 防火墙数据包分流/重新注入。参见 [divert(4)](../man4/divert.4.md)。

**`PF_ROUTE`** 用于控制路由表和从内核接收网络配置事件的遗留协议。新应用应优先使用 [rtnetlink(4)](../man4/rtnetlink.4.md) 而非 [route(4)](../man4/route.4.md)。

**`PF_KEY`** 内部密钥管理功能。参见 [ipsec(4)](../man4/ipsec.4.md)。

**`PF_NETGRAPH`** Netgraph 套接字。参见 netgraph(3) 和 [ng_socket(4)](../man4/ng_socket.4.md)。

**`PF_NETLINK`** Netlink 协议。参见 [genetlink(4)](../man4/genetlink.4.md), [netlink(4)](../man4/netlink.4.md), [rtnetlink(4)](../man4/rtnetlink.4.md)。

**`PF_BLUETOOTH`** 蓝牙协议。参见 [ng_btsocket(4)](../man4/ng_btsocket.4.md)。

**`PF_INET_SDP`** OFED 套接字直接协议（IPv4）。

**`PF_HYPERV`** HyperV 套接字。

每个协议族都连接到一个地址族，地址族具有相同的名称，但前缀由 “`PF_`” 变为 “`AF_`”。还可以定义其他协议族，以 “`PF_`” 开头，并具有相应的地址族。

套接字具有指定的 `type`，用于指定通信语义。当前定义的类型有：

**`SOCK_STREAM`** 流套接字。

**`SOCK_DGRAM`** 数据报套接字。

**`SOCK_RAW`** 原始协议接口。

**`SOCK_SEQPACKET`** 有序分组流。

此外，`type` 参数中允许使用以下标志：

**`SOCK_CLOEXEC`** 在新套接字上设置 close-on-exec。参见 [fcntl(2)](fcntl.2.md) 中 `F_GETFD` 命令的 `FD_CLOEXEC` 标志。

**`SOCK_CLOFORK`** 在新套接字上设置 close-on-fork。参见 [fcntl(2)](fcntl.2.md) 中 `F_GETFD` 命令的 `FD_CLOFORK` 标志。

**`SOCK_NONBLOCK`** 在新套接字上设置非阻塞模式。参见 [fcntl(2)](fcntl.2.md) 中 `F_SETFL` 命令的 `O_NONBLOCK` 标志。

`protocol` 参数指定套接字要使用的特定协议。通常，在给定协议族中只有一种协议支持特定套接字类型。但是，也可能存在多种协议，此时必须以这种方式指定特定协议。使用的协议号特定于进行通信的 “通信域”；参见 [protocols(5)](../man5/protocols.5.md)。`protocol` 参数可设为零（0），以请求协议的套接字类型的默认实现（如果存在）。

## 流套接字类型

`SOCK_STREAM` 套接字类型在套接字与其连接的对端之间提供可靠、有序、全双工的字节流。`SOCK_STREAM` 类型的套接字在发送或接收任何数据之前需要处于 *已连接* 状态。通过 [connect(2)](connect.2.md) 系统调用创建到另一个套接字的连接。（某些协议族，如 Internet 族，支持 “隐式连接” 的概念，允许通过 sendto(2) 系统调用将数据附带在连接操作上发送。）一旦连接，可使用 [send(2)](send.2.md)、sendto(2)、sendmsg(2) 和 [write(2)](write.2.md) 系统调用发送数据。可使用 [recv(2)](recv.2.md)、recvfrom(2)、recvmsg(2) 和 [read(2)](read.2.md) 系统调用接收数据。不维护记录边界；使用一种大小的输出操作在流套接字上发送的数据可以使用较小或较大大小的输入操作接收，不会丢失数据。数据可能被缓冲；从输出函数成功返回并不意味着数据交付给对端，甚至不代表从本地系统发送。对于某些协议，可以如 [send(2)](send.2.md) 中所述传输带外数据，并如 [recv(2)](recv.2.md) 中所述接收。

如果数据无法在给定时间内成功传输，则连接被视为断开，后续操作将以协议特定的错误代码失败。如果线程尝试在断开的流（不再连接的流）上发送数据，将引发 `SIGPIPE` 信号。可以通过在 [send(2)](send.2.md)、sendto(2) 和 sendmsg(2) 系统调用中使用 `MSG_NOSIGNAL` 标志来抑制此信号，也可以通过 setsockopt(2) 在套接字上设置 `SO_NOSIGPIPE` 套接字选项来抑制。

`SOCK_STREAM` 套接字由以下协议族支持：`PF_INET`、`PF_INET6`、`PF_UNIX`、`PF_BLUETOOTH`、`PF_HYPERV` 和 `PF_INET_SDP`。`PF_INET` 和 `PF_INET6` 协议族的流套接字支持带外数据传输机制。

## 数据报套接字类型

`SOCK_DGRAM` 套接字类型支持无连接数据传输，这种传输不一定被确认或可靠。数据报可以发送到每次输出操作中指定的地址（可能是多播或广播），传入的数据报可以从多个来源接收。使用 recvfrom(2) 或 recvmsg(2) 接收数据报时可获取每个数据报的源地址。应用程序也可以使用 sendto(2) 或 sendmsg(2) 预先指定对端地址，在这种情况下，未指定对端地址的输出函数调用将发送到预先指定的对端。如果指定了对端，则只接收来自该对端的数据报。数据报应在单个输出操作中发送，并需在单个输入操作中接收。数据报的最大大小是协议特定的。输出数据报可能在系统内被缓冲；因此，从输出函数成功返回并不保证数据报实际被发送或接收。

`SOCK_DGRAM` 套接字由以下协议族支持：`PF_INET`、`PF_INET6`、`PF_UNIX`、`PF_NETGRAPH` 和 `PF_NETLINK`。

## 有序分组套接字类型

`SOCK_SEQPACKET` 套接字类型类似于 `SOCK_STREAM` 类型，也是面向连接的。这些类型之间的唯一区别是 `SOCK_SEQPACKET` 类型维护记录边界。可以使用一个或多个输出操作发送一个记录，并使用一个或多个输入操作接收，但单个操作永远不会传输多于一个记录的部分。记录边界由发送方使用 [send(2)](send.2.md) 或 sendmsg(2) 函数的 `MSG_EOR` 标志设置。无法通过 [write(2)](write.2.md) 设置记录边界。记录边界通过 recvmsg(2) 函数返回的接收消息标志中的 `MSG_EOR` 标志对接收方可见。是否施加最大记录大小是协议特定的。

`SOCK_SEQPACKET` 套接字由以下协议族支持：`PF_INET`、`PF_INET6` 和 `PF_UNIX`。

## 原始套接字类型

`SOCK_RAW` 套接字类型提供对内部网络协议和接口的访问。它本质上是一个数据报套接字，因此具有相同的读和写操作语义。`SOCK_RAW` 类型仅对超级用户可用，并在 [ip(4)](../man4/ip.4.md) 和 [ip6(4)](../man4/ip6.4.md) 中描述。

## 非阻塞模式

可借助 `SOCK_NONBLOCK` 标志以 *非阻塞模式* 创建套接字。或者，可以借助 [fcntl(2)](fcntl.2.md) 系统调用的 `O_NONBLOCK` 标志开启和关闭套接字的非阻塞模式。

当非阻塞套接字的接收缓冲区中没有足够数据来填满应用程序提供的缓冲区时，[recv(2)](recv.2.md)、recvfrom(2)、recvmsg(2) 和 [read(2)](read.2.md) 等数据接收系统调用不会阻塞等待数据，而是立即返回。返回值将指示读入所提供缓冲区的字节数。`errno` 将被设置为 `EAGAIN`（与 `EWOULDBLOCK` 值相同）。

如果应用程序尝试在非阻塞套接字上通过 [send(2)](send.2.md)、sendto(2)、sendmsg(2) 或 [write(2)](write.2.md) 系统调用发送超过套接字发送缓冲区可容纳的数据，将只发送部分数据。返回值将指示发送的字节数。`errno` 将被设置为 `EAGAIN`。注意，`SOCK_DGRAM` 类型的套接字是不可靠的，因此对于这些套接字，在非阻塞模式下发送操作永远不会以 `EAGAIN` 失败，在阻塞模式下也不会阻塞。

## 套接字的其他操作

由于套接字描述符是文件描述符，[fcntl(2)](fcntl.2.md) 执行的许多通用文件操作都适用。套接字描述符可用于所有事件引擎，如 kevent(2)、[select(2)](select.2.md) 和 [poll(2)](poll.2.md)。

[fcntl(2)](fcntl.2.md) 系统调用可用于指定在带外数据到达时接收 `SIGURG` 信号的进程组。它还可以通过 `SIGIO` 启用非阻塞 I/O 和 I/O 事件的异步通知。

套接字的操作由套接字级 *选项* 控制。这些选项定义于文件

`#include <sys/socket.h>`

setsockopt(2) 和 [getsockopt(2)](getsockopt.2.md) 系统调用分别用于设置和获取选项。

与套接字关联的连接可通过 [close(2)](close.2.md) 系统调用终止。可使用 [shutdown(2)](shutdown.2.md) 禁用通信的某个方向。

## 返回值

发生错误时返回 -1，否则返回值为引用该套接字的描述符。

## 错误

`socket()` 系统调用在以下情况下失败：

**[`EACCES`]** 拒绝创建指定类型和/或协议的套接字的权限。

**[`EAFNOSUPPORT`]** 不支持该地址族（域），或该协议族不支持指定的域。

**[`EMFILE`]** 每进程描述符表已满。

**[`ENFILE`]** 系统文件表已满。

**[`ENOBUFS`]** 没有足够的缓冲区空间。在释放足够资源之前无法创建套接字。

**[`EPERM`]** 用户没有足够权限执行所请求的操作。

**[`EPROTONOSUPPORT`]** 此域内不支持该协议类型或指定协议。

**[`EPROTOTYPE`]** 该协议不支持此套接字类型。

## 参见

[accept(2)](accept.2.md), [bind(2)](bind.2.md), [close(2)](close.2.md), [connect(2)](connect.2.md), [fcntl(2)](fcntl.2.md), [getpeername(2)](getpeername.2.md), [getsockname(2)](getsockname.2.md), [getsockopt(2)](getsockopt.2.md), [ioctl(2)](ioctl.2.md), kevent(2), [listen(2)](listen.2.md), [poll(2)](poll.2.md), [read(2)](read.2.md), [recv(2)](recv.2.md), [select(2)](select.2.md), [send(2)](send.2.md), sendmsg(2), sendto(2), [signal(3)](../gen/signal.3.md), [shutdown(2)](shutdown.2.md), [socketpair(2)](socketpair.2.md), [write(2)](write.2.md), [CMSG_DATA(3)](../man3/CMSG_DATA.3.md), [getprotoent(3)](../net/getprotoent.3.md), netgraph(3), [divert(4)](../man4/divert.4.md), [genetlink(4)](../man4/genetlink.4.md), [icmp(4)](../man4/icmp.4.md), [icmp6(4)](../man4/icmp6.4.md), [igmp(4)](../man4/igmp.4.md), [ip(4)](../man4/ip.4.md), [ip6(4)](../man4/ip6.4.md), [ipsec(4)](../man4/ipsec.4.md), [netintro(4)](../man4/netintro.4.md), [netlink(4)](../man4/netlink.4.md), [ng_socket(4)](../man4/ng_socket.4.md), [route(4)](../man4/route.4.md), [rtnetlink(4)](../man4/rtnetlink.4.md), [sctp(4)](../man4/sctp.4.md), [tcp(4)](../man4/tcp.4.md), [udp(4)](../man4/udp.4.md), [protocols(5)](../man5/protocols.5.md)

> "An Introductory 4.3 BSD Interprocess Communication Tutorial", *PS1*, 7.

> "BSD Interprocess Communication Tutorial", *PS1*, 8.

## 标准

`socket()` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。POSIX 标准仅指定地址族的 `AF_INET`、`AF_INET6` 和 `AF_UNIX` 常量，并要求在 `socket()` 的 `domain` 参数中使用 `AF_*` 常量。`SOCK_CLOEXEC` 和 `SOCK_CLOFORK` 标志预期遵循 -p1003.1-2024 POSIX 标准。`SOCK_RDM` `type`、`PF_*` 常量和其他地址族是 FreeBSD 扩展。

## 历史

`socket()` 系统调用出现于 4.2BSD。

`SOCK_CLOFORK` 标志出现于 FreeBSD 15.0。
