# bus_set_resource.9

`bus_set_resource` — 将明确资源与给定资源 ID 关联

## 名称

`bus_set_resource`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <machine/bus.h>
#include <sys/rman.h>
#include <machine/resource.h>

int
bus_set_resource(device_t dev, int type, int rid, rman_res_t start,
    rman_res_t count)
```

## 描述

`bus_set_resource` 函数将资源 `type`、`rid` 对的起始地址设置为 `start`，长度为 `count`。通常，客户端驱动程序不使用此接口。但总线驱动程序经常使用它来设置客户端驱动程序使用的资源。

参数如下：

**`dev`** 要在其上设置资源的设备。

**`type`** 要分配的资源类型。可以是以下之一：

- `SYS_RES_IRQ` 用于 IRQ
- `SYS_RES_DRQ` 用于 ISA DMA 线
- `SYS_RES_IOPORT` 用于 I/O 端口
- `SYS_RES_MEMORY` 用于 I/O 内存

**`rid`** 标识要分配的资源的总线特定句柄。

**`start`** 此资源的起始地址。

**`count`** 资源的长度。例如，内存的大小（以字节为单位）。

## 返回值

成功时返回零，否则返回错误。

## 参见

[bus_alloc_resource(9)](bus_alloc_resource.9.md), [bus_get_resource(9)](bus_get_resource.9.md), [device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Warner Losh <imp@FreeBSD.org> 编写。
