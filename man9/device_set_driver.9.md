# device_set_driver(9)

`device_set_driver` — 将特定驱动程序关联到树中的设备节点

## 名称

`device_set_driver`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

void
device_set_driver(device_t dev, driver_t *driver);
```

## 描述

此函数将特定驱动程序关联到树中的给定设备节点。它通常用于 [DEVICE_IDENTIFY(9)](device_identify.9.md) 函数中，以将设备添加到不支持自动添加的总线（如 ISA 总线）。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 M. Warner Losh 编写。
