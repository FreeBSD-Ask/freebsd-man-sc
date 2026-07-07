# isblank(3)

`isblank` — 空格或制表符测试

## 名称

`isblank`, `isblank_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn isblank int c Ft int Fn isblank_l int c locale_t loc`

## 描述

`isblank` 和 `isblank_l` 函数测试空格或制表符。对于任何 locale，这包含以下标准字符：

| `'\t'` | `' '` |
| ------ | ----- |

在 `"C"` locale 中，`isblank` 或 `isblank_l` 的成功测试仅限于这些字符。参数的值必须可表示为 `unsigned char` 或 `EOF` 的值。

`isblank_l` 函数接受一个显式的 locale 参数，而 `isblank` 函数使用当前的全局或每线程 locale。

## 返回值

`isblank` 和 `isblank_l` 函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `iswblank` 或 `iswblank_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), iswblank(3), iswblank_l(3), [xlocale(3)](xlocale.3.md), [ascii(7)](../man7/ascii.7.md)

## 标准

`isblank` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。`isblank_l` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。
