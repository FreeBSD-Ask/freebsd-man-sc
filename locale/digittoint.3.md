# digittoint(3)

`digittoint` — 将数字字符转换为其整数值

## 名称

`digittoint`, `digittoint_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn digittoint int c Ft int Fn digittoint_l int c locale_t loc`

## 描述

`digittoint` 和 `digittoint_l` 函数将数字字符转换为对应的整数值。该字符可以是任何十进制数字或十六进制数字。对于十六进制字符，其大小写不影响数值。

`digittoint_l` 函数接受一个显式的 locale 参数，而 `digittoint` 函数使用当前的全局或每线程 locale。

## 返回值

`digittoint` 和 `digittoint_l` 函数始终返回 0 到 15 范围内的整数。若给定字符不是由 [isxdigit(3)](isxdigit.3.md) 或 isxdigit_l(3) 定义的数字，函数将返回 0。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), [isdigit(3)](isdigit.3.md), isdigit_l(3), [isxdigit(3)](isxdigit.3.md), isxdigit_l(3), [xlocale(3)](xlocale.3.md)
