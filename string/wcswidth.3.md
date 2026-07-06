# wcswidth.3

`wcswidth` — 宽字符串占用的列位置数

## 名称

`wcswidth`

## 库

Lb libc

## 概要

`#include <wchar.h>`

```c
int
wcswidth(const wchar_t *pwcs, size_t n);
```

## 描述

`wcswidth` 函数确定 `pwcs` 的前 `n` 个字符所占用的列位置数，直至遇到空宽字符（`L'\0'`）为止。

## 返回值

若 `pwcs` 为空字符串（`L""`），`wcswidth` 函数返回 0；若遇到不可打印的宽字符，返回 -1；否则返回所占用的列位置数。

## 参见

iswprint(3), [wcwidth(3)](wcwidth.3.md)

## 标准

`wcswidth` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。
