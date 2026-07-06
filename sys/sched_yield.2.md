# sched_yield(2)

`sched_yield` — 让出处理器

## 名称

`sched_yield`

## 库

Lb libc

## 概要

`#include <sched.h>`

```c
int
sched_yield(void);
```

## 描述

`sched_yield()` 系统调用强制正在运行的进程让出处理器，直到它再次成为其进程列表的头部。它不接受任何参数。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

失败时 `errno` 将被设置为相应的值：

**[ENOSYS]** 系统未配置支持此功能。

## 标准

`sched_yield()` 系统调用符合 -p1003.1b-93。
