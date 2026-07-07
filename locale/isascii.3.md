# isascii(3)

`isascii` — 测试 ASCII 字符

## 名称

`isascii`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn isascii int c`

## 描述

`isascii` 函数测试是否为 ASCII 字符，即 0 到八进制 0177 之间（含边界）的任何字符。

## 参见

[ctype(3)](ctype.3.md), iswascii(3), [ascii(7)](../man7/ascii.7.md)

## 历史

`isascii` 函数首次出现于 Version 7 AT&T UNIX。
