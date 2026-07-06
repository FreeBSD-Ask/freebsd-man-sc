# bus_generic_new_pass.9

`bus_generic_new_pass` — 总线设备 BUS_NEW_PASS 的通用实现

## 名称

`bus_generic_new_pass`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

void
bus_generic_new_pass(device_t dev)
```

## 描述

此函数提供 [BUS_NEW_PASS(9)](BUS_NEW_PASS.9.md) 方法的实现，可供总线驱动程序使用。它首先为 pass 级别等于新 pass 级别的任何驱动程序调用 [DEVICE_IDENTIFY(9)](DEVICE_IDENTIFY.9.md) 方法。然后，对于每个已附加的子设备，调用 [BUS_NEW_PASS(9)](BUS_NEW_PASS.9.md) 重新扫描子总线；对于每个未附加的子设备，调用 [device_probe_and_attach(9)](device_probe_and_attach.9.md)。

## 参见

[BUS_NEW_PASS(9)](BUS_NEW_PASS.9.md), [bus_set_pass(9)](bus_set_pass.9.md), [device(9)](device.9.md), [DEVICE_IDENTIFY(9)](DEVICE_IDENTIFY.9.md)
