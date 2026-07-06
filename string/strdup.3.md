# strdup.3

`strdup` — 保存字符串的副本

## 名称

`strdup`, `strdupa`, `strndup`, `strndupa`

## 库

Lb libc

## 概要

`#include <string.h>`

```c
char *
strdup(const char *str);

char *
strdupa(const char *str);

char *
strndup(const char *str, size_t len);

char *
strndupa(const char *str, size_t len);
```

## 描述

`strdup` 函数为字符串 `str` 的副本分配足够的内存，执行复制，并返回指向该副本的指针。所分配的内存使用 malloc(3) 分配，不再需要时应使用 free(3) 释放。

`strndup` 函数从字符串 `str` 中最多复制 `len` 个字符，并始终在复制的字符串末尾添加 `NUL` 终止符。

`strdupa` 函数与 `strdup` 功能相同，但使用 [alloca(3)](alloca.3.md) 分配内存。类似地，`strndupa` 函数与 `strndup` 功能相同，但使用 [alloca(3)](alloca.3.md) 分配内存。

## 返回值

若内存不足，返回 `NULL` 并将 `errno` 设置为 `ENOMEM`。否则，`strdup` 系列函数返回指向所复制字符串的指针。

## 参见

[alloca(3)](alloca.3.md), free(3), malloc(3), wcsdup(3)

## 标准

`strdup` 函数由 IEEE Std 1003.1-2001 ("POSIX.1") 规定。`strndup` 函数由 IEEE Std 1003.1-2008 ("POSIX.1") 规定。`strdupa` 和 `strndupa` 函数是扩展，取自 glibc。

## 历史

`strdup` 函数首次出现于 4.3BSD。`strndup` 函数在 FreeBSD 7.2 中引入。`strdupa` 和 `strndupa` 函数在 FreeBSD 15.1 中引入。
