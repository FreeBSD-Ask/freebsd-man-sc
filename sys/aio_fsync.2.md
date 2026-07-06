# aio_fsync(2)

`aio_fsync` — 异步文件同步（REALTIME）

## 名称

`aio_fsync`

## 库

Lb libc

## 概要

`#include <aio.h>`

```c
int
aio_fsync(int op, struct aiocb *iocb);
```

## 描述

`aio_fsync()` 系统调用允许调用进程将描述符 `iocb->aio_fildes` 关联的所有已修改数据移动到永久存储设备。该调用在同步请求加入描述符的队列后立即返回；调用返回时同步操作可能已完成，也可能尚未完成。

`op` 参数可设置为 `O_SYNC`，使所有当前排队的 I/O 操作如同调用 [fsync(2)](fsync.2.md) 一般完成；或设置为 `O_DSYNC`，以获得 fdatasync(2) 的行为。

`iocb` 指针随后可用作 `aio_return()` 和 `aio_error()` 的参数，用于在入队操作执行期间确定其返回值或错误状态。

如果请求无法入队（通常由于参数无效），调用将在未入队请求的情况下返回。

`iocb->aio_sigevent` 结构体可用于请求操作完成时的通知，如 [aio(4)](../man4/aio.4.md) 中所述。

## 限制

`iocb` 所指向的异步 I/O 控制块结构体在操作完成之前必须保持有效。

异步 I/O 控制缓冲区 `iocb` 应在调用 `aio_fsync()` 之前清零，以避免向内核传递虚假的上下文信息。

请求入队期间不允许修改异步 I/O 控制块结构体。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

`aio_fsync()` 系统调用在以下情况下会失败：

**[EAGAIN]** 由于系统资源限制，请求未入队。

**[EINVAL]** `iocb->aio_sigevent.sigev_notify` 中的异步通知方法无效或不被支持。

**[EOPNOTSUPP]** 文件描述符 `iocb->aio_fildes` 上的异步文件同步操作不安全，且已禁用不安全的异步 I/O 操作。

**[EINVAL]** `op` 参数的值未设置为 `O_SYNC` 或 `O_DSYNC`。

以下情况可在调用 `aio_fsync()` 时同步检测到，也可在此后任何时间异步检测到。如果在调用时检测到，`aio_fsync()` 返回 -1 并适当设置 `errno`；否则必须调用 `aio_return()`，它将返回 -1，并且必须调用 `aio_error()` 以确定本应在 `errno` 中返回的实际值。

**[EBADF]** `iocb->aio_fildes` 参数不是有效的描述符。

**[EINVAL]** 本实现不支持此文件的同步 I/O。

如果请求成功入队但随后被取消或发生错误，`aio_return()` 系统调用返回的值遵循 [read(2)](read.2.md) 和 [write(2)](write.2.md) 系统调用的规定，`aio_error()` 系统调用返回的值为 [read(2)](read.2.md) 或 [write(2)](write.2.md) 系统调用的错误返回值之一。

## 参见

[aio_cancel(2)](aio_cancel.2.md), [aio_error(2)](aio_error.2.md), [aio_read(2)](aio_read.2.md), [aio_return(2)](aio_return.2.md), [aio_suspend(2)](aio_suspend.2.md), [aio_waitcomplete(2)](aio_waitcomplete.2.md), [aio_write(2)](aio_write.2.md), [fsync(2)](fsync.2.md), [sigevent(3)](../man3/sigevent.3.md), [siginfo(3)](../man3/siginfo.3.md), [aio(4)](../man4/aio.4.md)

## 标准

`aio_fsync()` 系统调用预期符合 IEEE Std 1003.1 ("POSIX.1") 标准。

## 历史

`aio_fsync()` 系统调用首次出现于 FreeBSD 7.0。`O_DSYNC` 选项出现于 FreeBSD 13.0。
