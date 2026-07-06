# strxfrm.3

`strxfrm` — 在 locale 下转换字符串

## 名称

`strxfrm`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft size_t Fn strxfrm char * restrict dst const char * restrict src size_t n Ft size_t Fn strxfrm_l char * restrict dst const char *restrict src size_t n locale_t loc`

## 描述

`strxfrm` 函数按照当前 locale 的排序规则（若有）转换 `src` 所指向的以 NUL 结尾的字符串，然后将转换后的字符串复制到 `dst`。复制到 `dst` 的字符数不超过 `n`，包括末尾添加的 NUL 字符。若 `n` 设为 0（用于确定转换所需的实际大小），`dst` 可以为 `NULL` 指针。

对 `strxfrm` 转换后的两个字符串使用 `strcmp` 进行比较，等价于对原始的两个字符串使用 `strcoll` 进行比较。

`strxfrm_l` 功能相同，但接受显式指定的 locale 而非全局 locale。

## 返回值

成功完成时，`strxfrm` 和 `strxfrm_l` 返回转换后字符串的长度（不含末尾的 NUL 字符）。若该值大于等于 `n`，则 `dst` 的内容不确定。

## 参见

[setlocale(3)](setlocale.3.md), [strcmp(3)](strcmp.3.md), [strcoll(3)](strcoll.3.md), [wcsxfrm(3)](wcsxfrm.3.md)

## 标准

`strxfrm` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`strxfrm_l` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。
