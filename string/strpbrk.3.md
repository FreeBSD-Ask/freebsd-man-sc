# strpbrk(3)

`strpbrk` — 在字符串中定位多个字符

## 名称

`strpbrk`

## 库

Lb libc

## 概要

`#include <string.h>`

```c
char *
strpbrk(const char *s, const char *charset);
```

## 描述

`strpbrk` 函数在以 NUL 结尾的字符串 `s` 中定位 `charset` 字符串中任意字符首次出现的位置，并返回指向该字符的指针。若 `charset` 中的字符在 `s` 中均未出现，`strpbrk` 返回 `NULL`。

## 参见

[memchr(3)](memchr.3.md), [strchr(3)](strchr.3.md), strcspn(3), strrchr(3), [strsep(3)](strsep.3.md), [strspn(3)](strspn.3.md), [strstr(3)](strstr.3.md), [strtok(3)](strtok.3.md), wcspbrk(3)

## 标准

`strpbrk` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。
