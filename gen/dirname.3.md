# dirname(3)

`dirname` — 提取路径名的目录部分

## 名称

`dirname`

## 概要

`#include <libgen.h>`

```c
char *
dirname(char *path);
```

## 描述

`dirname` 函数与 [basename(3)](basename.3.md) 相反；它返回指向 `path` 所指向路径名的父目录的指针。任何尾随的 "`/`" 字符不计入目录名的一部分。

## 实现说明

此 `dirname` 实现使用调用者提供的缓冲区来存储结果父目录。其他厂商的实现可能返回指向内部存储空间的指针。前者的优势在于确保线程安全，同时不对所支持的路径名长度设置上限。

## 返回值

如果 `path` 是空指针、空字符串或不包含 "`/`" 字符，`dirname` 返回指向字符串 "." 的指针，表示当前目录。否则，返回指向 `path` 父目录的指针。

## 参见

[basename(1)](../man1/basename.1.md), dirname(1), [basename(3)](basename.3.md)

## 标准

`dirname` 函数遵循 X/Open Portability Guide Issue 4, Version 2（"XPG4.2"）。

## 历史

`dirname` 函数首次出现于 OpenBSD 2.2 和 FreeBSD 4.2。

在 FreeBSD 12.0 中，此函数被重新实现，将结果存储在所提供的输入缓冲区中。

## 作者

Nuxi, the Netherlands