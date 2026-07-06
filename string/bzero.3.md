# bzero.3

`bzero` — 向内存写入零

## 名称

`bzero`, `explicit_bzero`

## 库

Lb libc

## 概要

`#include <strings.h>`

`Ft void Fn bzero void *b size_t len Ft void Fn explicit_bzero void *b size_t len`

## 描述

`bzero` 函数向对象 `b` 写入 `len` 个零字节。若 `len` 为零，`bzero` 不做任何事情。

`explicit_bzero` 变体的行为相同，但不会被编译器的死存储优化过程移除，适用于清除敏感内存（如密码）。

## 参见

[memset(3)](memset.3.md), [swab(3)](swab.3.md)

## 历史

`bzero` 函数出现于 4.3BSD。其原型此前位于

`#include <string.h>`

之后为遵循 IEEE Std 1003.1-2001 ("POSIX.1") 而移至

`#include <strings.h>`

`explicit_bzero` 函数首次出现于 OpenBSD 5.5 和 FreeBSD 11.0。

IEEE Std 1003.1-2008 ("POSIX.1") 移除了 `bzero` 的规范，且在 IEEE Std 1003.1-2004 ("POSIX.1") 中被标记为 LEGACY。为与其他系统兼容，新程序应使用 [memset(3)](memset.3.md)。
