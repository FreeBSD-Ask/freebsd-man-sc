# fpclassify(3)

`fpclassify` — 对浮点数进行分类

## 名称

`fpclassify`

## 库

Lb libm

## 概要

`#include <math.h>`

```c
int
fpclassify(real-floating x);

int
isfinite(real-floating x);

int
isinf(real-floating x);

int
isnan(real-floating x);

int
isnormal(real-floating x);
```

## 描述

`fpclassify` 宏接受参数 `x`，返回以下常量之一。

**`FP_INFINITE`** 表示 `x` 是一个无穷大数。

**`FP_NAN`** 表示 `x` 不是一个数（NaN）。

**`FP_NORMAL`** 表示 `x` 是一个规格化数。

**`FP_SUBNORMAL`** 表示 `x` 是一个非规格化数。

**`FP_ZERO`** 表示 `x` 为零（0 或 -0）。

`isfinite` 宏当且仅当其参数为有限值（零、次规格化数或规格化数）时返回非零值。`isinf`、`isnan` 和 `isnormal` 宏当且仅当 `x` 分别为无穷大、NaN 或非零规格化数时返回非零值。

`isnanf` 符号作为 `isnan` 的别名提供以保持兼容性，其使用已弃用。类似地，`finite` 和 `finitef` 是 `isfinite` 的弃用版本。

## 参见

[isgreater(3)](isgreater.3.md), math(3), signbit(3)

## 标准

`fpclassify`、`isfinite`、`isinf`、`isnan` 和 `isnormal` 宏遵循 ISO/IEC 9899:1999（"ISO C99"）标准。

## 历史

`fpclassify`、`isfinite`、`isinf`、`isnan` 和 `isnormal` 宏添加于 FreeBSD 5.1。3BSD 引入了 `isinf` 和 `isnan` 函数，接受 `double` 参数；上述宏取代了这些函数。
