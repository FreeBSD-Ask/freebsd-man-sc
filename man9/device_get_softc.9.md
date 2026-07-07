# device_get_softc(9)

`device_get_softc` — 访问驱动程序私有实例变量

## 名称

`device_get_softc`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

void *
device_get_softc(device_t dev);
```

## 描述

返回 `dev` 的驱动程序特定软件上下文（softc）。softc 在设备 attach 时自动分配并清零。在设备 probe 时 softc 也会被初始化并存在，但需遵守 [DEVICE_PROBE(9)](device_probe.9.md) 中所述的注意事项。分配的大小由定义驱动程序时所用的设备 `driver_t` 信息决定。softc 通常封装了该设备实例的状态。

不鼓励驱动程序作者使用自己的 softc 管理机制。驱动程序作者不应复制源码树中早于此函数的驱动程序中的此类机制。

## 返回值

返回指向驱动程序特定实例变量的指针。

## 参见

[device(9)](device.9.md), [DEVICE_PROBE(9)](device_probe.9.md), device_set_softc(9), [driver(9)](driver.9.md)

## 作者

本手册页由 Doug Rabson 编写。
