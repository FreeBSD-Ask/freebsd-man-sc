# aio_read(2)

`aio_read` — 异步读取文件（REALTIME）

## 名称

`aio_read`, `aio_read2`, `aio_readv`

## 库

Lb libc

## 概要

`#include <aio.h>`

```c
int
aio_read(struct aiocb *iocb);

int
aio_read2(struct aiocb *iocb, int flags);
```

`#include <sys/uio.h>`

```c
int
aio_readv(struct aiocb *iocb);
```

## 描述

`aio_read()`、`aio_read2()` 和 `aio_readv()` 系统调用允许调用进程从描述符 `iocb->aio_fildes` 读取数据。这些系统调用在读取请求加入描述符队列后立即返回；调用返回时读取操作可能已完成，也可能尚未完成。

对于 `aio_read()` 和 `aio_readv()` 调用，读取操作从偏移量 `iocb->aio_offset` 处开始。

`aio_read()` 调用将读取 `iocb->aio_nbytes` 字节到 `iocb->aio_buf` 所指向的缓冲区中，而 `aio_readv()` 将数据读取到由 `iocb->aio_iov` 数组成员指定的 `iocb->aio_iovcnt` 个缓冲区中。对于 `aio_readv()`，`iovec` 结构体在 readv(2) 中定义。

`aio_read2()` 调用接受 `flags` 参数。如果 `flags` 传入零，该调用的行为与 `aio_read()` 完全相同。可通过逻辑或指定以下标志：

**AIO_OP2_FOFFSET** 读取操作在文件描述符偏移量处进行，该偏移量会像 [read(2)](read.2.md) 系统调用那样随操作推进。`iocb->aio_offset` 字段被忽略。

**AIO_OP2_VECTORED** 类似于 `aio_readv()`，读取缓冲区由 `aiocb->aio_iov` 数组指定。

`iocb` 指针随后可用作 `aio_return()` 和 `aio_error()` 的参数，用于在入队操作执行期间确定其返回值或错误状态。

如果请求无法入队（通常由于参数无效），调用将在未入队请求的情况下返回。

如果请求成功入队，`iocb->aio_offset` 的值可能在请求期间作为上下文被修改，因此在请求入队后不得再引用该值。

`iocb->aio_sigevent` 结构体可用于请求操作完成时的通知，如 [aio(4)](../man4/aio.4.md) 中所述。

## 限制

`iocb` 所指向的异步 I/O 控制块结构体以及该结构体中 `iocb->aio_buf` 成员所引用的缓冲区在操作完成之前必须保持有效。

异步 I/O 控制缓冲区 `iocb` 应在调用系统调用之前清零，以避免向内核传递虚假的上下文信息。

请求入队期间不允许修改异步 I/O 控制块结构体或缓冲区内容。

如果 `iocb->aio_offset` 中的文件偏移量超过了 `iocb->aio_fildes` 的偏移量上限，将不会执行任何 I/O 操作。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 诊断

无。

## 错误

`aio_read()`、`aio_read2()` 和 `aio_readv()` 系统调用在以下情况下会失败：

**[EAGAIN]** 由于系统资源限制，请求未入队。

**[EFAULT]** `aio_iov` 的某部分指向了进程分配地址空间之外。

**[EINVAL]** `iocb->aio_sigevent.sigev_notify` 中的异步通知方法无效或不被支持。

**[EOPNOTSUPP]** 文件描述符 `iocb->aio_fildes` 上的异步读取操作不安全，且已禁用不安全的异步 I/O 操作。

以下情况可在调用 `aio_read()` 或 `aio_readv()` 系统调用时同步检测到，也可在此后任何时间异步检测到。如果在调用时检测到，调用返回 -1 并适当设置 `errno`；否则必须调用 `aio_return()`，它将返回 -1，并且必须调用 `aio_error()` 以确定本应在 `errno` 中返回的实际值。

**[EBADF]** `iocb->aio_fildes` 参数无效。

**[EINVAL]** 偏移量 `iocb->aio_offset` 无效，`iocb->aio_reqprio` 指定的优先级不是有效优先级，或 `iocb->aio_nbytes` 指定的字节数无效。

**[EOVERFLOW]** 该文件是常规文件，`iocb->aio_nbytes` 大于零，`iocb->aio_offset` 中的起始偏移量在文件末尾之前，但达到或超过了 `iocb->aio_fildes` 的偏移量上限。

如果请求成功入队但随后被取消或发生错误，`aio_return()` 系统调用返回的值遵循 [read(2)](read.2.md) 系统调用的规定，`aio_error()` 系统调用返回的值为 [read(2)](read.2.md) 系统调用的错误返回值之一，或为以下之一：

**[EBADF]** `iocb->aio_fildes` 参数对于读取操作无效。

**[ECANCELED]** 该请求通过调用 `aio_cancel()` 被显式取消。

**[EINVAL]** 偏移量 `iocb->aio_offset` 将无效。

## 参见

[aio_cancel(2)](aio_cancel.2.md), [aio_error(2)](aio_error.2.md), [aio_return(2)](aio_return.2.md), [aio_suspend(2)](aio_suspend.2.md), [aio_waitcomplete(2)](aio_waitcomplete.2.md), [aio_write(2)](aio_write.2.md), [sigevent(3)](../man3/sigevent.3.md), [siginfo(3)](../man3/siginfo.3.md), [aio(4)](../man4/aio.4.md)

## 标准

`aio_read()` 系统调用预期符合 IEEE Std 1003.1 ("POSIX.1") 标准。`aio_read2()` 和 `aio_readv()` 系统调用是 FreeBSD 扩展，不应在可移植代码中使用。

## 历史

`aio_read()` 系统调用首次出现于 FreeBSD 3.0。`aio_readv()` 系统调用首次出现于 FreeBSD 13.0。`aio_read2()` 系统调用首次出现于 FreeBSD 14.1。

## 作者

本手册页由 Terry Lambert <terry@whistle.com> 编写。

## 缺陷

`iocb->_aiocb_private` 中的无效信息可能会干扰内核。
