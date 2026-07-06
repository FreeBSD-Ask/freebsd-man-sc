# strcmp(3)

`strcmp` — 比较字符串

## 名称

`strcmp`, `strncmp`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft int Fn strcmp const char *s1 const char *s2 Ft int Fn strncmp const char *s1 const char *s2 size_t len`

## 描述

`strcmp` 和 `strncmp` 函数按字典序比较以 NUL 结尾的字符串 `s1` 和 `s2`。

`strncmp` 函数比较不超过 `len` 个字符。由于 `strncmp` 设计用于比较字符串而非二进制数据，出现在 **`\0`** 字符之后的字符不参与比较。

## 返回值

`strcmp` 和 `strncmp` 函数返回一个大于、等于或小于 0 的整数，分别对应字符串 `s1` 大于、等于或小于字符串 `s2`。比较使用无符号字符进行，因此 **`\200`** 大于 **`\0`**。

## 参见

[bcmp(3)](bcmp.3.md), [memcmp(3)](memcmp.3.md), strcasecmp(3), [strcoll(3)](strcoll.3.md), [strxfrm(3)](strxfrm.3.md), wcscmp(3)

## 标准

`strcmp` 和 `strncmp` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。

## 历史

`strcmp` 函数首次出现于 Programmer's Workbench (PWB/UNIX)，并移植到 Version 7 AT&T UNIX；`strncmp` 首次出现于 Version 7 AT&T UNIX。
