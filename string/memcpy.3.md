# memcpy(3)

`memcpy` — 复制内存中的字节

## 名称

`memcpy`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft void * Fn memcpy void *dst const void *src size_t len Ft void * Fn mempcpy void *dst const void *src size_t len`

## 描述

`memcpy` 和 `mempcpy` 函数从对象 `src` 复制 `len` 个字节到对象 `dst`。若 `src` 和 `dst` 重叠，结果未定义。

## 返回值

`memcpy` 函数返回 `dst` 的原始值。

`mempcpy` 函数返回指向最后写入字节之后字节的指针。

## 参见

[bcopy(3)](bcopy.3.md), [memccpy(3)](memccpy.3.md), [memmove(3)](memmove.3.md), [strcpy(3)](strcpy.3.md), wmemcpy(3), wmempcpy(3)

## 标准

`memcpy` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。

## 历史

`memcpy` 函数首次出现于 AT&T System V UNIX，并为 4.3BSD 重新实现。`mempcpy` 函数首次出现于 FreeBSD 13.1。
