# mq_notify(2)

`mq_notify` — 通知进程有消息可用（REALTIME）

## 名称

`mq_notify`

## 库

Lb librt

## 概要

`#include <mqueue.h>`

```c
int
mq_notify(mqd_t mqdes, const struct sigevent *notification);
```

## 描述

如果参数 notification 不是 `NULL`，此系统调用将注册调用进程，以便在与指定消息队列描述符 `mqdes` 关联的空消息队列有消息到达时收到通知。当消息队列从空转为非空时，由 `notification` 参数指定的通知将发送给该进程。在任何时候，一个消息队列只能有一个进程注册接收通知。如果调用进程或任何其他进程已经注册了指定消息队列的消息到达通知，后续尝试注册该消息队列将会失败。

`notification` 参数指向一个 `sigevent` 结构，该结构定义了调用进程将如何被通知。如果 `notification->sigev_notify` 为 `SIGEV_NONE`，则不会发送信号，但错误状态和操作返回状态会被适当设置。对于 `SIGEV_SIGNO` 和 `SIGEV_THREAD_ID` 通知，`notification->sigev_signo` 中指定的信号将发送给调用进程（`SIGEV_SIGNO`）或发送给 LWP ID 为 `notification->sigev_notify_thread_id` 的线程（`SIGEV_THREAD_ID`）。排队信号的信息将包括：

| Member | Value |
| --- | --- |
| `si_code` | `SI_MESGQ` |
| `si_value` | 存储在 `notification->sigev_value` 中的值 |
| `si_mqd` | `mqdes` |

如果 `notification` 为 `NULL` 且进程当前已注册了指定消息队列的通知，则现有的注册将被移除。

当通知发送给已注册的进程时，其注册将被移除。该消息队列随后可用于重新注册。

如果一个进程已注册了消息队列的消息到达通知，且当消息到达队列时某个线程正阻塞在 `mq_receive()` 中等待接收消息，则到达的消息将满足相应的 `mq_receive()`。其结果行为就如同消息队列仍然为空一样，不会发送通知。

## 返回值

若成功，`mq_notify()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mq_notify()` 系统调用在以下情况下会失败：

**[`EBADF`]** `mqdes` 参数不是有效的消息队列描述符。

**[`EBUSY`]** 进程已经注册了该消息队列的通知。

**[`EINVAL`]** `notification->sigev_notify` 中的异步通知方法无效或不受支持。

## 参见

[mq_open(2)](mq_open.2.md), [mq_send(2)](mq_send.2.md), [mq_timedsend(2)](mq_send.2.md), [sigevent(3)](../man3/sigevent.3.md), [siginfo(3)](../man3/siginfo.3.md)

## 标准

`mq_notify()` 系统调用遵循 IEEE Std 1003.1-2004 ("POSIX.1") 标准。

## 历史

对 POSIX 消息队列的支持首次出现于 FreeBSD 7.0。

## COPYRIGHT

Portions of this text are reprinted and reproduced in electronic form from IEEE Std 1003.1, 2004 Edition, Standard for Information Technology -- Portable Operating System Interface (POSIX), The Open Group Base Specifications Issue 6, Copyright (C) 2001-2004 by the Institute of Electrical and Electronics Engineers, Inc and The Open Group. In the event of any discrepancy between this version and the original IEEE and The Open Group Standard, the original IEEE and The Open Group Standard is the referee document. The original Standard can be obtained online at http://www.opengroup.org/unix/online.html.
