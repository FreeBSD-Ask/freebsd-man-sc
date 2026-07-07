# PHOLD(9)

`PHOLD` — 保持进程

## 名称

`PHOLD`

## 概要

```c
#include <sys/proc.h>

PHOLD(struct proc *p)
_PHOLD(struct proc *p)
PRELE(struct proc *p)
_PRELE(struct proc *p)
PROC_ASSERT_HELD(struct proc *p)
PROC_ASSERT_NOT_HELD(struct proc *p)
```

## 描述

`PHOLD` 宏递增进程的保持计数，`PRELE` 宏递减进程的保持计数。

如果保持计数非零的进程尝试退出，它将睡眠直到其保持计数降至零，然后内核才开始释放与该进程关联的资源。一旦进程开始退出，增加其保持计数是无效的。因此，调用者不得尝试保持已设置 `P_WEXIT` 标志的进程。VM 守护进程不会换出属于保持计数非零进程的线程的内核栈。

`_PHOLD` 和 `_PRELE` 宏与 `PHOLD` 和 `PRELE` 相同，但必须在持有进程锁的情况下调用。

## 作者

本手册页由 Mark Johnston <markj@FreeBSD.org> 编写。
