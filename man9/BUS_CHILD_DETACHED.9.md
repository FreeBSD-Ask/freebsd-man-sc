# BUS_CHILD_DETACHED.9

`BUS_CHILD_DETACHED` — 通知总线设备子设备已分离

## 名称

`BUS_CHILD_DETACHED`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
void
BUS_CHILD_DETACHED(device_t dev, device_t child)
```

## 描述

`BUS_CHILD_DETACHED` 方法在设备被分离后，或驱动程序的 attach 例程（参见 [DEVICE_ATTACH(9)](device_attach.9.md)）失败时，由 new-bus 框架调用。总线驱动程序可以实现此方法，以回收代表子设备分配的资源，或清理未被 [DEVICE_DETACH(9)](device_detach.9.md) 方法正确释放的状态。

## 参见

[device(9)](device.9.md), [DEVICE_DETACH(9)](device_detach.9.md)
