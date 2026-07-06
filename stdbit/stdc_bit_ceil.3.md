# stdc_bit_ceil(3)

`stdc_bit_ceil` — 向上取整到下一个 2 的幂

## 名称

`stdc_bit_ceil`

## 概要

`Lb libc`

```c
#include <stdbit.h>
```

```c
unsigned char stdc_bit_ceil_uc(unsigned char value);
unsigned short stdc_bit_ceil_us(unsigned short value);
unsigned int stdc_bit_ceil_ui(unsigned int value);
unsigned long stdc_bit_ceil_ul(unsigned long value);
unsigned long long stdc_bit_ceil_ull(unsigned long long value);
typeof(value) stdc_bit_ceil(value);
```

## 描述

`stdc_bit_ceil_`*type*() 函数族将 `value` 向上取整到下一个 2 的幂，其中 `value` 的类型分别为 `unsigned char`、`unsigned short`、`unsigned int`、`unsigned long` 或 `unsigned long long`，对应 *type* 为 **uc**、**us**、**ui**、**ul** 或 **ull**。类型通用宏 `stdc_bit_ceil`(*value*) 根据 `value` 的类型选择适当的 `stdc_bit_ceil_`*type*() 函数。

## 返回值

返回 `value` 向上取整到下一个 2 的幂的结果。如果该值无法表示，则返回 0。

## 参见

[stdbit(3)](stdbit.3.md), [stdc_bit_floor(3)](stdc_bit_floor.3.md)

## 标准

`stdc_bit_ceil_`*type*() 函数族和 `stdc_bit_ceil` 类型通用宏遵循 -isoC-2023 标准。

## 历史

`stdc_bit_ceil_`*type*() 函数族和 `stdc_bit_ceil` 类型通用宏在 FreeBSD 15.1 中添加。

## 作者

Robert Clausecker <fuz@FreeBSD.org>
