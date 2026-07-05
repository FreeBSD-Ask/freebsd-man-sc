# pfind.9

`pfind` — 按编号定位进程

## 名称

`pfind`, `pfind_any`, `pfind_any_locked`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/proc.h>
```

```c
struct proc *
pfind(pid_t pid)

struct proc *
pfind_any(pid_t pid)

struct proc *
pfind_any_locked(pid_t pid)
```

## 描述

`pfind` 函数遍历系统中的进程列表，查找进程 ID 为 `pid` 的进程。如果进程存在且不处于僵尸状态，将返回指向该进程结构的指针。

`pfind_any` 接受 `pid` 作为参数。`pfind_any` 搜索 `allproc` 列表并返回第一个具有匹配 PID 的进程，其状态可以是 `PRS_ZOMBIE`。

`pfind_any_locked` 类似于 `pfind_any`，但它不锁定给定 `pid` 的进程哈希桶。相反，它断言相应的进程哈希桶已被锁定。

所有三个函数 `pfind`、`pfind_any` 和 `pfind_any_locked` 在返回前都锁定 `proc` 结构。

## 返回值

`pfind`、`pfind_any` 和 `pfind_any_locked` 成功时返回指向 `proc` 结构的指针，失败时返回 `NULL`。

## 参见

[pget(9)](pget.9.md), [pgfind(9)](pgfind.9.md)

## 作者

本手册页由 Evan Sarmiento <kaworu@sektor7.ath.cx> 编写。
