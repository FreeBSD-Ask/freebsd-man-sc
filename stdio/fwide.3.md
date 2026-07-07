# fwide.3

`fwide` — 获取/设置流的方向

## 名称

`fwide`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`#include <wchar.h>`

`Ft int Fn fwide FILE *stream int mode`

## 描述

`fwide` 函数确定 `stream` 所指向的流的方向。

若 `stream` 的方向已经确定，`fwide` 不作更改。否则，`fwide` 根据 `mode` 设置 `stream` 的方向。

若 `mode` 小于零，`stream` 被设置为字节方向。若大于零，`stream` 被设置为宽字符方向。否则，`mode` 为零，`stream` 保持不变。

## 返回值

`fwide` 函数在调用后根据方向返回相应的值：若为字节方向则返回小于零的值，若为宽字符方向则返回大于零的值，若流没有方向则返回零。

## 参见

[ferror(3)](ferror.3.md), fgetc(3), fgetwc(3), [fopen(3)](fopen.3.md), fputc(3), fputwc(3), freopen(3), [stdio(3)](stdio.3.md)

## 标准

`fwide` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
