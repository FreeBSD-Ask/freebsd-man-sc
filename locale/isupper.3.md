# isupper.3

`isupper` — 大写字母测试

## 名称

`isupper`, `isupper_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn isupper int c Ft int Fn isupper_l int c locale_t loc`

## 描述

`isupper` 和 `isupper_l` 函数测试任何大写字母。参数的值必须可表示为 `unsigned char` 或 `EOF` 的值。

在 ASCII 字符集中，这包含以下字符（数值以八进制表示）：

| `101 'A'` | `102 'B'` | `103 'C'` | `104 'D'` | `105 'E'` |
| --------- | --------- | --------- | --------- | --------- |
| `106 'F'` | `107 'G'` | `110 'H'` | `111 'I'` | `112 'J'` |
| `113 'K'` | `114 'L'` | `115 'M'` | `116 'N'` | `117 'O'` |
| `120 'P'` | `121 'Q'` | `122 'R'` | `123 'S'` | `124 'T'` |
| `125 'U'` | `126 'V'` | `127 'W'` | `130 'X'` | `131 'Y'` |
| `132 'Z'` | | | | |

`isupper_l` 函数接受一个显式的 locale 参数，而 `isupper` 函数使用当前的全局或每线程 locale。

## 返回值

`isupper` 和 `isupper_l` 函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `iswupper` 或 `iswupper_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), iswupper(3), iswupper_l(3), [toupper(3)](toupper.3.md), toupper_l(3), [xlocale(3)](xlocale.3.md), [ascii(7)](../man7/ascii.7.md)

## 标准

`isupper` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。

## 历史

`isupper` 函数首次出现于 Version 7 AT&T UNIX。
