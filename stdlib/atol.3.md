# atol.3

`atol`, `atoll` — 将 ASCII 字符串转换为 `long` 或 `long long` 整数

## 名称

`atol`, `atoll`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
long
atol(const char *nptr);
long long
atoll(const char *nptr);
```

## 描述

`atol` 函数将 `nptr` 所指字符串的初始部分转换为 `long` 整数表示。

它等价于：

```c
strtol(nptr, (char **)NULL, 10);
```

`atoll` 函数将 `nptr` 所指字符串的初始部分转换为 `long long` 整数表示。

它等价于：

```c
strtoll(nptr, (char **)NULL, 10);
```

## 兼容性

FreeBSD 对 `atol` 和 `atoll` 函数的实现分别是 `strtol` 和 `strtoll` 的薄封装，因此这些函数会以与 `strtol` 和 `strtoll` 函数相同的方式影响 `errno` 的值。ISO/IEC 9899:1990 ("ISO C89") 和 ISO/IEC 9899:1999 ("ISO C99") 并未要求 `atol` 和 `atoll` 的这一行为，但 ISO/IEC 9899:1990 ("ISO C89")、ISO/IEC 9899:1999 ("ISO C99") 和 IEEE Std 1003.1-2001 ("POSIX.1") 均允许该行为。

## 错误

`atol` 和 `atoll` 函数在出错时可能会影响 `errno` 的值。

## 参见

[atof(3)](atof.3.md), [atoi(3)](atoi.3.md), [strtod(3)](strtod.3.md), [strtol(3)](strtol.3.md), [strtoul(3)](strtoul.3.md)

## 标准

`atol` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`atoll` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
