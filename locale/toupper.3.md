# toupper(3)

`toupper` — 小写字母转换为大写字母

## 名称

`toupper`, `toupper_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn toupper int c Ft int Fn toupper_l int c locale_t loc`

## 描述

`toupper` 和 `toupper_l` 函数将小写字母转换为对应的大写字母。参数必须可表示为 `unsigned char` 或 `EOF` 的值。

`toupper_l` 函数接受一个显式的 locale 参数，而 `toupper` 函数使用当前的全局或每线程 locale。

## 返回值

若参数为小写字母，`toupper` 和 `toupper_l` 函数在存在对应大写字母时返回该大写字母；否则，参数原样返回。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `towupper` 或 `towupper_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), [isupper(3)](isupper.3.md), isupper_l(3), [towupper(3)](towupper.3.md), towupper_l(3), [xlocale(3)](xlocale.3.md)

## 标准

`toupper` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。
