# querylocale(3)

`querylocale` — 查询指定类别的 locale 名称或版本

## 名称

`querylocale`

## 库

Lb libc

## 概要

`#include <locale.h>`

`Ft const char * Fn querylocale int mask locale_t locale`

## 描述

返回由 `mask` 指定类别的 locale 名称或版本。请求 locale 名称时，mask 的可能取值与 [newlocale(3)](newlocale.3.md) 中的相同。指定 `LC_VERSION_MASK` 与另一个 mask 值的按位或，可请求版本字符串。版本字符串可进行比较以检测 locale 定义的变更。版本字符串的结构未指定。目前，版本信息仅对 `LC_COLLATE_MASK` 可用，其他类别返回空字符串。若 mask 中设置了不止一个位（不计 `LC_VERSION_MASK`），返回值未定义。

## 参见

[duplocale(3)](duplocale.3.md), [freelocale(3)](freelocale.3.md), [localeconv(3)](localeconv.3.md), [newlocale(3)](newlocale.3.md), [uselocale(3)](uselocale.3.md), [xlocale(3)](xlocale.3.md)

## 历史

`querylocale` 函数首次出现于 FreeBSD 9.1，基于 Darwin 中同名函数。`LC_VERSION_MASK` 首次出现于 FreeBSD 13.0。
