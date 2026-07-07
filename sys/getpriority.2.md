# getpriority(2)

`getpriority` — 获取/设置程序调度优先级

## 名称

`getpriority`, `setpriority`

## 库

Lb libc

## 概要

`#include <sys/time.h>`

`#include <sys/resource.h>`

```c
int
getpriority(int which, int who);

int
setpriority(int which, int who, int prio);
```

## 描述

由 `which` 和 `who` 指示的进程、进程组或用户的调度优先级，通过 `getpriority()` 系统调用获取，通过 `setpriority()` 系统调用设置。`which` 参数为 `PRIO_PROCESS`、`PRIO_PGRP` 或 `PRIO_USER` 之一，`who` 相对于 `which` 进行解释（`PRIO_PROCESS` 时为进程标识符，`PRIO_PGRP` 时为进程组标识符，`PRIO_USER` 时为用户 ID）。`who` 为零表示当前进程、进程组或用户。`prio` 参数是 -20 到 20 范围内的值。默认优先级为 0；较低的优先级数值会获得更有利的调度。

`getpriority()` 系统调用返回任何指定进程所享有的最高优先级（最小数值）。`setpriority()` 系统调用将所有指定进程的优先级设置为指定值。只有超级用户可以降低优先级数值。

## 返回值

由于 `getpriority()` 合法地可能返回值 -1，因此有必要在调用前清除外部变量 `errno`，然后之后检查它以确定 -1 是错误还是合法值。

`setpriority()` 系统调用在成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getpriority()` 和 `setpriority()` 系统调用在以下情况下会失败：

**[`ESRCH`]** 使用指定的 `which` 和 `who` 值未找到进程。

**[`EINVAL`]** `which` 参数不是 `PRIO_PROCESS`、`PRIO_PGRP` 或 `PRIO_USER` 之一。

除上述错误外，`setpriority()` 还会在以下情况下失败：

**[`EPERM`]** 找到了进程，但其有效用户 ID 和实际用户 ID 均不匹配调用者的有效用户 ID。

**[`EACCES`]** 非超级用户试图降低进程的优先级数值。

## 参见

[nice(1)](../man1/nice.1.md), [fork(2)](fork.2.md), [renice(8)](../man8/renice.8.md)

## 历史

`getpriority()` 系统调用首次出现于 4.2BSD。
