# creat(2)

`creat` — 创建新文件

## 名称

`creat`

## 库

Lb libc

## 概要

`#include <fcntl.h>`

```c
int
creat(const char *path, mode_t mode);
```

## 描述

此接口由 [open(2)](open.2.md) 取代。

`creat()` 函数等同于：

```c
open(path, O_CREAT | O_TRUNC | O_WRONLY, mode);
```

## 参见

[open(2)](open.2.md)

## 历史

`creat()` 函数出现于 Version 1 AT&T UNIX。
