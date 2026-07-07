# sctp_send(3)

`sctp_send` — 从 SCTP 套接字发送消息

## 名称

`sctp_send`, `sctp_sendx`, `sctp_sendv`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
ssize_t
sctp_send(int sd, const void *msg, size_t len,
    const struct sctp_sndrcvinfo *sinfo, int flags);

ssize_t
sctp_sendx(int sd, const void *msg, size_t len, struct sockaddr *addrs,
    int addrcnt, const struct sctp_sndrcvinfo *sinfo, int flags);

ssize_t
sctp_sendv(int sd, const struct iovec *iov, int iocnt,
    struct sockaddr *addrs, int addrcnt, void *info, socklen_t infolen,
    unsigned int infotype, int flags);
```

## 描述

`sctp_send` 系统调用用于向另一个 SCTP 端点传输消息。`sctp_sendx` 函数用于在创建隐式关联时指定多个对端地址，如 [sctp_connectx(3)](sctp_connectx.3.md) 中所述。`sctp_sendv` 函数用于传输数据从提供的 I/O 缓冲区中收集的消息。

`sctp_send` 可用于向一对多（SOCK_SEQPACKET）和一对一（SOCK_STREAM）套接字类型的现有关联发送数据。消息 `msg` 的长度由 `len` 给出。如果消息太长而无法通过底层协议原子地传递，则 `errno` 被设置为 `EMSGSIZE`，返回 -1，且消息不会被传输。

`sctp_send` 中不隐含传递失败的指示。本地检测到的错误由返回值 -1 指示。

如果套接字上没有可用空间来保存待传输的消息，则 `sctp_send` 通常会阻塞，除非套接字已置于非阻塞 I/O 模式。可以使用 [select(2)](../sys/select.2.md) 系统调用来确定何时可以在一对一类型（SOCK_STREAM）套接字上发送更多数据。

`sinfo` 结构用于控制各种 SCTP 特性，格式如下：

```c
struct sctp_sndrcvinfo {
	uint16_t sinfo_stream;  /* 发送到的流 */
	uint16_t sinfo_ssn;     /* 仅用于接收 */
	uint16_t sinfo_flags;   /* 控制发送的标志 */
	uint32_t sinfo_ppid;    /* ppid 字段 */
	uint32_t sinfo_context; /* 上下文字段 */
	uint32_t sinfo_timetolive; /* PR-SCTP 的生存时间 */
	uint32_t sinfo_tsn;        /* 仅用于接收 */
	uint32_t sinfo_cumtsn;     /* 仅用于接收 */
	sctp_assoc_t sinfo_assoc_id; /* 关联 ID */
};
```

`sinfo->sinfo_ppid` 参数是一个不透明的 32 位值，通过协议栈透明地传递到对端端点。它将在接收到消息时可用（见 [sctp_recvmsg(3)](sctp_recvmsg.3.md)）。注意，协议栈传递此值时不考虑字节序。

`sinfo->sinfo_flags` 参数可能包含以下一个或多个值：

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

`SCTP_PR_SCTP_TTL` 用于指示对数据应用基于时间的生存期。`sinfo->sinfo_timetolive` 参数则是尝试传输数据的毫秒数。如果经过这么多毫秒且对端未确认数据，则数据将被跳过且不再传输。注意，此策略甚至不保证数据会被发送。在大量数据排队拥塞的情况下，`sinfo->sinfo_timetolive` 可能在第一次传输之前就已过期。

基于 `SCTP_PR_SCTP_BUF` 的策略将 `sinfo->sinfo_timetolive` 字段转换为出站发送队列上允许的总字节数。如果队列中的字节数达到或超过此数量，则会查找其他基于缓冲区的发送并将其移除和跳过。注意，如果队列中没有基于缓冲区的发送且队列中已达到 `timetolive` 指定的最大字节数，此策略也可能导致数据永远不会被发送。

`SCTP_PR_SCTP_RTX` 策略将 `sinfo->sinfo_timetolive` 转换为允许的重传次数。此策略始终保证至少对数据进行一次发送尝试。之后，在数据被跳过之前，重传次数不超过 `sinfo->sinfo_timetolive` 次。

`sinfo->sinfo_stream` 是你希望发送消息的 SCTP 流。SCTP 中的流是可靠（或部分可靠）的有序消息流。

`sinfo->sinfo_assoc_id` 字段用于在一对多套接字上选择要发送到的关联。对于一对一套接字，此字段被忽略。

`sinfo->sinfo_context` 字段仅在消息无法发送时使用。这是一个不透明的值，由协议栈保留，并在启用了通知的情况下，当发送失败时提供给用户（见 [sctp(4)](../man4/sctp.4.md)）。通常，用户进程可以使用此值在发送无法完成时索引某些特定于应用程序的数据结构。

`flags` 参数的含义和值与 sendmsg(2) 中的相同，但通常被 SCTP 忽略。

字段 `sinfo->sinfo_ssn`、`sinfo->sinfo_tsn` 和 `sinfo->sinfo_cumtsn` 仅在接收消息时使用，因此被 `sctp_send` 忽略。

`sctp_sendx` 函数具有与 `sctp_send` 相同的属性，但增加了传入 sockaddr 结构数组作为附加参数。`addrs` 参数作为要发送到的地址数组给出，`addrcnt` 参数指示传入数组中有多少个套接字地址。注意，所有地址仅在设置隐式关联时使用。这允许用户获得相当于执行 `sctp_connectx` 后对关联执行 `sctp_send` 的行为。注意，如果 `sinfo->sinfo_assoc_id` 字段为 0，则使用第一个地址来查找关联以代替关联 ID。如果同时指定了地址和关联 ID，则关联 ID 优先。

`sctp_sendv` 函数的工作方式与 `sctp_sendx` 相同，但有两个区别。首先，要写入的数据以包含 `iocnt` 个 `struct iovec` 类型对象的数组形式传递，将以与 writev(2) 相同的方式聚集发送。其次，`info` 参数被元组 `sinfo`、`infolen`、`infotype` 替换，其中 `sinfo` 是指向大小为 `infolen` 的结构的指针，其类型由 `infotype` 参数指示。

如果未传递任何信息，将 `infotype` 设置为 `SCTP_SENDV_NOINFO`。`sinfo` 可以为空指针。

如果 `sinfo` 指向 `struct sctp_sndinfo`，将 `infotype` 设置为 `SCTP_SENDV_SNDINFO`。`sctp_sndinfo` 结构具有以下格式：

```c
struct sctp_sndinfo {
	uint16_t snd_sid;		/* 流标识 */
	uint16_t snd_flags;		/* 标志 */
	uint32_t snd_ppid;		/* ppid 字段 */
	uint32_t snd_context;		/* 上下文字段 */
	sctp_assoc_t snd_assoc_id;	/* 关联 ID */
};
```

这些字段的含义与上文描述的 `struct sctp_sndrcvinfo` 中的相同。

如果 `sinfo` 指向 `struct sctp_authinfo`，将 `infotype` 设置为 `SCTP_SENDV_AUTHINFO`。`sctp_authinfo` 结构具有以下格式：

```c
struct sctp_authinfo {
	uint16_t auth_keynumber;	/* 共享密钥标识 */
};
```

`auth_keynumber` 字段指定用于发送消息的共享密钥标识。

如果 `sinfo` 指向 `struct sctp_prinfo`，将 `infotype` 设置为 `SCTP_SENDV_PRINFO`。`sctp_prinfo` 结构具有以下格式：

```c
struct sctp_prinfo {
	uint16_t pr_policy;	/* PR-SCTP 策略 */
	uint32_t pr_value;	/* PR-SCTP 策略选项 */
};
```

`pr_policy` 字段应设置为 `SCTP_PR_SCTP_NONE` 以使用可靠传输（在这种情况下字段 `pr_value` 被忽略），或 `SCTP_PR_SCTP_TTL` 以使用 RFC 3758 定时可靠性，在这种情况下字段 `pr_value` 包含以毫秒为单位的生存期。

要在 `sinfo` 中传递两种或更多类型，将 `infotype` 设置为 `SCTP_SENDV_SPA` 并在 `sinfo` 中传递指向 `struct sctp_sendv_spa` 的指针。`sctp_sendv_spa` 结构具有以下格式：

```c
struct sctp_sendv_spa {
	uint32_t sendv_flags;
	struct sctp_sndinfo sendv_sndinfo;
	struct sctp_prinfo sendv_prinfo;
	struct sctp_authinfo sendv_authinfo;
};
```

`sendv_flags` 成员应设置为标志 `SCTP_SEND_SNDINFO_VALID`、`SCTP_SEND_PRINFO_VALID` 和 `SCTP_SEND_AUTHINFO_VALID` 的按位或，以指示结构的哪些字段包含有效数据。

如果 `infotype` 设置为 `SCTP_SENDV_NOINFO`，`infolen` 参数应设置为零。否则，`infolen` 应设置为 `info` 所指向的数据结构的长度。

## 返回值

调用返回发送的字符数，出错时返回 -1。

## 错误

`sctp_send` 系统调用在以下情况失败：

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

## 注释

`sctp_send` 和 `sctp_sendx` 函数已弃用。新应用程序应使用 `sctp_sendv`。

## 参见

[getsockopt(2)](../sys/getsockopt.2.md), [recv(2)](../sys/recv.2.md), [select(2)](../sys/select.2.md), sendmsg(2), [socket(2)](../sys/socket.2.md), [write(2)](../sys/write.2.md), [sctp_connectx(3)](sctp_connectx.3.md), [sctp_recvmsg(3)](sctp_recvmsg.3.md), [sctp_sendmsg(3)](sctp_sendmsg.3.md), [sctp(4)](../man4/sctp.4.md)

> R. Stewart, M. Tuexen, K. Poon, P. Lei, V. Yasevich, "Sockets API Extensions for the Stream Control Transmission Protocol (SCTP)", December 2011.

## 标准

本文档中所述函数遵循 RFC 6458。

## 缺陷

由于 `sctp_send` 在一个端点下可能有多个关联，对写入的 select 仅对一对一风格套接字有效。
