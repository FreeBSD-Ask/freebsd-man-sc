# index(3)

`index` — 在字符串中定位字符

## 名称

`index`

## 库

Lb libc

## 概要

`#include <strings.h>`

```c
char *
index(const char *s, int c);

char *
rindex(const char *s, int c);
```

## 描述

> **注意**：`index` 和 `rindex` 函数已弃用，建议改用 [strchr(3)](strchr.3.md) 和 strrchr(3)。

`index` 函数在 `s` 所指向的字符串中定位 `c`（转换为 `char` 类型）首次出现的位置。字符串结尾的空字符被视为字符串的一部分；因此若 `c` 为 `\0`，则定位到结尾的 `\0`。

`rindex` 函数与 `index` 功能相同，区别在于它定位 `c` 最后一次出现的位置。

## 返回值

`index` 和 `rindex` 函数返回指向所定位字符的指针；若字符串中不存在该字符，则返回 `NULL`。

## 参见

[memchr(3)](memchr.3.md), [strchr(3)](strchr.3.md), strcspn(3), [strpbrk(3)](strpbrk.3.md), strrchr(3), [strsep(3)](strsep.3.md), [strspn(3)](strspn.3.md), [strstr(3)](strstr.3.md), [strtok(3)](strtok.3.md)

## 历史

`index` 和 `rindex` 函数出现于 Version 6 AT&T UNIX。其原型最初位于

`#include <string.h>`

之后为遵循 IEEE Std 1003.1-2001 ("POSIX.1") 而移至

`#include <strings.h>`

这两个函数未在 IEEE Std 1003.1-2008 ("POSIX.1") 中规定。
