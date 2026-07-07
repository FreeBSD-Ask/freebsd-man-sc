# isideogram(3)

`isideogram` — 表意字符测试

## 名称

`isideogram`, `isideogram_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn isideogram int c Ft int Fn isideogram_l int c locale_t loc`

## 描述

`isideogram` 和 `isideogram_l` 函数测试是否为表意字符。

`isideogram_l` 函数接受一个显式的 locale 参数，而 `isideogram` 函数使用当前的全局或每线程 locale。

## 返回值

`isideogram` 和 `isideogram_l` 函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `iswideogram` 或 `iswideogram_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), [isphonogram(3)](isphonogram.3.md), isphonogram_l(3), iswideogram(3), iswideogram_l(3), [xlocale(3)](xlocale.3.md)

## 历史

`isideogram` 函数出现于 4.4BSD。
