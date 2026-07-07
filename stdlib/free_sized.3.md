# free_sized.3

`free_sized` — C23 带尺寸释放函数

## 名称

`free_sized`, `free_aligned_sized`

## 概要

`Lb libc`

`#include <stdlib.h>`

```c
void
free_sized(void *ptr, size_t size);

void
free_aligned_sized(void *ptr, size_t alignment, size_t size);
```

## 描述

`free_sized` 函数释放由 `ptr` 所指向的、此前由 malloc(3)、realloc(3) 或 calloc(3) 分配的内存。`size` 参数应等于传递给分配函数的尺寸。aligned_alloc(3) 的结果不能传递给 `free_sized`。

`free_aligned_sized` 函数释放由 `ptr` 所指向的、此前由 aligned_alloc(3) 分配的内存。`alignment` 和 `size` 参数应等于提供给分配函数的值。malloc(3)、calloc(3) 或 realloc(3) 的结果不能传递给 `free_aligned_sized`。

如果 `ptr` 既不是空指针，也不是由上述对应释放函数所描述的分配函数返回的指针，则行为未定义；同样，提供的 `size` 或 `alignment` 与原始分配不匹配时，行为也是未定义的。

## 实现说明

C 标准允许实现忽略 `size` 和 `alignment` 提示。当前实现直接转发给 free(3)，不验证这些参数，因此对于正确使用的情况，行为保持正确。

一旦系统分配器支持带尺寸释放，这些函数将连接到系统分配器的带尺寸释放功能，与内存分配 API 的其余部分一致，从而使 `size` 和 `alignment` 提示用于提升性能和安全性。该行为遵循 C 标准中为每个函数推荐的做法。

## 参见

free(3), malloc(3), calloc(3), realloc(3), aligned_alloc(3), jemalloc(3)

## 标准

`free_sized` 和 `free_aligned_sized` 函数遵循 -isoC-2023。

## 作者

Faraz Vahedi <kfv@kfv.io>
