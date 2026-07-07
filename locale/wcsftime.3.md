# wcsftime(3)

`wcsftime` — 将日期和时间转换为宽字符字符串

## 名称

`wcsftime`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft size_t Fo wcsftime wchar_t * restrict wcs size_t maxsize const wchar_t * restrict format const struct tm * restrict timeptr Fc`

## 描述

`wcsftime` 函数等同于 `strftime` 函数，区别在于参数的类型。详细描述请参阅 strftime(3)。

## 兼容性

`wcsftime` 的一些早期实现中，`format` 参数的类型为 `const char *` 而非 `const wchar_t *`。

## 参见

strftime(3)

## 标准

`wcsftime` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
