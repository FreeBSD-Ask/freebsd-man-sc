# ffs(3)

`ffs` — 在位串中查找首个或最后一个被置位的位

## 名称

`ffs`, `ffsl`, `ffsll`, `fls`, `flsl`, `flsll`

## 库

Lb libc

## 概要

`#include <strings.h>`

```c
int
ffs(int value);

int
ffsl(long value);

int
ffsll(long long value);

int
fls(int value);

int
flsl(long value);

int
flsll(long long value);
```

## 描述

`ffs`、`ffsl` 和 `ffsll` 函数查找 `value` 中首个（最低有效位）被置位的位，并返回该位的索引。

`fls`、`flsl` 和 `flsll` 函数查找 `value` 中最后一个（最高有效位）被置位的位，并返回该位的索引。

位的编号从 1 开始，即最低有效位。这些函数中任何一个返回零都表示参数为零。

## 参见

bitstring(3), stdc_first_trailing_one(3), stdc_trailing_zeros(3), bitset(9)

## 标准

`ffs` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。`ffsl` 和 `ffsll` 函数遵循 -p1003.1-2024。

## 历史

`ffs` 函数出现于 4.3BSD。其原型原先位于 `#include <string.h>` 中，后为遵循 IEEE Std 1003.1-2001 ("POSIX.1") 而移至 `#include <strings.h>`。

`ffsl`、`fls` 和 `flsl` 函数出现于 FreeBSD 5.3。`ffsll` 和 `flsll` 函数出现于 FreeBSD 7.1。
