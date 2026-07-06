# bstring(3)

`bstring` — 字节字符串操作

## 名称

`bcmp`, `bcopy`, `bzero`, `memccpy`, `memchr`, `memcmp`, `memcpy`, `memmove`, `memset`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft int Fn bcmp const void *b1 const void *b2 size_t len Ft void Fn bcopy const void *src void *dst size_t len Ft void Fn bzero void *b size_t len Ft void * Fn memchr const void *b int c size_t len Ft int Fn memcmp const void *b1 const void *b2 size_t len Ft void * Fo memccpy void * restrict dst const void * restrict src int c size_t len Fc Ft void * Fn memcpy void *dst const void *src size_t len Ft void * Fn memmove void *dst const void *src size_t len Ft void * Fn memset void *b int c size_t len`

## 描述

这些函数对可变长度的字节字符串进行操作。它们不像 string(3) 中列出的例程那样检查结尾的 NUL 字节。

更多信息请参阅具体的手册页。

## 参见

[bcmp(3)](bcmp.3.md), bcopy(3), [bzero(3)](bzero.3.md), memccpy(3), memchr(3), [memcmp(3)](memcmp.3.md), memcpy(3), memmove(3), memset(3)

## 标准

`memchr`、`memcmp`、`memcpy`、`memmove` 和 `memset` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。

## 历史

`bzero` 和 `memccpy` 函数出现于 4.3BSD；`bcmp` 和 `bcopy` 函数出现于 4.2BSD。
