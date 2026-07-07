# ispunct(3)

`ispunct` — 标点符号字符测试

## 名称

`ispunct`, `ispunct_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn ispunct int c Ft int Fn ispunct_l int c locale_t loc`

## 描述

`ispunct` 和 `ispunct_l` 函数测试任何打印字符，空格或 [isalnum(3)](isalnum.3.md) 或 isalnum_l(3) 为真的字符除外。参数的值必须可表示为 `unsigned char` 或 `EOF` 的值。

在 ASCII 字符集中，这包含以下字符（数值以八进制表示）：

| `041 '!'` | `042 '"'` | `043 '#'` | `044 '$'` | `045 '%'` |
| --------- | --------- | --------- | --------- | --------- |
| `046 '&'` | `047 '''` | `050 '('` | `051 ')'` | `052 '*'` |
| `053 '+'` | `054 ','` | `055 '-'` | `056 '.'` | `057 '/'` |
| `072 ':'` | `073 ';'` | `074 '<'` | `075 '='` | `076 '>'` |
| `077 '?'` | `100 '@'` | `133 '['` | `134 '\'` | `135 ']'` |
| `136 '^'` | `137 '_'` | `140 GRAVE` | `173 '{'` | **174 '\|'** |
| `175 '}'` | `176 '~'` | | | |

`ispunct_l` 函数接受一个显式的 locale 参数，而 `ispunct` 函数使用当前的全局或每线程 locale。

## 返回值

`ispunct` 和 `ispunct_l` 函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `iswpunct` 或 `iswpunct_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), iswpunct(3), iswpunct_l(3), [xlocale(3)](xlocale.3.md), [ascii(7)](../man7/ascii.7.md)

## 标准

`ispunct` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`ispunct_l` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`ispunct` 函数首次出现于 Version 7 AT&T UNIX。
