# isgreater(3)

`isgreater` — 比较两个浮点数

## 名称

`isgreater`, `islessgreater`

## 库

Lb libc

## 概要

`#include <math.h>`

```c
int
isgreater(real-floating x, real-floating y);

int
isgreaterequal(real-floating x, real-floating y);

int
isless(real-floating x, real-floating y);

int
islessequal(real-floating x, real-floating y);

int
islessgreater(real-floating x, real-floating y);

int
isunordered(real-floating x, real-floating y);
```

## 描述

`isgreater`、`isgreaterequal`、`isless`、`islessequal` 和 `islessgreater` 宏接受参数 `x` 和 `y`，当且仅当 `x` 和 `y` 之间的名义关系成立时返回非零值。如果任一参数为 NaN（非数），这些宏始终返回零，但与对应的 C 运算符不同，它们不会引发浮点异常。

`isunordered` 宏接受参数 `x` 和 `y`，当且仅当 `x` 或 `y` 中任一为 NaN 时返回非零值。对于任意一对浮点数值，四种关系（小于、大于、等于、无序）中必有一种成立。

## 参见

[fpclassify(3)](fpclassify.3.md), math(3), signbit(3)

## 标准

`isgreater`、`isgreaterequal`、`isless`、`islessequal`、`islessgreater` 和 `isunordered` 宏遵循 ISO/IEC 9899:1999（"ISO C99"）标准。

## 历史

上述关系宏首次出现于 FreeBSD 5.1。
