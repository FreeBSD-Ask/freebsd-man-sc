# mq_send(2)

`mq_send` — 向消息队列发送消息（REALTIME）

## 名称

`mq_send`, `mq_timedsend`

## 库

Lb librt

## 概要

`#include <mqueue.h>`

```c
int
mq_send(mqd_t mqdes, const char *msg_ptr, size_t msg_len,
    unsigned msg_prio);

int
mq_timedsend(mqd_t mqdes, const char *msg_ptr, size_t msg_len,
    unsigned msg_prio, const struct timespec *abs_timeout);
```

## 描述

`mq_send()` 系统调用将参数 `msg_ptr` 所指向的消息添加到由 `mqdes` 指定的消息队列中。`msg_len` 参数指定 `msg_ptr` 所指向消息的长度（以字节为单位）。`msg_len` 的值应小于或等于消息队列的 `mq_msgsize` 属性，否则 `mq_send()` 将失败。

如果指定的消息队列未满，`mq_send()` 会将消息插入到消息队列中由 `msg_prio` 参数指示的位置。`msg_prio` 数值较大的消息会插入到 `msg_prio` 值较小的消息之前。消息会插入到队列中具有相同 `msg_prio` 的其他消息（如果有）之后。`msg_prio` 的值应小于 `{MQ_PRIO_MAX}`。

如果指定的消息队列已满，且与 `mqdes` 关联的消息队列描述中未设置 `O_NONBLOCK`，`mq_send()` 将阻塞，直到有空间可用于将消息入队，或者 `mq_send()` 被信号中断。如果有多个线程在等待发送，而消息队列中变为可用空间，且支持优先级调度选项，则等待时间最长且优先级最高的线程将被解除阻塞以发送其消息。否则，未指定哪个等待线程被解除阻塞。如果指定的消息队列已满，且与 `mqdes` 关联的消息队列描述中设置了 `O_NONBLOCK`，则消息不会入队，`mq_send()` 将返回错误。

`mq_timedsend()` 系统调用按为 `mq_send()` 系统调用定义的方式，将消息添加到由 `mqdes` 指定的消息队列中。但是，如果指定的消息队列已满，且与 `mqdes` 关联的消息队列描述中未设置 `O_NONBLOCK`，则当指定的超时到期时，等待队列中有足够空间的操作将被终止。如果消息队列描述中设置了 `O_NONBLOCK`，此系统调用等价于 `mq_send()`。

当 `abs_timeout` 所指定的绝对时间过去时（以超时所基于的时钟来衡量，即当该时钟的值等于或超过 `abs_timeout` 时），或者在调用时 `abs_timeout` 所指定的绝对时间已经过去时，超时将到期。

超时基于 `CLOCK_REALTIME` 时钟。

## 返回值

成功完成时，`mq_send()` 和 `mq_timedsend()` 系统调用返回零。否则，不会入队任何消息，系统调用返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mq_send()` 和 `mq_timedsend()` 系统调用在以下情况下会失败：

**[EAGAIN]** 与 `mqdes` 关联的消息队列描述中设置了 `O_NONBLOCK` 标志，且指定的消息队列已满。

**[EBADF]** `mqdes` 参数不是为写入打开的有效消息队列描述符。

**[EINTR]** 信号中断了对 `mq_send()` 或 `mq_timedsend()` 的调用。

**[EINVAL]** `msg_prio` 的值超出有效范围。

**[EINVAL]** 进程或线程本应阻塞，且 `abs_timeout` 参数指定的纳秒字段值小于零或大于等于 10 亿。

**[EMSGSIZE]** 指定的消息长度 `msg_len` 超过了消息队列的消息大小属性。

**[ETIMEDOUT]** 打开消息队列时未设置 `O_NONBLOCK` 标志，但在消息能被添加到队列之前超时已到期。

## 参见

[mq_open(2)](mq_open.2.md), [mq_receive(2)](mq_receive.2.md), [mq_setattr(2)](mq_setattr.2.md), [mq_timedreceive(2)](mq_receive.2.md)

## 标准

`mq_send()` 和 `mq_timedsend()` 系统调用遵循 IEEE Std 1003.1-2004 ("POSIX.1")。

## 历史

对 POSIX 消息队列的支持首次出现于 FreeBSD 7.0。

## 版权

本文部分内容转载并复制自 IEEE Std 1003.1, 2004 Edition, Standard for Information Technology -- Portable Operating System Interface (POSIX), The Open Group Base Specifications Issue 6, Copyright (C) 2001-2004 by the Institute of Electrical and Electronics Engineers, Inc and The Open Group。如果本版本与原始 IEEE 及 The Open Group 标准之间存在任何差异，以原始 IEEE 及 The Open Group 标准为准。原始标准可在线获取：http://www.opengroup.org/unix/online.html。
