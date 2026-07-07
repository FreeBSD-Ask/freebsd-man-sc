# BUF_LOCK(9)

`BUF_LOCK` — 锁定缓冲区

## 名称

`BUF_LOCK`

## 概要

```c
#include <sys/param.h>

#include <sys/systm.h>

#include <sys/uio.h>

#include <sys/bio.h>

#include <sys/buf.h>

int
BUF_LOCK(struct buf *bp, int locktype)
```

## 描述

`BUF_LOCK` 函数锁定给定的缓冲区。如果锁已被持有，此调用将阻塞直到能获取锁，除非设置了 `LK_NOWAIT`。

其参数如下：

**`bp`** 要锁定的缓冲区。

**`locktype`** 控制锁类型的标志。详见 lockmgr(9)。

## 返回值

成功时返回 0。非零返回值的信息参见 lockmgr(9)。

## 参见

[buf(9)](buf.9.md), [BUF_TIMELOCK(9)](buf_timelock.9.md), [BUF_UNLOCK(9)](buf_unlock.9.md), lockmgr(9)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
