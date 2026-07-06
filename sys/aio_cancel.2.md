# aio_cancel(2)

`aio_cancel` — 取消未完成的异步 I/O 操作（REALTIME）

## 名称

`aio_cancel`

## 库

Lb libc

## 概要

`#include <aio.h>`

```c
int
aio_cancel(int fildes, struct aiocb *iocb);
```

## 描述

`aio_cancel()` 系统调用取消指定文件描述符 `fildes` 上未完成的异步 I/O 请求。如果指定了 `iocb`，则仅取消该特定的异步 I/O 请求。

被取消的请求会进行正常的异步通知。这些请求将以 `ECANCELED` 错误结果完成。

## 限制

`aio_cancel()` 系统调用不会取消裸盘设备的异步 I/O 请求。对于与裸盘设备关联的文件描述符，`aio_cancel()` 系统调用将始终返回 `AIO_NOTCANCELED`。

## 返回值

`aio_cancel()` 系统调用出错时返回 -1，或返回以下值之一：

**[`AIO_CANCELED`]** 所有符合条件的未完成请求均已取消。

**[`AIO_NOTCANCELED`]** 部分请求未被取消，应使用 [aio_error(2)](aio_error.2.md) 检查这些请求的状态。

**[`AIO_ALLDONE`]** 所有符合条件的请求均已完成。

## 错误

`aio_cancel()` 返回错误表示：

**[EBADF]** `fildes` 参数是无效的文件描述符。

## 参见

[aio_error(2)](aio_error.2.md), [aio_read(2)](aio_read.2.md), [aio_return(2)](aio_return.2.md), [aio_suspend(2)](aio_suspend.2.md), [aio_write(2)](aio_write.2.md), [aio(4)](../man4/aio.4.md)

## 标准

`aio_cancel()` 系统调用预期符合 IEEE Std 1003.1 ("POSIX.1") 标准。

## 历史

`aio_cancel()` 系统调用首次出现于 FreeBSD 3.0。`aio_cancel()` 的首个可用实现出现于 FreeBSD 4.0。

## 作者

本手册页最初由 Wes Peters <wes@softweyr.com> 编写。Christopher M Sedore <cmsedore@maxwell.syr.edu> 在 FreeBSD 4.0 中实现 `aio_cancel()` 时对其进行了更新。
