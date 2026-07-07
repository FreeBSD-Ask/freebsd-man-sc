# recv(2)

`recv` — 从套接字接收消息

## 名称

`recv`, `recvfrom`, `recvmsg`, `recvmmsg`

## 库

Lb libc

## 概要

`#include <sys/socket.h>`

```c
ssize_t
recv(int s, void *buf, size_t len, int flags);

ssize_t
recvfrom(int s, void *buf, size_t len, int flags,
    struct sockaddr * restrict from, socklen_t * restrict fromlen);

ssize_t
recvmsg(int s, struct msghdr *msg, int flags);

ssize_t
recvmmsg(int s, struct mmsghdr * restrict msgvec, size_t vlen,
    int flags, const struct timespec * restrict timeout);
```

## 描述

`recvfrom()`、`recvmsg()` 和 `recvmmsg()` 系统调用用于从套接字接收消息，可用于在面向连接或非面向连接的套接字上接收数据。

如果 `from` 不是空指针且套接字不是面向连接的，将填入消息的源地址。`fromlen` 参数是值-结果参数，初始化为与 `from` 关联的缓冲区大小，返回时修改为指示实际存储的地址大小。

`recv()` 函数通常仅在 *已连接* 套接字上使用（参见 [connect(2)](connect.2.md)），等效于将空指针作为 `from` 参数传递给 `recvfrom()`。

`recvmmsg()` 函数用于在一次调用中接收多条消息。其数量由 `vlen` 提供。消息在接收后放置在 `msgvec` 向量所描述的缓冲区中。每条接收到的消息的大小放置在向量每个元素的 `msg_len` 字段中。如果 `timeout` 为 NULL，调用将阻塞，直到每个提供的消息缓冲区都有数据可用。否则，它将等待数据一段指定的时间。如果超时到期且未接收到数据，返回值 0。在首次接收之前，使用 ppoll(2) 系统调用实现超时机制。

`recv()`、`recvfrom()` 和 `recvmsg()` 成功完成时返回消息的长度，而 `recvmmsg()` 返回接收到的消息数。如果消息太长无法放入提供的缓冲区，多余的字节可能被丢弃，具体取决于接收消息的套接字类型（参见 [socket(2)](socket.2.md)）。

如果套接字上没有可用消息，接收调用将等待消息到达，除非套接字是非阻塞的（参见 [fcntl(2)](fcntl.2.md)），此时返回值 -1，全局变量 `errno` 设置为 `EAGAIN`。除 `recvmmsg()` 外的接收调用通常返回任何可用数据（最多到请求的数量），而不是等待接收到全部请求的数量；此行为受 [getsockopt(2)](getsockopt.2.md) 中描述的套接字级选项 `SO_RCVLOWAT` 和 `SO_RCVTIMEO` 影响。`recvmmsg()` 函数对向量中的每条消息实现此行为。

可以使用 [select(2)](select.2.md) 系统调用确定何时有更多数据到达。

`recv()` 函数的 `flags` 参数通过对一个或多个以下值进行 *OR 运算* 形成：

| `MSG_OOB` | 处理带外数据 |
| --- | --- |
| `MSG_PEEK` | 查看传入消息 |
| `MSG_TRUNC` | 返回实际数据包或数据报长度 |
| `MSG_WAITALL` | 等待完整请求或错误 |
| `MSG_DONTWAIT` | 不阻塞 |
| `MSG_CMSG_CLOEXEC` | 将接收到的文件描述符设置为 close-on-exec |
| `MSG_CMSG_CLOFORK` | 将接收到的文件描述符设置为 close-on-fork |
| `MSG_WAITFORONE` | 接收第一条消息后不阻塞（仅用于 `recvmmsg()`） |

`MSG_OOB` 标志请求接收在正常数据流中不会接收到的带外数据。某些协议将加速数据放在正常数据队列的头部，因此此标志不能与此类协议一起使用。`MSG_PEEK` 标志使接收操作从接收队列开头返回数据，而不从队列中移除该数据。因此，后续的接收调用将返回相同的数据。`MSG_TRUNC` 标志使接收操作返回数据包或数据报的完整长度，即使大于提供的缓冲区。该标志在 `AF_INET`、`AF_INET6` 和 `AF_UNIX` 协议族的 `SOCK_DGRAM` 套接字上受支持。`MSG_WAITALL` 标志请求操作阻塞直到满足完整请求。但是，如果捕获到信号、发生错误或断开连接，或下一个要接收的数据类型与返回的类型不同，调用仍可能返回少于请求的数据。`MSG_DONTWAIT` 标志请求调用在会阻塞时返回。如果没有可用数据，`errno` 设置为 `EAGAIN`。此标志在 ANSI X3.159-1989 ("ANSI C89") 或 ISO/IEC 9899:1999 ("ISO C99") 编译模式下不可用。`MSG_WAITFORONE` 标志在接收到第一条消息后设置 MSG_DONTWAIT。此标志仅与 `recvmmsg()` 相关。

`recvmsg()` 系统调用使用 `msghdr` 结构以减少直接提供的参数数量。该结构形式如下（定义于 `#include <sys/socket.h>`）：

```c
struct msghdr {
        void            *msg_name;      /* 可选地址 */
        socklen_t        msg_namelen;   /* 地址大小 */
        struct iovec    *msg_iov;       /* scatter/gather 数组 */
        int              msg_iovlen;    /* msg_iov 中的元素数量 */
        void            *msg_control;   /* 辅助数据，见下文 */
        socklen_t        msg_controllen;/* 辅助数据缓冲区长度 */
        int              msg_flags;     /* 接收消息上的标志 */
};
```

其中 `msg_name` 和 `msg_namelen` 在套接字未连接时指定源地址；如果不需要或未要求名称，`msg_name` 可以给定空指针。`msg_iov` 和 `msg_iovlen` 参数描述 scatter gather 位置，如 [read(2)](read.2.md) 所述。`msg_control` 参数长度为 `msg_controllen`，指向用于其他协议控制相关消息或其他杂项辅助数据的缓冲区。消息形式如下：

```c
struct cmsghdr {
        socklen_t  cmsg_len;    /* 数据字节计数，包括头 */
        int        cmsg_level;  /* 起源协议 */
        int        cmsg_type;   /* 协议特定类型 */
/* 后跟
        u_char     cmsg_data[]; */
};
```

例如，SO_TIMESTAMP 套接字选项为 UDP 数据包返回接收时间戳。

对于 `AF_UNIX` 域套接字，辅助数据可用于传递文件描述符和进程凭证。详细信息请参见 [unix(4)](../man4/unix.4.md)。

`msg_flags` 字段在返回时根据接收到的消息进行设置。`MSG_EOR` 指示记录结束；返回的数据完成了一条记录（通常与 `SOCK_SEQPACKET` 类型的套接字一起使用）。`MSG_TRUNC` 指示数据报的尾部被丢弃，因为数据报大于提供的缓冲区。`MSG_CTRUNC` 指示由于辅助数据缓冲区空间不足，某些控制数据被丢弃。返回 `MSG_OOB` 指示接收到加速或带外数据。

`recvmmsg()` 系统调用使用 `mmsghdr` 结构，定义如下（在 `#include <sys/socket.h>` 头文件中）：

```c
struct mmsghdr {
        struct msghdr    msg_hdr;       /* 消息头 */
        ssize_t          msg_len;       /* 消息长度 */
};
```

数据接收时，`msg_len` 字段更新为接收到的消息长度。

## 返回值

成功完成时，`recv()`、`recvfrom()` 和 `recvmsg()` 函数返回接收到的字节数，而 `recvmmsg()` 函数返回接收到的消息数。如果没有可接收的消息且对端已执行有序关闭，返回 0。否则，返回 -1，并设置 `errno` 以指示错误。

## 错误

调用在以下情况下失败：

**[`EBADF`]** `s` 参数是无效的描述符。

**[`ECONNRESET`]** 远端套接字被强制关闭。

**[`ENOTCONN`]** 套接字与面向连接的协议关联，但尚未连接（参见 [connect(2)](connect.2.md) 和 [accept(2)](accept.2.md)）。

**[`ENOTSOCK`]** `s` 参数不引用套接字。

**[`EMFILE`]** `recvmsg()` 系统调用用于接收连接上正在传输中的权限（文件描述符），但接收程序没有足够的空闲文件描述符槽位来接受它们。在这种情况下，描述符被关闭，对于不可靠数据报协议，待处理数据被丢弃；对于可靠协议，待处理数据被保留。待处理数据可通过再次调用 `recvmsg()` 检索。

**[`EMSGSIZE`]** `msg` 所指向的 `msghdr` 结构的 `msg_iovlen` 成员小于等于 0，或大于 `IOV_MAX`。

**[`EAGAIN`]** 套接字标记为非阻塞，接收操作会阻塞，或已设置接收超时且超时在接收到数据之前到期。

**[`EINTR`]** 在任何数据可用之前，接收被信号传递中断。

**[`EFAULT`]** 接收缓冲区指针指向进程地址空间之外。

## 参见

[fcntl(2)](fcntl.2.md), [getsockopt(2)](getsockopt.2.md), [read(2)](read.2.md), [select(2)](select.2.md), [socket(2)](socket.2.md), [CMSG_DATA(3)](../man3/CMSG_DATA.3.md), [unix(4)](../man4/unix.4.md)

## 历史

`recv()` 函数首次出现于 4.2BSD。`recvmmsg()` 函数首次出现于 FreeBSD 11.0。
