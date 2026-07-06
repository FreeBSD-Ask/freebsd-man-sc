# memcmp(3)

`memcmp` — 比较内存中的字节

## 名称

`memcmp`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft int Fn memcmp const void *b1 const void *b2 size_t len`

## 描述

`memcmp` 函数将字节对象 `b1` 与字节对象 `b2` 进行比较。两个对象均假定为 `len` 字节长。

## 返回值

`memcmp` 函数在两个对象相同时返回零。零长度对象视为相同。若第一个不同的字节在 `b1` 中的值较小，`memcmp` 函数返回负值；若第一个不同的字节在 `b1` 中的值较大，返回正值。

## 参见

[bcmp(3)](bcmp.3.md), strcasecmp(3), [strcmp(3)](strcmp.3.md), [strcoll(3)](strcoll.3.md), [strxfrm(3)](strxfrm.3.md), timingsafe_memcmp(3), wmemcmp(3)

## 标准

`memcmp` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。

## 注意事项

若两个对象不同，C 库的 `memcmp` 实现返回前两个不同字节之间的差值（视为 `unsigned char` 值）。此行为未由 ISO/IEC 9899:1990 ("ISO C89") 规定，不可移植，且可能因编译器优化而不成立。
