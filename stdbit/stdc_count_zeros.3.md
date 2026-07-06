# stdc_count_zeros(3)

`stdc_count_zeros` — 统计整数中 0 的数量

## 名称

`stdc_count_zeros`

## 概要

`Lb libc`

```c
#include <stdbit.h>
```

```c
unsigned int stdc_count_zeros_uc(unsigned char value);
unsigned int stdc_count_zeros_us(unsigned short value);
unsigned int stdc_count_zeros_ui(unsigned int value);
unsigned int stdc_count_zeros_ul(unsigned long value);
unsigned int stdc_count_zeros_ull(unsigned long long value);
unsigned int stdc_count_zeros(value);
```

## 描述

`stdc_count_zeros_`*type*() 函数族返回 `value` 中置 0 的位数，其中 `value` 的类型分别为 `unsigned char`、`unsigned short`、`unsigned int`、`unsigned long` 或 `unsigned long long`，对应 *type* 为 **uc**、**us**、**ui**、**ul** 或 **ull**。此操作也称为 `value` 按位取反后的 "Hamming weight"。类型通用宏 `stdc_count_zeros`(*value*) 根据 `value` 的类型选择适当的 `stdc_count_zeros_`*type*() 函数。

## 返回值

返回 `value` 中置 0 的位数。

## 参见

[stdbit(3)](stdbit.3.md), [stdc_count_ones(3)](stdc_count_ones.3.md)

## 标准

`stdc_count_zeros_`*type*() 函数族和 `stdc_count_zeros` 类型通用宏遵循 -isoC-2023 标准。

## 历史

`stdc_count_zeros_`*type*() 函数族和 `stdc_count_zeros` 类型通用宏在 FreeBSD 15.1 中添加。

## 作者

Robert Clausecker <fuz@FreeBSD.org>
