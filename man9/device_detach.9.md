# DEVICE_DETACH.9

`DEVICE_DETACH` — 分离设备

## 名称

`DEVICE_DETACH`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
int
DEVICE_DETACH(device_t dev)
```

## 描述

分离设备。当用户正在替换驱动程序软件，或设备即将从系统中物理移除时，可以调用此方法。

此方法应释放在 [DEVICE_ATTACH(9)](DEVICE_ATTACH.9.md) 方法期间分配的所有系统资源，并将硬件重置为一致状态（即禁用中断等）。

## 返回值

成功时返回零，否则返回一个适当的错误。

## 参见

[device(9)](device.9.md), [DEVICE_ATTACH(9)](DEVICE_ATTACH.9.md), [DEVICE_IDENTIFY(9)](device_identify.9.md), [DEVICE_PROBE(9)](DEVICE_PROBE.9.md), [DEVICE_SHUTDOWN(9)](device_shutdown.9.md)

## 作者

本手册页由 Doug Rabson 编写。
