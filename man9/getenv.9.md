# getenv.9

`freeenv` — 内核环境变量函数

## 名称

`freeenv`, `kern_getenv`, `getenv_int`, `getenv_long`, `getenv_string`, `getenv_quad`, `getenv_uint`, `getenv_ulong`, `getenv_bool`, `getenv_is_true`, `getenv_is_false`, `kern_setenv`, `testenv`, `kern_unsetenv`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/systm.h>
```

```c
void
freeenv(char *env)
char *
kern_getenv(const char *name)
int
getenv_int(const char *name, int *data)
int
getenv_long(const char *name, long *data)
int
getenv_string(const char *name, char *data, int size)
int
getenv_quad(const char *name, quad_t *data)
int
getenv_uint(const char *name, unsigned int *data)
int
getenv_ulong(const char *name, unsigned long *data)
int
getenv_bool(const char *name, bool *data)
bool
getenv_is_true(const char *name)
bool
getenv_is_false(const char *name)
int
kern_setenv(const char *name, const char *value)
int
testenv(const char *name)
int
kern_unsetenv(const char *name)
```

## 描述

这些函数从内核环境中设置、取消设置、获取和解析变量。

`kern_getenv` 函数获取内核环境变量 `name` 的当前值，并返回指向字符串值的指针。调用者不应修改返回值指向的字符串。`kern_getenv` 函数可能分配临时存储空间，因此当 `kern_getenv` 返回的值不再需要时，必须调用 `freeenv` 函数释放任何分配的资源。

`freeenv` 函数用于释放先前调用 `kern_getenv` 分配的资源。`freeenv` 的 `env` 参数是先前调用 `kern_getenv` 返回的指针。与 free(3) 一样，`env` 参数可以为 `NULL`，此时不执行任何操作。

`kern_setenv` 函数将内核环境变量 `name` 插入或将其值重置为 `value`。如果变量 `name` 已存在，会替换其值。如果超出环境变量数量的内部限制，此函数可能失败。

`kern_unsetenv` 函数删除内核环境变量 `name`。

`testenv` 函数用于确定内核环境变量是否存在。如果变量 `name` 存在则返回非零值，不存在则返回零。

`getenv_int`、`getenv_long`、`getenv_quad`、`getenv_uint` 和 `getenv_ulong` 函数查找内核环境变量 `name`，并将其分别解析为有符号整数、长整数、有符号 64 位整数、无符号整数或无符号长整数。如果 `name` 不存在或其值中存在任何无效字符，这些函数失败并返回零。成功时，这些函数将解析的值存储在 `data` 所指向的整型变量中。如果解析的值溢出整数类型，截断的值存储在 `data` 中并返回零。如果值以“0x”前缀开头，则解释为十六进制。如果以“0”前缀开头，则解释为八进制。否则，值解释为十进制。值可包含指定值单位的单个字符后缀。解释的值在返回前乘以单位的量级。支持以下单位后缀：

| **单位** | **量级** |
| -------- | -------- |
| k | 2^10 |
| m | 2^20 |
| g | 2^30 |
| t | 2^40 |

`getenv_string` 函数将内核环境变量 `name` 的副本存储在由 `data` 和 `size` 描述的缓冲区中。如果变量不存在，返回零。如果变量存在，最多将其值的 `size - 1` 个字符复制到 `data` 所指向的缓冲区，后跟空字符，并返回非零值。

`getenv_bool` 函数通过与字符串“1”、“0”、“true”和“false”进行不区分大小写的比较，将内核环境变量 `name` 的值解释为布尔值。如果环境变量存在且具有有效的布尔值，则该值将被复制到 `data` 所指向的变量中。如果环境变量存在但不是布尔值，则将向内核消息缓冲区打印警告。`getenv_is_true` 和 `getenv_is_false` 函数是 `getenv_bool` 的包装，简化了对所需布尔值的测试。

## 返回值

`kern_getenv` 函数成功时返回指向环境变量值的指针，如果变量不存在则返回 `NULL`。

`kern_setenv` 和 `kern_unsetenv` 函数成功时返回零，失败时返回 -1。

`testenv` 函数在指定的环境变量不存在时返回零，存在时返回非零值。

`getenv_int`、`getenv_long`、`getenv_string`、`getenv_quad`、`getenv_uint`、`getenv_ulong` 和 `getenv_bool` 函数成功时返回非零值，失败时返回零。

`getenv_is_true` 和 `getenv_is_false` 函数在指定的环境变量存在且其值匹配所需的布尔条件时返回 `true`，否则返回 `false`。
