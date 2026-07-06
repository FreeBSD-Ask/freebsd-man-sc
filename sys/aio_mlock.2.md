# aio_mlock(2)

`aio_mlock` — 异步 [mlock(2)](mlock.2.md) 操作

## 名称

`aio_mlock`

## 库

Lb libc

## 概要

`#include <aio.h>`

```c
int
aio_mlock(struct aiocb *iocb);
```

## 描述

`aio_mlock()` 系统调用允许调用进程将起始于 `iocb->aio_buf`、长度为 `iocb->aio_nbytes` 字节的虚拟地址范围所关联的物理页面锁定在内存中。该调用在锁定请求入队后立即返回；调用返回时操作可能已完成，也可能尚未完成。

`iocb` 指针随后可用作 `aio_return()` 和 `aio_error()` 的参数，用于在入队操作执行期间确定其返回值或错误状态。

如果请求无法入队（通常由于 [aio(4)](../man4/aio.4.md) 限制），调用将在未入队请求的情况下返回。

`iocb->aio_sigevent` 结构体可用于请求操作完成时的通知，如 [aio(4)](../man4/aio.4.md) 中所述。

## 限制

`iocb` 所指向的异步 I/O 控制块结构体以及该结构体中 `iocb->aio_buf` 成员所引用的缓冲区在操作完成之前必须保持有效。

异步 I/O 控制缓冲区 `iocb` 应在调用 `aio_mlock()` 之前清零，以避免向内核传递虚假的上下文信息。

请求入队期间不允许修改异步 I/O 控制块结构体或虚拟地址范围所描述的内存映射。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

`aio_mlock()` 系统调用在以下情况下会失败：

**[EAGAIN]** 由于系统资源限制，请求未入队。

**[EINVAL]** `iocb->aio_sigevent.sigev_notify` 中的异步通知方法无效或不被支持。

如果请求成功入队但随后被取消或发生错误，`aio_return()` 系统调用返回的值遵循 [mlock(2)](mlock.2.md) 系统调用的规定，`aio_error()` 系统调用返回的值为 [mlock(2)](mlock.2.md) 系统调用的错误返回值之一，或为 `ECANCELED`（如果请求通过调用 `aio_cancel()` 被显式取消）。

## 参见

[aio_cancel(2)](aio_cancel.2.md), [aio_error(2)](aio_error.2.md), [aio_return(2)](aio_return.2.md), [mlock(2)](mlock.2.md), [sigevent(3)](../man3/sigevent.3.md), [aio(4)](../man4/aio.4.md)

## 可移植性

`aio_mlock()` 系统调用是 FreeBSD 扩展，不应在可移植代码中使用。

## 历史

`aio_mlock()` 系统调用首次出现于 FreeBSD 10.0。

## 作者

该系统调用由 Gleb Smirnoff <glebius@FreeBSD.org> 引入。
