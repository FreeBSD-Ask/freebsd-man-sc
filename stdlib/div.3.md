# div.3

`div` — 返回除法的商和余数

## 名称

`div`, `ldiv`, `lldiv`, `imaxdiv`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
div_t
div(int numer, int denom);

ldiv_t
ldiv(long numer, long denom);

lldiv_t
lldiv(long long numer, long long denom);
```

`#include <inttypes.h>`

```c
imaxdiv_t
imaxdiv(intmax_t numer, intmax_t denom);
```

## 描述

`div`、`ldiv`、`lldiv` 和 `imaxdiv` 函数计算 `numer`（分子）除以 `denom`（分母）的值，并分别以 `div_t`、`ldiv_t`、`lldiv_t` 或 `imaxdiv_t` 类型的存储结果返回。这些类型是结构体，分别包含两个名为 `quot`（商）和 `rem`（余数）的 `int`、`long`、`long long` 或 `intmax_t` 成员。

## 标准

`div`、`ldiv`、`lldiv` 和 `imaxdiv` 函数遵循 ISO/IEC 9899:2023 ("ISO C23") 和 IEEE Std 1003.1-2024 ("POSIX.1")。

## 历史

`div` 和 `ldiv` 函数首次出现于 4.3BSD。`lldiv` 和 `imaxdiv` 函数首次出现于 FreeBSD 5.0。
