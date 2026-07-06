# BUF\_LOCKINIT.9

`BUF_LOCKINIT` — 初始化缓冲区锁

## 名称

`BUF_LOCKINIT`

## 概要

```c
#include <sys/param.h>

#include <sys/systm.h>

#include <sys/uio.h>

#include <sys/bio.h>

#include <sys/buf.h>

void
BUF_LOCKINIT(struct buf *bp)
```

## 描述

`BUF_LOCKINIT` 宏初始化缓冲区锁。

其参数如下：

**`bp`** 要初始化其锁的缓冲区。

## 参见

[buf(9)](buf.9.md), [BUF_LOCK(9)](BUF_LOCK.9.md), [BUF_TIMELOCK(9)](BUF_TIMELOCK.9.md), [BUF_UNLOCK(9)](BUF_UNLOCK.9.md), lockinit(9), lockmgr(9)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
