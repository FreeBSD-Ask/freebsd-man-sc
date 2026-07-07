# setmode(3)

`getmode` — 修改模式位

## 名称

`getmode`, `setmode`

## 库

Lb libc

## 概要

```c
#include <unistd.h>

mode_t
getmode(const void *set, mode_t mode);

void *
setmode(const char *mode_str);
```

## 描述

`getmode()` 函数返回 `mode` 文件权限位的副本，该副本由 `set` 所指向的值进行修改。虽然仅修改模式位，但文件模式的其他部分也可能被检查。

`setmode()` 函数接受一个绝对值（八进制）或符号值（如 [chmod(1)](../man1/chmod.1.md) 中所述）作为参数，并返回一个指向模式值的指针，该模式值将提供给 `getmode()`。由于某些符号值是相对于文件创建掩码的，`setmode()` 可能会调用 [umask(2)](../sys/umask.2.md)。如果发生这种情况，文件创建掩码将在 `setmode()` 返回之前恢复。如果调用程序在调用 `setmode()` 之后更改了其文件创建掩码的值，则必须再次调用 `setmode()`，`getmode()` 才能正确修改未来的文件模式。

如果传递给 `setmode()` 的模式无效，或无法为返回值分配内存，`setmode()` 返回 `NULL`。

从 `setmode()` 返回的值通过 `malloc()` 获得，当程序使用完毕后，应使用 `free()` 将其返还给系统，通常在调用 `getmode()` 之后。

## 错误

`setmode()` 函数可能失败并为 [malloc(3)](../stdlib/memory.3.md) 或 [strtol(3)](../stdlib/strtol.3.md) 库例程指定的任何错误设置 errno。此外，`setmode()` 将失败并将 `errno` 设置为：

**`[EINVAL]`** `mode` 参数不表示有效的模式。

## 参见

[chmod(1)](../man1/chmod.1.md), [stat(2)](../sys/stat.2.md), [umask(2)](../sys/umask.2.md), [malloc(3)](../stdlib/memory.3.md)

## 历史

`getmode()` 和 `setmode()` 函数首次出现在 4.4BSD 中。

## 缺陷

`setmode()` 函数不是线程安全的。在调用 `setmode()` 时，其他线程中创建的文件可能以 umask 0 创建。
