# sendfile(2)

`sendfile` — 将文件发送到套接字

## 名称

`sendfile`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <sys/uio.h>`

```c
int
sendfile(int fd, int s, off_t offset, size_t nbytes,
    struct sf_hdtr *hdtr, off_t *sbytes, int flags);
```

## 描述

`sendfile()` 系统调用将由描述符 `fd` 指定的常规文件或共享内存对象发送到由描述符 `s` 指定的流套接字。

`offset` 参数指定文件中开始发送的位置。如果 `offset` 超出文件结尾，系统将返回成功并按以下所述报告发送了 0 字节。`nbytes` 参数指定应发送文件的多少字节，其中 0 具有特殊含义，即一直发送到文件结尾。

通过指定一个指向 `struct sf_hdtr` 的指针，可以在文件数据之前和之后发送可选的头部和/或尾部，该结构具有以下形式：

```c
struct sf_hdtr {
        struct iovec *headers;  /* 指向头部 iovec 的指针 */
        int hdr_cnt;            /* 头部 iovec 的数量 */
        struct iovec *trailers; /* 指向尾部 iovec 的指针 */
        int trl_cnt;            /* 尾部 iovec 的数量 */
};
```

`headers` 和 `trailers` 指针若非 `NULL`，则指向 `struct iovec` 结构数组。有关 iovec 结构的信息，请参见 `writev()` 系统调用。这些数组中 iovec 的数量由 `hdr_cnt` 和 `trl_cnt` 指定。

若非 `NULL`，系统会将套接字上已发送的总字节数写入 `sbytes` 所指向的变量。

`flags` 参数的最低 16 位是以下值的位图：

**`SF_NODISKIO`** 此标志使 `sendfile` 在遇到忙页时返回 `EBUSY` 而非阻塞。这种罕见情况可能发生在其他进程正在处理文件同一区域时。建议在短时间内重试该操作。注意，在较早的 FreeBSD 版本中，`SF_NODISKIO` 的含义略有不同。该标志阻止 `sendfile` 在遇到无效（未缓存）页时运行 I/O 操作，从而避免阻塞在 I/O 上。从 FreeBSD 11 开始，`sendfile` 从 [ffs(4)](../man4/ffs.4.md) 文件系统发送文件时不会阻塞在 I/O 上（参见 [实现说明](#实现说明)），因此该条件不再适用。然而，如果应用程序使用了 `SF_NODISKIO` 并在遇到 `EBUSY` 时执行与较早 FreeBSD 版本相同的操作（例如 [aio_read(2)](aio_read.2.md)、[read(2)](read.2.md) 或在不同上下文中调用 `sendfile`），则是安全的。

**`SF_NOCACHE`** 发送到套接字的数据不会被虚拟内存系统缓存，而是直接释放到空闲页面池中。

**`SF_USER_READAHEAD`** `sendfile` 在发送数据时具有一些内部启发式算法来执行预读。此标志强制 `sendfile` 覆盖任何启发式计算的预读，并精确使用应用程序指定的预读。有关预读的更多细节，请参见 [设置预读](#设置预读)。

当使用标记为非阻塞 I/O 的套接字时，`sendfile()` 可能发送少于请求的字节数。在这种情况下，成功写入的字节数会在 `*sbytes` 中返回（如果指定了），并返回错误 `EAGAIN`。

## 设置预读

`sendfile` 使用基于请求大小和文件系统布局的内部启发式算法来执行预读。此外，应用程序可以请求额外的预读。`flags` 参数的最高 16 位指定 `sendfile` 在读取文件时可以预读的页面数量。提供了一个宏 `SF_FLAGS()` 用于组合预读量和标志。以下示例展示如何指定 16 页的预读和 `SF_NOCACHE` 标志：

```c
        SF_FLAGS(16, SF_NOCACHE)
```

`sendfile` 将使用应用程序指定的预读或内部计算的预读中的较大者。设置 `SF_USER_READAHEAD` 标志会关闭所有启发式算法，并将最大可能的预读长度设置为通过标志指定的页面数量。

## 实现说明

FreeBSD 的 `sendfile()` 实现在从 [ffs(4)](../man4/ffs.4.md) 文件系统发送文件时不会阻塞在磁盘 I/O 上。系统调用在实际 I/O 完成之前就返回成功，数据稍后会被无人值守地放入套接字。但是，套接字中数据的顺序会被保留，因此对套接字进行进一步的写入是安全的。

FreeBSD 的 `sendfile()` 实现是“零拷贝”的，意味着它经过了优化，以避免对文件数据进行拷贝。

## 调优

### 物理分页缓冲区

`sendfile()` 使用 vnode pager 将文件页读入内存。pager 使用一个物理缓冲区池来运行其 I/O 操作。当系统的 pbuf 耗尽时，sendfile 会阻塞并报告状态“`zonelimit`”。该池的大小可以通过 `vm.vnode_pbufs` [loader.conf(5)](../man5/loader.conf.5.md) 可调参数进行调整，并可在运行时通过同名 [sysctl(8)](../man8/sysctl.8.md) OID 查看。

### sendfile(2) 缓冲区

在某些架构上，此系统调用内部使用一种特殊的 `sendfile()` 缓冲区（`struct sf_buf`）来处理向客户端发送文件数据。如果发送套接字是阻塞的，且没有足够的 `sendfile()` 缓冲区可用，`sendfile()` 会阻塞并报告状态“`sfbufa`”。如果发送套接字是非阻塞的且没有足够的 `sendfile()` 缓冲区可用，调用将阻塞并等待必要的缓冲区变为可用后再完成调用。

分配的 `sf_buf` 数量应与通过 `sendfile()` 向客户端发送数据所使用的 nmbclusters 数量成比例。请相应调整以避免阻塞！大量使用 `sendfile()` 的繁忙安装可能希望增加这些值，使其与 `kern.ipc.nmbclusters` 一致（详情参见 [tuning(7)](../man7/tuning.7.md)）。

可用的 `sendfile()` 缓冲区数量在启动时由 `kern.ipc.nsfbufs` [loader.conf(5)](../man5/loader.conf.5.md) 变量或 `NSFBUFS` 内核配置可调参数决定。`sendfile()` 缓冲区数量随 `kern.maxusers` 缩放。只读的 [sysctl(8)](../man8/sysctl.8.md) 变量 `kern.ipc.nsfbufsused` 和 `kern.ipc.nsfbufspeak` 分别显示当前和峰值的 `sendfile()` 缓冲区使用量。这些值也可通过 `netstat` `-m` 查看。

如果 [sysctl(8)](../man8/sysctl.8.md) OID `kern.ipc.nsfbufs` 不存在，则你的架构不需要使用 `sendfile()` 缓冲区，因为它们的任务可以由通用虚拟内存结构高效地完成。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

**[EAGAIN]** 套接字被标记为非阻塞 I/O，且由于套接字缓冲区已满，并非所有数据都已发送。如果指定了 `sbytes`，成功发送的字节数将在 `*sbytes` 中返回。

**[EBADF]** `fd` 参数不是有效的文件描述符。

**[EBADF]** `s` 参数不是有效的套接字描述符。

**[EBUSY]** 遇到忙页且指定了 `SF_NODISKIO`。可能已发送部分数据。

**[EFAULT]** 为某个参数指定了无效地址。

**[EINTR]** 信号在 `sendfile()` 完成之前中断了它。如果指定了 `sbytes`，成功发送的字节数将在 `*sbytes` 中返回。

**[EINVAL]** `fd` 参数不是常规文件。

**[EINVAL]** `s` 参数不是 SOCK_STREAM 类型的套接字。

**[EINVAL]** `offset` 参数为负数。

**[EIO]** 从 `fd` 读取时发生错误。

**[EINTEGRITY]** 从 `fd` 读取时检测到损坏的数据。

**[ENOTCAPABLE]** `fd` 或 `s` 参数权限不足。

**[ENOBUFS]** 系统无法分配内部缓冲区。

**[ENOTCONN]** `s` 参数指向未连接的套接字。

**[ENOTSOCK]** `s` 参数不是套接字。

**[EOPNOTSUPP]** 描述符 `fd` 的文件系统不支持 `sendfile()`。

**[EPIPE]** 套接字对端已关闭连接。

## 参见

[netstat(1)](../man1/netstat.1.md), [open(2)](open.2.md), [send(2)](send.2.md), [socket(2)](socket.2.md), [writev(2)](write.2.md), [loader.conf(5)](../man5/loader.conf.5.md), [tuning(7)](../man7/tuning.7.md), [sysctl(8)](../man8/sysctl.8.md)

> K. Elmeleegy, A. Chanda, A. L. Cox, W. Zwaenepoel, "A Portable Kernel Abstraction for Low-Overhead Ephemeral Mapping Management", *The Proceedings of the 2005 USENIX Annual Technical Conference*, pp. 223-236, 2005.

## 历史

`sendfile()` 系统调用首次出现于 FreeBSD 3.0。本手册页首次出现于 FreeBSD 3.1。在 FreeBSD 10 中引入了对发送共享内存描述符的支持。在 FreeBSD 11 中引入了非阻塞实现。

## 作者

`sendfile()` 系统调用的初始实现和本手册页由 David G. Lawrence <dg@dglawrence.com> 编写。FreeBSD 11 的实现由 Gleb Smirnoff <glebius@FreeBSD.org> 编写。

## 缺陷

如果为 `sbytes` 提供了无效地址，`sendfile()` 系统调用不会失败，即不会返回 `-1` 并将 `errno` 设置为 `EFAULT`。`sendfile()` 系统调用不支持 SCTP 套接字，它会返回 `-1` 并将 `errno` 设置为 `EINVAL`。
