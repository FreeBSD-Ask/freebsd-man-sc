# device_get_children.9

`device_get_children` — 检查连接到设备的子设备

## 名称

`device_get_children`, `device_has_children`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
device_get_children(device_t dev, device_t **devlistp, int *devcountp)

bool
device_has_children(device_t dev)
```

## 描述

`device_get_children` 函数检索当前连接到 `dev` 的所有设备实例的列表。它在 `*devlistp` 中返回该列表，在 `*devcountp` 中返回计数。为该列表分配的内存应使用 `free(*devlistp, M_TEMP)` 释放。返回错误时，`devlistp` 和 `devcountp` 不会改变。

作为特殊情况，如果 `devlistp` 为空，则不分配内存，但计数仍会在 `*devcountp` 中返回。

`device_has_children` 函数在 `dev` 至少有一个子设备时返回 `true`，没有子设备时返回 `false`。

## 返回值

`device_get_children` 函数成功时返回零，否则返回适当的错误。`device_has_children` 函数在指定设备至少有一个子设备时返回真，否则返回假。

## 参见

[devclass(9)](devclass.9.md), [device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson <dfr@FreeBSD.org> 和 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。
