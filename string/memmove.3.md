# memmove(3)

`memmove` — 复制内存中的字节

## 名称

`memmove`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft void * Fn memmove void *dst const void *src size_t len`

## 描述

`memmove` 函数从对象 `src` 复制 `len` 个字节到对象 `dst`。两个对象可以重叠；复制始终以非破坏性方式完成。

## 返回值

`memmove` 函数返回 `dst` 的原始值。

## 参见

[bcopy(3)](bcopy.3.md), [memccpy(3)](memccpy.3.md), [memcpy(3)](memcpy.3.md), [strcpy(3)](strcpy.3.md), wmemmove(3)

## 标准

`memmove` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。
