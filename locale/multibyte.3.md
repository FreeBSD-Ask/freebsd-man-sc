# multibyte(3)

`multibyte` — 多字节和宽字符操作函数

## 名称

`multibyte`

## 库

Lb libc

## 概要

`#include <limits.h>`

`#include <stdlib.h>`

`#include <wchar.h>`

## 描述

某些书面自然语言（如中文）的基本元素无法用单个 C `char` 唯一表示。C 标准支持两种处理扩展自然语言编码的不同方式：宽字符和多字节字符。宽字符是一种内部表示，允许每个基本元素映射到 `wchar_t` 类型的单个对象。多字节字符用于输入和输出，将每个基本元素编码为 C `char` 的序列。单个基本元素在多字节字符中可能映射到一个或多个（最多 `MB_LEN_MAX`）字节。

当前 locale（[setlocale(3)](setlocale.3.md)）控制宽字符和多字节字符的解释。locale 类别 `LC_CTYPE` 专门控制此解释。`wchar_t` 类型足够宽，可以容纳所有 locale 中宽字符表示的最大值。

多字节字符串可能包含“移位”指示符，用于在给定表示内的特定模式之间切换。如果使用显式字节来信号移位，这些字节不会被识别为独立字符，而是与相邻字符合并。始终存在一个独特的“初始”移位状态。某些函数（例如 [mblen(3)](mblen.3.md)、[mbtowc(3)](mbtowc.3.md) 和 [wctomb(3)](wctomb.3.md)）在内部维护静态移位状态，而其他函数则将其存储在调用者传递的 `mbstate_t` 对象中。在使用 `LC_CTYPE` 或 `LC_ALL` 类别调用 [setlocale(3)](setlocale.3.md) 之后，移位状态是未定义的。

为便于处理，值为 0 的宽字符（空宽字符）被识别为宽字符串终止符，值为 0 的字符（空字节）被识别为多字节字符串终止符。多字节字符中不允许空字节。

C 库提供以下函数用于处理多字节字符：

| 函数 | 描述 |
| --- | --- |
| [mblen(3)](mblen.3.md) | 获取字符的字节数 |
| [mbrlen(3)](mbrlen.3.md) | 获取字符的字节数（可重启） |
| [mbrtowc(3)](mbrtowc.3.md) | 将字符转换为宽字符码（可重启） |
| [mbsrtowcs(3)](mbsrtowcs.3.md) | 将字符串转换为宽字符字符串（可重启） |
| [mbstowcs(3)](mbstowcs.3.md) | 将字符串转换为宽字符字符串 |
| [mbtowc(3)](mbtowc.3.md) | 将字符转换为宽字符码 |
| [wcrtomb(3)](wcrtomb.3.md) | 将宽字符码转换为字符（可重启） |
| [wcstombs(3)](wcstombs.3.md) | 将宽字符字符串转换为字符串 |
| [wcsrtombs(3)](wcsrtombs.3.md) | 将宽字符字符串转换为字符串（可重启） |
| [wctomb(3)](wctomb.3.md) | 将宽字符码转换为字符 |

## 参见

localedef(1), [setlocale(3)](setlocale.3.md), stdio(3), big5(5), euc(5), gb18030(5), gb2312(5), gbk(5), mskanji(5), utf8(5)

## 标准

这些函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
