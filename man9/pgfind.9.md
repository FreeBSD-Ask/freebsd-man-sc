# pgfind.9

`pgfind` — 按编号定位进程组

## 名称

`pgfind`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/proc.h>
```

```c
struct pgrp *
pgfind(pid_t pgid)
```

## 描述

`pgfind` 函数接受 `pgid` 作为参数，返回指向 `pg_id` 在参数中指定的 `pgrp` 结构的指针。

`pgfind` 锁定返回的 `pgrp` 结构。

## 返回值

`pgfind` 函数失败时返回 `NULL`，成功完成时返回指向 `pgrp` 结构的指针。

## 参见

[pfind(9)](pfind.9.md)

## 作者

本手册页由 Evan Sarmiento <kaworu@sektor7.ath.cx> 编写。
