# wcstombs(3)

`wcstombs` — 将宽字符串转换为字符串

## 名称

`wcstombs`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

`Ft size_t Fo wcstombs char * restrict mbstring const wchar_t * restrict wcstring size_t nbytes Fc`

## 描述

`wcstombs` 函数从初始转换状态开始，将宽字符串 `wcstring` 转换为多字节字符串 `mbstring`。最多将 `nbytes` 字节存储到 `mbstring` 中。字符串末尾的不完整多字节字符不会被存储。若仍有空间，多字节字符串以 NUL 结尾。

## 返回值

`wcstombs` 函数若成功则返回转换的字节数（不含末尾的 NUL 字符），否则返回 (`size_t`)-1。

## 错误

`wcstombs` 函数在以下情况下会失败：

**[Er** EILSEQ] 遇到无效的宽字符。

**[Er** EINVAL] 转换状态无效。

## 参见

[mbstowcs(3)](mbstowcs.3.md), [multibyte(3)](multibyte.3.md), [wcsrtombs(3)](wcsrtombs.3.md), [wctomb(3)](wctomb.3.md)

## 标准

`wcstombs` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
