# utime(3)

`utime` — 设置文件时间

## 名称

`utime` — 设置文件时间

## 库

Lb libc

## 概要

```c
#include <utime.h>

int
utime(const char *file, const struct utimbuf *timep);
```

## 描述

> **注意** 此接口已被 [utimensat(2)](../sys/utimensat.2.md) 取代，因为它无法精确到秒以下。

`utime` 函数根据 `timep` 所指向的 `struct utimbuf` 中的 `actime` 和 `modtime` 字段设置指定文件的访问时间和修改时间。

如果指定了时间（`timep` 参数非 `NULL`），调用者必须是文件所有者或超级用户。

如果未指定时间（`timep` 参数为 `NULL`），调用者必须是文件所有者、有写文件的权限，或是超级用户。

## 错误

`utime` 函数可能失败并为库函数 [utimes(2)](../sys/utimes.2.md) 指定的任何错误设置 `errno`。

## 参见

[stat(2)](../sys/stat.2.md), [utimensat(2)](../sys/utimensat.2.md), [utimes(2)](../sys/utimes.2.md)

## 标准

`utime` 函数遵循 -p1003.1-88 标准。

## 历史

`utime` 函数出现于 Version 7 AT&T UNIX。
