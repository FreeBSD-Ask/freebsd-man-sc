# isalnum.3

`isalnum` — 字母数字字符测试

## 名称

`isalnum`, `isalnum_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn isalnum int c Ft int Fn isalnum_l int c locale_t loc`

## 描述

`isalnum` 和 `isalnum_l` 函数测试任何满足 [isalpha(3)](isalpha.3.md)、isalpha_l(3) 或 [isdigit(3)](isdigit.3.md)、isdigit_l(3) 为真的字符。参数的值必须可表示为 `unsigned char` 或 `EOF` 的值。

在 ASCII 字符集中，这包含以下字符（数值以八进制表示）：

| `060 '0'` | `061 '1'` | `062 '2'` | `063 '3'` | `064 '4'` |
| --------- | --------- | --------- | --------- | --------- |
| `065 '5'` | `066 '6'` | `067 '7'` | `070 '8'` | `071 '9'` |
| `101 'A'` | `102 'B'` | `103 'C'` | `104 'D'` | `105 'E'` |
| `106 'F'` | `107 'G'` | `110 'H'` | `111 'I'` | `112 'J'` |
| `113 'K'` | `114 'L'` | `115 'M'` | `116 'N'` | `117 'O'` |
| `120 'P'` | `121 'Q'` | `122 'R'` | `123 'S'` | `124 'T'` |
| `125 'U'` | `126 'V'` | `127 'W'` | `130 'X'` | `131 'Y'` |
| `132 'Z'` | `141 'a'` | `142 'b'` | `143 'c'` | `144 'd'` |
| `145 'e'` | `146 'f'` | `147 'g'` | `150 'h'` | `151 'i'` |
| `152 'j'` | `153 'k'` | `154 'l'` | `155 'm'` | `156 'n'` |
| `157 'o'` | `160 'p'` | `161 'q'` | `162 'r'` | `163 's'` |
| `164 't'` | `165 'u'` | `166 'v'` | `167 'w'` | `170 'x'` |
| `171 'y'` | `172 'z'` | | | |

`isalnum_l` 函数接受一个显式的 locale 参数，而 `isalnum` 函数使用当前的全局或每线程 locale。

## 返回值

`isalnum` 和 `isalnum_l` 函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `iswalnum` 或 `iswalnum_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), [isalpha(3)](isalpha.3.md), isalpha_l(3), [isdigit(3)](isdigit.3.md), isdigit_l(3), [iswalnum(3)](iswalnum.3.md), [iswalnum_l(3)](iswalnum_l.3.md), [xlocale(3)](xlocale.3.md), [ascii(7)](../man7/ascii.7.md)

## 标准

`isalnum` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`isalnum_l` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`isalnum` 函数首次出现于 Version 7 AT&T UNIX。
