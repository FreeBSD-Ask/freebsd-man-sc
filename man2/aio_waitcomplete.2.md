# aio_waitcomplete(2)

`aio_waitcomplete` — 等待下一个 aio 请求完成

## 名称

`aio_waitcomplete`

## 库

Lb libc

## 概要

`#include <aio.h>`

```c
ssize_t
aio_waitcomplete(struct aiocb **iocbp, struct timespec *timeout);
```

## 描述

`aio_waitcomplete()` 系统调用等待一个异步 I/O 请求完成。完成后，`aio_waitcomplete()` 返回该函数的结果，并将 `iocbp` 设置为指向与原始请求关联的结构体。如果在调用 `aio_waitcomplete()` 之前已有异步 I/O 请求完成，它将立即返回已完成的请求。

如果 `timeout` 是非 NULL 指针，它指定等待异步 I/O 请求完成的最大间隔时间。如果 `timeout` 是 NULL 指针，`aio_waitcomplete()` 将无限期等待。要进行轮询，`timeout` 参数应为非 NULL，指向一个零值的 timeval 结构体。

`aio_waitcomplete()` 系统调用还兼具 `aio_return()` 的功能，因此对于 `iocbp` 中返回的控制块，不应再调用 `aio_return()`。

## 返回值

如果异步 I/O 请求已完成，`iocbp` 被设置为指向原始请求中传入的控制块，返回值的状态如 [read(2)](read.2.md)、[write(2)](write.2.md) 或 [fsync(2)](fsync.2.md) 中所述。失败时，`aio_waitcomplete()` 返回 `-1`，将 iocbp 设置为 `NULL`，并设置 `errno` 以指示错误条件。

## 错误

`aio_waitcomplete()` 系统调用在以下情况下会失败：

**[EAGAIN]** 进程尚未调用 `aio_read()` 或 `aio_write()`。

**[EINTR]** 在超时到期之前且在任何异步 I/O 请求完成之前收到信号。

**[EINVAL]** 指定的时间限制无效。

**[EWOULDBLOCK]**

**[EINPROGRESS]** 在任何异步 I/O 请求完成之前，指定的时间限制已到期。

## 参见

[aio_cancel(2)](aio_cancel.2.md), [aio_error(2)](aio_error.2.md), [aio_read(2)](aio_read.2.md), [aio_return(2)](aio_return.2.md), [aio_suspend(2)](aio_suspend.2.md), [aio_write(2)](aio_write.2.md), [fsync(2)](fsync.2.md), [read(2)](read.2.md), [write(2)](write.2.md), [aio(4)](../man4/aio.4.md)

## 标准

`aio_waitcomplete()` 系统调用是 FreeBSD 特有的扩展。

## 历史

`aio_waitcomplete()` 系统调用首次出现于 FreeBSD 4.0。

## 作者

`aio_waitcomplete()` 系统调用及本手册页由 Christopher M Sedore <cmsedore@maxwell.syr.edu> 编写。
