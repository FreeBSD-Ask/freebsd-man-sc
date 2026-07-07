# memcpy(9)

`memcpy` — 复制内存中的字节

## 名称

`memcpy`, `memcpy_data`

## 概要

```c
#include <sys/systm.h>
```

```c
void *
memcpy(void *dst, const void *src, size_t len)

void *
memcpy_data(void *dst, const void *src, size_t len)
```

## 描述

`memcpy` 函数从对象 `src` 复制 `len` 字节到对象 `dst`，复制方式保留所复制对象中指针的来源（参见 [memory_model(7)](../man7/memory_model.7.md)）。如果 `src` 和 `dst` 重叠，结果未定义。`memcpy_data` 函数执行相同操作，但不保留所复制对象中指针的来源。在 CHERI 目标上，会显式清除任何所复制能力的有效性标签。

## 返回值

`memcpy` 和 `memcpy_data` 函数返回 `dst` 的原始值。

## 参见

[bcopy(9)](bcopy.9.md), [memmove(9)](memmove.9.md), memmove_data(9)

## 标准

`memcpy` 函数遵循 ISO/IEC 9899:1990（"ISO C89"）。

## 历史

`memcpy` 函数首次出现于 AT&T System V UNIX，并为 4.3BSD 重新实现。`memcpy_data` 函数首次出现于 FreeBSD 16.0。
