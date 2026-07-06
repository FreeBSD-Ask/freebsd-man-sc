# bus_get_resource.9

`bus_get_resource` — 读取具有给定资源 ID 的资源范围/值

## 名称

`bus_get_resource`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <sys/rman.h>

int
bus_get_resource(device_t dev, int type, int rid, rman_res_t *startp,
    rman_res_t *countp)
```

## 描述

`bus_get_resource` 函数读取资源 `type`、`rid` 对的范围或值，并将其存储在 `startp` 和 `countp` 参数中。

参数如下：

**`dev`** 要从中读取资源的设备。

**`type`** 要读取的资源类型。可以是以下之一：

- `SYS_RES_IRQ` 用于 IRQ
- `SYS_RES_DRQ` 用于 ISA DMA 线
- `SYS_RES_MEMORY` 用于 I/O 内存
- `SYS_RES_IOPORT` 用于 I/O 端口

**`rid`** 标识要读取的资源的总线特定句柄。

**`startp`** 指向此资源起始地址的指针。

**`countp`** 指向资源长度的指针。例如，内存的大小（以字节为单位）。

## 返回值

成功时返回零，否则返回错误。

## 参见

[bus_set_resource(9)](bus_set_resource.9.md), [device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Sascha Wildner 编写。
