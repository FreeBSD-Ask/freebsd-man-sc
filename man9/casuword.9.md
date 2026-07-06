# casuword.9

`casuword` — 从用户空间获取、比较和存储数据

## 名称

`casueword`, `casueword32`, `casuword`, `casuword32`

## 概要

```c
#include <sys/types.h>
#include <sys/systm.h>

int
casueword(volatile u_long *base, u_long oldval, u_long *oldvalp,
    u_long newval)

int
casueword32(volatile uint32_t *base, uint32_t oldval,
    uint32_t *oldvalp, uint32_t newval)

u_long
casuword(volatile u_long *base, u_long oldval, u_long newval)

uint32_t
casuword32(volatile uint32_t *base, uint32_t oldval, uint32_t newval)
```

## 描述

`casuword` 函数旨在对当前进程的用户态内存中的值执行原子比较并交换操作。

`casuword` 例程从地址为 `base` 的用户内存读取值，并将读取的值与 `oldval` 比较。如果两值相等，则将 `newval` 写入 `*base`。对于 `casueword32` 和 `casueword`，旧值存储到由 `*oldvalp` 指向的（内核态）变量中。用户空间的值必须自然对齐。

`casuword` 和 `casuword32` 函数的调用者无法区分从用户空间读取的 -1 与函数失败。

## 返回值

`casuword` 和 `casuword32` 函数返回获取的数据，失败时返回 -1。`casueword` 和 `casueword32` 函数成功时返回 0，访问内存失败时返回 -1，比较或存储失败时返回 1。在 load-linked/store-conditional 架构上，存储可能失败。

## 参见

[atomic(9)](atomic.9.md), [fetch(9)](fetch.9.md), [store(9)](store.9.md)
