# BUF\_RECURSED.9

`BUF_RECURSED` — 检查与缓冲区关联的锁是否递归

## 名称

`BUF_RECURSED`

## 概要

```c
#include <sys/param.h>

#include <sys/systm.h>

#include <sys/uio.h>

#include <sys/bio.h>

#include <sys/buf.h>

int
BUF_RECURSED(struct buf *bp)
```

## 描述

`BUF_RECURSED` 函数检查与给定缓冲区关联的锁是否递归，如果条件为真则返回 1，否则返回 0。

其参数如下：

**`bp`** 与锁关联的缓冲区。详见 lockmgr_recursed(9)。

## 参见

[buf(9)](buf.9.md), [BUF_LOCK(9)](BUF_LOCK.9.md), [BUF_UNLOCK(9)](BUF_UNLOCK.9.md), lockmgr(9)

## 作者

本手册页由 Attilio Rao <attilio@FreeBSD.org> 编写。
