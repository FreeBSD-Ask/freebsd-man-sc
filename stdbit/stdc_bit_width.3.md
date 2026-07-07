# stdc_bit_width(3)

`stdc_bit_width` — 查找表示整数所需的位数

## 名称

`stdc_bit_width`

## 概要

`Lb libc`

```c
#include <stdbit.h>
```

```c
unsigned int stdc_bit_width_uc(unsigned char value);
unsigned int stdc_bit_width_us(unsigned short value);
unsigned int stdc_bit_width_ui(unsigned int value);
unsigned int stdc_bit_width_ul(unsigned long value);
unsigned int stdc_bit_width_ull(unsigned long long value);
unsigned int stdc_bit_width(value);
```

## 描述

`stdc_bit_width_`*type*() 函数族返回表示 `value` 所需的位数，其中 `value` 的类型分别为 `unsigned char`、`unsigned short`、`unsigned int`、`unsigned long` 或 `unsigned long long`，对应 *type* 为 **uc**、**us**、**ui**、**ul** 或 **ull**。类型通用宏 `stdc_bit_width`(*value*) 根据 `value` 的类型选择适当的 `stdc_bit_width_`*type*() 函数。

函数 `stdc_bit_width_ui`、`stdc_bit_width_ul` 和 `stdc_bit_width_ull` 分别与 4.3BSD 的 fls(3)、flsl(3) 和 flsll(3) 函数相同，只是操作的是无符号值而非有符号值。

## 返回值

返回表示 `value` 所需的最少位数。如果 `value` 为零，则返回值为零。否则为 1 + log₂(`value`)。

## 参见

bit_fls(3), fls(3), flsl(3), flsll(3), [stdbit(3)](../man3/stdbit.3.md), stdc_count_leading_zeros(3), [stdc_first_leading_one(3)](stdc_first_leading_one.3.md)

## 标准

`stdc_bit_width_`*type*() 函数族和 `stdc_bit_width` 类型通用宏遵循 -isoC-2023 标准。

## 历史

`stdc_bit_width_`*type*() 函数族和 `stdc_bit_width` 类型通用宏在 FreeBSD 15.1 中添加。

## 作者

Robert Clausecker <fuz@FreeBSD.org>
