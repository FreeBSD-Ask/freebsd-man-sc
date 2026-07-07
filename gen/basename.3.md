# basename(3)

`basename` — 提取路径名的基本部分

## 名称

`basename`

## 概要

`#include <libgen.h>`

```c
char *
basename(char *path);
```

## 描述

`basename` 函数返回 `path` 所指向路径名的最后一个组件，并删除任何尾随的 "`/`" 字符。

## 实现说明

此 `basename` 实现使用调用者提供的缓冲区来存储结果路径名组件。其他厂商的实现可能返回指向内部存储空间的指针。前者的优势在于确保线程安全，同时不对所支持的路径名长度设置上限。

## 返回值

如果 `path` 全部由 "`/`" 字符组成，则返回指向字符串 "/" 的指针。如果 `path` 是空指针或空字符串，则返回指向字符串 "." 的指针。否则，返回指向 `path` 最后一个组件的指针。

## 参见

[basename(1)](../man1/basename.1.md), dirname(1), [dirname(3)](dirname.3.md)

## 标准

`basename` 函数遵循 X/Open Portability Guide Issue 4, Version 2（"XPG4.2"）。

## 历史

`basename` 函数首次出现于 OpenBSD 2.2 和 FreeBSD 4.2。

在 FreeBSD 12.0 中，此函数被重新实现，将结果存储在所提供的输入缓冲区中。不再需要使用 `basename_r` 函数。

## 作者

Nuxi, the Netherlands
