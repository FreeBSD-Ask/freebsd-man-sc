# bcopy(3)

`bcopy` — 复制内存中的字节

## 名称

`bcopy`

## 库

Lb libc

## 概要

`#include <strings.h>`

`Ft void Fn bcopy const void *src void *dst size_t len`

## 描述

`bcopy` 函数从对象 `src` 复制 `len` 个字节到对象 `dst`。两个对象可以重叠。若 `len` 为零，不复制任何字节。

## 参见

[memccpy(3)](memccpy.3.md), [memcpy(3)](memcpy.3.md), [memmove(3)](memmove.3.md), [strcpy(3)](strcpy.3.md), strncpy(3)

## 历史

`bcopy` 函数出现于 4.2BSD。其原型此前位于

`#include <string.h>`

之后为遵循 IEEE Std 1003.1-2001 ("POSIX.1") 而移至

`#include <strings.h>`

IEEE Std 1003.1-2008 ("POSIX.1") 移除了 `bcopy` 的规范，且在 IEEE Std 1003.1-2004 ("POSIX.1") 中被标记为 LEGACY。新程序应使用 [memmove(3)](memmove.3.md)。若输入和输出缓冲区不重叠，则 [memcpy(3)](memcpy.3.md) 更高效。注意，`bcopy` 的 `src` 和 `dst` 参数顺序与 `memmove` 和 `memcpy` 相反。
