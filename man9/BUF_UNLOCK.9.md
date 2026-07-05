# BUF_UNLOCK.9

`BUF_UNLOCK` — 解锁已锁定的缓冲区

## 名称

`BUF_UNLOCK`

## 概要

```c
#include <sys/param.h>
#include <sys/systm.h>
#include <sys/uio.h>
#include <sys/bio.h>
#include <sys/buf.h>
```

```c
void
BUF_UNLOCK(struct buf *bp)
```

## 描述

`BUF_UNLOCK` 函数解锁先前由 `BUF_LOCK` 或 `BUF_TIMELOCK` 锁定的缓冲区。

其参数如下：

**`bp`** 要解锁的缓冲区。该缓冲区必须已被锁定。

## 参见

[buf(9)](buf.9.md), [BUF_LOCK(9)](BUF_LOCK.9.md), [BUF_TIMELOCK(9)](BUF_TIMELOCK.9.md), lockmgr(9)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
