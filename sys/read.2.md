# read(2)

`read` — 读取输入

## 名称

`read`, `readv`, `pread`, `preadv`

## 库

Lb libc

## 概要

```c
#include <unistd.h>

ssize_t
read(int fd, void *buf, size_t nbytes);

ssize_t
pread(int fd, void *buf, size_t nbytes, off_t offset);
```

```c
#include <sys/uio.h>

ssize_t
readv(int fd, const struct iovec *iov, int iovcnt);

ssize_t
preadv(int fd, const struct iovec *iov, int iovcnt, off_t offset);
```

## 描述

`read()` 系统调用尝试从描述符 `fd` 所引用的对象读取 `nbytes` 数据到 `buf` 所指向的缓冲区。`readv()` 系统调用执行相同操作，但将输入数据分散到 `iov` 数组成员指定的 `iovcnt` 个缓冲区：iov[0]、iov[1]、...、iov[iovcnt-1]。`pread()` 和 `preadv()` 系统调用执行相同功能，但从文件中指定位置读取而不修改文件指针。

对于 `readv()` 和 `preadv()`，`iovec` 结构定义为：

```c
struct iovec {
        void   *iov_base;  /* 基地址 */
        size_t iov_len;    /* 长度 */
};
```

每个 `iovec` 条目指定内存中应放置数据的区域的基地址和长度。`readv()` 系统调用在继续下一个区域之前始终完全填满一个区域。

对于可定位的对象，`read()` 从与 `fd` 关联的指针给定的位置开始（参见 [lseek(2)](lseek.2.md)）。从 `read()` 返回时，指针增加实际读取的字节数。

不可定位的对象始终从当前位置读取。与此类对象关联的指针值未定义。

成功完成时，`read()`、`readv()`、`pread()` 和 `preadv()` 返回实际读取并放入缓冲区的字节数。当描述符引用一个在文件结束前还有那么多字节的常规文件时，系统保证读取请求的字节数，但在其他情况下不保证。

根据 IEEE Std 1003.1-2004 ("POSIX.1")，当 `read()` 和 `write()` 系统调用对常规文件操作时，它们在文件内容方面的效果彼此是原子的。如果两个线程分别调用 `read()` 或 `write()` 系统调用，每个调用将看到另一个调用的所有更改或看不到任何更改。FreeBSD 内核通过锁定受调用影响的文件范围来实现此保证。

## 返回值

如果成功，返回实际读取的字节数。读取到文件结束时返回零。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`read()`、`readv()`、`pread()` 和 `preadv()` 系统调用在以下情况下会失败：

**[EBADF]** `fd` 参数不是有效的、以读方式打开的文件或套接字描述符。

**[ECONNRESET]** `fd` 参数引用套接字，且远程套接字端被强制关闭。

**[EFAULT]** `buf` 参数指向分配地址空间之外。

**[EIO]** 从文件系统读取时发生 I/O 错误。

**[EINTEGRITY]** 从文件系统读取数据时检测到损坏的数据。

**[EBUSY]** 无法从文件读取，例如 **/proc/<pid>/regs** 而 <pid> 未停止时。

**[EINTR]** 从慢速设备（即可能阻塞任意时间的设备）的读取在数据到达之前被信号传递中断。

**[EINVAL]** 与 `fd` 关联的指针为负。

**[EAGAIN]** 文件标记为非阻塞 I/O，且没有可读数据。

**[EISDIR]** 文件描述符与目录关联。仅当文件系统支持且 `security.bsd.allow_read_dir` sysctl MIB 设置为非零值时，root 才能直接读取目录。对于大多数场景，应改用 [readdir(3)](../gen/directory.3.md) 函数。

**[EOPNOTSUPP]** 文件描述符与不允许常规读操作的文件系统和文件类型关联。

**[EOVERFLOW]** 文件描述符与常规文件关联，`nbytes` 大于 0，`offset` 在文件结束之前，且 `offset` 大于或等于为此文件系统建立的最大偏移量。

**[EINVAL]** 值 `nbytes` 大于 `SSIZE_MAX`（或如果 sysctl `debug.iosize_max_clamp` 非零，则大于 `INT_MAX`）。

此外，`readv()` 和 `preadv()` 可能返回以下错误之一：

**[EINVAL]** `iovcnt` 参数小于等于 0，或大于 `IOV_MAX`。

**[EINVAL]** `iov` 数组中的某个 `iov_len` 值为负。

**[EINVAL]** `iov` 数组中 `iov_len` 值的总和大于 `SSIZE_MAX`（或如果 sysctl `debug.iosize_max_clamp` 非零，则大于 `INT_MAX`）。

**[EFAULT]** `iov` 数组的一部分指向进程分配地址空间之外。

`pread()` 和 `preadv()` 系统调用还可能返回以下错误：

**[EINVAL]** `offset` 值为负。

**[ESPIPE]** 文件描述符与管道、套接字或 FIFO 关联。

## 参见

[dup(2)](dup.2.md), [fcntl(2)](fcntl.2.md), [getdirentries(2)](getdirentries.2.md), [lseek(2)](lseek.2.md), [open(2)](open.2.md), [pipe(2)](pipe.2.md), [select(2)](select.2.md), [socket(2)](socket.2.md), [socketpair(2)](socketpair.2.md), [write(2)](write.2.md), [fread(3)](../stdio/fread.3.md), [readdir(3)](../gen/directory.3.md)

## 标准

`read()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。`readv()` 和 `pread()` 系统调用预期符合 -xpg4.2。

## 历史

`preadv()` 系统调用首次出现于 FreeBSD 6.0。`pread()` 函数首次出现于 AT&T System V Release 4 UNIX。`readv()` 系统调用首次出现于 4.2BSD。`read()` 函数首次出现于 Version 1 AT&T UNIX。