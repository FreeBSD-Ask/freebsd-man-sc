# wcsxfrm(3)

`wcsxfrm` — 在 locale 下转换宽字符串

## 名称

`wcsxfrm`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft size_t Fn wcsxfrm wchar_t * restrict dst const wchar_t * restrict src size_t n`

## 描述

`wcsxfrm` 函数按照当前 locale 的排序规则转换 `src` 所指向的以 NUL 结尾的宽字符串，然后将转换后的字符串复制到 `dst`。复制到 `dst` 的宽字符数不超过 `n`，包括末尾添加的 NUL 字符。若 `n` 设为 0（用于确定转换所需的实际大小），`dst` 可以为 `NULL` 指针。

对 `wcsxfrm` 转换后的两个字符串使用 `wcscmp` 进行比较，等价于对原始的两个字符串使用 `wcscoll` 进行比较。

## 返回值

成功完成时，`wcsxfrm` 返回转换后字符串的长度（不含末尾的 NUL 字符）。若该值大于等于 `n`，则 `dst` 的内容不确定。

## 参见

[setlocale(3)](setlocale.3.md), [strxfrm(3)](strxfrm.3.md), wcscmp(3), [wcscoll(3)](wcscoll.3.md)

## 标准

`wcsxfrm` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。

## 缺陷

`wcsxfrm` 的当前实现仅在单字节 `LC_CTYPE` locale 下工作，在扩展字符集的 locale 中回退到使用 `wcsncpy`。

对 `wcsxfrm` 转换后的两个字符串使用 `wcscmp` 进行比较，*并不总是* 等价于使用 `wcscoll` 进行比较；`wcsxfrm` 仅将主排序权重的信息存储到 `dst`，而 `wcscoll` 使用主权重和次权重比较字符。
