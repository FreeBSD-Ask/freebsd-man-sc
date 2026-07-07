# strspn(3)

`strspn` — 跨越字符串

## 名称

`strspn`, `strcspn`

## 库

Lb libc

## 概要

`#include <string.h>`

```c
size_t
strspn(const char *s, const char *charset);

size_t
strcspn(const char *s, const char *charset);
```

## 描述

`strspn` 函数扫描以 NUL 结尾的字符串 `s` 的起始部分，只要这些字符出现在以 NUL 结尾的字符串 `charset` 中即继续。换言之，它计算 `s` 中第一个不在 `charset` 中的字符的字符串数组索引，若所有字符都在 `charset` 中，则返回第一个 NUL 字符的索引。

`strcspn` 函数扫描以 NUL 结尾的字符串 `s` 的起始部分，只要这些字符**不**出现在以 NUL 结尾的字符串 `charset` 中即继续（它扫描 `charset` 的**补集**）。换言之，它计算 `s` 中第一个也出现在 `charset` 中的字符的字符串数组索引，若没有字符在 `charset` 中，则返回第一个 NUL 字符的索引。

## 返回值

`strspn` 和 `strcspn` 函数返回所跨越的字符数。

## 参见

[memchr(3)](memchr.3.md), [strchr(3)](strchr.3.md), [strpbrk(3)](strpbrk.3.md), strrchr(3), [strsep(3)](strsep.3.md), [strstr(3)](strstr.3.md), [strtok(3)](strtok.3.md), wcsspn(3)

## 标准

`strspn` 和 `strcspn` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。
