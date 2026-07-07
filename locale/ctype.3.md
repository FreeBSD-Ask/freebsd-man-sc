# ctype.3

`ctype` — 字符分类函数

## 名称

`digittoint`, `isalnum`, `isalpha`, `isascii`, `isblank`, `iscntrl`, `isdigit`, `isgraph`, `ishexnumber`, `isideogram`, `islower`, `isnumber`, `isphonogram`, `isprint`, `ispunct`, `isrune`, `isspace`, `isspecial`, `isupper`, `isxdigit`, `toascii`, `tolower`, `toupper`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn digittoint int c Ft int Fn isalnum int c Ft int Fn isalpha int c Ft int Fn isascii int c Ft int Fn iscntrl int c Ft int Fn isdigit int c Ft int Fn isgraph int c Ft int Fn ishexnumber int c Ft int Fn isideogram int c Ft int Fn islower int c Ft int Fn isnumber int c Ft int Fn isphonogram int c Ft int Fn isspecial int c Ft int Fn isprint int c Ft int Fn ispunct int c Ft int Fn isrune int c Ft int Fn isspace int c Ft int Fn isupper int c Ft int Fn isxdigit int c Ft int Fn toascii int c Ft int Fn tolower int c Ft int Fn toupper int c`

## 描述

上述函数对整数 `c` 执行字符测试和转换。它们可作为宏使用，定义在包含文件

`#include <ctype.h>`

中，也可作为 C 库中的真实函数使用。更多信息参见具体的手册页。

## 参见

[digittoint(3)](digittoint.3.md), [isalnum(3)](isalnum.3.md), [isalpha(3)](isalpha.3.md), [isascii(3)](isascii.3.md), [isblank(3)](isblank.3.md), [iscntrl(3)](iscntrl.3.md), [isdigit(3)](isdigit.3.md), [isgraph(3)](isgraph.3.md), [isideogram(3)](isideogram.3.md), [islower(3)](islower.3.md), [isphonogram(3)](isphonogram.3.md), [isprint(3)](isprint.3.md), [ispunct(3)](ispunct.3.md), [isrune(3)](isrune.3.md), [isspace(3)](isspace.3.md), [isspecial(3)](isspecial.3.md), [isupper(3)](isupper.3.md), [isxdigit(3)](isxdigit.3.md), [toascii(3)](toascii.3.md), [tolower(3)](tolower.3.md), [toupper(3)](toupper.3.md), [wctype(3)](wctype.3.md), [ascii(7)](../man7/ascii.7.md)

## 标准

这些函数（除 `digittoint`、`isascii`、`ishexnumber`、`isideogram`、`isnumber`、`isphonogram`、`isrune`、`isspecial` 和 `toascii` 外）遵循 ISO/IEC 9899:1990 ("ISO C89")。

## 历史

`isalpha`、`isupper`、`islower`、`isdigit`、`isalnum`、`isspace`、`ispunct`、`isprint`、`iscntrl` 和 `isascii` 函数首次出现于 Version 7 AT&T UNIX。
