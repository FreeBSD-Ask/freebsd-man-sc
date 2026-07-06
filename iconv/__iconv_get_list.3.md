# \_\_iconv\_get\_list.3

`__iconv_get_list` — 获取 [iconv(3)](iconv.3.md) 所支持的字符编码列表

## 名称

`__iconv_get_list`, `__iconv_free_list`

## 库

Lb libc

## 概要

`#include <iconv.h>`

`Ft int Fn __iconv_get_list char ***names size_t count bool paired Ft void Fn __iconv_free_list char **names size_t count`

## 描述

`__iconv_get_list` 函数获取 [iconv(3)](iconv.3.md) 调用所支持的字符编码列表。编码名称列表将存储在 `names` 中，条目数量存储在 `count` 中。若 `paired` 变量为真，列表将按规范名称/别名配对排列。

`__iconv_free_list` 函数用于释放调用 `__iconv_get_list` 时分配的内存。

## 返回值

成功完成时，`__iconv_get_list` 返回 0 并设置 `names` 和 `count` 参数。否则，返回 -1 并设置 errno 以指示错误。

## 参见

[iconv(3)](iconv.3.md), [iconvlist(3)](iconvlist.3.md)

## 标准

`__iconv_get_list` 和 `__iconv_free_list` 函数是非标准接口，最早出现于 Citrus 项目的实现。Citrus 项目的 iconv 实现在 FreeBSD 9.0 中引入。

## 作者

本手册页由 Gabor Kovesdan <gabor@FreeBSD.org> 编写。
