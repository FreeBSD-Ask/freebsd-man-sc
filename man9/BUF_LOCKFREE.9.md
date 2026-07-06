# BUF\_LOCKFREE.9

`BUF_LOCKFREE` — 销毁缓冲区的锁

## 名称

`BUF_LOCKFREE`

## 概要

```c
#include <sys/param.h>

#include <sys/systm.h>

#include <sys/uio.h>

#include <sys/bio.h>

#include <sys/buf.h>

void
BUF_LOCKFREE(struct buf *bp)
```

## 描述

`BUF_LOCKFREE` 宏销毁缓冲区锁。调用此宏时不能持有锁，否则将导致 panic。

其参数如下：

**`bp`** 要销毁其锁的缓冲区。

## 参见

[buf(9)](buf.9.md), [BUF_LOCK(9)](BUF_LOCK.9.md), [BUF_TIMELOCK(9)](BUF_TIMELOCK.9.md), [BUF_UNLOCK(9)](BUF_UNLOCK.9.md), lockdestroy(9)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
