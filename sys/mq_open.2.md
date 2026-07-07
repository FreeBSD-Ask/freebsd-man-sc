# mq_open(2)

`mq_open` — 打开消息队列（REALTIME）

## 名称

`mq_open`

## 库

Lb librt

## 概要

`#include <mqueue.h>`

```c
mqd_t
mq_open(const char *name, int oflag, ...);
```

## 描述

`mq_open()` 系统调用通过消息队列描述符建立进程与消息队列之间的连接。它创建一个引用该消息队列的打开消息队列描述，以及一个引用该打开消息队列描述的消息队列描述符。消息队列描述符被其他函数用来引用该消息队列。`name` 参数指向命名消息队列的字符串。`name` 参数应符合路径名的构造规则。`name` 应以斜杠字符开头。使用相同 `name` 值调用 `mq_open()` 的进程引用同一个消息队列对象，只要该名称未被移除。如果 `name` 参数不是现有消息队列的名称且未请求创建，`mq_open()` 将失败并返回错误。

`oflag` 参数请求对消息队列的所需接收和/或发送访问。接收消息或发送消息的请求访问权限将分别授予调用进程对同等保护文件的读或写访问权限。

`oflag` 的值是以下列表中值的按位或。应用程序应在 `oflag` 的值中指定前三个值（访问模式）中的恰好一个：

**`O_RDONLY`** 打开消息队列以接收消息。进程可以将返回的消息队列描述符与 `mq_receive()` 一起使用，但不能与 `mq_send()` 一起使用。消息队列可以在相同或不同进程中多次打开以接收消息。

**`O_WRONLY`** 打开队列以发送消息。进程可以将返回的消息队列描述符与 `mq_send()` 一起使用，但不能与 `mq_receive()` 一起使用。消息队列可以在相同或不同进程中多次打开以发送消息。

**`O_RDWR`** 打开队列以接收和发送消息。进程可以使用 `O_RDONLY` 和 `O_WRONLY` 允许的任何函数。消息队列可以在相同或不同进程中多次打开以发送消息。

可以在 `oflag` 的值中指定剩余标志的任意组合：

**`O_CREAT`** 创建消息队列。它需要两个额外参数：`mode`（类型为 `mode_t`）和 `attr`（指向 `mq_attr` 结构的指针）。如果路径名 `name` 已经用于创建仍然存在的消息队列，则此标志无效，`O_EXCL` 下注明的情况除外。否则，将创建一个不包含任何消息的消息队列。消息队列的用户 ID 将设置为进程的有效用户 ID，消息队列的组 ID 将设置为进程的有效组 ID。消息队列的权限位将设置为 `mode` 参数的值，但进程文件模式创建掩码中设置的位除外。当 `mode` 中指定了文件权限位以外的位时，效果未定义。如果 `attr` 为 `NULL`，消息队列以实现定义的默认消息队列属性创建。如果 `attr` 为非 `NULL` 且调用进程对 name 具有适当权限，消息队列的 `mq_maxmsg` 和 `mq_msgsize` 属性将设置为 `attr` 所引用的 `mq_attr` 结构中相应成员的值。如果 `attr` 为非 `NULL`，但调用进程对 name 没有适当权限，`mq_open()` 函数将失败并返回错误，不创建消息队列。

**`O_EXCL`** 如果设置了 `O_EXCL` 和 `O_CREAT`，当消息队列名称已存在时 `mq_open()` 将失败。

**`O_NONBLOCK`** 确定 `mq_send()` 或 `mq_receive()` 是等待当前不可用的资源或消息，还是以 `errno` 设置为 `EAGAIN` 失败；参见 [mq_send(2)](mq_send.2.md) 和 [mq_receive(2)](mq_receive.2.md) 获取详细信息。

`mq_open()` 系统调用不会从队列中添加或移除消息。

## 注释

FreeBSD 基于文件描述符实现消息队列。该描述符在 [fork(2)](fork.2.md) 后由子进程继承。该描述符在 [exec(3)](../man3/exec.3.md) 后的新映像中被关闭。[select(2)](select.2.md) 和 [kevent(2)](kevent.2.md) 系统调用支持消息队列描述符。

关于加载模块或将服务编译到内核中的说明，请参见 [mqueuefs(4)](../man4/mqueuefs.4.md) 联机手册。

可用队列数、每个队列的最大消息数和最大消息大小是可调的 [sysctl(8)](../man8/sysctl.8.md) 参数。其默认值如下。

| Name | Type | Default |
| --- | --- | --- |
| kern.mqueue.maxmq | integer | 100 |
| kern.mqueue.maxmsgsize | integer | 16384 |
| kern.mqueue.maxmsg | integer | 100 |

## 返回值

成功完成后，函数返回一个消息队列描述符；否则，函数返回 (`mqd_t`)-1，并设置全局变量 `errno` 以指示错误。

## 错误

`mq_open()` 系统调用在以下情况下会失败：

**[`EACCES`]** 消息队列存在且 `oflag` 指定的权限被拒绝，或消息队列不存在且创建消息队列的权限被拒绝。

**[`EEXIST`]** 设置了 `O_CREAT` 和 `O_EXCL`，且命名的消息队列已存在。

**[`EINTR`]** `mq_open()` 函数被信号中断。

**[`EINVAL`]** `mq_open()` 函数不支持给定的 name。

**[`EINVAL`]** `oflag` 中指定了 `O_CREAT`，`attr` 的值不为 `NULL`，且 `mq_maxmsg` 或 `mq_msgsize` 小于或等于零。

**[`EINVAL`]** `oflag` 中指定了 `O_CREAT`，`attr` 的值不为 `NULL`，且 `mq_maxmsg` 超过 `kern.mqueue.maxmsg` sysctl 限制，或 `mq_msgsize` 超过 `kern.mqueue.maxmsgsize` sysctl 限制。

**[`EMFILE`]** 此进程当前使用了太多的消息队列描述符或文件描述符。

**[`ENAMETOOLONG`]** `name` 参数的长度超过 `PATH_MAX`，或某个路径名分量超过 `NAME_MAX`。

**[`ENFILE`]** 系统中当前打开了太多消息队列。系统限制由 `kern.mqueue.maxmq` sysctl 控制。

**[`ENOENT`]** 未设置 `O_CREAT` 且命名的消息队列不存在。

**[`ENOSPC`]** 没有足够的空间来创建新的消息队列。

## 参见

[mq_close(2)](mq_close.2.md), [mq_getattr(2)](mq_getattr.2.md), [mq_receive(2)](mq_receive.2.md), [mq_send(2)](mq_send.2.md), [mq_setattr(2)](mq_setattr.2.md), [mq_unlink(2)](mq_unlink.2.md), [mq_timedreceive(3)](../man3/mq_timedreceive.3.md), [mq_timedsend(3)](../man3/mq_timedsend.3.md), [mqueuefs(4)](../man4/mqueuefs.4.md)

## 标准

`mq_open()` 系统调用遵循 IEEE Std 1003.1-2004 ("POSIX.1") 标准。

## 历史

对 POSIX 消息队列的支持首次出现于 FreeBSD 7.0。

## 缺陷

此实现对 `name` 的值有严格要求：它必须以斜杠（`/`）开头，且不包含其他斜杠字符。

`mode` 和 `attr` 参数是可变参数，可能导致与预期不同的调用约定。

## COPYRIGHT

Portions of this text are reprinted and reproduced in electronic form from IEEE Std 1003.1, 2004 Edition, Standard for Information Technology -- Portable Operating System Interface (POSIX), The Open Group Base Specifications Issue 6, Copyright (C) 2001-2004 by the Institute of Electrical and Electronics Engineers, Inc and The Open Group. In the event of any discrepancy between this version and the original IEEE and The Open Group Standard, the original IEEE and The Open Group Standard is the referee document. The original Standard can be obtained online at http://www.opengroup.org/unix/online.html.
