# scanf_l(3)

`scanf_l` — 输入格式转换

## 名称

`scanf_l`, `fscanf_l`, `sscanf_l`, `vfscanf_l`, `vscanf_l`, `vsscanf_l`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`#include <xlocale.h>`

`Ft int Fn scanf_l locale_t loc const char * restrict format ... Ft int Fn fscanf_l FILE * restrict stream locale_t loc const char * restrict format ... Ft int Fn sscanf_l const char * restrict str locale_t loc const char * restrict format ... Ft int Fn vfscanf_l FILE * restrict stream locale_t loc const char * restrict format va_list ap Ft int Fn vscanf_l locale_t loc const char * restrict format va_list ap Ft int Fn vsscanf_l const char * restrict str locale_t loc const char * restrict format va_list ap`

## 描述

上述函数根据指定的 `format` 在 locale `loc` 中扫描输入。它们的行为与不带 _l 后缀的版本相同，但使用特定 locale 而非全局或每线程 locale。更多信息参见具体手册页。

## 参见

[scanf(3)](scanf.3.md), [xlocale(3)](../locale/xlocale.3.md)

## 标准

这些函数不遵循任何特定标准，应视为不可移植的本地扩展。

## 历史

这些函数首次出现于 Darwin，最早在 FreeBSD 9.1 中实现。
