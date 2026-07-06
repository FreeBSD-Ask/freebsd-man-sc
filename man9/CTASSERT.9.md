# CTASSERT.9

`CTASSERT` — 编译时断言宏

## 名称

`CTASSERT`

## 概要

```c
#include <sys/param.h>
#include <sys/systm.h>
```

```c
CTASSERT(expression);
```

## 描述

`CTASSERT` 宏已弃用，应使用 C11 标准的 `_Static_assert` 替代。应包含头文件 `sys/cdefs.h` 以提供对 C11 之前编译器的兼容性。

`CTASSERT` 宏在编译时评估 `expression`，如果为假则导致编译器错误。

`CTASSERT` 宏可用于在编译期间断言重要数据结构和变量的大小或对齐方式，否则这些问题只会在运行时导致代码失败。

## 实例

断言 `uuid` 结构的大小为 16 字节。

```c
CTASSERT(sizeof(struct uuid) == 16);
```

## 参见

[KASSERT(9)](kassert.9.md)

## 作者

本手册页由 Hiten M. Pandya <hmp@FreeBSD.org> 编写。
