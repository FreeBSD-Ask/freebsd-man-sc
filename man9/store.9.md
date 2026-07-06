# store.9

`store` — 向用户空间存储数据

## 名称

`store`, `subyte`, `suptr`, `suword`

## 概要

```c
#include <sys/types.h>
#include <sys/time.h>
#include <sys/systm.h>

int
subyte(volatile void *base, int byte)

int
suptr(volatile void *base, intptr_t ptr)

int
suword(volatile void *base, long word)

int
suword16(volatile void *base, int word)

int
suword32(volatile void *base, int32_t word)

int
suword64(volatile void *base, int64_t word)
```

## 描述

`suword` 函数旨在向用户空间复制少量数据。如果用户地址自然对齐，则操作将原子地执行。否则它可能失败或以非原子方式执行，具体取决于平台。

`suword` 例程提供以下功能：

`subyte` 向用户空间地址 `base` 存储一字节数据。

`suptr` 向用户空间地址 `base` 存储指针，保留该指针的来源（参见 [memory_model(7)](../man7/memory_model.7.md)）。

`suword` 向用户空间地址 `base` 存储一个字的数据。

`suword16` 向用户空间地址 `base` 存储 16 位数据。

`suword32` 向用户空间地址 `base` 存储 32 位数据。

`suword64` 向用户空间地址 `base` 存储 64 位数据。

## 返回值

`suword` 函数成功时返回 0，失败时返回 -1。

## 参见

[copy(9)](copy.9.md), [fetch(9)](fetch.9.md)
