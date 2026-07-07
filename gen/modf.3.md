# modf(3)

`modf` — 从浮点数中提取有符号整数和小数部分

## 名称

`modf`, `modff`, `modfl`

## 库

Lb libm

## 概要

`#include <math.h>`

```c
double
modf(double value, double *iptr);

float
modff(float value, float *iptr);

long double
modfl(long double value, long double *iptr);
```

## 描述

`modf`、`modff` 和 `modfl` 函数将参数 `value` 分解为整数部分和小数部分，每部分都与参数具有相同的符号。整数部分以浮点数形式存储在 `iptr` 所指向的对象中。

## 返回值

这些函数返回 `value` 的带符号小数部分。

## 参见

[frexp(3)](frexp.3.md), [ldexp(3)](ldexp.3.md), math(3)

## 标准

`modf`、`modff` 和 `modfl` 函数遵循 ISO/IEC 9899:1999（"ISO C99"）。
