# sigpending(2)

`sigpending` — 获取待处理信号

## 名称

`sigpending`

## 库

Lb libc

## 概要

`#include <signal.h>`

```c
int
sigpending(sigset_t *set);
```

## 描述

`sigpending()` 系统调用在 `set` 所指示的位置返回待递送给调用线程或调用进程的信号的掩码。信号可能因为当前被屏蔽而处于待处理状态，或在递交之前的瞬时处于待处理状态（尽管后一种情况通常无法检测）。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`sigpending()` 系统调用在以下情况下会失败：

**[`EFAULT`]** `set` 参数指定了无效地址。

## 参见

[sigaction(2)](sigaction.2.md), [sigprocmask(2)](sigprocmask.2.md), [sigsuspend(2)](sigsuspend.2.md), [sigsetops(3)](../gen/sigsetops.3.md)

## 标准

`sigpending()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1") 规范。
