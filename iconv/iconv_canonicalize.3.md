# iconv_canonicalize(3)

`iconv_canonicalize` — 将字符编码名称解析为规范形式

## 名称

`iconv_canonicalize`

## 库

Lb libc

## 概要

`#include <iconv.h>`

`Ft const char * Fn iconv_canonicalize const char *name`

## 描述

`iconv_canonicalize` 函数将 `name` 参数指定的字符编码名称解析为其规范形式。

## 返回值

`iconv_canonicalize` 成功完成时返回给定编码的规范名称。若指定名称已经是规范名称，返回相同值。若指定名称不是已存在的字符编码名称，返回 NULL。

## 参见

[iconv(3)](iconv.3.md)

## 标准

`iconv_canonicalize` 函数是非标准扩展，最早出现于 GNU 实现，为兼容性考虑在 FreeBSD 9.0 中引入。

## 作者

本手册页由 Gabor Kovesdan <gabor@FreeBSD.org> 编写。
