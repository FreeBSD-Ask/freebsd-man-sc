# printf_l(3)

`printf_l` — 格式化输出转换

## 名称

`printf_l`, `asprintf_l`, `fprintf_l`, `snprintf_l`, `sprintf_l`, `vasprintf_l`, `vfprintf_l`, `vprintf_l`, `vsnprintf_l`, `vsprintf_l`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`#include <xlocale.h>`

`Ft int Fn printf_l locale_t loc const char * restrict format ... Ft int Fn asprintf_l char **ret locale_t loc const char * format ... Ft int Fn fprintf_l FILE * restrict stream locale_t loc const char * restrict format ... Ft int Fn snprintf_l char * restrict str size_t size locale_t loc const char * restrict format ... Ft int Fn sprintf_l char * restrict str locale_t loc const char * restrict format ... Ft int Fn vasprintf_l char **ret locale_t loc const char *format va_list ap Ft int Fn vfprintf_l FILE * restrict stream locale_t loc const char * restrict format va_list ap Ft int Fn vprintf_l locale_t loc const char * restrict format va_list ap Ft int Fn vsnprintf_l char * restrict str size_t size locale_t loc const char * restrict format va_list ap Ft int Fn vsprintf_l char * restrict str locale_t loc const char * restrict format va_list ap`

## 描述

上述函数用于在 locale `loc` 中进行格式化输出转换。它们的行为与不带 _l 后缀的版本相同，但使用指定的 locale 而非全局或每线程 locale。更多信息请参阅各自的手册页。

## 参见

[printf(3)](printf.3.md), xlocale(3)

## 标准

这些函数不遵循任何特定标准，应视为不可移植的本地扩展。

## 历史

这些函数首次出现于 Darwin，并在 FreeBSD 9.1 中首次实现。
