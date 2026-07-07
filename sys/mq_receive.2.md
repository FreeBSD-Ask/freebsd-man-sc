# mq_receive(2)

`mq_receive` — 从消息队列接收消息 (REALTIME)

## 名称

`mq_receive`

## 库

Lb librt

## 概要

`#include <mqueue.h>`

```c
ssize_t
mq_receive(mqd_t mqdes, char *msg_ptr, size_t msg_len,
    unsigned *msg_prio);

ssize_t
mq_timedreceive(mqd_t mqdes, char *msg_ptr, size_t msg_len,
    unsigned *msg_prio, const struct timespec *abs_timeout);
```

## 描述

`mq_receive()` 系统调用从 `mqdes` 指定的消息队列中接收最高优先级消息中最旧的一条。如果 `msg_len` 参数指定的缓冲区大小（以字节为单位）小于消息队列的 `mq_msgsize` 属性，系统调用将失败并返回错误。否则，选中的消息将从队列中移除并复制到 `msg_ptr` 参数所指向的缓冲区。

如果 `msg_prio` 参数不是 `NULL`，选中消息的优先级将存储在 `msg_prio` 所引用的位置。如果指定的消息队列为空，且与 `mqdes` 关联的消息队列描述中未设置 `O_NONBLOCK`，`mq_receive()` 将阻塞，直到消息队列中有消息入队或 `mq_receive()` 被信号中断。如果多个线程在等待接收消息，且支持优先级调度选项，当消息到达空队列时，等待时间最长且优先级最高的线程将被选中接收消息。否则，未指定哪个等待线程接收消息。如果指定的消息队列为空，且与 `mqdes` 关联的消息队列描述中设置了 `O_NONBLOCK`，则不会从队列中移除任何消息，`mq_receive()` 将返回错误。

`mq_timedreceive()` 系统调用从 `mqdes` 指定的消息队列中接收最高优先级消息中最旧的一条，如 `mq_receive()` 系统调用所述。但是，如果通过 `mq_open()` 系统调用打开消息队列时未指定 `O_NONBLOCK`，且队列中没有满足接收条件的消息，则当指定的超时到期时，等待此类消息的过程将终止。如果设置了 `O_NONBLOCK`，此系统调用等效于 `mq_receive()`。

当 `abs_timeout` 指定的绝对时间过去时（按超时所基于的时钟测量，即该时钟的值等于或超过 `abs_timeout` 时），或在调用时 `abs_timeout` 指定的绝对时间已经过去，则超时到期。

超时基于 `CLOCK_REALTIME` 时钟。

## 返回值

成功完成时，`mq_receive()` 和 `mq_timedreceive()` 系统调用返回选中消息的长度（以字节为单位），并将该消息从队列中移除。否则，不会从队列中移除任何消息，系统调用返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mq_receive()` 和 `mq_timedreceive()` 系统调用在以下情况下会失败：

**[`EAGAIN`]** 与 `mqdes` 关联的消息队列描述中设置了 `O_NONBLOCK` 标志，且指定的消息队列为空。

**[`EBADF`]** `mqdes` 参数不是有效的、为读取而打开的消息队列描述符。

**[`EMSGSIZE`]** 指定的消息缓冲区大小 `msg_len` 小于消息队列的消息大小属性。

**[`EINTR`]** `mq_receive()` 或 `mq_timedreceive()` 操作被信号中断。

**[`EINVAL`]** 进程或线程本应阻塞，且 `abs_timeout` 参数指定的纳秒字段值小于零或大于等于 10 亿。

**[`ETIMEDOUT`]** 打开消息队列时未设置 `O_NONBLOCK` 标志，但在指定超时到期之前没有消息到达队列。

## 参见

[mq_open(2)](mq_open.2.md), [mq_send(2)](mq_send.2.md), mq_timedsend(2)

## 标准

`mq_receive()` 和 `mq_timedreceive()` 系统调用遵循 IEEE Std 1003.1-2004 ("POSIX.1")。

## 历史

对 POSIX 消息队列的支持首次出现于 FreeBSD 7.0。

## COPYRIGHT

本文部分内容转载并复现自 IEEE Std 1003.1, 2004 Edition, Standard for Information Technology -- Portable Operating System Interface (POSIX), The Open Group Base Specifications Issue 6, Copyright (C) 2001-2004 by the Institute of Electrical and Electronics Engineers, Inc and The Open Group。如果本版本与原始 IEEE 和 The Open Group 标准之间存在任何差异，以原始 IEEE 和 The Open Group 标准为准。原始标准可从 http://www.opengroup.org/unix/online.html 在线获取。
