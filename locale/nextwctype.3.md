# nextwctype(3)

`nextwctype` — 遍历字符类

## 名称

`nextwctype`

## 库

Lb libc

## 概要

`#include <wctype.h>`

`Ft wint_t Fn nextwctype wint_t ch wctype_t wct`

## 描述

`nextwctype` 函数确定 `ch` 之后属于字符类 `wct` 的下一个字符。若 `ch` 为 -1，则从 `wct` 的第一个成员开始搜索。

## 返回值

`nextwctype` 函数返回下一个字符，若没有更多字符则返回 -1。

## 兼容性

此函数是一个非标准的 FreeBSD 扩展，在标准的 `iswctype` 函数足以胜任的情况下不应使用。

## 参见

[wctype(3)](wctype.3.md)

## 历史

`nextwctype` 函数出现于 FreeBSD 5.4。
