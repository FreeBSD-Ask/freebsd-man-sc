# p\_cansee.9

`p_cansee` — 确定进程的可见性

## 名称

`p_cansee`

## 概要

```c
#include <sys/proc.h>
```

```c
int
p_cansee(struct thread *td, struct proc *p)
```

## 描述

此函数确定给定进程 `p` 是否对线程 `td` 可见，其中“可见性”的概念可理解为“对其存在的感知”。

此函数明确允许线程始终能看到自己的进程，即使有挂起的凭证更改（参见 [ucred(9)](ucred.9.md)）。否则，它简单地交给 [cr_cansee(9)](cr_cansee.9.md) 处理。

## 返回值

`p_cansee` 函数如果由 `p` 表示的进程对线程 `td` 可见，则返回 `0`，否则返回 ESRCH。

## 错误

**[ESRCH]** 线程 `td` 不是进程 `p` 的一部分，并且根据 [cr_cansee(9)](cr_cansee.9.md) 的判定无法看到它。

## 参见

[cr_cansee(9)](cr_cansee.9.md), [p_candebug(9)](p_candebug.9.md), [ucred(9)](ucred.9.md)
