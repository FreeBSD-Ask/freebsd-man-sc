# atof(3)

`atof` — 将 ASCII 字符串转换为 `double`

## 名称

`atof`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
double
atof(const char *nptr);
```

## 描述

`atof` 函数将 `nptr` 所指字符串的初始部分转换为 `double` 表示。

它等价于：

```c
strtod(nptr, (char **)NULL);
```

小数点字符由程序的 locale（类别 `LC_NUMERIC`）定义。

## 实现说明

`atof` 函数不是线程安全的，也不是异步取消安全的。

`atof` 函数已被 `strtod` 取代，不应在新代码中使用。

## 错误

`atof` 函数在出错时不需要影响 `errno` 的值。

## 参见

[atoi(3)](atoi.3.md), [atol(3)](atol.3.md), [strtod(3)](strtod.3.md), [strtol(3)](strtol.3.md), [strtoul(3)](strtoul.3.md)

## 标准

`atof` 函数遵循 IEEE Std 1003.1-1990 ("POSIX.1")、ISO/IEC 9899:1990 ("ISO C89") 和 ISO/IEC 9899:1999 ("ISO C99")。

## 历史

`atof` 函数首次出现于 Version 1 AT&T UNIX。
