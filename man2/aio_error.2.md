# aio_error(2)

`aio_error` — 获取异步 I/O 操作的错误状态（REALTIME）

## 名称

`aio_error`

## 库

Lb libc

## 概要

`#include <aio.h>`

```c
int
aio_error(const struct aiocb *iocb);
```

## 描述

`aio_error()` 系统调用返回与 `iocb` 所指向结构体关联的异步 I/O 请求的错误状态。

## 返回值

如果异步 I/O 请求已成功完成，`aio_error()` 返回 0。如果请求尚未完成，返回 `EINPROGRESS`。如果请求已完成但失败，则返回错误状态，如 [read(2)](read.2.md)、readv(2)、[write(2)](write.2.md)、writev(2) 或 [fsync(2)](fsync.2.md) 中所述。失败时，`aio_error()` 返回 `-1` 并设置 `errno` 以指示错误条件。

## 错误

`aio_error()` 系统调用在以下情况下会失败：

**[EINVAL]** `iocb` 参数未引用未完成的异步 I/O 请求。

## 参见

[aio_cancel(2)](aio_cancel.2.md), [aio_read(2)](aio_read.2.md), aio_readv(2), [aio_return(2)](aio_return.2.md), [aio_suspend(2)](aio_suspend.2.md), [aio_write(2)](aio_write.2.md), aio_writev(2), [fsync(2)](fsync.2.md), [read(2)](read.2.md), [write(2)](write.2.md), [aio(4)](../man4/aio.4.md)

## 标准

`aio_error()` 系统调用预期符合 IEEE Std 1003.1 ("POSIX.1") 标准。

## 历史

`aio_error()` 系统调用首次出现于 FreeBSD 3.0。

## 作者

本手册页由 Wes Peters <wes@softweyr.com> 编写。
