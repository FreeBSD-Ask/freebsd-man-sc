# ldexp(3)

`ldexp` — 将浮点数乘以 2 的整数幂

## 名称

`ldexp`, `ldexpf`, `ldexpl`

## 库

Lb libm

## 概要

```c
#include <math.h>

double
ldexp(double x, int exp);

float
ldexpf(float x, int exp);

long double
ldexpl(long double x, int exp);
```

## 描述

`ldexp()`、`ldexpf()` 和 `ldexpl()` 函数将浮点数乘以 2 的整数幂。

## 返回值

这些函数返回 `x` 乘以 2 的 `exp` 次幂的值。

## 参见

[frexp(3)](frexp.3.md), math(3), [modf(3)](modf.3.md)

## 标准

`ldexp()`、`ldexpf()` 和 `ldexpl()` 函数遵循 ISO/IEC 9899:1999 ("ISO C99") 标准。
