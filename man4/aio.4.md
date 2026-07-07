# aio(4)

`aio` — 异步 I/O

## 名称

`aio`

## 描述

`aio` 设施为异步 I/O 提供系统调用。调用线程不会同步完成异步 I/O 操作。相反，调用线程调用系统调用来请求异步 I/O 操作。已完成请求的状态稍后通过单独的系统调用检索。

对某些文件描述符类型的异步 I/O 操作可能无限期阻塞 AIO 守护进程，导致进程和/或系统挂起。对这些文件描述符类型的操作被视为“不安全”，默认禁用。可以通过将 `vfs.aio.enable_unsafe` sysctl 节点设置为非零值来启用。

对套接字、原始磁盘设备和本地文件系统上常规文件的异步 I/O 操作不会无限期阻塞，始终启用。

`aio` 设施使用内核进程（也称为 AIO 守护进程）来服务大多数异步 I/O 请求。这些进程分组为包含可变数量进程的池。每个池根据负载添加或删除进程。池可通过 sysctl 节点配置，这些节点定义最小和最大进程数以及空闲进程退出前等待的时间量。

一个 AIO 守护进程池用于服务套接字的异步 I/O 请求。这些进程名为“soaiod<N>”。以下 sysctl 节点用于此池：

**`kern.ipc.aio.num_procs`** 池中当前进程数。

**`kern.ipc.aio.target_procs`** 池中应存在的最小进程数。

**`kern.ipc.aio.max_procs`** 池中允许的最大进程数。

**`kern.ipc.aio.lifetime`** 进程允许空闲的时间量（时钟滴答）。如果进程空闲此时长且池中进程数多于目标最小值，则该进程将退出。

第二个 AIO 守护进程池用于服务除原始磁盘 I/O 请求外的所有其他异步 I/O 请求。这些进程名为“aiod<N>”。以下 sysctl 节点用于此池：

**`vfs.aio.num_aio_procs`** 池中当前进程数。

**`vfs.aio.target_aio_procs`** 池中应存在的最小进程数。

**`vfs.aio.max_aio_procs`** 池中允许的最大进程数。

**`vfs.aio.aiod_lifetime`** 进程允许空闲的时间量（时钟滴答）。如果进程空闲此时长且池中进程数多于目标最小值，则该进程将退出。

原始磁盘的异步 I/O 请求在临时连接与请求关联的用户页面后，直接排队到磁盘设备层。这些请求不由任何 AIO 守护进程池服务。

系统范围和每进程都施加了对异步 I/O 请求的若干限制。这些限制通过以下 sysctl 配置：

**`vfs.aio.max_buf_aio`** 单个进程允许的对原始磁盘排队的异步 I/O 请求的最大数量。已完成但状态尚未通过 aio_return(2) 或 aio_waitcomplete(2) 检索的异步 I/O 请求不计入此限制。

**`vfs.aio.num_buf_aio`** 系统范围的对原始磁盘排队的异步 I/O 请求数。

**`vfs.aio.max_aio_queue_per_proc`** 单个进程由默认 AIO 守护进程池同时服务的异步 I/O 请求的最大数量。

**`vfs.aio.max_aio_per_proc`** 单个进程允许的未完成异步 I/O 请求的最大数量。这包括尚未服务的请求、当前正在服务的请求以及已完成但状态尚未通过 aio_return(2) 或 aio_waitcomplete(2) 检索的请求。

**`vfs.aio.num_queue_count`** 系统范围的未完成异步 I/O 请求数。

**`vfs.aio.max_aio_queue`** 系统范围允许的未完成异步 I/O 请求的最大数量。

异步 I/O 控制缓冲区在初始化各个字段之前应清零。这确保所有字段都被初始化。

所有异步 I/O 控制缓冲区都在 `aio_sigevent` 字段中包含一个 `sigevent` 结构，可用于在操作完成时请求通知。

对于 `SIGEV_KEVENT` 通知，`sigevent` 的 `sigev_notify_kqueue` 字段应包含事件应附加到的 kqueue 的描述符，其 `sigev_notify_kevent_flags` 字段可包含 `EV_ONESHOT`、`EV_CLEAR` 和/或 `EV_DISPATCH`，其 `sigev_notify` 字段应设置为 `SIGEV_KEVENT`。发布的 kevent 将包含：

存储在 `aio_sigevent.sigev_value` 中的值

| **Member** | **Value** |
| ---------- | --------- |
| `ident` | 异步 I/O 控制缓冲区指针 |
| `filter` | `EVFILT_AIO` |
| `flags` | `EV_EOF` |
| `udata` | |

对于 `SIGEV_SIGNO` 和 `SIGEV_THREAD_ID` 通知，排队信号的信息将在 `si_code` 字段中包含 `SI_ASYNCIO`，在 `si_value` 字段中包含存储在 `sigevent.sigev_value` 中的值。

对于 `SIGEV_THREAD` 通知，存储在 `aio_sigevent.sigev_value` 中的值将传递给 `aio_sigevent.sigev_notify_function`，如 [sigevent(3)](../man3/sigevent.3.md) 所述。

## 参见

aio_cancel(2), aio_error(2), aio_read(2), aio_readv(2), aio_return(2), aio_suspend(2), aio_waitcomplete(2), aio_write(2), aio_writev(2), lio_listio(2), [sigevent(3)](../man3/sigevent.3.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`aio` 设施作为内核选项出现在 FreeBSD 3.0 中。`aio` 内核模块出现在 FreeBSD 5.0 中。`aio` 设施在 FreeBSD 11.0 中集成到所有内核中。
