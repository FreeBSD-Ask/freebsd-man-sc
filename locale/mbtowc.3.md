# mbtowc(3)

`mbtowc` — 将字符转换为宽字符码

## 名称

`mbtowc`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

`Ft int Fo mbtowc wchar_t * restrict wcharp const char * restrict mbchar size_t nbytes Fc`

## 描述

`mbtowc` 函数根据当前转换状态将多字节字符 `mbchar` 转换为宽字符，并将结果存储在 `wcharp` 所指向的对象中。最多检查 `nbytes` 个字节。

以空 `mbchar` 指针调用时，若当前编码需要移位状态则返回非零值，否则返回零；若需要移位状态，则将移位状态重置为初始状态。

## 返回值

若 `mbchar` 为 `NULL`，当支持移位状态时 `mbtowc` 函数返回非零值，否则返回零。

否则，若 `mbchar` 不是空指针，`mbtowc` 在 `mbchar` 表示空的宽字符时返回 0，在成功时返回 `mbchar` 中处理的字节数，在无法识别或转换任何多字节字符时返回 -1。在这种情况下，`mbtowc` 的内部转换状态是未定义的。

## 错误

`mbtowc` 函数在以下情况下会失败：

**[Er** EILSEQ] 检测到无效的多字节序列。

**[Er** EINVAL] 内部转换状态无效。

## 参见

[btowc(3)](btowc.3.md), [mblen(3)](mblen.3.md), [mbrtowc(3)](mbrtowc.3.md), [mbstowcs(3)](mbstowcs.3.md), [multibyte(3)](multibyte.3.md), [wctomb(3)](wctomb.3.md)

## 标准

`mbtowc` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
