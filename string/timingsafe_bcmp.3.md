# timingsafe_bcmp(3)

`timingsafe_bcmp` — 时序安全的字节序列比较

## 名称

`timingsafe_bcmp`, `timingsafe_memcmp`

## 概要

`#include <string.h>`

`Ft int Fn timingsafe_bcmp const void *b1 const void *b2 size_t len Ft int Fn timingsafe_memcmp const void *b1 const void *b2 size_t len`

## 描述

`timingsafe_bcmp` 和 `timingsafe_memcmp` 函数按字典序比较 `b1` 和 `b2` 所指向前 `len` 个字节（每个字节解释为 `unsigned char`）。

此外，它们的运行时间与所比较的字节序列无关，使其可安全用于比较密码学 MAC 等机密值。相比之下，[bcmp(3)](bcmp.3.md) 和 [memcmp(3)](memcmp.3.md) 可能在找到第一个不同的字节后短路。

## 返回值

若 `b1` 所指向的字节序列等于 `b2` 所指向的字节序列，`timingsafe_bcmp` 函数返回 0，否则返回非零值。

若 `b1` 所指向的字节序列分别小于、等于或大于 `b2` 所指向的字节序列，`timingsafe_memcmp` 函数返回负值、0 或正值。

## 参见

[bcmp(3)](bcmp.3.md), [memcmp(3)](memcmp.3.md)

## 标准

`timingsafe_bcmp` 和 `timingsafe_memcmp` 函数是 FreeBSD 扩展。

## 历史

`timingsafe_bcmp` 函数首次出现于 OpenBSD 4.9。

`timingsafe_memcmp` 函数首次出现于 OpenBSD 5.6。

两个函数首次出现于 FreeBSD 11.1。
