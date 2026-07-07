# msgsnd(2)

`msgsnd` — 向消息队列发送消息

## 名称

`msgsnd`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/ipc.h>`

`#include <sys/msg.h>`

```c
int
msgsnd(int msqid, const void *msgp, size_t msgsz, int msgflg);
```

## 描述

`msgsnd()` 函数向 `msqid` 指定的消息队列发送消息。`msgp` 参数指向包含该消息的结构。此结构应包含以下成员：

```c
    long mtype;    /* 消息类型 */
    char mtext[1]; /* 消息正文 */
```

`mtype` 是一个大于 0 的整数，可用于选择消息（参见 [msgrcv(2)](msgrcv.2.md)），`mtext` 是一个长度为 `msgsz` 字节的数组。参数 `msgsz` 的取值范围从 0 到系统规定的上限 `MSGMAX`。

如果消息队列上已有的字节数加上 `msgsz` 大于消息队列上的最大字节数（`msg_qbytes`，参见 [msgctl(2)](msgctl.2.md)），或者全系统所有队列上的消息数量已等于系统限制，`msgflg` 决定 `msgsnd()` 的行为。如果 `msgflg` 中设置了 `IPC_NOWAIT` 掩码，调用将立即返回。如果 `msgflg` 中未设置 `IPC_NOWAIT`，调用将阻塞直到：

- 导致调用阻塞的条件不再存在。消息将被发送。
- 消息队列被删除，此时返回 -1，并将 `errno` 设置为 `EINVAL`。
- 调用者捕获到信号。调用返回时将 `errno` 设置为 `EINTR`。

成功调用后，与消息队列关联的数据结构将按以下方式更新：

- `msg_cbytes` 增加消息的大小。
- `msg_qnum` 增加 1。
- `msg_lspid` 设置为调用进程的 pid。
- `msg_stime` 设置为当前时间。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

`msgsnd()` 函数在以下情况下会失败：

**[EINVAL]** `msqid` 参数不是有效的消息队列标识符。消息队列在 `msgsnd()` 等待资源变为可用以投递消息时被删除。`msgsz` 参数大于 `msg_qbytes`。`mtype` 参数不大于 0。

**[EACCES]** 调用进程没有对消息队列的写访问权限。

**[EAGAIN]** 队列上或整个系统中没有空间容纳此消息，且 `msgflg` 中设置了 `IPC_NOWAIT`。

**[EFAULT]** `msgp` 参数指向无效地址。

**[EINTR]** 系统调用被信号传递所中断。

## 历史

消息队列出现于 AT&T Unix System V 的第一个版本。

## 缺陷

NetBSD 和 FreeBSD 未定义 `EIDRM` 错误值，该值应在消息队列被删除的情况下使用。
