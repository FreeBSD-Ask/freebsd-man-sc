# alq(9)

`alq` — 异步日志队列

## 名称

`alq`, `alq_open_flags`, `alq_open`, `alq_writen`, `alq_write`, `alq_flush`, `alq_close`, `alq_getn`, `alq_get`, `alq_post_flags`, `alq_post`

## 概要

```c
#include <sys/alq.h>
```

```c
int
alq_open_flags(struct alq **app, const char *file, struct ucred *cred,
    int cmode, int size, int flags)

int
alq_open(struct alq **app, const char *file, struct ucred *cred,
    int cmode, int size, int count)

int
alq_writen(struct alq *alq, void *data, int len, int flags)

int
alq_write(struct alq *alq, void *data, int flags)

void
alq_flush(struct alq *alq)

void
alq_close(struct alq *alq)

struct ale *
alq_getn(struct alq *alq, int len, int flags)

struct ale *
alq_get(struct alq *alq, int flags)

void
alq_post_flags(struct alq *alq, struct ale *ale, int flags)

void
alq_post(struct alq *alq, struct ale *ale)
```

## 描述

`alq_post` 设施提供异步固定或可变长度记录机制，称为异步日志队列（Asynchronous Logging Queues）。它可以记录到任何 [vnode(9)](vnode.9.md)，从而提供将日志记录到字符设备和常规文件的能力。所有函数都接受 `struct alq` 参数，这是一个不透明类型，维护异步日志队列的状态信息。日志记录设施在单独的内核线程中运行，为所有日志条目请求提供服务。

"异步日志条目"定义为 `struct ale`，具有以下成员：

```c
struct ale {
	intptr_t	ae_bytesused;	/* 写入到 ALE 的字节数。 */
	char		*ae_data;	/* 写指针。 */
	int		ae_pad;		/* 未使用，兼容性字段。 */
};
```

`alq_post` 可以以固定长度或可变长度模式创建。可变长度 `alq_post` 使用 `alq_writen` 和 `alq_getn` 适应可变长度的写入。固定长度 `alq_post` 使用 `alq_write` 和 `alq_get` 适应固定数量的写入，每次写入大小固定（在队列创建时设置）。固定长度模式已弃用，建议使用可变长度模式。

## 函数

`alq_open_flags` 函数创建一个新的可变长度异步日志队列。`file` 参数是要打开用于日志记录的文件名。如果文件尚不存在，`alq_open` 将尝试创建它。`cmode` 参数将作为请求的创建模式传递给 `vn_open`，在 `alq_open` 创建文件时使用。此 API 的使用者可能希望传递 `ALQ_DEFAULT_CMODE`，这是适合大多数应用程序的默认创建模式。`cred` 参数指定打开文件和对文件执行 I/O 时使用的凭证。`size` 参数设置底层队列的大小（以字节为单位）。可以通过 `flags` 传递 ALQ_ORDERED 标志，指示应保留等待繁忙 `alq_post` 释放资源的写入线程的顺序。

已弃用的 `alq_open` 函数实现为 `alq_open_flags` 的包装器，为尚未更新以使用较新 `alq_open_flags` 函数的使用者提供向后兼容性。它将所有参数原样传递给 `alq_open_flags`，但 `size` 和 `count` 除外，并将 `flags` 设置为 0。要创建可变长度模式 `alq_post`，`size` 参数应设置为底层队列的大小（以字节为单位），`count` 参数应设置为 0。要创建固定长度模式 `alq_post`，`size` 参数应设置为每次写入的大小（以字节为单位），`count` 参数应设置为为其预留容量的 `size` 字节块的数量。

`alq_writen` 函数将 `len` 字节从 `data` 写入到指定的可变长度模式队列 `alq`。如果 `alq_writen` 无法立即写入条目且 `flags` 中设置了 `ALQ_WAITOK`，则允许函数以 "`alqwnord`" 或 "`alqwnres`" 等待消息调用 msleep_spin(9)。写入会自动调度队列 `alq` 刷新到磁盘。可以通过 `flags` 传递 ALQ_NOACTIVATE 来控制此行为，指示写入不应调度 `alq` 刷新到磁盘。

已弃用的 `alq_write` 函数实现为 `alq_writen` 的包装器，为尚未更新以使用可变长度模式队列的使用者提供向后兼容性。该函数将 `size` 字节数据（其中 `size` 在队列创建时指定）从 `data` 缓冲区写入到 `alq`。注意，在可变长度模式队列上调用 `alq_write` 是错误的。

`alq_flush` 函数用于将 `alq` 刷新到传递给 `alq_open` 的日志介质。如果 `alq` 有数据要刷新且尚未在刷新过程中，该函数将阻塞执行 IO。否则，函数立即返回。

`alq_close` 函数关闭异步日志队列 `alq`，并将所有挂起的写入请求刷新到日志介质。它将释放先前分配的所有资源。

`alq_getn` 函数从 `alq` 返回一个异步日志条目，初始化为指向能够接收 `len` 字节数据的缓冲区。此函数使 `alq` 保持锁定状态，直到后续调用 `alq_post` 或 `alq_post_flags`。如果 `alq_getn` 无法立即获得 `len` 字节的缓冲区且 `flags` 中设置了 `ALQ_WAITOK`，则允许函数以 "`alqgnord`" 或 "`alqgnres`" 等待消息调用 msleep_spin(9)。调用者可以通过将条目的 ae_bytesused 字段设置为实际写入的字节数，选择向返回的异步日志条目写入少于 `len` 字节的数据。这必须在调用 `alq_post` 之前完成。

已弃用的 `alq_get` 函数实现为 `alq_getn` 的包装器，为尚未更新以使用可变长度模式队列的使用者提供向后兼容性。返回的异步日志条目将初始化为指向能够接收 `size` 字节数据的缓冲区（其中 `size` 在队列创建时指定）。注意，在可变长度模式队列上调用 `alq_get` 是错误的。

`alq_post_flags` 函数调度异步日志条目 `ale`（从 `alq_getn` 或 `alq_get` 获得）写入到 `alq`。可以通过 `flags` 传递 ALQ_NOACTIVATE 标志，指示不应立即调度队列刷新到磁盘。此函数使 `alq` 处于解锁状态。

`alq_post` 函数实现为 `alq_post_flags` 的包装器，为尚未更新以使用较新 `alq_post_flags` 函数的使用者提供向后兼容性。它只是将所有参数原样传递给 `alq_post_flags`，并将 `flags` 设置为 0。

## 实现说明

`alq_writen` 和 `alq_write` 函数都从提供的 `data` 缓冲区执行 bcopy(3) 到底层 `alq_post` 缓冲区。性能关键的代码路径可能希望考虑使用 `alq_getn`（可变长度队列）或 `alq_get`（固定长度队列）以避免额外的内存复制。注意，队列在调用 `alq_getn` 或 `alq_get` 与调用 `alq_post` 或 `alq_post_flags` 之间保持锁定状态，因此这种写入队列的方法不适用于调用之间时间可能较长的情况。

## 锁定

每个异步日志队列由自旋互斥锁保护。

`alq_flush` 和 `alq_open` 函数可能尝试获取内部睡眠互斥锁，因此不应在不允许睡眠的上下文中使用。

## 返回值

如果 `alq_open` 函数无法打开 `file`，则返回 open(2) 中列出的错误代码之一，否则返回 0。

如果 `flags` 中设置了 `ALQ_NOWAIT` 且队列已满或系统正在关闭，`alq_writen` 和 `alq_write` 函数返回 `EWOULDBLOCK`。

如果 `flags` 中设置了 `ALQ_NOWAIT` 且队列已满或系统正在关闭，`alq_getn` 和 `alq_get` 函数返回 `NULL`。

注意：向非 void 函数传递无效参数将导致未定义行为。

## 参见

[syslog(3)](../gen/syslog.3.md), [kproc(9)](kproc.9.md), [ktr(9)](ktr.9.md), msleep_spin(9), [vnode(9)](vnode.9.md)

## 历史

异步日志队列（ALQ）设施首次出现于 FreeBSD 5.0。

## 作者

`alq_post` 设施由 Jeffrey Roberson <jeff@FreeBSD.org> 编写，并由 Lawrence Stewart <lstewart@freebsd.org> 扩展。

本手册页由 Hiten Pandya <hmp@FreeBSD.org> 编写，并由 Lawrence Stewart <lstewart@freebsd.org> 修订。
