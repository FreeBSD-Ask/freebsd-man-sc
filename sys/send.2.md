# send(2)

`send` — 从套接字发送消息

## 名称

`send`, `sendto`, `sendmsg`, `sendmmsg`

## 库

Lb libc

## 概要

`#include <sys/socket.h>`

```c
ssize_t
send(int s, const void *msg, size_t len, int flags);

ssize_t
sendto(int s, const void *msg, size_t len, int flags,
    const struct sockaddr *to, socklen_t tolen);

ssize_t
sendmsg(int s, const struct msghdr *msg, int flags);

ssize_t
sendmmsg(int s, struct mmsghdr * restrict msgvec, size_t vlen,
    int flags);
```

## 描述

`send()` 和 `sendmmsg()` 函数，以及 `sendto()` 和 `sendmsg()` 系统调用用于向另一个套接字传输一个或多个消息（使用 `sendmmsg()` 调用时）。`send()` 函数仅在套接字处于 *已连接* 状态时使用。如果套接字是无连接模式，`sendto()`、`sendmsg()` 和 `sendmmsg()` 函数可在任何时候使用。如果套接字是面向连接的模式，协议必须支持隐式连接（目前只有 [tcp(4)](../man4/tcp.4.md) 协议支持），或者套接字在使用前必须处于已连接状态。

目标的地址由 `to` 给出，`tolen` 指定其大小，或在 `struct msghdr` 中由等价的 `msg_name` 和 `msg_namelen` 给出。如果套接字处于已连接状态，传递给 `sendto()`、`sendmsg()` 或 `sendmmsg()` 的目标地址会被忽略。消息的长度由 `len` 给出。如果消息太长，无法通过底层协议原子地传递，则返回错误 `EMSGSIZE`，且消息不会被传输。

`sendmmsg()` 函数一次调用发送多条消息。消息由 `msgvec` 向量给出，`vlen` 指定向量大小。每条消息发送的八位数被放置在向量中每个已处理元素的 `msg_len` 字段中。

`send()` 不会隐式指示投递失败。本地检测到的错误通过返回值 -1 来指示。

如果套接字上没有可用的消息空间来保存待传输的消息，则 `send()` 通常会阻塞，除非套接字已置于非阻塞 I/O 模式。可以使用 [select(2)](select.2.md) 系统调用来确定何时可以发送更多数据。

`flags` 参数可以包含以下一个或多个标志：

```c
#define MSG_OOB         0x00001 /* 处理带外数据 */
#define MSG_DONTROUTE   0x00004 /* 绕过路由，使用直接接口 */
#define MSG_EOR         0x00008 /* 数据完成记录 */
#define MSG_DONTWAIT    0x00080 /* 不阻塞 */
#define MSG_EOF         0x00100 /* 数据完成事务 */
#define MSG_NOSIGNAL    0x20000 /* 在 EOF 时不生成 SIGPIPE */
```

`MSG_OOB` 标志用于在支持此概念的套接字上发送“带外”数据（例如 `SOCK_STREAM`）；底层协议也必须支持“带外”数据。`MSG_EOR` 用于为支持该概念的协议指示记录标记。`MSG_DONTWAIT` 标志请求调用在本来会阻塞时返回。`MSG_EOF` 请求关闭套接字的发送端，并在指定数据的末尾发送适当的指示；此标志仅在 `PF_INET` 协议族的 `SOCK_STREAM` 套接字上实现。`MSG_DONTROUTE` 通常仅由诊断或路由程序使用。`MSG_NOSIGNAL` 用于在写入可能已关闭的套接字时防止生成 `SIGPIPE`。

有关 `msghdr` 结构和 `mmsghdr` 结构的描述，请参见 [recv(2)](recv.2.md)。

## 返回值

`send()`、`sendto()` 和 `sendmsg()` 调用返回发送的八位数。`sendmmsg()` 调用返回发送的消息数。如果发生错误，返回值为 -1。

## 错误

`send()` 和 `sendmmsg()` 函数以及 `sendto()` 和 `sendmsg()` 系统调用在以下情况下会失败：

**[EBADF]** 指定了无效的描述符。

**[EACCES]** 目标地址是广播地址，且套接字上未设置 `SO_BROADCAST`。

**[ENOTCONN]** 套接字是面向连接模式但未连接。

**[ENOTSOCK]** 参数 `s` 不是套接字。

**[EFAULT]** 为某个参数指定了无效的用户空间地址。

**[EMSGSIZE]** 套接字要求消息以原子方式发送，而待发送消息的大小使这无法实现。

**[EAGAIN]** 套接字被标记为非阻塞，或指定了 `MSG_DONTWAIT`，且请求的操作会阻塞。

**[ENOBUFS]** 系统无法分配内部缓冲区。当缓冲区变为可用时，操作可能会成功。

**[ENOBUFS]** 网络接口的输出队列已满。这通常表示接口已停止发送，但也可能由瞬时拥塞引起。

**[EHOSTUNREACH]** 远程主机不可达。

**[EISCONN]** 指定了目标地址且套接字已连接。

**[ECONNREFUSED]** 套接字从上次发送的消息中收到了 ICMP 目标不可达消息。这通常意味着接收方未在远程端口上监听。

**[EHOSTDOWN]** 远程主机已宕机。

**[ENETDOWN]** 远程网络已宕机。

**[EADDRNOTAVAIL]** 使用 `SOCK_RAW` 套接字的进程被监禁，且 IP 头中指定的源地址与绑定到该监禁的 IP 地址不匹配。

**[EPERM]** `msg` 包含 `SCM_RIGHTS` 控制消息，且接收 [unix(4)](../man4/unix.4.md) 套接字被配置为拒绝新的 `SCM_RIGHTS`。

**[EPIPE]** 套接字无法再发送数据（套接字上已设置 `SBS_CANTSENDMORE`）。这通常意味着套接字未连接。

## 参见

[connect(2)](connect.2.md), [fcntl(2)](fcntl.2.md), [getsockopt(2)](getsockopt.2.md), [recv(2)](recv.2.md), [select(2)](select.2.md), [socket(2)](socket.2.md), [write(2)](write.2.md), [CMSG_DATA(3)](../man3/CMSG_DATA.3.md), [unix(4)](../man4/unix.4.md)

## 历史

`send()` 函数首次出现于 4.2BSD。`sendmmsg()` 函数首次出现于 FreeBSD 11.0。

## 缺陷

由于 `sendmsg()` 不一定阻塞到数据传输完成，因此可能通过 `AF_UNIX` 域套接字传输一个打开的文件描述符（参见 [recv(2)](recv.2.md)），然后在实际发送之前 `close()` 它，结果是接收方获得一个已关闭的文件描述符。这留给应用程序实现确认机制来防止此类情况发生。
