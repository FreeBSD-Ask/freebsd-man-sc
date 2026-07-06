# mbsinit.3

`mbsinit` — 确定转换对象状态

## 名称

`mbsinit`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft int Fn mbsinit const mbstate_t *ps`

## 描述

`mbsinit` 函数确定 `ps` 所指向的 `mbstate_t` 对象是否描述初始转换状态。

## 返回值

若 `ps` 为 `NULL` 或描述初始转换状态，`mbsinit` 函数返回非零，否则返回零。

## 参见

[mbrlen(3)](mbrlen.3.md), [mbrtowc(3)](mbrtowc.3.md), [mbsrtowcs(3)](mbsrtowcs.3.md), [multibyte(3)](multibyte.3.md), [wcrtomb(3)](wcrtomb.3.md), [wcsrtombs(3)](wcsrtombs.3.md)

## 标准

`mbsinit` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
