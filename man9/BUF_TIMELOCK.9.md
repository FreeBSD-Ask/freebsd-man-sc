# BUF_TIMELOCK.9

`BUF_TIMELOCK` — 锁定缓冲区

## 名称

`BUF_TIMELOCK`

## 概要

```c
#include <sys/param.h>
#include <sys/systm.h>
#include <sys/uio.h>
#include <sys/bio.h>
#include <sys/buf.h>
```

```c
int
BUF_TIMELOCK(struct buf *bp, int locktype, char *wmesg,
    int catch, int timo)
```

## 描述

`BUF_TIMELOCK` 函数锁定给定的缓冲区，并将睡眠时间限制为 `timo`，同时将 `catch` 按位或到睡眠优先级中。`wmesg` 是睡眠时使用的等待消息。

其参数如下：

**`bp`** 要锁定的缓冲区。

**`locktype`** 控制锁类型的标志。详见 lockmgr(9)。

**`wmesg`** 获取锁期间睡眠时使用的等待消息。

**`catch`** 按位或到睡眠优先级中的优先级。

**`timo`** 锁定过程中遇到的任何睡眠的超时时间。

## 返回值

成功时返回 0。关于非零返回值的详细信息，参见 lockmgr(9)。

## 参见

[buf(9)](buf.9.md), [BUF_LOCK(9)](BUF_LOCK.9.md), [BUF_UNLOCK(9)](BUF_UNLOCK.9.md), lockmgr(9)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
