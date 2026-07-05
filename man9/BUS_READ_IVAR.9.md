# BUS_READ_IVAR.9

`BUS_READ_IVAR` — 操作总线特定的设备实例变量

## 名称

`BUS_READ_IVAR`, `BUS_WRITE_IVAR`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
int
BUS_READ_IVAR(device_t dev, device_t child, int index,
    uintptr_t *result);

int
BUS_WRITE_IVAR(device_t dev, device_t child, int index,
    uintptr_t value);
```

## 描述

这两个方法管理子设备的总线特定实例变量集合。其设计意图是每种不同类型的总线定义一组适当的实例变量（例如 ISA 总线的端口和 IRQ 等）。

这些信息可以作为结构体传递给子设备，但这使得总线难以在不强制编辑和重新编译所有驱动程序的情况下添加或删除变量，而对于厂商提供的二进制驱动程序来说，这可能无法实现。

## 返回值

成功时返回零，否则返回适当的错误码。

## 参见

[device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Doug Rabson 编写。
