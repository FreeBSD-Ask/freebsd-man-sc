# strcoll(3)

`strcoll` — 按当前排序规则比较字符串

## 名称

`strcoll`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft int Fn strcoll const char *s1 const char *s2 Ft int Fn strcoll_l const char *s1 const char *s2 locale_t loc`

## 描述

`strcoll` 函数根据当前 locale 的排序规则，按字典序比较以 NUL 结尾的字符串 `s1` 和 `s2`，返回一个大于、等于或小于 0 的整数，分别对应 `s1` 大于、等于或小于 `s2`。若当前 locale 排序规则的信息不可用，则返回 `strcmp(s1, s2)` 的值。`strcoll_l` 函数使用显式指定的 locale 参数而非系统 locale。

## 参见

setlocale(3), [strcmp(3)](strcmp.3.md), [strxfrm(3)](strxfrm.3.md), wcscoll(3)

## 标准

`strcoll` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`strcoll_l` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。
