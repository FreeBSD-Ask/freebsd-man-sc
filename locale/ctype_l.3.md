# ctype_l.3

`ctype_l` — 字符分类函数

## 名称

`digittoint_l`, `isalnum_l`, `isalpha_l`, `isblank_l`, `iscntrl_l`, `isdigit_l`, `isgraph_l`, `ishexnumber_l`, `isideogram_l`, `islower_l`, `isnumber_l`, `isphonogram_l`, `isprint_l`, `ispunct_l`, `isrune_l`, `isspace_l`, `isspecial_l`, `isupper_l`, `isxdigit_l`, `tolower_l`, `toupper_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn digittoint_l int c locale_t loc Ft int Fn isalnum_l int c locale_t loc Ft int Fn isalpha_l int c locale_t loc Ft int Fn iscntrl_l int c locale_t loc Ft int Fn isdigit_l int c locale_t loc Ft int Fn isgraph_l int c locale_t loc Ft int Fn ishexnumber_l int c locale_t loc Ft int Fn isideogram_l int c locale_t loc Ft int Fn islower_l int c locale_t loc Ft int Fn isnumber_l int c locale_t loc Ft int Fn isphonogram_l int c locale_t loc Ft int Fn isspecial_l int c locale_t loc Ft int Fn isprint_l int c locale_t loc Ft int Fn ispunct_l int c locale_t loc Ft int Fn isrune_l int c locale_t loc Ft int Fn isspace_l int c locale_t loc Ft int Fn isupper_l int c locale_t loc Ft int Fn isxdigit_l int c locale_t loc Ft int Fn tolower_l int c locale_t loc Ft int Fn toupper_l int c locale_t loc`

## 描述

上述函数在 locale `loc` 下对整数 `c` 执行字符测试和转换。它们的行为与不带 _l 后缀的版本相同，但使用指定的 locale 而非全局或每线程 locale。这些函数可作为宏定义在包含文件

`#include <ctype.h>`

中，也可作为 C 库中的真实函数使用。更多信息参见具体的手册页。

## 参见

digittoint_l(3), isalnum_l(3), isalpha_l(3), isblank_l(3), iscntrl_l(3), isdigit_l(3), isgraph_l(3), isideogram_l(3), islower_l(3), isphonogram_l(3), isprint_l(3), ispunct_l(3), isrune_l(3), isspace_l(3), isspecial_l(3), isupper_l(3), isxdigit_l(3), tolower_l(3), toupper_l(3), wctype_l(3), xlocale_l(3)

## 标准

这些函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")，但 `digittoint_l`、`ishexnumber_l`、`isideogram_l`、`isnumber_l`、`isphonogram_l`、`isrune_l` 和 `isspecial_l` 除外，它们是 FreeBSD 扩展。
