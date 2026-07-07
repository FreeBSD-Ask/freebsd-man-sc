# mq_getattr(2)

`mq_getattr` — 获取消息队列属性（REALTIME）

## 名称

`mq_getattr`

## 库

Lb librt

## 概要

`#include <mqueue.h>`

```c
int
mq_getattr(mqd_t mqdes, struct mq_attr *mqstat);
```

## 描述

`mq_getattr()` 系统调用获取消息队列的状态信息和属性，以及与消息队列描述符关联的打开消息队列描述的属性。

`mqdes` 参数指定一个消息队列描述符。

结果通过 `mqstat` 参数所引用的 `mq_attr` 结构返回。

返回时，以下成员将具有与打开消息队列描述关联的值，这些值在消息队列打开时设置，并由后续的 `mq_setattr()` 调用修改：`mq_flags`。

以下消息队列属性将按消息队列创建时设置的值返回：`mq_maxmsg`、`mq_msgsize`。

返回时，`mqstat` 参数所引用的 `mq_attr` 结构中的以下成员将被设置为消息队列的当前状态：

**`mq_curmsgs`** 队列中当前的消息数量。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mq_getattr()` 系统调用在以下情况下会失败：

**[`EBADF`]** `mqdes` 参数不是有效的消息队列描述符。

## 参见

[mq_open(2)](mq_open.2.md), [mq_send(2)](mq_send.2.md), [mq_setattr(2)](mq_setattr.2.md), [mq_timedsend(2)](mq_send.2.md)

## 标准

`mq_getattr()` 系统调用符合 IEEE Std 1003.1-2004 ("POSIX.1") 规范。

## 历史

对 POSIX 消息队列的支持首次出现于 FreeBSD 7.0。

## COPYRIGHT

Portions of this text are reprinted and reproduced in electronic form from IEEE Std 1003.1, 2004 Edition, Standard for Information Technology -- Portable Operating System Interface (POSIX), The Open Group Base Specifications Issue 6, Copyright (C) 2001-2004 by the Institute of Electrical and Electronics Engineers, Inc and The Open Group. In the event of any discrepancy between this version and the original IEEE and The Open Group Standard, the original IEEE and The Open Group Standard is the referee document. The original Standard can be obtained online at http://www.opengroup.org/unix/online.html.
