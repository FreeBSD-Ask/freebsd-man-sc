# sctp_recvmsg(3)

`sctp_recvmsg` — 从 SCTP 套接字接收消息

## 名称

`sctp_recvmsg`, `sctp_recvv`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
ssize_t
sctp_recvmsg(int s, void *msg, size_t len, struct sockaddr *from,
    socklen_t *fromlen, struct sctp_sndrcvinfo *sinfo, int *flags);

ssize_t
sctp_recvv(int s, const struct iovec *iov, int iovlen, struct sockaddr *from,
    socklen_t *fromlen, void *info, socklen_t *infolen,
    unsigned int *infotype, int *flags);
```

## 描述

`sctp_recvmsg` 和 `sctp_recvv` 函数用于从另一个 SCTP 端点接收消息。它们用于一对一（SOCK_STREAM）类型套接字，在成功调用 `connect` 之后，或应用程序执行 `listen` 并随后成功 `accept` 之后使用。对于一对多（SOCK_SEQPACKET）类型套接字，端点可以在通过发送调用（包括 `sctp_sendmsg`、`sendto` 和 `sendmsg`）隐式启动关联后调用 `sctp_recvmsg` 或 `sctp_recvv`。或者，应用程序也可以在调用 `listen` 并使用正的 backlog 值以启用新关联的接收之后接收消息。

发送者的地址保存在 `from` 参数中，`fromlen` 指定其大小。成功完成 `sctp_recvmsg` 调用时，`from` 将保存对端地址，`fromlen` 将保存该地址的长度。注意，地址受 `fromlen` 初始值的限制，该参数用作输入/输出变量。

要接收的消息 `msg` 的长度受 `len` 限制。如果消息太长而无法容纳在用户的接收缓冲区中，则 `flags` 参数*不会*应用 `MSG_EOR` 标志。如果消息是完整消息，则 `flags` 参数将设置 `MSG_EOR`。本地检测到的错误由返回值 -1 指示，并相应地设置 `errno`。`flags` 参数还可以持有值 `MSG_NOTIFICATION`。当出现此情况时，表示接收到的消息*不是*来自对端端点，而是来自 SCTP 协议栈的通知（更多细节见 [sctp(4)](../man4/sctp.4.md)）。注意，除非用户使用 `SCTP_EVENTS` 套接字选项订阅了此类通知，否则永远不会给出任何通知。

如果套接字上没有可用消息，则 `sctp_recvmsg` 通常会阻塞等待消息或通知的接收，除非套接字已置于非阻塞 I/O 模式。可以使用 [select(2)](../sys/select.2.md) 系统调用来确定何时可以接收消息。

`sinfo` 参数定义如下。

```c
struct sctp_sndrcvinfo {
	uint16_t sinfo_stream;  /* 到达的流 */
	uint16_t sinfo_ssn;     /* 流序列号 */
	uint16_t sinfo_flags;   /* 传入消息的标志 */
	uint32_t sinfo_ppid;    /* ppid 字段 */
	uint32_t sinfo_context; /* 上下文字段 */
	uint32_t sinfo_timetolive; /* sctp_recvmsg 不使用 */
	uint32_t sinfo_tsn;        /* 传输序列号 */
	uint32_t sinfo_cumtsn;     /* 累计确认点 */
	sctp_assoc_t sinfo_assoc_id; /* 对端的关联 ID */
};
```

`sinfo->sinfo_ppid` 字段是一个不透明的 32 位值，从对端端点透明地通过协议栈传递。注意，协议栈传递此值时不考虑字节序。

`sinfo->sinfo_flags` 字段可能包含以下内容：

```c
#define SCTP_UNORDERED 	  0x0400	/* 消息是无序的 */
```

`SCTP_UNORDERED` 标志用于指定消息到达时没有特定顺序，并尽快传递给对端应用程序。当此标志不存在时，消息在接收到的流中按顺序传递。

`sinfo->sinfo_stream` 字段是接收消息的 SCTP 流。SCTP 中的流是可靠（或部分可靠）的有序消息流。

`sinfo->sinfo_context` 字段仅在本地应用程序使用 `SCTP_CONTEXT` 套接字选项设置了关联级别上下文时使用。用户进程可以选择使用此值来索引特定于应用程序的数据结构，以处理来自特定关联的所有数据。

如果消息*不是*无序的，`sinfo->sinfo_ssn` 字段将保存由对端端点分配的流序列号。对于无序消息，此字段保存未定义的值。

`sinfo->sinfo_tsn` 字段保存由对端端点分配给此消息的传输序列号（TSN）。对于小于或等于路径 MTU 的消息，这将是唯一分配的 TSN。注意，对于跨多个 TSN 的消息，此值将是该消息上使用的 TSN 之一。

`sinfo->sinfo_cumtsn` 字段保存传输关联的当前累计确认点。注意，此值可能大于或小于分配给消息本身的 TSN。

`sinfo->sinfo_assoc_id` 是分配给关联的唯一关联标识。对于一对多（SOCK_SEQPACKET）类型套接字，此值可用于在不使用地址字段的情况下向对端发送数据。它在为特定关联设置各种套接字选项时也非常有用（见 [sctp(4)](../man4/sctp.4.md)）。

`sinfo->info_timetolive` 字段不被 `sctp_recvmsg` 使用。

`sctp_recvv` 函数的工作方式与 `sctp_recvmsg` 相同，但有两个区别。首先，接收缓冲区以包含 `iovlen` 个 `struct iovec` 类型对象的数组形式传递，接收到的数据将以与 readv(2) 相同的方式分散存放。其次，`sinfo` 参数被元组 `info`、`infolen` 和 `infotype` 替换，允许根据套接字选项接收不同的信息。

要接收 `sctp_rcvinfo` 结构，设置 `SCTP_RECVRCVINFO` 套接字选项，并在 `info` 中传递指向 `struct sctp_rcvinfo` 结构的指针。`sctp_rcvinfo` 结构具有以下格式：

```c
struct sctp_rcvinfo {
	uint16_t rcv_sid;		/* 到达的流 */
	uint16_t rcv_ssn;		/* 流序列号 */
	uint16_t rcv_flags;		/* 传入消息的标志 */
	uint32_t rcv_ppid;		/* ppid 字段 */
	uint32_t rcv_tsn;		/* 传输序列号 */
	uint32_t rcv_cumtsn;		/* 累计 TSN */
	uint32_t rcv_context;		/* 不透明的上下文字段 */
	sctp_assoc_t rcv_assoc_id;	/* 对端关联 ID */
};
```

这些字段与上文定义的 `struct sctp_sndrcvinfo` 中的等效字段具有相同含义。

要接收 `sctp_nxtinfo` 结构，设置 `SCTP_RECVNXTINFO` 套接字选项，并在 `info` 中传递指向 `struct sctp_nxtinfo` 结构的指针。`struct sctp_nxtinfo` 结构具有以下格式：

```c
struct sctp_nxtinfo {
	uint16_t nxt_sid;		/* 下一条消息的流号 */
	uint16_t nxt_flags;		/* 标志（见下文） */
	uint32_t nxt_ppid;		/* ppid 字段 */
	uint32_t nxt_length;		/* 下一条消息的长度 */
	sctp_assoc_t nxt_assoc_id;	/* 对端关联 ID */
};
```

字段 `nxt_sid`、`nxt_ppid` 和 `nxt_assoc_id` 与 `struct sctp_rcvinfo` 中的含义相同，但它们引用的是下一条消息而非已接收的消息。字段 `nxt_length` 包含当前在套接字缓冲区中可用的下一条消息部分的长度。除非在 `nxt_flags` 中设置了 `SCTP_COMPLETE` 标志，否则这不一定代表整个消息的长度。

`nxt_flags` 字段是一个位掩码，可能包含以下任何值：

- `SCTP_UNORDERED`：下一条消息是无序发送的。
- `SCTP_COMPLETE`：下一条消息的全部内容已接收到套接字缓冲区中。在此情况下，`nxt_length` 字段包含整个消息的长度。
- `SCTP_NOTIFICATION`：下一条消息是通知，而非用户消息。

如果同时设置了 `SCTP_RECVRCVINFO` 和 `SCTP_RECVNXTINFO` 套接字选项，则在 `info` 中传递指向 `struct sctp_recvv_rn` 结构的指针。此结构具有以下格式：

```c
struct sctp_recvv_rn {
	struct sctp_rcvinfo recvv_rcvinfo;
	struct sctp_nxtinfo recvv_nxtinfo;
};
```

`infolen` 所指向的值最初应包含 `info` 所指向结构的长度。函数返回时，该值将被设置为返回结构的长度。此外，`*infotype` 将根据返回的信息类型设置为以下值之一：

- `SCTP_RECVV_NOINFO`：未返回任何信息。
- `SCTP_RECVV_RCVINFO`：`*info` 包含 `struct sctp_rcvinfo` 类型的对象。
- `SCTP_RECVV_NXTINFO`：`*info` 包含 `struct sctp_nxtinfo` 类型的对象。
- `SCTP_RECVV_RN`：`*info` 包含 `struct sctp_recvv_rn` 类型的对象。

## 返回值

调用返回接收到的字节数，出错时返回 -1。

## 错误

`sctp_recvmsg` 系统调用在以下情况失败：

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

**`[ENOENT]`** 在一对多风格套接字上未指定地址，因此无法定位关联；或者在非现有关联上指定了 SCTP_ABORT 标志。

**`[EPIPE]`** 套接字无法再发送数据（套接字上已设置 `SBS_CANTSENDMORE`）。这通常表示套接字未连接且为一对一风格套接字。

## 注释

`sctp_recvmsg` 函数已弃用。新应用程序应使用 `sctp_recvv`。

## 参见

[getsockopt(2)](../sys/getsockopt.2.md), [recv(2)](../sys/recv.2.md), [select(2)](../sys/select.2.md), sendmsg(2), setsockopt(2), [socket(2)](../sys/socket.2.md), [write(2)](../sys/write.2.md), [sctp_send(3)](sctp_send.3.md), [sctp_sendmsg(3)](sctp_sendmsg.3.md), [sctp(4)](../man4/sctp.4.md)

> R. Stewart, M. Tuexen, K. Poon, P. Lei, V. Yasevich, "Sockets API Extensions for the Stream Control Transmission Protocol (SCTP)", December 2011.

## 标准

本文档中所述函数遵循 RFC 6458。
