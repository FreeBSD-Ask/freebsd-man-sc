# isxdigit(3)

`isxdigit` — 十六进制数字字符测试

## 名称

`isxdigit`, `ishexnumber`, `isxdigit_l`, `ishexnumber_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn isxdigit int c Ft int Fn ishexnumber int c Ft int Fn isxdigit_l int c locale_t loc Ft int Fn ishexnumber_l int c locale_t loc`

## 描述

`isxdigit` 和 `isxdigit_l` 函数测试任何十六进制数字字符。无论 locale 如何，仅包含以下字符：

| `0` | `1` | `2` | `3` | `4` |
| --- | --- | --- | --- | --- |
| `5` | `6` | `7` | `8` | `9` |
| `A` | `B` | `C` | `D` | `E` |
| `F` | `a` | `b` | `c` | `d` |
| `e` | `f` | | | |

`ishexnumber` 和 `ishexnumber_l` 函数的行为类似于 `isxdigit` 和 `isxdigit_l`，但可能识别额外的字符，取决于当前的 locale 设置。

参数的值必须可表示为 `unsigned char` 或 `EOF` 的值。

带 _l 后缀的版本接受显式的 locale 参数，而不带后缀的版本使用当前的全局或每线程 locale。

## 返回值

`isxdigit` 和 `isxdigit_l` 函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `iswxdigit` 或 `iswxdigit_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), iswxdigit(3), iswxdigit_l(3), [xlocale(3)](xlocale.3.md), [ascii(7)](../man7/ascii.7.md)

## 标准

`isxdigit` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。

## 历史

`ishexnumber` 函数出现于 4.4BSD。
