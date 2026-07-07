# isspecial(3)

`isspecial` — 特殊字符测试

## 名称

`isspecial`, `isspecial_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn isspecial int c Ft int Fn isspecial_l int c locale_t loc`

## 描述

`isspecial` 和 `isspecial_l` 函数测试是否为特殊字符。

`isspecial_l` 函数接受一个显式的 locale 参数，而 `isspecial` 函数使用当前的全局或每线程 locale。

## 返回值

`isspecial` 和 `isspecial_l` 函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `iswspecial` 或 `iswspecial_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), iswspecial(3), iswspecial_l(3), [xlocale(3)](xlocale.3.md)

## 历史

`isspecial` 函数首次出现于 4.4BSD。
