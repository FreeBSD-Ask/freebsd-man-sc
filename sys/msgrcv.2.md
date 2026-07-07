# msgrcv(2)

`msgrcv` — 从消息队列接收消息

## 名称

`msgrcv`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/ipc.h>`

`#include <sys/msg.h>`

```c
ssize_t
msgrcv(int msqid, void *msgp, size_t msgsz, long msgtyp,
    int msgflg);
```

## 描述

`msgrcv()` 函数从 `msqid` 指定的消息队列中接收消息，并将其放入 `msgp` 所指向的结构中。该结构应包含以下成员：

```c
    long mtype;    /* 消息类型 */
    char mtext[1]; /* 消息正文 */
```

`mtype` 是一个大于 0 的整数，可用于选择消息；`mtext` 是一个字节数组，大小上限为系统限制（`MSGMAX`）。

`msgtyp` 的值有以下含义之一：

- `msgtyp` 参数大于 0。将接收类型为 `msgtyp` 的第一条消息。
- `msgtyp` 参数等于 0。将接收队列上的第一条消息。
- `msgtyp` 参数小于 0。将接收消息类型小于或等于 `msgtyp` 绝对值的最低类型的第一条消息。

`msgsz` 参数指定请求消息的最大长度。如果接收到的消息长度大于 `msgsz`，当 `msgflg` 中设置了 `MSG_NOERROR` 标志时，消息会被静默截断，否则返回错误。

如果 `msqid` 指定的消息队列中没有匹配的消息，`msgrcv()` 的行为取决于 `msgflg` 中是否设置了 `IPC_NOWAIT` 标志。如果设置了 `IPC_NOWAIT`，`msgrcv()` 会立即返回 -1，并将 `errno` 设置为 `ENOMSG`。如果未设置 `IPC_NOWAIT`，调用进程将被阻塞，直到：

- 请求类型的消息在消息队列中可用。
- 消息队列被删除，此时返回 -1，`errno` 设置为 `EINVAL`。
- 收到并捕获信号。返回 -1，`errno` 设置为 `EINTR`。

如果成功接收到消息，与 `msqid` 关联的数据结构将作如下更新：

- `msg_cbytes` 减去消息大小。
- `msg_lrpid` 设置为调用者的 pid。
- `msg_lrtime` 设置为当前时间。
- `msg_qnum` 减 1。

## 返回值

成功完成时，`msgrcv()` 返回接收到 `msgp` 所指向结构的 `mtext` 字段中的字节数。否则，返回 -1，并设置 `errno` 以指示错误。

## 错误

`msgrcv()` 函数在以下情况下会失败：

**[`EINVAL`]** `msqid` 参数不是有效的消息队列标识符。消息队列在 `msgrcv()` 等待请求类型的消息可用期间被删除。`msgsz` 参数小于 0。

**[`E2BIG`]** 收到匹配的消息，但其大小大于 `msgsz`，且 `msgflg` 中未设置 `MSG_NOERROR` 标志。

**[`EACCES`]** 调用进程对该消息队列没有读访问权限。

**[`EFAULT`]** `msgp` 参数指向无效地址。

**[`EINTR`]** 系统调用被信号传递中断。

**[`ENOMSG`]** 消息队列中没有请求类型的消息可用，且 `msgflg` 中设置了 `IPC_NOWAIT`。

## 参见

[msgctl(2)](msgctl.2.md), [msgget(2)](msgget.2.md), [msgsnd(2)](msgsnd.2.md)

## 历史

消息队列首次出现于 AT&T System V UNIX 的第一个版本。
