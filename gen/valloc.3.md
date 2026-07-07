# valloc(3)

`valloc` — 对齐的内存分配函数

## 名称

`valloc`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
void *
valloc(size_t size)
```

## 描述

`valloc` 函数已被 posix_memalign(3) 取代，后者可用于请求页面对齐的分配。

`valloc` 函数分配按页边界对齐的 `size` 字节。

## 返回值

`valloc` 函数成功时返回指向所分配空间的指针；否则返回空指针。

## 参见

posix_memalign(3)

## 历史

`valloc` 函数出现于 3.0BSD。

从 FreeBSD 7.0 起，`valloc` 函数正确分配的内存可以通过 `free` 释放。
