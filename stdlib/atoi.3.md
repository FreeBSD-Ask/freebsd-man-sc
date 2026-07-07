# atoi(3)

`atoi` — 将 ASCII 字符串转换为整数

## 名称

`atoi`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
int
atoi(const char *nptr);
```

## 描述

`atoi` 函数将 `nptr` 所指字符串的初始部分转换为 `int` 表示。

它等价于：

```c
(int)strtol(nptr, NULL, 10);
```

`atoi` 函数已被 `strtol` 取代，不应在新代码中使用。

## 错误

`atoi` 函数在出错时不需要影响 `errno` 的值。

## 参见

[atof(3)](atof.3.md), [atol(3)](atol.3.md), [strtod(3)](strtod.3.md), [strtol(3)](strtol.3.md), [strtoul(3)](strtoul.3.md)

## 标准

`atoi` 函数遵循 IEEE Std 1003.1-1990 ("POSIX.1")、ISO/IEC 9899:1990 ("ISO C89") 和 ISO/IEC 9899:1999 ("ISO C99")。

## 历史

`atoi` 函数首次出现于 Version 1 AT&T UNIX。
