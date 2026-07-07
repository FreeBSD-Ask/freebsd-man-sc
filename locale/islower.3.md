# islower(3)

`islower` — 小写字母测试

## 名称

`islower`, `islower_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn islower int c Ft int Fn islower_l int c locale_t loc`

## 描述

`islower` 和 `islower_l` 函数测试任何小写字母。参数的值必须可表示为 `unsigned char` 或 `EOF` 的值。

在 ASCII 字符集中，这包含以下字符（数值以八进制表示）：

| `141 'a'` | `142 'b'` | `143 'c'` | `144 'd'` | `145 'e'` |
| --------- | --------- | --------- | --------- | --------- |
| `146 'f'` | `147 'g'` | `150 'h'` | `151 'i'` | `152 'j'` |
| `153 'k'` | `154 'l'` | `155 'm'` | `156 'n'` | `157 'o'` |
| `160 'p'` | `161 'q'` | `162 'r'` | `163 's'` | `164 't'` |
| `165 'u'` | `166 'v'` | `167 'w'` | `170 'x'` | `171 'y'` |
| `172 'z'` | | | | |

`islower_l` 函数接受一个显式的 locale 参数，而 `islower` 函数使用当前的全局或每线程 locale。

## 返回值

`islower` 和 `islower_l` 函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `iswlower` 或 `iswlower_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), iswlower(3), iswlower_l(3), [tolower(3)](tolower.3.md), tolower_l(3), [xlocale(3)](xlocale.3.md), [ascii(7)](../man7/ascii.7.md)

## 标准

`islower` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`islower_l` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`islower` 函数首次出现于 Version 7 AT&T UNIX。
