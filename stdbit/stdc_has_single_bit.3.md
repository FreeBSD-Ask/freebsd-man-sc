# stdc_has_single_bit(3)

`stdc_has_single_bit` — 检查是否仅设置了一个位

## 名称

`stdc_has_single_bit`

## 概要

`Lb libc`

```c
#include <stdbit.h>
```

```c
bool stdc_has_single_bit_uc(unsigned char value);
bool stdc_has_single_bit_us(unsigned short value);
bool stdc_has_single_bit_ui(unsigned int value);
bool stdc_has_single_bit_ul(unsigned long value);
bool stdc_has_single_bit_ull(unsigned long long value);
bool stdc_has_single_bit(value);
```

## 描述

`stdc_has_single_bit_`*type*() 函数族检查 `value` 中是否恰好设置了一个位，其中 `value` 的类型分别为 `unsigned char`、`unsigned short`、`unsigned int`、`unsigned long` 或 `unsigned long long`，对应 *type* 为 **uc**、**us**、**ui**、**ul** 或 **ull**。类型通用宏 `stdc_has_single_bit`(*value*) 根据 `value` 的类型选择适当的 `stdc_has_single_bit_`*type*() 函数。

该函数族的行为与 `<sys/param.h>` 中 `powerof2`(*value*) 宏相似，但在 `value` 为零时有所不同：`powerof2` 认为零是 2 的幂，而 `stdc_has_single_bit` 不将零视为 2 的幂。

## 返回值

如果 `value` 中恰好设置了一个位，则返回 **true**，否则返回 **false**。即该函数判断 `value` 是否为 2 的幂。

## 参见

[stdbit(3)](../man3/stdbit.3.md), [stdc_count_ones(3)](stdc_count_ones.3.md)

## 标准

`stdc_has_single_bit_`*type*() 函数族和 `stdc_has_single_bit` 类型通用宏遵循 -isoC-2023 标准。

## 历史

`stdc_has_single_bit_`*type*() 函数族和 `stdc_has_single_bit` 类型通用宏在 FreeBSD 15.1 中添加。

## 作者

Robert Clausecker <fuz@FreeBSD.org>
