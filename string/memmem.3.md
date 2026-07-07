# memmem(3)

`memmem` — 在字节序列中定位字节子序列

## 名称

`memmem`

## 库

Lb libc

## 概要

`#include <string.h>`

```c
void *
memmem(const void *big, size_t big_len, const void *little, size_t little_len);
```

## 描述

`memmem` 函数在字节序列 `big` 中定位字节序列 `little` 的首次出现。

## 返回值

若 `little_len` 为零，返回 `big`（即空的 little 视为匹配 big 的开头）；若 `big` 中找不到 `little`，返回 `NULL`；否则返回指向 `little` 首次出现的第一个字符的指针。

## 参见

[memchr(3)](memchr.3.md), [strchr(3)](strchr.3.md), [strstr(3)](strstr.3.md)

## 标准

`memmem` 遵循 -p1003.1-2024。

## 历史

`memmem` 函数首次出现于 FreeBSD 6.0。在 FreeBSD 12.0 中，被替换为来自 musl libc 项目的优化 O(n) 实现。Pascal Gloor <pascal.gloor@spale.com> 提供了此手册页及先前的实现。

## 缺陷

此函数在 Linux libc 5.0.9 及之前版本以及 GNU libc 2.1 之前版本中存在问题。在 FreeBSD 11.0 之前，当 `little_len` 等于 0 时 `memmem` 返回 `NULL`。
