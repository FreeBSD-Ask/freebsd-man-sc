# abs(3)

`abs` — 返回整数类型的绝对值

## 名称

`abs`, `labs`, `llabs`, `imaxabs`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
int
abs(int i);

long
labs(long i);

long long
llabs(long long i);
```

`#include <inttypes.h>`

```c
intmax_t
imaxabs(intmax_t i);
```

## 描述

`abs`、`labs`、`llabs` 和 `imaxabs` 函数计算 `i` 的绝对值。

## 返回值

`abs`、`labs`、`llabs` 和 `imaxabs` 函数返回绝对值。

## 参见

cabs(3), fabs(3), floor(3), hypot(3)

## 标准

`abs`、`labs`、`llabs` 和 `imaxabs` 函数遵循 ISO/IEC 9899:2023 ("ISO C23") 和 IEEE Std 1003.1-2024 ("POSIX.1")。

## 历史

`abs` 函数首次出现于 Version 6 AT&T UNIX。`labs` 函数首次出现于 4.3BSD。`llabs` 和 `imaxabs` 函数首次出现于 FreeBSD 5.0。

## 缺陷

最负的整数的绝对值仍为负数。
