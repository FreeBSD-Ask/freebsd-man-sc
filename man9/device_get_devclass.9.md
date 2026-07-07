# device_get_devclass(9)

`device_get_devclass` — 访问设备的 devclass

## 名称

`device_get_devclass`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

devclass_t
device_get_devclass(device_t dev)
```

## 描述

返回与设备关联的当前 devclass。如果设备没有 devclass，则返回 `NULL`。

## 参见

[devclass(9)](devclass.9.md), [device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
