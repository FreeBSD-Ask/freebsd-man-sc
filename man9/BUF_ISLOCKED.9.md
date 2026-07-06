# BUF\_ISLOCKED.9

`BUF_ISLOCKED` — 返回与缓冲区关联的锁的状态

## 名称

`BUF_ISLOCKED`

## 概要

```c
#include <sys/param.h>

#include <sys/systm.h>

#include <sys/uio.h>

#include <sys/bio.h>

#include <sys/buf.h>

int
BUF_ISLOCKED(struct buf *bp)
```

## 描述

`BUF_ISLOCKED` 函数返回与缓冲区关联的锁相对于 curthread 的状态。

可能返回以下值：

**`LK_EXCLUSIVE`** curthread 持有独占锁。

**`LK_EXCLOTHER`** 除 curthread 以外的其他对象持有独占锁。

**`LK_SHARED`** 持有共享锁。

**`0`** 锁未被任何对象持有。

## 参见

[buf(9)](buf.9.md), [BUF_LOCK(9)](buf_lock.9.md), [BUF_UNLOCK(9)](buf_unlock.9.md), lockmgr(9)

## 作者

本手册页由 Attilio Rao <attilio@FreeBSD.org> 编写。
