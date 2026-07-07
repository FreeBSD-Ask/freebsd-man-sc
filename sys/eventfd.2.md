# eventfd(2)

`eventfd` — 创建用于事件通知的文件描述符

## 名称

`eventfd`

## 库

Lb libc

## 概要

`#include <sys/eventfd.h>`

```c
int
eventfd(unsigned int initval, int flags);

int
eventfd_read(int fd, eventfd_t *value);

int
eventfd_write(int fd, eventfd_t value);
```

## 描述

`eventfd()` 创建一个具有事件计数器或信号量语义的特殊文件描述符，专为进程间通信设计。返回的文件描述符引用一个内核对象，该对象包含一个无符号 64 位整数计数器，使用 `initval` 参数的值进行初始化。

`flags` 参数可包含以下值按位*或*的结果：

**`EFD_CLOEXEC`** 在文件描述符上设置 FD_CLOEXEC

**`EFD_NONBLOCK`** 在读/写操作上不阻塞

**`EFD_SEMAPHORE`** 使用信号量语义

文件操作具有以下语义：

- 如果未设置 `EFD_SEMAPHORE`，返回计数器的当前值，并将该值重置为零。
- 如果设置了 `EFD_SEMAPHORE`，返回常量 1，并将该值减 1。

- 当计数器大于零时，文件描述符可读。
- 当计数器小于最大值时，文件描述符可写。

**[read(2)](read.2.md)** 如果计数器为零，调用阻塞直到计数器变为非零，除非设置了 `EFD_NONBLOCK`，在这种情况下改为以 `EAGAIN` 失败。如果计数器非零：数值以 64 位（8 字节）按主机字节序编码。如果提供的缓冲区中可用字节少于 8 字节，[read(2)](read.2.md) 调用以 `EINVAL` 失败。

**[write(2)](write.2.md)** 将给定值加到计数器上。计数器中可存储的最大值为无符号 64 位整数的最大值减一（0xfffffffffffffffe）。如果结果值超过最大值，调用将阻塞直到该值通过 [read(2)](read.2.md) 减少，除非设置了 `EFD_NONBLOCK`，在这种情况下改为以 `EAGAIN` 失败。数值以 64 位（8 字节）按主机字节序编码。如果提供的缓冲区中可用字节少于 8 字节，或给定了值 0xffffffffffffffff，[write(2)](write.2.md) 调用以 `EINVAL` 失败。

**[poll(2)](poll.2.md)** 通过 [poll(2)](poll.2.md)、ppoll(2)、[select(2)](select.2.md)、[pselect(2)](pselect.2.md)、[kqueue(2)](kqueue.2.md) 接收通知时，适用以下语义：

由 `eventfd()` 创建的文件描述符可通过 sendmsg(2) 传递给其他进程，并在 [fork(2)](fork.2.md) 之间保留；在两种情况下，描述符在两个进程中引用同一计数器。除非指定了 `O_CLOEXEC` 标志，否则创建的文件描述符在 [execve(2)](execve.2.md) 系统调用之间保持打开；参见 [close(2)](close.2.md)、[fcntl(2)](fcntl.2.md) 和 `O_CLOEXEC` 描述。

`eventfd_read()` 和 `eventfd_write()` 是 [read(2)](read.2.md) 和 [write(2)](write.2.md) 系统调用的轻量封装，为与 glibc 兼容而提供。

## 返回值

如果成功，`eventfd()` 返回一个非负整数，称为文件描述符。失败时返回 -1，并设置 `errno` 以指示错误。

`eventfd_read()` 和 `eventfd_write()` 函数在操作成功时返回 0，否则返回 -1。

## 错误

`eventfd()` 可能因以下情况失败：

**[`EINVAL`]** 给定给 `eventfd()` 的 `flags` 参数包含未知位。

**[`EMFILE`]** 进程已达到其打开文件描述符限制。

**[`ENFILE`]** 系统文件表已满。

**[`ENOMEM`]** 没有可用于创建内核对象的内存。

## 参见

[close(2)](close.2.md), [kqueue(2)](kqueue.2.md), [poll(2)](poll.2.md), [read(2)](read.2.md), [select(2)](select.2.md), [write(2)](write.2.md)

## 标准

`eventfd()` 系统调用是非标准的。它存在于 Linux 中。

## 历史

`eventfd()` 系统调用首次出现于 FreeBSD 13.0。
