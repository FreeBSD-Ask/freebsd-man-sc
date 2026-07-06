# wcrtomb(3)

`wcrtomb` — 将宽字符码转换为字符（可重启）

## 名称

`wcrtomb`, `c16rtomb`, `c32rtomb`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft size_t Fn wcrtomb char * restrict s wchar_t c mbstate_t * restrict ps`

`#include <uchar.h>`

`Ft size_t Fn c16rtomb char * restrict s char16_t c mbstate_t * restrict ps Ft size_t Fn c32rtomb char * restrict s char32_t c mbstate_t * restrict ps`

## 描述

`wcrtomb`、`c16rtomb` 和 `c32rtomb` 函数将表示宽字符 `c` 的多字节序列（包括任何必要的移位序列）存储到字符数组 `s` 中，最多存储 `MB_CUR_MAX` 字节。

若 `s` 为 `NULL`，这些函数的行为如同 `s` 指向内部缓冲区且 `c` 为空的宽字符（L'e0'）。

`mbstate_t` 参数 `ps` 用于跟踪移位状态。若为 `NULL`，这些函数使用一个内部的静态 `mbstate_t` 对象，该对象在程序启动时初始化为初始转换状态。

由于某些多字节字符可能只能由一系列 16 位字符表示，`c16rtomb` 可能需要调用多次才能返回一个完整的多字节序列。

## 返回值

这些函数返回表示 `c` 所需的多字节序列的长度（以字节为单位），若 `c` 不是有效的宽字符码则返回 (`size_t`)-1。

## 错误

`wcrtomb`、`c16rtomb` 和 `c32rtomb` 函数在以下情况下会失败：

**[Er** EILSEQ] 指定了无效的宽字符码。

**[Er** EINVAL] 转换状态无效。

## 参见

[mbrtowc(3)](mbrtowc.3.md), [multibyte(3)](multibyte.3.md), [setlocale(3)](setlocale.3.md), [wctomb(3)](wctomb.3.md)

## 标准

`wcrtomb`、`c16rtomb` 和 `c32rtomb` 函数遵循 ISO/IEC 9899:2011 ("ISO C11")。
