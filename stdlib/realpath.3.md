# realpath.3

`realpath` — 返回规范化的绝对路径名

## 名称

`realpath`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
char *
realpath(const char * restrict pathname, char * restrict resolved_path);
```

## 描述

`realpath` 函数解析 `pathname` 中的所有符号链接、多余的 `"/"` 字符以及对 **/./** 和 **/../** 的引用，并将所得的绝对路径名复制到 `resolved_path` 所指向的内存中。`resolved_path` 参数*必须*指向一个能存储至少 `PATH_MAX` 个字符的缓冲区，或为 `NULL`。

`realpath` 函数会解析绝对路径和相对路径，并返回对应于 `pathname` 的绝对路径名。调用 `realpath` 时 `pathname` 的所有组件都必须存在，且除最后一个组件外，所有组件必须是目录或指向目录的符号链接。

## 返回值

成功时，若 `resolved_path` 不为 `NULL`，`realpath` 函数返回 `resolved_path`；若为 `NULL`，则返回指向以 null 结尾的字符串的指针，该字符串必须由调用者释放。若发生错误，`realpath` 返回 `NULL`，且若 `resolved_path` 不为 `NULL`，其所指向的数组将包含导致问题的路径名。

## 错误

`realpath` 函数可能失败，并为库函数 lstat(2)、[readlink(2)](../sys/readlink.2.md) 和 [getcwd(3)](../gen/getcwd.3.md) 所指定的任何错误设置外部变量 `errno`。

## 参见

[basename(3)](../gen/basename.3.md), [dirname(3)](../gen/dirname.3.md), free(3), [getcwd(3)](../gen/getcwd.3.md)

## 标准

`realpath` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`realpath` 函数首次出现于 4.4BSD。
