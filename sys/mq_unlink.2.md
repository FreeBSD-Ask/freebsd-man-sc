# mq_unlink(2)

`mq_unlink` — 移除消息队列（REALTIME）

## 名称

`mq_unlink`

## 库

Lb librt

## 概要

`#include <mqueue.h>`

```c
int
mq_unlink(const char *name);
```

## 描述

`mq_unlink()` 函数移除由字符串 `name` 命名的消息队列。如果在调用 `mq_unlink()` 时有一个或多个进程已打开该消息队列，则该消息队列的销毁将推迟到所有对该消息队列的引用都已关闭之后。不过，`mq_unlink()` 调用不必阻塞到所有引用都已关闭；它可以立即返回。

成功调用 `mq_unlink()` 后，重用该名称将导致 [mq_open(2)](mq_open.2.md) 的行为就像不存在此名称的消息队列一样。

## 返回值

若成功，`mq_unlink()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mq_unlink()` 系统调用在以下情况下会失败：

**[`EACCES`]** 拒绝对由 `name` 表示的消息队列执行 unlink 操作的权限。

**[`EINVAL`]** `name` 无效。

**[`ENAMETOOLONG`]** `name` 参数的长度超过 `PATH_MAX`，或某个路径名分量超过 `NAME_MAX`。

**[`ENOENT`]** 消息队列不存在。

**[`ENOSYS`]** [mqueuefs(4)](../man4/mqueuefs.4.md) 模块既未加载也未包含在内核中。

## 参见

[mq_open(2)](mq_open.2.md)

## 标准

`mq_unlink()` 系统调用遵循 IEEE Std 1003.1-2004 ("POSIX.1") 标准。`EACCES` 错误代码是对标准的扩展。

## 历史

对 POSIX 消息队列的支持首次出现于 FreeBSD 7.0。

## COPYRIGHT

Portions of this text are reprinted and reproduced in electronic form from IEEE Std 1003.1, 2004 Edition, Standard for Information Technology -- Portable Operating System Interface (POSIX), The Open Group Base Specifications Issue 6, Copyright (C) 2001-2004 by the Institute of Electrical and Electronics Engineers, Inc and The Open Group. In the event of any discrepancy between this version and the original IEEE and The Open Group Standard, the original IEEE and The Open Group Standard is the referee document. The original Standard can be obtained online at http://www.opengroup.org/unix/online.html.
