# bcmp(3)

`bcmp` — 比较字节字符串

## 名称

`bcmp`

## 库

Lb libc

## 概要

`#include <strings.h>`

`Ft int Fn bcmp const void *b1 const void *b2 size_t len`

## 描述

`bcmp` 函数将字节字符串 `b1` 与字节字符串 `b2` 进行比较，若两者相同则返回零，否则返回非零值。两个字符串均假定为 `len` 字节长。零长度字符串总是相同的。

两个字符串可以重叠。

## 参见

[memcmp(3)](memcmp.3.md), strcasecmp(3), [strcmp(3)](strcmp.3.md), [strcoll(3)](strcoll.3.md), [strxfrm(3)](strxfrm.3.md), timingsafe_bcmp(3)

## 历史

`bcmp` 函数首次出现于 4.2BSD。其原型此前位于

`#include <string.h>`

之后为遵循 IEEE Std 1003.1-2001 ("POSIX.1") 而移至

`#include <strings.h>`

IEEE Std 1003.1-2008 ("POSIX.1") 移除了 `bcmp` 的规范，且在 IEEE Std 1003.1-2004 ("POSIX.1") 中被标记为 LEGACY。为与其他系统兼容，新程序应使用 [memcmp(3)](memcmp.3.md)。
