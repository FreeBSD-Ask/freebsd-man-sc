# mq_close(2)

`mq_close` — 关闭消息队列（REALTIME）

## 名称

`mq_close`

## 库

Lb librt

## 概要

`#include <mqueue.h>`

```c
int
mq_close(mqd_t mqdes);
```

## 描述

`mq_close()` 系统调用移除消息队列描述符 `mqdes` 与其消息队列之间的关联。在从此 `mq_close()` 成功返回之后，直到通过随后的 `mq_open()` 再次返回此消息队列描述符之前，使用此消息队列描述符的结果是未定义的。

如果进程已通过此 `mqdes` 成功附加了通知请求到消息队列，则此附加将被移除，消息队列可供另一个进程附加通知。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mq_close()` 系统调用在以下情况下会失败：

**[`EBADF`]** `mqdes` 参数不是有效的消息队列描述符。

## 参见

[mq_open(2)](mq_open.2.md), [mq_unlink(2)](mq_unlink.2.md)

## 标准

`mq_close()` 系统调用符合 IEEE Std 1003.1-2004 ("POSIX.1")。

## 历史

对 POSIX 消息队列的支持首次出现于 FreeBSD 7.0。

## 版权

本文的部分内容以电子形式转载和复制自 IEEE Std 1003.1, 2004 Edition, Standard for Information Technology -- Portable Operating System Interface (POSIX), The Open Group Base Specifications Issue 6, Copyright (C) 2001-2004 by the Institute of Electrical and Electronics Engineers, Inc and The Open Group。如果此版本与原始 IEEE 和 The Open Group 标准之间存在任何差异，以原始 IEEE 和 The Open Group 标准为准。原始标准可在 <http://www.opengroup.org/unix/online.html> 在线获取。
