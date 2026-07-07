# getcwd(3)

`getcwd` — 获取工作目录路径名

## 名称

`getcwd`, `getwd`

## 库

Lb libc

## 概要

`#include <unistd.h>`

`Ft char * Fn getcwd char *buf size_t size Ft char * Fn getwd char *buf`

## 描述

`getcwd` 函数将当前工作目录的绝对路径名复制到 `buf` 所引用的内存中，并返回指向 `buf` 的指针。`size` 参数是 `buf` 所引用数组的字节大小。

若 `buf` 为 `NULL`，将根据需要分配空间以存储路径名。该空间随后可由 free(3) 释放。

`getwd` 函数是一个兼容例程，它以 `buf` 参数和大小 `MAXPATHLEN`（定义于头文件

`#include <sys/param.h>`

中）调用 `getcwd`。显然，`buf` 的长度应至少为 `MAXPATHLEN` 字节。

这些例程传统上被程序用于保存工作目录名以便稍后返回。一种更快且更不易出错的方法是打开当前目录（`.`）并使用 fchdir(2) 函数返回。

## 返回值

成功完成时，返回指向路径名的指针。否则返回 `NULL` 指针，并设置全局变量 `errno` 以指示错误。此外，`getwd` 将与 `errno` 关联的错误消息复制到 `buf` 所引用的内存中。

## 错误

`getcwd` 函数将在以下情况下失败：

**[Er** EINVAL] `size` 参数为零。

**[Er** ENOENT] 路径名的某个组件不再存在。

**[Er** ENOMEM] 内存不足。

**[Er** ERANGE] `size` 参数大于零但小于路径名长度加 1。

`getcwd` 函数可能在以下情况下失败：

**[Er** EACCES] 对路径名的某个组件拒绝读取或搜索权限。根据实现细节，仅在有限情况下检查此项。

## 参见

[chdir(2)](../sys/chdir.2.md), fchdir(2), malloc(3), [strerror(3)](../string/strerror.3.md)

## 标准

`getcwd` 函数遵循 IEEE Std 1003.1-1990 ("POSIX.1")。指定 `NULL` 指针并让 `getcwd` 根据需要分配内存的能力是一种扩展。

## 历史

`getwd` 函数出现于 4.0BSD。

## 缺陷

`getwd` 函数未进行充分的错误检查，且无法返回很长但有效的路径。提供它是为了兼容性。
