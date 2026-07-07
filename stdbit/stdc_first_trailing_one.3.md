# stdc_first_trailing_one(3)

`stdc_first_trailing_one` — 查找整数中首个尾随 1

## 名称

`stdc_first_trailing_one`

## 概要

`Lb libc`

```c
#include <stdbit.h>
```

```c
unsigned int stdc_first_trailing_one_uc(unsigned char value);
unsigned int stdc_first_trailing_one_us(unsigned short value);
unsigned int stdc_first_trailing_one_ui(unsigned int value);
unsigned int stdc_first_trailing_one_ul(unsigned long value);
unsigned int stdc_first_trailing_one_ull(unsigned long long value);
unsigned int stdc_first_trailing_one(value);
```

## 描述

`stdc_first_trailing_one_`*type*() 函数族返回 `value` 中最低有效置 1 位的索引，其中 `value` 的类型分别为 `unsigned char`、`unsigned short`、`unsigned int`、`unsigned long` 或 `unsigned long long`，对应 *type* 为 **uc**、**us**、**ui**、**ul** 或 **ull**。类型通用宏 `stdc_first_trailing_one`(*value*) 根据 `value` 的类型选择适当的 `stdc_first_trailing_one_`*type*() 函数。

函数 `stdc_first_trailing_one_ui`、`stdc_first_trailing_one_ul` 和 `stdc_first_trailing_one_ull` 分别与 4.3BSD 的 ffs(3)、ffsl(3) 和 ffsll(3) 函数相同，只是操作的是无符号值而非有符号值。

## 返回值

返回 `value` 中最低有效置 1 位的索引。位的编号方式为：最低有效位编号为 1，最高有效位编号为 w，其中 w 是 `value` 类型的位数。如果 `value` 中没有置 1 的位（即 `value` 为零），则返回 1。

## 参见

bit_ffs(3), ffs(3), ffsl(3), ffsll(3), [stdbit(3)](../man3/stdbit.3.md), [stdc_trailing_zeros(3)](stdc_trailing_zeros.3.md), [stdc_first_trailing_zero(3)](stdc_first_trailing_zero.3.md), [stdc_first_leading_one(3)](stdc_first_leading_one.3.md)

## 标准

`stdc_first_trailing_one_`*type*() 函数族和 `stdc_first_trailing_one` 类型通用宏遵循 -isoC-2023 标准。

## 历史

`stdc_first_trailing_one_`*type*() 函数族和 `stdc_first_trailing_one` 类型通用宏在 FreeBSD 15.1 中添加。

## 作者

Robert Clausecker <fuz@FreeBSD.org>
