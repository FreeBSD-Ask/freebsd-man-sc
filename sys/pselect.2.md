# pselect(2)

`pselect` — 按 POSIX.1g 风格的同步 I/O 多路复用

## 名称

`pselect`

## 库

Lb libc

## 概要

`#include <sys/select.h>`

```c
int
pselect(int nfds, fd_set * restrict readfds, fd_set * restrict writefds,
    fd_set * restrict exceptfds,
    const struct timespec * restrict timeout,
    const sigset_t * restrict newsigmask);
```

## 描述

`pselect` 函数由 -p1003.1g-2000 引入，作为 [select(2)](select.2.md) 的一个稍强版本。`nfds`、`readfds`、`writefds` 和 `exceptfds` 参数均与 `select` 的相应参数相同。`pselect` 中的 `timeout` 参数指向一个 `const struct timespec`，而不是 `select` 所使用的可能被修改的 `struct timeval`；与 `select` 中一样，可传递空指针以指示 `pselect` 应无限期等待。最后，`newsigmask` 指定一个在等待输入时设置的信号掩码。当 `pselect` 返回时，原始信号掩码会被恢复。如果 `newsigmask` 是空指针，`pselect` 的行为类似于 `select`，不设置或恢复信号掩码。

关于此接口语义的更详细讨论以及用于操作 `fd_set` 数据类型的宏，参见 [select(2)](select.2.md)。

## 返回值

`pselect` 函数在与 `select` 相同的条件下返回相同的值。

## 错误

`pselect` 函数可能因 [select(2)](select.2.md) 中记录的任何原因而失败，以及（如果提供了信号掩码）[sigprocmask(2)](sigprocmask.2.md) 中记录的原因。

## 参见

[kqueue(2)](kqueue.2.md), [poll(2)](poll.2.md), [select(2)](select.2.md), [sigprocmask(2)](sigprocmask.2.md), [sigsuspend(2)](sigsuspend.2.md)

## 标准

`pselect` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`pselect` 函数首次出现于 FreeBSD 5.0。

## 作者

`pselect` 函数的首个实现及本手册页由 Garrett Wollman <wollman@FreeBSD.org> 编写。
