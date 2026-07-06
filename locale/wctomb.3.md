# wctomb(3)

`wctomb` — 将宽字符码转换为字符

## 名称

`wctomb`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

`Ft int Fn wctomb char *mbchar wchar_t wchar`

## 描述

`wctomb` 函数将宽字符 `wchar` 转换为多字节字符，并将结果存储在 `mbchar` 中。`mbchar` 所指向的对象必须足够大以容纳该多字节字符，最多可能需要 `MB_LEN_MAX` 字节。

以空 `mbchar` 指针调用时，若当前 locale 需要移位状态则返回非零值，否则返回零；若需要移位状态，则将移位状态重置为初始状态。

## 返回值

若 `mbchar` 为 `NULL`，当支持移位状态时 `wctomb` 函数返回非零值，否则返回零。若 `mbchar` 有效，`wctomb` 返回 `mbchar` 中处理的字节数，若无法识别或转换任何多字节字符则返回 -1。在这种情况下，`wctomb` 的内部转换状态是未定义的。

## 错误

`wctomb` 函数在以下情况下会失败：

**[Er** EILSEQ] 检测到无效的多字节序列。

**[Er** EINVAL] 内部转换状态无效。

## 参见

[mbtowc(3)](mbtowc.3.md), [wcrtomb(3)](wcrtomb.3.md), [wcstombs(3)](wcstombs.3.md), wctob(3)

## 标准

`wctomb` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
