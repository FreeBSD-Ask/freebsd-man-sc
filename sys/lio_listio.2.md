# lio_listio(2)

`lio_listio` — 列表定向 I/O (REALTIME)

## 名称

`lio_listio`

## 库

Lb libc

## 概要

`#include <aio.h>`

```c
int
lio_listio(int mode, struct aiocb * const list[],
    int nent, struct sigevent *sig);
```

## 描述

`lio_listio()` 函数通过单次函数调用发起一组 I/O 请求。`list` 参数是一个指向 `aiocb` 结构体的指针数组，描述要执行的每个操作，共 `nent` 个元素。`NULL` 元素将被忽略。

每个 `aiocb` 的 `aio_lio_opcode` 字段指定要执行的操作。支持以下操作：

**`LIO_READ`** 读取数据，如同调用 [aio_read(2)](aio_read.2.md)。

**`LIO_READV`** 读取数据，如同调用 [aio_readv(2)](aio_readv.2.md)。

**`LIO_NOP`** 不执行操作。

**`LIO_WRITE`** 写入数据，如同调用 [aio_write(2)](aio_write.2.md)。

**`LIO_WRITEV`** 写入数据，如同调用 [aio_writev(2)](aio_writev.2.md)。

如果 `LIO_READ`、`LIO_READV`、`LIO_WRITE`、`LIO_WRITEV` 操作码与 `LIO_FOFFSET` 标志按位或，则相应的读或写操作使用当前文件描述符偏移量，而不是 `aiocb` 中的 `aio_offset`。

如果 `mode` 参数为 `LIO_WAIT`，`lio_listio()` 在所有请求的操作完成之前不会返回。如果 `mode` 为 `LIO_NOWAIT`，可使用 `sig` 请求在所有操作完成时的异步通知。如果 `sig` 为 `NULL`，则不发送通知。

对于 `SIGEV_KEVENT` 通知，发布的 kevent 将包含：

| Member | Value |
| --- | --- |
| `ident` | `list` |
| `filter` | `EVFILT_LIO` |
| `udata` | 存储在 `sig->sigev_value` 中的值 |

对于 `SIGEV_SIGNO` 和 `SIGEV_THREAD_ID` 通知，排队信号的信息将在 `si_code` 字段中包含 `SI_ASYNCIO`，并在 `si_value` 字段中包含存储在 `sig->sigev_value` 中的值。

对于 `SIGEV_THREAD` 通知，存储在 `sig->sigev_value` 中的值将传递给 `sig->sigev_notify_function`，如 [sigevent(3)](../man3/sigevent.3.md) 中所述。

请求执行的顺序未指定；特别是，不保证它们会按 0、1、...、`nent`-1 的顺序执行。

## 返回值

如果 `mode` 为 `LIO_WAIT`，`lio_listio()` 函数在操作成功完成时返回 0，否则返回 -1。

如果 `mode` 为 `LIO_NOWAIT`，`lio_listio()` 函数在操作成功入队时返回 0，否则返回 -1。

## 错误

`lio_listio()` 函数在以下情况下会失败：

**[`EAGAIN`]** 没有足够的资源来将请求入队。

**[`EAGAIN`]** 该请求将导致超出系统范围限制 `{AIO_MAX}`。

**[`EINVAL`]** `mode` 参数既不是 `LIO_WAIT` 也不是 `LIO_NOWAIT`，或 `nent` 大于 `{AIO_LISTIO_MAX}`。

**[`EINVAL`]** `sig->sigev_notify` 中的异步通知方法无效或不被支持。

**[`EINTR`]** 系统调用在完成之前被信号中断。

**[`EIO`]** 一个或多个请求失败。

此外，`lio_listio()` 函数可能因 [aio_read(2)](aio_read.2.md) 和 [aio_write(2)](aio_write.2.md) 中列出的任何原因而失败。

如果 `lio_listio()` 成功，或以 `EAGAIN`、`EINTR` 或 `EIO` 错误码失败，部分请求可能已经被发起。调用者应通过调用 [aio_error(2)](aio_error.2.md) 逐个检查每个 `aiocb` 结构体的错误状态。

## 参见

[aio_error(2)](aio_error.2.md), [aio_read(2)](aio_read.2.md), [aio_readv(2)](aio_readv.2.md), [aio_write(2)](aio_write.2.md), [aio_writev(2)](aio_writev.2.md), [read(2)](read.2.md), [write(2)](write.2.md), [sigevent(3)](../man3/sigevent.3.md), [siginfo(3)](../man3/siginfo.3.md), [aio(4)](../man4/aio.4.md)

## 标准

`lio_listio()` 函数预期符合 IEEE Std 1003.1-2001 ("POSIX.1") 标准。`LIO_READV` 和 `LIO_WRITEV` 操作是 FreeBSD 扩展。

## 历史

`lio_listio()` 系统调用首次出现于 FreeBSD 3.0。
