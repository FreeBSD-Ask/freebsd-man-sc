# wcstol(3)

`wcstol` — 将宽字符串值转换为 `long`、`unsigned long`、`long long`、`unsigned long long`、`intmax_t` 或 `uintmax_t` 整数

## 名称

`wcstol`, `wcstoll`, `wcstoimax`, `wcstoul`, `wcstoull`, `wcstoumax`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft long Fn wcstol const wchar_t * restrict nptr wchar_t ** restrict endptr int base Ft unsigned long Fn wcstoul const wchar_t * restrict nptr wchar_t ** restrict endptr int base Ft long long Fn wcstoll const wchar_t * restrict nptr wchar_t ** restrict endptr int base Ft unsigned long long Fn wcstoull const wchar_t * restrict nptr wchar_t ** restrict endptr int base`

`#include <inttypes.h>`

`Ft intmax_t Fn wcstoimax const wchar_t * restrict nptr wchar_t ** restrict endptr int base Ft uintmax_t Fn wcstoumax const wchar_t * restrict nptr wchar_t ** restrict endptr int base`

## 描述

`wcstol`、`wcstoul`、`wcstoll`、`wcstoull`、`wcstoimax` 和 `wcstoumax` 函数分别是 `strtol`、`strtoul`、`strtoll`、`strtoull`、`strtoimax` 和 `strtoumax` 函数的宽字符版本。详情请参阅它们的手册页（例如 [strtol(3)](strtol.3.md)）。

## 参见

[strtol(3)](strtol.3.md), [strtoul(3)](strtoul.3.md)

## 标准

`wcstol`、`wcstoul`、`wcstoll`、`wcstoull`、`wcstoimax` 和 `wcstoumax` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
