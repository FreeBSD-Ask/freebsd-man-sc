# bus_generic_read_ivar(9)

`bus_generic_read_ivar` — 总线 `BUS_READ_IVAR` 和 `BUS_WRITE_IVAR` 的通用实现

## 名称

`bus_generic_read_ivar`, `bus_generic_write_ivar`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
bus_generic_read_ivar(device_t dev, device_t child, int index,
    uintptr_t *result)

int
bus_generic_write_ivar(device_t dev, device_t child, int index,
    uintptr_t value)
```

## 描述

这些函数仅返回 `ENOENT`。

## 参见

[device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Doug Rabson 编写。
