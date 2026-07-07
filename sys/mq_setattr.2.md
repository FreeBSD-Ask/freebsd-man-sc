# mq_setattr(2)

`mq_setattr` — 设置消息队列属性 (REALTIME)

## 名称

`mq_setattr`

## 库

Lb librt

## 概要

```c
#include <mqueue.h>

int
mq_setattr(mqd_t mqdes, const struct mq_attr *restrict mqstat,
    struct mq_attr *restrict omqstat);
```

## 描述

`mq_setattr()` 系统调用设置与由 `mqdes` 指定的消息队列描述符所引用的打开消息队列描述相关联的属性。在 `mq_setattr()` 成功完成后，与 `mq_attr` 结构中定义的以下成员相对应的消息队列属性将被设置为指定值：

**`mq_flags`** 此成员的值为零或 `O_NONBLOCK`。

`mq_attr` 结构的 `mq_maxmsg`、`mq_msgsize` 和 `mq_curmsgs` 成员的值将被 `mq_setattr()` 忽略。

## 返回值

成功完成时，函数返回 0，消息队列的属性将按指定方式更改。

否则，消息队列属性保持不变，函数返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mq_setattr()` 系统调用将失败，如果：

**[`EBADF`]** `mqdes` 参数不是有效的消息队列描述符。

## 参见

[mq_open(2)](mq_open.2.md), [mq_send(2)](mq_send.2.md), mq_timedsend(2)

## 标准

`mq_setattr()` 系统调用符合 IEEE Std 1003.1-2004 ("POSIX.1")。

## 历史

对 POSIX 消息队列的支持首次出现于 FreeBSD 7.0。

## 版权

本文部分内容转载并复制自 IEEE Std 1003.1, 2004 Edition, Standard for Information Technology -- Portable Operating System Interface (POSIX), The Open Group Base Specifications Issue 6, Copyright (C) 2001-2004 by the Institute of Electrical and Electronics Engineers, Inc and The Open Group。若此版本与原始 IEEE 及 The Open Group 标准之间存在任何差异，以原始 IEEE 及 The Open Group 标准为准。原始标准可在线获取，地址为 http://www.opengroup.org/unix/online.html。
