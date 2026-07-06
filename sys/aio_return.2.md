# aio_return(2)

`aio_return` — 获取异步 I/O 操作的返回状态（REALTIME）

## 名称

`aio_return`

## 库

Lb libc

## 概要

`#include <aio.h>`

```c
ssize_t
aio_return(struct aiocb *iocb);
```

## 描述

`aio_return()` 系统调用返回与 `iocb` 所指向结构体关联的异步 I/O 请求的最终状态。

`aio_return()` 系统调用应仅调用一次，用于在异步 I/O 操作完成后获取其最终状态（即 `aio_error()` 返回值不再是 `EINPROGRESS` 时）。

## 返回值

如果异步 I/O 请求已完成，返回值的状态如 [read(2)](read.2.md)、readv(2)、[write(2)](write.2.md)、writev(2) 或 [fsync(2)](fsync.2.md) 中所述。否则，`aio_return()` 返回 -1 并设置 `errno` 以指示错误条件。

## 错误

`aio_return()` 系统调用在以下情况下会失败：

**[EINVAL]** `iocb` 参数未引用已完成的异步 I/O 请求。

**[EINVAL]** 该 I/O 操作通过 `lio_listio()` 提交，且 `aio_lio_opcode` 的值无效。

## 参见

[aio_cancel(2)](aio_cancel.2.md), [aio_error(2)](aio_error.2.md), [aio_suspend(2)](aio_suspend.2.md), [aio_waitcomplete(2)](aio_waitcomplete.2.md), [aio_write(2)](aio_write.2.md), [fsync(2)](fsync.2.md), [read(2)](read.2.md), [write(2)](write.2.md), [aio(4)](../man4/aio.4.md)

## 标准

`aio_return()` 系统调用预期符合 IEEE Std 1003.1 ("POSIX.1") 标准。

## 历史

`aio_return()` 系统调用首次出现于 FreeBSD 3.0。

## 作者

本手册页由 Wes Peters <wes@softweyr.com> 编写。
