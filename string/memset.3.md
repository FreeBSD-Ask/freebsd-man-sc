# memset(3)

`memset` — 设置内存中的字节

## 名称

`memset`

## 库

Lb libc

## 概要

`#include <string.h>`

```c
void *
memset(void *dest, int c, size_t len);

void *
memset_explicit(void *dest, int c, size_t len);
```

```c
#define __STDC_WANT_LIB_EXT1__ 1
#include <string.h>
errno_t
memset_s(void *dest, rsize_t destsz, int c, rsize_t len);
```

## 描述

`memset` 函数向对象 `dest` 写入 `len` 个字节，每个字节的值为 `c`（转换为 `unsigned char`）。若 `len` 大于 `dest` 缓冲区的长度，`memset` 将因存储溢出而产生未定义行为。若 `dest` 是无效指针，行为也未定义。

`memset_explicit` 函数的行为与 `memset` 相同，但不会被编译器的死存储优化（dead store optimization）移除，适用于清除密码等敏感内存。

`memset_s` 函数的行为与 `memset` 相同，区别在于：若 `dest` 是空指针、`destsz` 或 `len` 大于 `RSIZE_MAX`、或 `len` 大于 `destsz`（将发生缓冲区溢出），则返回错误并调用当前注册的运行时约束处理器（runtime-constraint handler）。首先调用运行时约束处理器，该处理器可能不返回。若处理器返回，则向调用者返回错误。与 explicit_bzero(3) 类似，`memset_s` 不会通过死存储消除（Dead Store Elimination, DSE）被移除，适用于清除敏感数据。相反，若函数修改的对象之后不再被访问，`memset` 函数可能被优化掉。对于之后不再访问的内存，建议使用 `memset_s` 而非 `memset` 进行清除。例如，包含密码的缓冲区在 free(3) 之前应使用 `memset_s` 清除。

## 返回值

`memset` 和 `memset_explicit` 函数返回其第一个参数。`memset_s` 函数成功时返回零，出错时返回非零值。

## 参见

[bzero(3)](bzero.3.md), explicit_bzero(3), set_constraint_handler_s(3), [swab(3)](swab.3.md), wmemset(3)

## 标准

`memset` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`memset_s` 遵循 ISO/IEC 9899:2011 ("ISO C11") K.3.7.4.1。`memset_explicit` 遵循 ISO/IEC 9899:2023 ("ISO C23")。
