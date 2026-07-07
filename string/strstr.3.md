# strstr(3)

`strstr` — 在字符串中定位子串

## 名称

`strstr`

## 库

Lb libc

## 概要

`#include <string.h>`

```c
char *
strstr(const char *big, const char *little);

char *
strcasestr(const char *big, const char *little);

char *
strnstr(const char *big, const char *little, size_t len);
```

`#include <string.h>`

`#include <xlocale.h>`

```c
char *
strcasestr_l(const char *big, const char *little, locale_t loc);
```

## 描述

`strstr` 函数在以 NUL 结尾的字符串 `big` 中定位以 NUL 结尾的字符串 `little` 的首次出现。

`strcasestr` 函数与 `strstr` 类似，但忽略两个字符串的大小写。

`strcasestr_l` 函数与 `strcasestr` 功能相同，但接受显式的 locale，而非使用当前 locale。

`strnstr` 函数在字符串 `big` 中定位以 NUL 结尾的字符串 `little` 的首次出现，查找的字符数不超过 `len`。不搜索 `\0` 字符之后出现的字符。由于 `strnstr` 函数是 FreeBSD 特有的 API，仅在不考虑可移植性时使用。

## 返回值

若 `little` 为空字符串，返回 `big`；若 `big` 中找不到 `little`，返回 `NULL`；否则返回指向 `little` 首次出现的第一个字符的指针。

## 实例

以下将指针 `ptr` 设置为 `largestring` 中 "Bar Baz" 部分的起始位置：

```c
const char *largestring = "Foo Bar Baz";
const char *smallstring = "Bar";
char *ptr;
ptr = strstr(largestring, smallstring);
```

以下将指针 `ptr` 设置为 `NULL`，因为仅搜索 `largestring` 的前 4 个字符：

```c
const char *largestring = "Foo Bar Baz";
const char *smallstring = "Bar";
char *ptr;
ptr = strnstr(largestring, smallstring, 4);
```

## 参见

[memchr(3)](memchr.3.md), [memmem(3)](memmem.3.md), [strchr(3)](strchr.3.md), strcspn(3), [strpbrk(3)](strpbrk.3.md), strrchr(3), [strsep(3)](strsep.3.md), [strspn(3)](strspn.3.md), [strtok(3)](strtok.3.md), wcsstr(3)

## 标准

`strstr` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。

## 历史

`strnstr` 函数由 FreeBSD 4.5 引入，是非标准的。
