# nice(3)

`nice` — 设置程序调度优先级

## 名称

`nice` — 设置程序调度优先级

## 库

Lb libc

## 概要

```c
#include <unistd.h>

int
nice(int incr);
```

## 描述

> **注意** 此接口已被 setpriority(2) 取代。

`nice` 函数将 `incr` 加到进程的调度优先级上。优先级是 -20 到 20 范围内的值。默认优先级为 0；较低的优先级会获得更有利的调度。只有超级用户可以降低优先级数值。

子进程通过 [fork(2)](../sys/fork.2.md) 继承父进程的优先级。

## 返回值

成功完成后，`nice` 返回 0，`errno` 保持不变。否则返回 -1，进程的 nice 值不变，`errno` 被设置以指示错误。

## 错误

`nice` 函数在以下情况下会失败：

**[`EPERM`]** `incr` 参数为负且调用者没有适当的权限。

## 参见

[nice(1)](../man1/nice.1.md), [fork(2)](../sys/fork.2.md), setpriority(2), [renice(8)](../man8/renice.8.md)

## 标准

`nice` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1") 标准，但返回值除外。本实现在成功完成后返回 0，但标准要求返回新的 nice 值，该值可能为 -1。

## 历史

`nice` 系统调用出现于 Version 6 AT&T UNIX。
