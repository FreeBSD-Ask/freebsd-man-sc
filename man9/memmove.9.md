# memmove(9)

`memmove` — 复制内存中的字节

## 名称

`memmove`, `memmove_data`

## 概要

```c
#include <sys/systm.h>
```

```c
void *
memmove(void *dst, const void *src, size_t len)

void *
memmove_data(void *dst, const void *src, size_t len)
```

## 描述

`memmove` 函数从对象 `src` 复制 `len` 字节到对象 `dst`。两个对象可以重叠；复制始终以非破坏性方式进行，并保留所复制对象中指针的来源（参见 [memory_model(7)](../man7/memory_model.7.md)）。`memmove_data` 函数执行相同操作，但不保留所复制对象中指针的来源。在 CHERI 目标上，会显式清除任何所复制能力的有效性标签。

## 返回值

`memmove` 和 `memmove_data` 函数返回 `dst` 的原始值。

## 参见

[bcopy(9)](bcopy.9.md), [memcpy(9)](memcpy.9.md), memcpy_data(9)

## 标准

`memmove` 函数遵循 ISO/IEC 9899:1990（"ISO C89"）。

## 历史

`memmove_data` 函数首次出现于 FreeBSD 16.0。
