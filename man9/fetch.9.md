# fetch.9

`fetch` — 从用户空间获取数据

## 名称

`fetch`, `fubyte`, `fuword`, `fuword16`, `fuword32`, `fuword64`, `fueptr`, `fueword`, `fueword32`, `fueword64`

## 概要

```c
#include <sys/types.h>

#include <sys/systm.h>

int
fubyte(volatile const void *base)

long
fuword(volatile const void *base)

int
fuword16(volatile const void *base)

int32_t
fuword32(volatile const void *base)

int64_t
fuword64(volatile const void *base)

int
fueptr(volatile const void *base, intptr_t *val)

int
fueword(volatile const void *base, long *val)

int
fueword32(volatile const void *base, int32_t *val)

int
fueword64(volatile const void *base, int64_t *val)
```

## 描述

`fueword64` 等函数设计用于从当前进程的用户空间复制少量数据。如果用户地址自然对齐，则操作将以原子方式执行。否则，可能失败或以非原子方式执行，具体取决于平台。

`fueword64` 等例程提供以下功能：

**`fubyte`** 从用户空间地址 `base` 获取一字节数据。读取的字节经零扩展后存入结果变量。

**`fuword`** 从用户空间地址 `base` 获取一个字（long）的数据。

**`fuword16`** 从用户空间地址 `base` 获取 16 位数据。读取的半字经零扩展后存入结果变量。

**`fuword32`** 从用户空间地址 `base` 获取 32 位数据。

**`fuword64`** 从用户空间地址 `base` 获取 64 位数据。

**`fueptr`** 从用户空间地址 `base` 获取一个指针，并将结果存入 `val` 所指向的变量。`fueptr` 保留从用户空间获取的指针的来源信息（参见 [memory_model(7)](../man7/memory_model.7.md)）。

**`fueword`** 从用户空间地址 `base` 获取一个字（long）的数据，并将结果存入 `val` 所指向的变量。

**`fueword32`** 从用户空间地址 `base` 获取 32 位数据，并将结果存入 `val` 所指向的变量。

**`fueword64`** 从用户空间地址 `base` 获取 64 位数据，并将结果存入 `val` 所指向的变量。

`fuword`、`fuword32` 和 `fuword64` 函数的调用者无法区分从用户空间读取的 -1 与函数失败。

## 返回值

`fubyte`、`fuword`、`fuword16`、`fuword32` 和 `fuword64` 函数返回获取的数据，失败时返回 -1。`fueptr`、`fueword`、`fueword32` 和 `fueword64` 函数成功时返回 0，失败时返回 -1。

## 参见

[copy(9)](copy.9.md), [store(9)](store.9.md)
