# aio_suspend(2)

`aio_suspend` — 挂起直到异步 I/O 操作或超时完成（REALTIME）

## 名称

`aio_suspend`

## 库

Lb libc

## 概要

`#include <aio.h>`

```c
int
aio_suspend(const struct aiocb *const iocbs[], int niocb,
    const struct timespec *timeout);
```

## 描述

`aio_suspend()` 系统调用挂起调用进程，直到至少一个指定的异步 I/O 请求已完成、收到信号或 `timeout` 超时。

`iocbs` 参数是由 `niocb` 个指向异步 I/O 请求的指针组成的数组。包含空指针的数组成员将被静默忽略。

如果 `timeout` 不是空指针，它指定挂起的最大间隔时间。如果 `timeout` 是空指针，挂起将无限期阻塞。要进行轮询，`timeout` 应指向一个零值的 timespec 结构体。

## 返回值

如果一个或多个指定的异步 I/O 请求已完成，`aio_suspend()` 返回 0。否则返回 -1 并设置 `errno` 以指示错误，如下所述。

## 错误

`aio_suspend()` 系统调用在以下情况下会失败：

**[EAGAIN]** 在任何 I/O 请求完成之前 `timeout` 已超时。

**[EINVAL]** `iocbs` 参数包含的异步 I/O 请求数量超过 `vfs.aio.max_aio_queue_per_proc` [sysctl(8)](../man8/sysctl.8.md) 变量的限制，或至少一个请求无效。

**[EINTR]** 挂起被信号中断。

## 参见

[aio_cancel(2)](aio_cancel.2.md), [aio_error(2)](aio_error.2.md), [aio_return(2)](aio_return.2.md), [aio_waitcomplete(2)](aio_waitcomplete.2.md), [aio_write(2)](aio_write.2.md), [aio(4)](../man4/aio.4.md)

## 标准

`aio_suspend()` 系统调用预期符合 IEEE Std 1003.1 ("POSIX.1") 标准。

## 历史

`aio_suspend()` 系统调用首次出现于 FreeBSD 3.0。

## 作者

本手册页由 Wes Peters <wes@softweyr.com> 编写。
