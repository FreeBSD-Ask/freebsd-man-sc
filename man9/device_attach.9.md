# DEVICE_ATTACH.9

`DEVICE_ATTACH` — 附加设备

## 名称

`DEVICE_ATTACH`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
int
DEVICE_ATTACH(device_t dev)
```

## 描述

在 `DEVICE_PROBE` 方法已被调用并指示设备存在之后，将设备附加到系统。`DEVICE_ATTACH` 方法应初始化硬件并分配其他系统资源（例如 [devfs(4)](../man4/devfs.4.md) 条目）。

实现总线的设备应使用此方法探测附加到该总线的设备是否存在，并将其作为子设备添加。如果与 [bus_attach_children(9)](bus_attach_children.9.md) 结合使用，子设备将被自动探测并附加。

## 返回值

成功时返回零，否则返回一个适当的错误。

## 参见

[devfs(4)](../man4/devfs.4.md), [bus_attach_children(9)](bus_attach_children.9.md), [device(9)](device.9.md), [DEVICE_DETACH(9)](device_detach.9.md), [DEVICE_IDENTIFY(9)](device_identify.9.md), [DEVICE_PROBE(9)](device_probe.9.md), [DEVICE_SHUTDOWN(9)](device_shutdown.9.md)

## 作者

本手册页由 Doug Rabson <dfr@FreeBSD.org> 编写。
