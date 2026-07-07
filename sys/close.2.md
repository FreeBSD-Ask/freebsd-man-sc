# close(2)

`close` — 删除描述符

## 名称

`close`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
close(int fd);
```

## 描述

`close()` 系统调用从每进程对象引用表中删除一个描述符。如果这是对底层对象的最后一个引用，该对象将被停用。例如，在最后一次关闭文件时，与该文件关联的当前 *seek* 指针会丢失；在最后一次关闭 [socket(2)](socket.2.md) 时，关联的命名信息和排队数据会被丢弃；在最后一次关闭持有咨询锁的文件时，该锁会被释放（参见 [flock(2)](flock.2.md)）。然而，System V 和 -p1003.1-88 的语义规定，当进程关闭该文件的 *任何* 文件描述符时，与该文件相关联的所有 [fcntl(2)](fcntl.2.md) 咨询记录锁都会被移除。

当进程退出时，所有关联的文件描述符都会被释放，但由于每个进程的活动描述符数量有限制，因此在处理大量文件描述符时，`close()` 系统调用非常有用。

当进程执行 fork 时（参见 [fork(2)](fork.2.md)），新子进程的所有描述符引用的对象与 fork 之前父进程中的相同。如果随后要通过 [execve(2)](execve.2.md) 运行新进程，该进程通常会继承这些描述符。在尝试 [execve(2)](execve.2.md) 之前，可以使用 dup2(2) 重新排列大多数描述符，或使用 `close()` 删除它们。但如果其中某些描述符在 execve 失败时仍需使用，就必须安排在 execve 成功时关闭它们。为此，提供了调用 “`fcntl(d, F_SETFD, FD_CLOEXEC)`”，用于安排描述符在成功 execve 后被关闭；调用 “`fcntl(d, F_SETFD, 0)`” 恢复默认行为，即不关闭描述符。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`close()` 系统调用在以下情况下会失败：

**[`EBADF`]** `fd` 参数不是活动的描述符。

**[`EINTR`]** 接收到中断。

**[`ENOSPC`]** 底层对象未完整写入，缓存数据丢失。

除 `EBADF` 外的任何错误情况下，所提供的文件描述符都会被释放，因此不再有效。

## 参见

[accept(2)](accept.2.md), [closefrom(2)](closefrom.2.md), [execve(2)](execve.2.md), [fcntl(2)](fcntl.2.md), [flock(2)](flock.2.md), [open(2)](open.2.md), [pipe(2)](pipe.2.md), [socket(2)](socket.2.md), [socketpair(2)](socketpair.2.md)

## 标准

`close()` 系统调用预期遵循 IEEE Std 1003.1-1990 ("POSIX.1")。

## 历史

`close()` 函数出现于 Version 1 AT&T UNIX。
