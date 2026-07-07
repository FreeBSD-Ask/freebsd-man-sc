# tolower(3)

`tolower` — 大写字母转换为小写字母

## 名称

`tolower`, `tolower_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn tolower int c Ft int Fn tolower_l int c locale_t loc`

## 描述

`tolower` 和 `tolower_l` 函数将大写字母转换为对应的小写字母。参数必须可表示为 `unsigned char` 或 `EOF` 的值。

`tolower_l` 函数接受一个显式的 locale 参数，而 `tolower` 函数使用当前的全局或每线程 locale。

## 返回值

若参数为大写字母，`tolower` 和 `tolower_l` 函数在存在对应小写字母时返回该小写字母；否则参数原样返回。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `towlower` 或 `towlower_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), [islower(3)](islower.3.md), islower_l(3), [towlower(3)](towlower.3.md), towlower_l(3), [xlocale(3)](xlocale.3.md)

## 标准

`tolower` 函数遵循 ISO/IEC 9899:1990 (“ISO C89”)。
