# write(2)

`write` — 写入输出

## 名称

`write`, `writev`, `pwrite`, `pwritev`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
ssize_t
write(int fd, const void *buf, size_t nbytes);

ssize_t
pwrite(int fd, const void *buf, size_t nbytes, off_t offset);
```

`#include <sys/uio.h>`

```c
ssize_t
writev(int fd, const struct iovec *iov, int iovcnt);

ssize_t
pwritev(int fd, const struct iovec *iov, int iovcnt, off_t offset);
```

## 描述

`write()` 系统调用尝试将 `nbytes` 字节的数据从 `buf` 所指向的缓冲区写入由描述符 `fd` 引用的对象。`writev()` 系统调用执行相同的操作，但输出数据从 `iov` 数组成员指定的 `iovcnt` 个缓冲区中聚集：iov[0]、iov[1]、...、iov[iovcnt-1]。`pwrite()` 和 `pwritev()` 系统调用执行相同的功能，但写入文件中指定的位置，而不修改文件指针。

对于 `writev()` 和 `pwritev()`，`iovec` 结构体定义如下：

```c
struct iovec {
	void   *iov_base;  /* 基址。 */
	size_t iov_len;    /* 长度。 */
};
```

每个 `iovec` 条目指定内存中应写入数据的区域的基址和长度。`writev()` 系统调用会先写完一个完整的区域，再处理下一个。

对于可寻址的对象，`write()` 从与 `fd` 关联的指针所给定的位置开始，参见 [lseek(2)](lseek.2.md)。从 `write()` 返回时，该指针会增加写入的字节数。

不可寻址的对象总是从当前位置写入。与这种对象关联的指针值是未定义的。

如果实际用户不是超级用户，则 `write()` 会清除文件上的 set-user-id 位。这可以防止用户通过“捕获”超级用户拥有的可写 set-user-id 文件来渗透系统安全。

在套接字等受流量控制的对象上使用非阻塞 I/O 时，`write()` 和 `writev()` 写入的字节数可能少于请求的数量；必须注意返回值，并在可能时重试操作的剩余部分。

## 写入的原子性

对本地文件系统上的常规文件进行操作时，`write()` 的效果是原子的。按照 POSIX 标准要求，对于常规文件的文件数据和元数据，`read()`、`write()` 和 `ftruncate()` 函数及其变体彼此之间是原子的。更多信息请参见 -p1003.1-2024 第 2 卷第 2.9.7 节。

FreeBSD 通过对相应函数影响的文件字节范围加读/写范围锁来实现该要求。

## 返回值

成功完成时返回写入的字节数。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`write()`、`writev()`、`pwrite()` 和 `pwritev()` 系统调用在以下情况下会失败，且文件指针保持不变：

**[EBADF]** `fd` 参数不是以写入方式打开的有效描述符。

**[EPIPE]** 尝试写入一个未被任何进程以读取方式打开的管道。

**[EPIPE]** 尝试写入一个未连接到对端套接字的 `SOCK_STREAM` 类型套接字。

**[EFBIG]** 尝试写入的文件超过了进程的文件大小限制或最大文件大小。

**[EFAULT]** `iov` 的某部分或要写入文件的数据指向进程分配地址空间之外。

**[EINVAL]** 与 `fd` 关联的指针为负值。

**[ENOSPC]** 包含该文件的文件系统上没有剩余可用空间。

**[EDQUOT]** 包含该文件的文件系统上用户的磁盘块配额已耗尽。

**[EIO]** 在对文件系统进行读写操作时发生 I/O 错误。

**[EINTR]** 在写入完成之前被信号中断。

**[EAGAIN]** 文件已标记为非阻塞 I/O，且无法立即写入任何数据。

**[EINVAL]** `nbytes` 的值大于 `SSIZE_MAX`（或者如果 sysctl `debug.iosize_max_clamp` 不为零，则大于 `INT_MAX`）。

**[EINVAL]** 文件描述符引用的是一个裸设备，且写入偏移量或大小不是设备块大小的整数倍。

**[EINTEGRITY]** `fd` 的后备存储在读取时检测到损坏的数据。（例如，写入部分文件系统块可能需要先读取现有块，这可能触发此错误。）

此外，`writev()` 和 `pwritev()` 可能返回以下错误之一：

**[EDESTADDRREQ]** 当写入一个已通过 [connect(2)](connect.2.md) 设置目标地址的 UNIX 域数据报套接字时，目标地址不再可用。

**[EINVAL]** `iovcnt` 参数小于或等于 0，或大于 `IOV_MAX`。

**[EINVAL]** `iov` 数组中的某个 `iov_len` 值为负。

**[EINVAL]** `iov_len` 值的总和大于 `SSIZE_MAX`（或者如果 sysctl `debug.iosize_max_clamp` 不为零，则大于 `INT_MAX`）。

**[ENOBUFS]** 写入套接字时 mbuf 池已完全耗尽。

`pwrite()` 和 `pwritev()` 系统调用还可能返回以下错误：

**[EINVAL]** `offset` 值为负。

**[ESPIPE]** 文件描述符与管道、套接字或 FIFO 关联。

## 参见

[fcntl(2)](fcntl.2.md), [lseek(2)](lseek.2.md), [open(2)](open.2.md), [pipe(2)](pipe.2.md), [select(2)](select.2.md)

## 标准

`write()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。`writev()` 和 `pwrite()` 系统调用预期符合 -xpg4.2。

## 历史

`pwritev()` 系统调用首次出现于 FreeBSD 6.0。`pwrite()` 函数首次出现于 AT&T System V Release 4 UNIX。`writev()` 系统调用首次出现于 4.2BSD。`write()` 函数首次出现于 Version 1 AT&T UNIX。

## 缺陷

如果设置了 `O_APPEND`，`pwrite()` 系统调用会追加到文件而不改变文件偏移量，这与 IEEE Std 1003.1-2008 ("POSIX.1") 的规定相反——按后者规定，无论是否设置 `O_APPEND`，`pwrite()` 都写入 `offset` 处。
