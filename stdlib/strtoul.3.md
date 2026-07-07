# strtoul(3)

`strtoul`, `strtoull`, `strtoumax`, `strtouq` — 将字符串转换为 `unsigned long`、`unsigned long long`、`uintmax_t` 或 `u_quad_t` 整数

## 名称

`strtoul`, `strtoull`, `strtoumax`, `strtouq`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

`#include <limits.h>`

```c
unsigned long
strtoul(const char * restrict nptr, char ** restrict endptr, int base);
unsigned long long
strtoull(const char * restrict nptr, char ** restrict endptr, int base);
```

`#include <inttypes.h>`

```c
uintmax_t
strtoumax(const char * restrict nptr, char ** restrict endptr, int base);
```

`#include <sys/types.h>`

`#include <stdlib.h>`

`#include <limits.h>`

```c
u_quad_t
strtouq(const char *nptr, char **endptr, int base);
```

## 描述

`strtoul` 函数将 `nptr` 中的字符串转换为 `unsigned long` 值。`strtoull` 函数将 `nptr` 中的字符串转换为 `unsigned long long` 值。`strtoumax` 函数将 `nptr` 中的字符串转换为 `uintmax_t` 值。`strtouq` 函数将 `nptr` 中的字符串转换为 `u_quad_t` 值。转换按给定的 `base` 进行，`base` 必须在 2 到 36 之间（含边界），或为特殊值 0。

字符串可以以任意数量的空白字符（由 [isspace(3)](../locale/isspace.3.md) 判定）开头，后跟一个可选的 `+` 或 `-` 符号。若 `base` 为零或 16，字符串随后可包含 `0b` 前缀，此时数字按二进制读取；或可包含 `0x` 前缀，此时数字按十六进制读取；否则，零 `base` 被当作 10（十进制），除非下一个字符是 `0`，此时被当作 8（八进制）。

字符串的其余部分以通常方式转换为 `unsigned long` 值，在字符串末尾或在给定进制中不产生有效数字的第一个字符处停止。（在大于 10 的进制中，字母 `A` 无论是大写还是小写都表示 10，`B` 表示 11，依此类推，`Z` 表示 35。）

若 `endptr` 不为 `NULL`，`strtoul` 将第一个无效字符的地址存入 `*endptr`。但若根本没有数字，`strtoul` 将 `nptr` 的原始值存入 `*endptr`。（因此，若 `*nptr` 不是 `\0` 但返回时 `**endptr` 是 `\0`，则整个字符串都是有效的。）

## 返回值

`strtoul`、`strtoull`、`strtoumax` 和 `strtouq` 函数返回转换结果；若存在前导减号，则返回转换结果的相反数，除非原始（未取反）值会导致上溢；在后一种情况下，`strtoul` 返回 `ULONG_MAX`，`strtoull` 返回 `ULLONG_MAX`，`strtoumax` 返回 `UINTMAX_MAX`，`strtouq` 返回 `ULLONG_MAX`。在所有这些情况下，`errno` 都被设置为 `ERANGE`。若无法执行转换，返回 0，并将全局变量 `errno` 设置为 `EINVAL`（后一特性在所有平台上不可移植）。

## 错误

**[`EINVAL`]** `base` 的值不受支持，或无法执行转换（后一特性在所有平台上不可移植）。

**[`ERANGE`]** 给定的字符串超出范围；转换的值已被钳制。

## 参见

[strtol(3)](strtol.3.md), [strtonum(3)](strtonum.3.md), wcstoul(3)

## 标准

`strtoul` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`strtoull` 和 `strtoumax` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。BSD 的 `strtouq` 函数已弃用。
