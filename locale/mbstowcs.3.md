# mbstowcs(3)

`mbstowcs` — 将字符串转换为宽字符字符串

## 名称

`mbstowcs`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

`Ft size_t Fo mbstowcs wchar_t * restrict wcstring const char * restrict mbstring size_t nwchars Fc`

## 描述

`mbstowcs` 函数将以初始转换状态开始的多字节字符串 `mbstring` 转换为宽字符字符串 `wcstring`。最多存储 `nwchars` 个宽字符。若有空间，则追加一个终止的空宽字符。

## 返回值

`mbstowcs` 函数返回转换的宽字符数（不包括任何终止的空宽字符），若遇到无效的多字节字符则返回 -1。

## 错误

`mbstowcs` 函数在以下情况下会失败：

**[Er** EILSEQ] 检测到无效的多字节序列。

**[Er** EINVAL] 转换状态无效。

## 参见

[mbsrtowcs(3)](mbsrtowcs.3.md), [mbtowc(3)](mbtowc.3.md), [multibyte(3)](multibyte.3.md)

## 标准

`mbstowcs` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
