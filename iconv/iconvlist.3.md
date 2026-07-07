# iconvlist(3)

`iconvlist` — 获取 [iconv(3)](iconv.3.md) 所支持的字符编码列表

## 名称

`iconvlist`

## 库

Lb libc

## 概要

`#include <iconv.h>`

`Ft void Fo iconvlist int *do_oneunsigned int count, const char * const *names, void *arg void *arg Fc`

## 描述

`iconvlist` 函数获取 [iconv(3)](iconv.3.md) 调用所支持的字符编码列表。将调用 `do_one` 回调函数，其中 `count` 参数设置为找到的编码名称数量，`names` 参数为支持的编码名称列表，`arg` 参数为 `iconvlist` 函数的 “外部” `arg` 参数。此参数可用于在 `iconvlist` 的调用者和回调函数之间交换自定义数据。

若发生错误，调用 `do_one` 时 `names` 将为 `NULL`。

## 参见

__iconv_free_list(3), [__iconv_get_list(3)](__iconv_get_list.3.md), [iconv(3)](iconv.3.md)

## 标准

`iconvlist` 函数是非标准扩展，最早出现于 GNU 实现，为兼容性考虑在 FreeBSD 9.0 中引入。

## 作者

本手册页由 Gabor Kovesdan <gabor@FreeBSD.org> 编写。
