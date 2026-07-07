# resource_int_value(9)

`resource_int_value` — 从提示机制获取值

## 名称

`resource_int_value`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/bus.h>
```

```c
int
resource_int_value(const char *name, int unit, const char *resname, int *result)

int
resource_long_value(const char *name, int unit, const char *resname, long *result)

int
resource_string_value(const char *name, int unit, const char *resname, const char **result)
```

## 描述

这些函数从“提示”（hints）机制中获取值。

这些函数接受以下参数：

**`name`** 要从中获取资源值的设备名称。

**`unit`** 设备的单元号。-1 是特殊值，用于通配符条目。

**`resname`** 资源名称。

**`result`** 指向用于存储资源值的内存的指针。

## 返回值

如果成功，函数返回 0。否则，返回非零错误代码。

## 错误

函数在以下情况下会失败：

**[`ENOENT`]** 找不到资源。

**[`EFTYPE`]** 资源类型不适当。

## 参见

[device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Warner Losh <imp@FreeBSD.org> 编写。
