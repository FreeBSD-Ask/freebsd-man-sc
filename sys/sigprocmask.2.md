# sigprocmask(2)

`sigprocmask` — 操作当前信号掩码

## 名称

`sigprocmask`

## 库

Lb libc

## 概要

`#include <signal.h>`

```c
int
sigprocmask(int how, const sigset_t * restrict set,
    sigset_t * restrict oset);
```

## 描述

`sigprocmask()` 系统调用检查和/或更改当前信号掩码（即被阻止传递的那些信号）。如果信号是当前信号掩码集的成员，则被阻止。

如果 `set` 不为 null，`sigprocmask()` 的行为取决于 `how` 参数的值。信号掩码根据指定的 `set` 和当前掩码的函数关系进行更改。函数由 `how` 使用 `signal.h` 中定义的以下值之一指定：

**`SIG_BLOCK`** 新掩码是当前掩码与指定 `set` 的并集。

**`SIG_UNBLOCK`** 新掩码是当前掩码与指定 `set` 补集的交集。

**`SIG_SETMASK`** 当前掩码被指定的 `set` 替换。

如果 `oset` 不为 null，它将被设置为信号掩码的前一个值。当 `set` 为 null 时，`how` 的值无意义，掩码保持不变，提供了一种在不修改的情况下检查信号掩码的方法。

系统静默地不允许阻止 `SIGKILL` 或 `SIGSTOP`。

在线程应用程序中，必须使用 [pthread_sigmask(3)](../man3/pthread_sigmask.3.md) 而非 `sigprocmask()`。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

`sigprocmask()` 系统调用在以下情况下会失败，且信号掩码保持不变：

**[`EINVAL`]** `how` 参数的值不是此处列出的值之一。

## 参见

[kill(2)](kill.2.md), [sigaction(2)](sigaction.2.md), [sigpending(2)](sigpending.2.md), [sigsuspend(2)](sigsuspend.2.md), [fpsetmask(3)](../man3/fpgetround.3.md), [pthread_sigmask(3)](../man3/pthread_sigmask.3.md), [sigsetops(3)](../gen/sigsetops.3.md)

## 标准

`sigprocmask()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。