# getpagesizes(3)

`getpagesizes` — 获取系统页面大小

## 名称

`getpagesizes`

## 库

libc

## 概要

```c
#include <sys/mman.h>

int
getpagesizes(size_t pagesize[], int nelem);
```

## 描述

`getpagesizes` 函数从系统中获取页面大小信息。当以 `pagesize` 指定为 `NULL` 且 `nelem` 指定为 0 调用时，返回系统支持的不同页面大小数量。否则，它将最多 `nelem` 个系统支持的页面大小赋值给 `pagesize` 所引用数组的连续元素。这些页面大小以字节为单位表示。在此情况下，`getpagesizes` 返回赋值给该数组的页面大小数量。

## 返回值

如果成功，`getpagesizes` 函数返回系统支持的页面大小数量，或赋值给 `pagesize` 所引用数组的已支持页面大小数量。否则，返回值 -1，并设置 `errno` 以指示错误。

## 错误

除非出现以下情况，`getpagesizes` 函数将成功：

**`[EINVAL]`** `pagesize` 参数为 `NULL` 且 `nelem` 参数非零。

**`[EINVAL]`** `nelem` 参数小于零。

## 参见

[getpagesize(3)](getpagesize.3.md)

## 历史

`getpagesizes` 函数首次出现于 Solaris 9。本手册页是与一个新的但兼容的实现一起编写的，该实现首次发布于 FreeBSD 7.3。

## 作者

本手册页由 Alan L. Cox <alc@cs.rice.edu> 编写。
