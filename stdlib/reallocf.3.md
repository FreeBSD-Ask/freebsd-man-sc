# reallocf(3)

`reallocf` — 内存重新分配函数

## 名称

`reallocf`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
void *
reallocf(void *ptr, size_t size);
```

## 描述

`reallocf` 函数与 `realloc` 函数相同，区别在于当请求的内存无法分配时，它会释放传入的指针。这是 FreeBSD 特有的 API，旨在缓解 `realloc` 传统编码风格在库中导致内存泄漏的问题。

## 返回值

`reallocf` 函数成功时返回指向已分配内存的指针，该指针可能与 `ptr` 相同；否则返回 `NULL` 指针，若错误由分配失败引起，则 `errno` 设置为 `ENOMEM`。发生错误时，`reallocf` 函数会删除原始缓冲区。

## 参见

realloc(3)

## 历史

`reallocf` 函数首次出现于 FreeBSD 3.0。
