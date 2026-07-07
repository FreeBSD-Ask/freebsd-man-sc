# device_set_flags(9)

`device_set_flags` — 操作驱动程序标志

## 名称

`device_set_flags`, `device_get_flags`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

void
device_set_flags(device_t dev, uint32_t flags);

uint32_t
device_get_flags(device_t dev);
```

## 描述

每个设备都支持一组依赖于驱动程序的标志，这些标志通常用于控制设备行为。通过调用 `device_get_flags` 读取这些标志，通过调用 `device_set_flags` 写入这些标志。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
