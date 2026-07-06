# strchr.3

`strchr` — 在字符串中定位字符

## 名称

`strchr`

## 库

Lb libc

## 概要

`#include <string.h>`

```c
char *
strchr(const char *s, int c);

char *
strrchr(const char *s, int c);

char *
strchrnul(const char *s, int c);
```

## 描述

`strchr` 函数在 `s` 所指向的字符串中定位 `c`（转换为 `char` 类型）首次出现的位置。字符串结尾的空字符被视为字符串的一部分；因此若 `c` 为 `\0`，则定位到结尾的 `\0`。

`strrchr` 函数与 `strchr` 功能相同，区别在于它定位 `c` 最后一次出现的位置。

`strchrnul` 函数与 `strchr` 功能相同，区别在于若 `s` 中未找到 `c`，则返回指向结尾 `\0` 的指针。

## 返回值

`strchr` 和 `strrchr` 函数返回指向所定位字符的指针；若字符串中不存在该字符，则返回 `NULL`。

若字符串中不存在该字符，`strchrnul` 返回指向结尾 `\0` 的指针。

## 参见

[memchr(3)](memchr.3.md), [memmem(3)](memmem.3.md), strcspn(3), [strpbrk(3)](strpbrk.3.md), [strsep(3)](strsep.3.md), [strspn(3)](strspn.3.md), [strstr(3)](strstr.3.md), [strtok(3)](strtok.3.md), wcschr(3)

## 标准

`strchr` 和 `strrchr` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`strchrnul` 函数是 GNU 扩展。

## 历史

`strchrnul` 函数首次出现于 glibc 2.1.1，并在 FreeBSD 10.0 中引入。
