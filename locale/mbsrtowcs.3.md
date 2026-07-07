# mbsrtowcs(3)

`mbsrtowcs` — 将字符串转换为宽字符字符串（可重启）

## 名称

`mbsrtowcs`, `mbsnrtowcs`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft size_t Fo mbsrtowcs wchar_t * restrict dst const char ** restrict src size_t len mbstate_t * restrict ps Fc Ft size_t Fo mbsnrtowcs wchar_t * restrict dst const char ** restrict src size_t nms size_t len mbstate_t * restrict ps Fc`

## 描述

`mbsrtowcs` 函数将 `src` 间接指向的多字节字符序列转换为相应的宽字符序列，并最多将 `len` 个宽字符存储到 `dst` 所指向的 `wchar_t` 数组中，直到遇到终止的空字符（'e0'）。

若 `dst` 为 `NULL`，则不存储任何字符。

若 `dst` 不为 `NULL`，`src` 所指向的指针会被更新，指向停止转换处的字符之后。若因遇到空字符而停止转换，则将 `*src` 设置为 `NULL`。

`mbstate_t` 参数 `ps` 用于跟踪移位状态。若为 `NULL`，`mbsrtowcs` 使用一个内部的静态 `mbstate_t` 对象，该对象在程序启动时初始化为初始转换状态。

`mbsnrtowcs` 函数的行为与 `mbsrtowcs` 相同，区别在于从 `src` 所指向的缓冲区读取最多 `nms` 字节后停止转换。

## 返回值

若成功且 `dst` 不为 NULL，`mbsrtowcs` 和 `mbsnrtowcs` 函数返回存储在 `dst` 所指向的数组中的宽字符数。

若 `dst` 为 NULL，则 `mbsrtowcs` 和 `mbsnrtowcs` 函数返回本应存储的宽字符数（假设 `dst` 指向一个无限大的数组）。

若任一函数不成功，则返回 (`size_t`)-1。

## 错误

`mbsrtowcs` 和 `mbsnrtowcs` 函数在以下情况下会失败：

**[Er** EILSEQ] 遇到无效的多字节字符序列。

**[Er** EINVAL] 转换状态无效。

## 参见

[mbrtowc(3)](mbrtowc.3.md), [mbstowcs(3)](mbstowcs.3.md), [multibyte(3)](multibyte.3.md), [wcsrtombs(3)](wcsrtombs.3.md)

## 标准

`mbsrtowcs` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。

`mbsnrtowcs` 函数是该标准的扩展。
