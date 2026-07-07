# strcasecmp(3)

`strcasecmp` — 比较字符串，忽略大小写

## 名称

`strcasecmp`, `strncasecmp`

## 库

Lb libc

## 概要

`#include <strings.h>`

`Ft int Fn strcasecmp const char *s1 const char *s2 Ft int Fn strncasecmp const char *s1 const char *s2 size_t len`

`#include <strings.h>`

`#include <xlocale.h>`

`Ft int Fn strcasecmp_l const char *s1 const char *s2 locale_t loc Ft int Fn strncasecmp_l const char *s1 const char *s2 size_t len locale_t loc`

## 描述

`strcasecmp` 和 `strncasecmp` 函数比较以 NUL 结尾的字符串 `s1` 和 `s2`。

`strncasecmp` 函数比较不超过 `len` 个字符。`strcasecmp_l` 和 `strncasecmp_l` 函数的功能与上述非 locale 版本相同，但接受显式指定的 locale 而非使用当前 locale。

## 返回值

`strcasecmp` 和 `strncasecmp` 函数返回一个大于、等于或小于 0 的整数，分别对应将每个对应字符转换为小写后 `s1` 按字典序大于、等于或小于 `s2`。字符串本身不会被修改。比较使用无符号字符进行，因此 **`\200`** 大于 **`\0`**。`strcasecmp_l` 和 `strncasecmp_l` 函数功能相同，但接受显式指定的 locale。

## 参见

[bcmp(3)](bcmp.3.md), [memcmp(3)](memcmp.3.md), [strcmp(3)](strcmp.3.md), [strcoll(3)](strcoll.3.md), [strxfrm(3)](strxfrm.3.md), tolower(3), wcscasecmp(3)

## 历史

`strcasecmp` 和 `strncasecmp` 函数首次出现于 4.4BSD。其原型原本位于

`#include <string.h>`

中，后为遵循 IEEE Std 1003.1-2001 ("POSIX.1") 而移至

`#include <strings.h>`
