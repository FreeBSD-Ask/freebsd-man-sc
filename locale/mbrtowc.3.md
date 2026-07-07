# mbrtowc(3)

`mbrtowc` — 将字符转换为宽字符码（可重启）

## 名称

`mbrtowc`, `mbrtoc16`, `mbrtoc32`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft size_t Fo mbrtowc wchar_t * restrict pc const char * restrict s size_t n mbstate_t * restrict ps Fc`

`#include <uchar.h>`

`Ft size_t Fo mbrtoc16 char16_t * restrict pc const char * restrict s size_t n mbstate_t * restrict ps Fc Ft size_t Fo mbrtoc32 char32_t * restrict pc const char * restrict s size_t n mbstate_t * restrict ps Fc`

## 描述

`mbrtowc`、`mbrtoc16` 和 `mbrtoc32` 函数检查 `s` 所指向的最多 `n` 个字节，以确定完成下一个多字节字符所需的字节数。若可以完成一个字符且 `pc` 不为 `NULL`，则将 `s` 所表示的宽字符存储到 `pc` 所指向的 `wchar_t`、`char16_t` 或 `char32_t` 中。

若 `s` 为 `NULL`，这些函数的行为如同 `pc` 为 `NULL`、`s` 为空字符串（""）且 `n` 为 1。

`mbstate_t` 参数 `ps` 用于跟踪移位状态。若为 `NULL`，这些函数使用一个内部的静态 `mbstate_t` 对象，该对象在程序启动时初始化为初始转换状态。

由于单个 `char16_t` 不足以表示某些多字节字符，`mbrtoc16` 函数可能需要调用多次才能转换一个多字节字符序列。

## 返回值

`mbrtowc`、`mbrtoc16` 和 `mbrtoc32` 函数返回：

**0** 接下来的 `n` 个或更少字节表示空的宽字符（L'e0'）。

**>0** 接下来的 `n` 个或更少字节表示一个有效字符，这些函数返回完成该多字节字符所使用的字节数。

**(`size_t`** )-1 发生编码错误。接下来的 `n` 个或更少字节不构成有效的多字节字符。

**(`size_t`** )-2 接下来的 `n` 个字节构成但未完成一个有效的多字节字符序列，且所有 `n` 个字节都已被处理。

`mbrtoc16` 函数还返回：

**(`size_t`** )-3 上一次调用所产生的下一个字符已被存储。未消耗输入中的任何字节。

## 错误

`mbrtowc`、`mbrtoc16` 和 `mbrtoc32` 函数在以下情况下会失败：

**[Er** EILSEQ] 检测到无效的多字节序列。

**[Er** EINVAL] 转换状态无效。

## 参见

[mbtowc(3)](mbtowc.3.md), [multibyte(3)](multibyte.3.md), [setlocale(3)](setlocale.3.md), [wcrtomb(3)](wcrtomb.3.md)

## 标准

`mbrtowc`、`mbrtoc16` 和 `mbrtoc32` 函数遵循 ISO/IEC 9899:2011 ("ISO C11")。
