# isrune.3

`isrune` — 有效字符测试

## 名称

`isrune`, `isrune_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn isrune int c Ft int Fn isrune_l int c locale_t loc`

## 描述

`isrune` 和 `isrune_l` 函数测试在当前字符集中有效的任何字符。在 ASCII 字符集中，这等价于 `isascii`。

`isrune_l` 函数接受一个显式的 locale 参数，而 `isrune` 函数使用当前的全局或每线程 locale。

## 返回值

`isrune` 和 `isrune_l` 函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `iswrune` 或 `iswrune_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), [isascii(3)](isascii.3.md), iswrune(3), iswrune_l(3), [xlocale(3)](xlocale.3.md), [ascii(7)](../man7/ascii.7.md)

## 历史

`isrune` 函数出现于 4.4BSD。
