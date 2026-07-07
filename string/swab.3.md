# swab(3)

`swab` — 交换相邻字节

## 名称

`swab`

## 库

Lb libc

## 概要

`#include <unistd.h>`

`Ft void Fn swab const void * restrict src void * restrict dst ssize_t len`

## 描述

`swab` 函数从 `src` 引用的位置复制 `len` 个字节到 `dst` 引用的位置，并交换相邻字节。

参数 `len` 必须是偶数。若 `len` 小于零，则不做任何事情。

## 参见

[bzero(3)](bzero.3.md), [memset(3)](memset.3.md)

## 历史

`swab` 函数首次出现于 Version 7 AT&T UNIX。
