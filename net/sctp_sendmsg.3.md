# sctp_sendmsg(3)

`sctp_sendmsg` — 从 SCTP 套接字发送消息

## 名称

`sctp_sendmsg`, `sctp_sendmsgx`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
ssize_t
sctp_sendmsg(int s, const void *msg, size_t len,
    const struct sockaddr *to, socklen_t tolen, uint32_t ppid,
    uint32_t flags, uint16_t stream_no, uint32_t timetolive,
    uint32_t context);

ssize_t
sctp_sendmsgx(int s, const void *msg, size_t len,
    const struct sockaddr *to, int addrcnt, uint32_t ppid, uint32_t flags,
    uint16_t stream_no, uint32_t timetolive, uint32_t context);
```

## 描述

`sctp_sendmsg` 系统调用用于向另一个 SCTP 端点传输消息。`sctp_sendmsg` 可在任何时候使用。如果套接字是一对多类型（SOCK_SEQPACKET）套接字，则尝试向不存在关联的地址发送将隐式创建新关联。在这种情况下发送的数据将导致数据在 SCTP 四次握手的第三段上发送。注意，如果套接字是一对一类型（SOCK_STREAM）套接字，则必须存在关联（通过使用 [connect(2)](../sys/connect.2.md) 系统调用）。在未连接的一对一套接字上调用 `sctp_sendmsg` 或 `sctp_sendmsgx` 将导致 `errno` 被设置为 `ENOTCONN`，返回 -1，且消息不会被传输。

目标的地址由 `to` 给出，`tolen` 指定其大小。消息 `msg` 的长度由 `len` 给出。如果消息太长而无法通过底层协议原子地传递，则 `errno` 被设置为 `EMSGSIZE`，返回 -1，且消息不会被传输。

`sctp_sendmsg` 调用中不隐含传递失败的指示。本地检测到的错误由返回值 -1 指示。

如果套接字上没有可用空间来保存待传输的消息，则 `sctp_sendmsg` 通常会阻塞，除非套接字已置于非阻塞 I/O 模式。可以使用 [select(2)](../sys/select.2.md) 系统调用来确定何时可以在一对一类型（SOCK_STREAM）套接字上发送更多数据。

`ppid` 参数是一个不透明的 32 位值，通过协议栈透明地传递到对端端点。它将在接收到消息时可用（见 [sctp_recvmsg(3)](sctp_recvmsg.3.md)）。注意，协议栈传递此值时不考虑字节序。

`flags` 参数可能包含以下一个或多个值：

```c
#define SCTP_EOF 	  0x0100	/* 启动关闭流程 */
#define SCTP_ABORT	  0x0200	/* 向对端发送 ABORT */
#define SCTP_UNORDERED 	  0x0400	/* 消息是无序的 */
#define SCTP_ADDR_OVER	  0x0800	/* 覆盖主地址 */
#define SCTP_SENDALL      0x1000	/* 在端点的所有关联上发送 */
					/* 此消息 */
/* 低位字节是 PR-SCTP 策略的枚举 */
#define SCTP_PR_SCTP_TTL  0x0001	/* 基于时间的 PR-SCTP */
#define SCTP_PR_SCTP_BUF  0x0002	/* 基于缓冲区的 PR-SCTP */
#define SCTP_PR_SCTP_RTX  0x0003	/* 基于重传次数的 PR-SCTP */
```

`SCTP_EOF` 标志用于指示 SCTP 协议栈将此消息排队，然后开始关联的优雅关闭。队列中所有剩余数据将被发送，之后关联将被关闭。

`SCTP_ABORT` 用于立即终止关联。向对端发送中止消息，并销毁本地 TCB。

`SCTP_UNORDERED` 用于指定正在发送的消息没有特定顺序，应尽快传递给对端应用程序。当此标志不存在时，消息在发送它们的流中按顺序传递，但不考虑对端流的顺序。

`SCTP_ADDR_OVER` 标志用于指定应使用特定地址。通常 SCTP 仅使用多宿主对端地址中的一个作为发送的主地址。默认情况下，无论 `to` 参数是什么，都使用此主地址发送数据。通过指定此标志，用户要求协议栈忽略主地址，而是使用指定地址不仅作为查找机制来找到关联，还作为实际发送地址。

对于一对多类型（SOCK_SEQPACKET）套接字，`SCTP_SENDALL` 标志可用作一种便捷方式，使得一次发送调用即可让该套接字下的所有关联都获得消息的副本。注意，此机制非常高效，仅创建一份数据的实际副本，由所有关联共享用于发送。

其余标志用于部分可靠性扩展（RFC3758），仅在对端端点支持此扩展时才有效。此选项指定本地端点在跳过数据时应使用的本地策略。如果未设置这些选项中的任何一个，则数据永远不会被跳过。

`SCTP_PR_SCTP_TTL` 用于指示对数据应用基于时间的生存期。`timetolive` 参数则是尝试传输数据的毫秒数。如果经过这么多毫秒且对端未确认数据，则数据将被跳过且不再传输。注意，此策略甚至不保证数据会被发送。在大量数据排队拥塞的情况下，`timetolive` 可能在第一次传输之前就已过期。

基于 `SCTP_PR_SCTP_BUF` 的策略将 `timetolive` 字段转换为出站发送队列上允许的总字节数。如果队列中的字节数达到或超过此数量，则会查找其他基于缓冲区的发送并将其移除和跳过。注意，如果队列中没有基于缓冲区的发送且队列中已达到 `timetolive` 指定的最大字节数，此策略也可能导致数据永远不会被发送。

`SCTP_PR_SCTP_RTX` 策略将 `timetolive` 转换为允许的重传次数。此策略始终保证至少对数据进行一次发送尝试。之后，在数据被跳过之前，重传次数不超过 `timetolive` 次。

`stream_no` 是你希望发送消息的 SCTP 流。SCTP 中的流是可靠（或部分可靠）的有序消息流。`context` 字段仅在消息无法发送时使用。这是一个不透明的值，由协议栈保留，并在启用了通知的情况下，当发送失败时提供给用户（见 [sctp(4)](../man4/sctp.4.md)）。通常，用户进程可以使用此值在发送无法完成时索引某些特定于应用程序的数据结构。`sctp_sendmsgx` 与 `sctp_sendmsg` 相同，区别在于它在 `to` 参数中接收 sockaddr 结构数组，并增加 `addrcnt` 参数指定数组中有多少个地址。这允许调用者通过传递多个地址隐式设置关联，就像调用 `sctp_connectx` 来设置关联一样。

## 返回值

调用返回发送的字符数，出错时返回 -1。

## 错误

`sctp_sendmsg` 系统调用在以下情况失败：

**`[EBADF]`** 指定了无效的描述符。

**`[ENOTSOCK]`** 参数 `s` 不是套接字。

**`[EFAULT]`** 为参数指定了无效的用户空间地址。

**`[EMSGSIZE]`** 套接字要求以原子方式发送消息，而要发送的消息大小使此成为不可能。

**`[EAGAIN]`** 套接字标记为非阻塞，且请求的操作将阻塞。

**`[ENOBUFS]`** 系统无法分配内部缓冲区。当缓冲区可用时，操作可能成功。

**`[ENOBUFS]`** 网络接口的输出队列已满。这通常表示接口已停止发送，但也可能由瞬态拥塞引起。

**`[EHOSTUNREACH]`** 远程主机不可达。

**`[ENOTCONN]`** 在一对一风格套接字上不存在关联。

**`[ECONNRESET]`** 当用户尝试向对端发送数据时，协议栈收到了中止消息。

**`[ENOENT]`** 在一对多风格套接字上未指定地址，因此无法定位关联；或者在非现有关联上指定了 `SCTP_ABORT` 标志。

**`[EPIPE]`** 套接字无法再发送数据（套接字上已设置 `SBS_CANTSENDMORE`）。这通常表示套接字未连接且为一对一风格套接字。

## 参见

[connect(2)](../sys/connect.2.md), [getsockopt(2)](../sys/getsockopt.2.md), [recv(2)](../sys/recv.2.md), [select(2)](../sys/select.2.md), sendmsg(2), [socket(2)](../sys/socket.2.md), [write(2)](../sys/write.2.md), [sctp_connectx(3)](sctp_connectx.3.md), [sctp(4)](../man4/sctp.4.md)

## 缺陷

由于在一对多风格套接字上 `sctp_sendmsg` 或 `sctp_sendmsgx` 在一个端点下可能有多个关联，对写入的 select 仅对一对一风格套接字有效。
