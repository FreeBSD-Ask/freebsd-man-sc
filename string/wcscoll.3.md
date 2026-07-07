# wcscoll(3)

`wcscoll` — 按当前排序规则比较宽字符串

## 名称

`wcscoll`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft int Fn wcscoll const wchar_t *s1 const wchar_t *s2`

## 描述

`wcscoll` 函数根据当前 locale 的排序规则比较以 NUL 结尾的字符串 `s1` 和 `s2`。在 “`C`” locale 中，`wcscoll` 等价于 `wcscmp`。

## 返回值

`wcscoll` 函数返回一个大于、等于或小于 0 的整数，分别对应 `s1` 大于、等于或小于 `s2`。

没有保留用于指示错误的返回值；调用者应在调用 `wcscoll` 前将 `errno` 设置为 0。若从 `wcscoll` 返回时 `errno` 为非零值，表示发生了错误。

## 错误

`wcscoll` 函数在以下情况下会失败：

**[Er** EILSEQ] 指定了无效的宽字符编码。

**[Er** ENOMEM] 无法为临时缓冲区分配足够的内存。

## 参见

setlocale(3), [strcoll(3)](strcoll.3.md), wcscmp(3), [wcsxfrm(3)](wcsxfrm.3.md)

## 标准

`wcscoll` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。

## 缺陷

`wcscoll` 的当前实现仅在单字节 `LC_CTYPE` locale 下工作，在扩展字符集的 locale 中回退到使用 `wcscmp`。
