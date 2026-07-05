# stdbit.3

`stdbit` — 位与字节实用工具

## 名称

`stdbit`

## 概要

`Lb libc`

```c
#include <stdbit.h>
```

```c
#define __STDC_ENDIAN_LITTLE__
#define __STDC_ENDIAN_BIG__
#define __STDC_ENDIAN_NATIVE__

unsigned int stdc_count_leading_zeros(value);
unsigned int stdc_count_leading_ones(value);
unsigned int stdc_count_trailing_zeros(value);
unsigned int stdc_count_trailing_ones(value);
unsigned int stdc_first_leading_zero(value);
unsigned int stdc_first_leading_one(value);
unsigned int stdc_first_trailing_zero(value);
unsigned int stdc_first_trailing_one(value);
unsigned int stdc_count_zeros(value);
unsigned int stdc_count_ones(value);
bool stdc_has_single_bit(value);
unsigned int stdc_bit_width(value);
typeof(value) stdc_bit_floor(value);
typeof(value) stdc_bit_ceil(value);
```

## 描述

`__STDC_ENDIAN_NATIVE__` 宏描述了构建程序所针对的机器的字节序或端序。如果机器具有大端字节序，此宏等于 `__STDC_ENDIAN_BIG__`。如果机器具有小端字节序，此宏等于 `__STDC_ENDIAN_LITTLE__`。否则，该宏具有不等于两者的值。

位与字节实用函数分析数据内的位。每个函数 *func* 以五种变体提供：`stdc_`*func*`_`*type*(*value*)，其中 `value` 的类型分别为 `unsigned char`、`unsigned short`、`unsigned int`、`unsigned long` 或 `unsigned long long`，对应 *type* 为 **uc**、**us**、**ui**、**ul** 或 **ull**。此外，对于每个 *func*，提供一个类型通用宏 `stdc_`*func*(*value*)，根据 `value` 的类型选择适当的函数 `stdc_`*func*`_`*type*(*value*)。

## 参见

[arch(7)](../man7/arch.7.md), [bitstring(3)](bitstring.3.md), ffs(3), fls(3), stdc_count_leading_zeros(3), stdc_count_leading_ones(3), stdc_count_trailing_zeros(3), stdc_count_trailing_ones(3), stdc_first_leading_zero(3), stdc_first_leading_one(3), stdc_first_trailing_zero(3), stdc_first_trailing_one(3), stdc_count_zeros(3), stdc_count_ones(3), stdc_has_single_bit(3), stdc_bit_width(3), stdc_bit_floor(3), stdc_bit_ceil(3)

## 标准

```c
#include <stdbit.h>
```

头文件中的宏和函数遵循 -isoC-2023 标准。

## 历史

```c
#include <stdbit.h>
```

头文件及其定义的宏和函数在 FreeBSD 15.1 中添加。

## 作者

Robert Clausecker <fuz@FreeBSD.org>
