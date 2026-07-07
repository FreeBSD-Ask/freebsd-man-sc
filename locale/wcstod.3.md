# wcstod(3)

`wcstod` — 将字符串转换为 `float`、`double` 或 `long double`

## 名称

`wcstof`, `wcstod`, `wcstold`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft float Fn wcstof const wchar_t * restrict nptr wchar_t ** restrict endptr Ft long double Fn wcstold const wchar_t * restrict nptr wchar_t ** restrict endptr Ft double Fn wcstod const wchar_t * restrict nptr wchar_t ** restrict endptr`

## 描述

`wcstof`、`wcstod` 和 `wcstold` 函数分别是 `strtof`、`strtod` 和 `strtold` 函数的宽字符版本。详情请参阅 strtod(3)。

## 参见

strtod(3), [wcstol(3)](wcstol.3.md)

## 标准

`wcstof`、`wcstod` 和 `wcstold` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
