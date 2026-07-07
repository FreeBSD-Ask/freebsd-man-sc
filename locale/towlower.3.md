# towlower(3)

`towlower` — 大写字母转换为小写字母（宽字符版本）

## 名称

`towlower`

## 库

Lb libc

## 概要

`#include <wctype.h>`

`Ft wint_t Fn towlower wint_t wc`

## 描述

`towlower` 函数将大写字母转换为对应的小写字母。

## 返回值

若参数为大写字母，`towlower` 函数在存在对应小写字母时返回该小写字母；否则参数原样返回。

## 参见

iswlower(3), [tolower(3)](tolower.3.md), [towupper(3)](towupper.3.md), [wctrans(3)](wctrans.3.md)

## 标准

`towlower` 函数遵循 ISO/IEC 9899:1999 (“ISO C99”)。
