# wcsrtombs(3)

`wcsrtombs` — 将宽字符字符串转换为字符串（可重启）

## 名称

`wcsrtombs`, `wcsnrtombs`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft size_t Fo wcsrtombs char * restrict dst const wchar_t ** restrict src size_t len mbstate_t * restrict ps Fc Ft size_t Fo wcsnrtombs char * restrict dst const wchar_t ** restrict src size_t nwc size_t len mbstate_t * restrict ps Fc`

## 描述

`wcsrtombs` 函数将 `src` 间接指向的宽字符字符串转换为相应的多字节字符字符串，并存储到 `dst` 所指向的数组中。最多将 `len` 字节写入 `dst`。

若 `dst` 为 `NULL`，则不存储任何字符。

若 `dst` 不为 `NULL`，`src` 所指向的指针会被更新，指向停止转换处的字符之后。若因遇到空字符而停止转换，则将 `*src` 设置为 `NULL`。

`mbstate_t` 参数 `ps` 用于跟踪移位状态。若为 `NULL`，`wcsrtombs` 使用一个内部的静态 `mbstate_t` 对象，该对象在程序启动时初始化为初始转换状态。

`wcsnrtombs` 函数的行为与 `wcsrtombs` 相同，区别在于从 `src` 所指向的缓冲区读取最多 `nwc` 个字符后停止转换。

## 返回值

若成功，`wcsrtombs` 和 `wcsnrtombs` 函数返回存储在 `dst` 所指向的数组中的字节数（不包括任何终止的空字符），否则返回 (`size_t`)-1。

## 错误

`wcsrtombs` 和 `wcsnrtombs` 函数在以下情况下会失败：

**[Er** EILSEQ] 遇到无效的宽字符。

**[Er** EINVAL] 转换状态无效。

## 参见

[mbsrtowcs(3)](mbsrtowcs.3.md), [wcrtomb(3)](wcrtomb.3.md), [wcstombs(3)](wcstombs.3.md)

## 标准

`wcsrtombs` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。

`wcsnrtombs` 函数是该标准的扩展。
