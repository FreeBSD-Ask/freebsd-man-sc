# remove(3)

`remove` — 删除目录项

## 名称

`remove`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft int Fn remove const char *path`

## 描述

`remove` 函数删除由 `path` 指定的文件或目录。

如果 `path` 指定的是一个目录，`remove(path)` 等价于 `rmdir(path)`。否则，等价于 `unlink(path)`。

## 返回值

`remove` 函数成功完成时返回 0。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`remove` 函数可能失败，并为 lstat(2)、[rmdir(2)](../man2/rmdir.2.md) 或 [unlink(2)](../man2/unlink.2.md) 例程所指定的任何错误设置 `errno`。

## 参见

[rmdir(2)](../man2/rmdir.2.md), [unlink(2)](../man2/unlink.2.md)

## 标准

`remove` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 和 X/Open CAE Specification, Issue 4, Version 2 ("XPG4.2") 标准。
