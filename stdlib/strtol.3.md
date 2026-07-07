# strtol(3)

`strtol`, `strtoll`, `strtoimax`, `strtoq` — 将字符串值转换为 `long`、`long long`、`intmax_t` 或 `quad_t` 整数

## 名称

`strtol`, `strtoll`, `strtoimax`, `strtoq`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

`#include <limits.h>`

```c
long
strtol(const char * restrict nptr, char ** restrict endptr, int base);
long long
strtoll(const char * restrict nptr, char ** restrict endptr, int base);
```

`#include <inttypes.h>`

```c
intmax_t
strtoimax(const char * restrict nptr, char ** restrict endptr, int base);
```

`#include <sys/types.h>`

`#include <stdlib.h>`

`#include <limits.h>`

```c
quad_t
strtoq(const char *nptr, char **endptr, int base);
```

## 描述

`strtol` 函数将 `nptr` 中的字符串转换为 `long` 值。`strtoll` 函数将 `nptr` 中的字符串转换为 `long long` 值。`strtoimax` 函数将 `nptr` 中的字符串转换为 `intmax_t` 值。`strtoq` 函数将 `nptr` 中的字符串转换为 `quad_t` 值。转换按给定的 `base` 进行，`base` 必须在 2 到 36 之间（含边界），或为特殊值 0。

字符串可以以任意数量的空白字符（由 [isspace(3)](../locale/isspace.3.md) 判定）开头，后跟一个可选的 `+` 或 `-` 符号。若 `base` 为零或 16，字符串随后可包含 `0b` 前缀，此时数字按二进制读取；或可包含 `0x` 前缀，此时数字按十六进制读取；否则，零 `base` 被当作 10（十进制），除非下一个字符是 `0`，此时被当作 8（八进制）。

字符串的其余部分以通常方式转换为 `long`、`long long`、`intmax_t` 或 `quad_t` 值，在给定进制中不是有效数字的第一个字符处停止。（在大于 10 的进制中，字母 `A` 无论是大写还是小写都表示 10，`B` 表示 11，依此类推，`Z` 表示 35。）

若 `endptr` 不为 `NULL`，`strtol` 将第一个无效字符的地址存入 `*endptr`。但若根本没有数字，`strtol` 将 `nptr` 的原始值存入 `*endptr`。（因此，若 `*nptr` 不是 `\0` 但返回时 `**endptr` 是 `\0`，则整个字符串都是有效的。）

## 返回值

`strtol`、`strtoll`、`strtoimax` 和 `strtoq` 函数返回转换结果，除非该值会导致下溢或上溢。若无法执行转换，返回 0，并将全局变量 `errno` 设置为 `EINVAL`（后一特性在所有平台上不可移植）。若发生上溢或下溢，`errno` 设置为 `ERANGE`，函数返回值按下表进行钳制。

| **函数** | **下溢** | **上溢** |
| -------- | -------- | -------- |
| `strtol` | `LONG_MIN` | `LONG_MAX` |
| `strtoll` | `LLONG_MIN` | `LLONG_MAX` |
| `strtoimax` | `INTMAX_MIN` | `INTMAX_MAX` |
| `strtoq` | `LLONG_MIN` | `LLONG_MAX` |

## 错误

**[`EINVAL`]** `base` 的值不受支持，或无法执行转换（后一特性在所有平台上不可移植）。

**[`ERANGE`]** 给定的字符串超出范围；转换的值已被钳制。

## 参见

[atof(3)](atof.3.md), [atoi(3)](atoi.3.md), [atol(3)](atol.3.md), [strtod(3)](strtod.3.md), [strtonum(3)](strtonum.3.md), [strtoul(3)](strtoul.3.md), [wcstol(3)](../locale/wcstol.3.md)

## 标准

`strtol` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`strtoll` 和 `strtoimax` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。BSD 的 `strtoq` 函数已弃用。
