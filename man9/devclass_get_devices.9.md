# devclass_get_devices.9

`devclass_get_devices` — 获取 devclass 中的设备列表

## 名称

`devclass_get_devices`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
devclass_get_devices(devclass_t dc, device_t **devlistp, int *devcountp)
```

## 描述

检索当前在 devclass 中的所有设备实例的列表，并在 `*devlistp` 中返回该列表，在 `*devcountp` 中返回计数。为该列表分配的内存应使用 `free(*devlistp, M_TEMP)` 释放，即使 `*devcountp` 为 0。

## 返回值

成功时返回零，否则返回适当的错误。

## 参见

[devclass(9)](devclass.9.md), [device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
