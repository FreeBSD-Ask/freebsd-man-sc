# stdc_first_trailing_zero(3)

`stdc_first_trailing_zero` — 查找整数中首个尾随 0

## 名称

`stdc_first_trailing_zero`

## 概要

`Lb libc`

```c
#include <stdbit.h>
```

```c
unsigned int stdc_first_trailing_zero_uc(unsigned char value);
unsigned int stdc_first_trailing_zero_us(unsigned short value);
unsigned int stdc_first_trailing_zero_ui(unsigned int value);
unsigned int stdc_first_trailing_zero_ul(unsigned long value);
unsigned int stdc_first_trailing_zero_ull(unsigned long long value);
unsigned int stdc_first_trailing_zero(value);
```

## 描述

`stdc_first_trailing_zero_`*type*() 函数族返回 `value` 中最低有效清 0 位的索引，其中 `value` 的类型分别为 `unsigned char`、`unsigned short`、`unsigned int`、`unsigned long` 或 `unsigned long long`，对应 *type* 为 **uc**、**us**、**ui**、**ul** 或 **ull**。类型通用宏 `stdc_first_trailing_zero`(*value*) 根据 `value` 的类型选择适当的 `stdc_first_trailing_zero_`*type*() 函数。

## 返回值

返回 `value` 中最低有效清 0 位的索引。位的编号方式为：最低有效位编号为 1，最高有效位编号为 w，其中 w 是 `value` 类型的位数。如果 `value` 中没有清 0 的位（即 `value` 是零的按位取反），则返回 0。

## 参见

bit_ffc(3), [stdbit(3)](stdbit.3.md), [stdc_trailing_ones(3)](stdc_trailing_ones.3.md), stdc_first_trailing_ones(3), [stdc_first_leading_zero(3)](stdc_first_leading_zero.3.md)

## 标准

`stdc_first_trailing_zero_`*type*() 函数族和 `stdc_first_trailing_zero` 类型通用宏遵循 -isoC-2023 标准。

## 历史

`stdc_first_trailing_zero_`*type*() 函数族和 `stdc_first_trailing_zero` 类型通用宏在 FreeBSD 15.1 中添加。

## 作者

Robert Clausecker <fuz@FreeBSD.org>
