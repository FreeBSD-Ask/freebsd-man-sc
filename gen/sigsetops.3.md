# sigsetops(3)

`sigemptyset` — 操作信号集

## 名称

`sigemptyset`, `sigfillset`, `sigaddset`, `sigandset`, `sigdelset`, `sigisemptyset`, `sigismember`, `sigorset`

## 库

Lb libc

## 概要

```c
#include <signal.h>

int
sigemptyset(sigset_t *set);

int
sigfillset(sigset_t *set);

int
sigaddset(sigset_t *set, int signo);

int
sigandset(sigset_t *set, const sigset_t *left, const sigset_t *right);

int
sigdelset(sigset_t *set, int signo);

int
sigisemptyset(const sigset_t *set);

int
sigismember(const sigset_t *set, int signo);

int
sigorset(sigset_t *set, const sigset_t *left, const sigset_t *right);
```

## 描述

这些函数操作存储在 `sigset_t` 中的信号集。在使用 `sigset_t` 类型的对象之前，必须先调用 `sigemptyset()` 或 `sigfillset()`。

`sigemptyset()` 函数将信号集初始化为空。

`sigfillset()` 函数将信号集初始化为包含所有信号。

`sigaddset()` 函数将指定的信号 `signo` 添加到信号集中。

`sigandset()` 函数将指定的 `set` 设置为 `left` 和 `right` 信号集中所有信号的逻辑与。

`sigdelset()` 函数从信号集中删除指定的信号 `signo`。

`sigisemptyset()` 函数返回指定的 `set` 是否为空。

`sigismember()` 函数返回指定的信号 `signo` 是否包含在信号集中。

`sigorset()` 函数将指定的 `set` 设置为 `left` 和 `right` 信号集中所有信号的逻辑或。

## 返回值

`sigisemptyset()` 函数在集合为空时返回 1，否则返回 0。

`sigismember()` 函数在信号是集合的成员时返回 1，否则返回 0。

其他函数成功时返回 0。返回 -1 表示发生错误，并设置全局变量 `errno` 以指示原因。

## 错误

这些函数在以下情况之一时可能失败：

**`[EINVAL]`** `signo` 的值无效。

## 参见

[kill(2)](../sys/kill.2.md), [sigaction(2)](../sys/sigaction.2.md), [sigpending(2)](../sys/sigpending.2.md), [sigprocmask(2)](../sys/sigprocmask.2.md), [sigsuspend(2)](../sys/sigsuspend.2.md)

## 标准

`sigandset()`、`sigisemptyset()` 和 `sigorset()` 函数是 FreeBSD 扩展，与 musl libc 和 GNU libc 提供的同名函数兼容。

其余函数由 IEEE Std 1003.1-1988 ("POSIX.1") 定义。
