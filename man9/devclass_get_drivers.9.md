# devclass_get_drivers.9

`devclass_get_drivers` — 获取 devclass 中的驱动程序列表

## 名称

`devclass_get_drivers`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
devclass_get_drivers(devclass_t dc, driver_t ***listp, int *countp)
```

## 描述

检索当前在 devclass 中的所有驱动程序实例的指针列表，并在 `*listp` 中返回该列表，在 `*countp` 中返回列表中的驱动程序数量。为该列表分配的内存应使用 `free(*listp, M_TEMP)` 释放，即使 `*countp` 为 0。

## 返回值

成功时返回零，否则返回适当的错误。

## 参见

[devclass(9)](devclass.9.md), [device(9)](device.9.md)

## 作者

本手册页由 Nate Lawson 编写。
