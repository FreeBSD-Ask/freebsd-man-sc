# BUS_NEW_PASS(9)

`BUS_NEW_PASS` — 通知总线 pass 级别已更改

## 名称

`BUS_NEW_PASS`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
void
BUS_NEW_PASS(device_t dev)
```

## 描述

`BUS_NEW_PASS` 方法在 pass 级别更改时在每个总线设备上调用，以重新扫描设备树。此方法负责在子总线设备上调用 `BUS_NEW_PASS`，以将重新扫描传播到子设备。它还负责重新探测任何未附加的子设备，并允许当前 pass 的驱动程序识别新的子设备。默认实现由 [bus_generic_new_pass(9)](bus_generic_new_pass.9.md) 提供。

## 参见

[bus_generic_new_pass(9)](bus_generic_new_pass.9.md), [bus_set_pass(9)](bus_set_pass.9.md), [device(9)](device.9.md)
