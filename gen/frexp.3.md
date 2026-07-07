# frexp.3

`frexp` — 将浮点数分解为小数部分和整数部分

## 名称

`frexp`, `frexpf`, `frexpl`

## 库

Lb libm

## 概要

`#include <math.h>`

```c
double
frexp(double value, int *exp);

float
frexpf(float value, int *exp);

long double
frexpl(long double value, int *exp);
```

## 描述

`frexp`、`frexpf` 和 `frexpl` 函数将浮点数分解为归一化的小数部分和 2 的整数次幂。它们将整数存储在 `exp` 所指向的 `int` 对象中。

## 返回值

这些函数返回值 `x`，使得 `x` 是一个幅度在 [1/2, 1) 区间内或为零的 `double`，且 `value` 等于 `x` 乘以 2 的 `*exp` 次方。如果 `value` 为零，则结果的两部分均为零。

## 参见

[ldexp(3)](ldexp.3.md), math(3), [modf(3)](modf.3.md)

## 标准

`frexp`、`frexpf` 和 `frexpl` 函数遵循 ISO/IEC 9899:1999（"ISO C99"）。
