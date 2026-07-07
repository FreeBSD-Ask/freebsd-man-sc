# towupper(3)

`towupper` — 小写字母转换为大写字母（宽字符版本）

## 名称

`towupper`

## 库

Lb libc

## 概要

`#include <wctype.h>`

`Ft wint_t Fn towupper wint_t wc`

## 描述

`towupper` 函数将小写字母转换为对应的大写字母。

## 返回值

若参数为小写字母，`towupper` 函数在存在对应大写字母时返回该大写字母；否则参数原样返回。

## 参见

iswupper(3), [toupper(3)](toupper.3.md), [towlower(3)](towlower.3.md), [wctrans(3)](wctrans.3.md)

## 标准

`towupper` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
