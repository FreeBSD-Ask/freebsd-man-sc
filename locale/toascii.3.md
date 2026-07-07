# toascii(3)

`toascii` — 将字节转换为 7 位 ASCII

## 名称

`toascii`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn toascii int c`

## 描述

`toascii` 函数去除一个字符中除低 7 位以外的所有位，包括奇偶校验位或其他标记位。

## 返回值

`toascii` 函数始终返回一个有效的 ASCII 字符。

## 参见

[digittoint(3)](digittoint.3.md), [isalnum(3)](isalnum.3.md), [isalpha(3)](isalpha.3.md), [isascii(3)](isascii.3.md), [iscntrl(3)](iscntrl.3.md), [isdigit(3)](isdigit.3.md), [isgraph(3)](isgraph.3.md), [islower(3)](islower.3.md), [isprint(3)](isprint.3.md), [ispunct(3)](ispunct.3.md), [isspace(3)](isspace.3.md), [isupper(3)](isupper.3.md), [isxdigit(3)](isxdigit.3.md), stdio(3), [tolower(3)](tolower.3.md), [toupper(3)](toupper.3.md), ascii(7)
