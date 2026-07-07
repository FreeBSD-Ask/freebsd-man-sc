# strtod.3

`strtod`, `strtof`, `strtold` — 将 ASCII 字符串转换为浮点数

## 名称

`strtod`, `strtof`, `strtold`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
double
strtod(const char * restrict nptr, char ** restrict endptr);
float
strtof(const char * restrict nptr, char ** restrict endptr);
long double
strtold(const char * restrict nptr, char ** restrict endptr);
```

## 描述

这些转换函数将 `nptr` 所指字符串的初始部分分别转换为 `double`、`float` 和 `long double` 表示。

字符串的预期形式为一个可选的加号（`+`）或减号（`-`），后跟以下二者之一：

- 由一串十进制数字组成的十进制有效数字，可选择包含一个小数点字符；或
- 由 `0X` 或 `0x` 后跟一串十六进制数字组成的十六进制有效数字，可选择包含一个小数点字符。

在两种情况下，有效数字后可选择跟随一个指数。指数由 `E` 或 `e`（用于十进制常量）或 `P` 或 `p`（用于十六进制常量）组成，后跟一个可选的加号或减号，再跟一串十进制数字。对于十进制常量，指数表示有效数字应乘以的 10 的幂。对于十六进制常量，则按 2 的幂进行缩放。

或者，如果字符串中跟在可选加号或减号后面的部分以 "INFINITY" 或 "NAN" 开头（忽略大小写），则分别解释为无穷大或静默 NaN。语法 "NAN(s)"（其中 `s` 为字母数字字符串）所产生的值与调用 `nan("s")` 相同（分别对应 `nanf("s")` 和 `nanl("s")`）。

在上述任何情况下，字符串中的前导空白字符（由 [isspace(3)](../locale/isspace.3.md) 函数定义）都会被跳过。小数点字符由程序的 locale（类别 `LC_NUMERIC`）定义。

## 返回值

`strtod`、`strtof` 和 `strtold` 函数返回转换后的值（如果有）。

若 `endptr` 不为 `NULL`，则指向转换中所用最后一个字符之后那个字符的指针会被存入 `endptr` 所引用的位置。

若未执行转换，返回零，并将 `nptr` 的值存入 `endptr` 所引用的位置。

若正确值会导致上溢，则返回正或负的 `HUGE_VAL`、`HUGE_VALF` 或 `HUGE_VALL`（根据返回值的符号和类型），并将 `ERANGE` 存入 `errno`。若正确值会导致下溢，返回零，并将 `ERANGE` 存入 `errno`。

## 错误

**[`ERANGE`]** 发生上溢或下溢。

## 参见

[atof(3)](atof.3.md), [atoi(3)](atoi.3.md), [atol(3)](atol.3.md), nan(3), [strtol(3)](strtol.3.md), [strtoul(3)](strtoul.3.md), [wcstod(3)](../locale/wcstod.3.md)

## 标准

`strtod` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。

## 作者

本软件的作者是 David M. Gay。

```sh
Copyright (c) 1998 by Lucent Technologies
All Rights Reserved
Permission to use, copy, modify, and distribute this software and
its documentation for any purpose and without fee is hereby
granted, provided that the above copyright notice appear in all
copies and that both that the copyright notice and this
permission notice and warranty disclaimer appear in supporting
documentation, and that the name of Lucent or any of its entities
not be used in advertising or publicity pertaining to
distribution of the software without specific, written prior
permission.
LUCENT DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
IN NO EVENT SHALL LUCENT OR ANY OF ITS ENTITIES BE LIABLE FOR ANY
SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,
ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
THIS SOFTWARE.
```
