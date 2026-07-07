# devclass_get_device(9)

`devclass_get_device` — 将单元号转换为设备

## 名称

`devclass_get_device`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

device_t
devclass_get_device(devclass_t dc, int unit)
```

## 描述

此函数检索具有给定单元号的设备实例并返回它。

## 返回值

如果设备存在，则返回它，否则返回 NULL。

## 参见

[devclass(9)](devclass.9.md), [device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
