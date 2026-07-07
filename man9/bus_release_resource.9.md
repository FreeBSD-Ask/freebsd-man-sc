# bus_release_resource(9)

`bus_release_resource` — 释放总线上的资源

## 名称

`bus_release_resource`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <machine/bus.h>
#include <sys/rman.h>
#include <machine/resource.h>

int
bus_release_resource(device_t dev, struct resource *r)
```

## 描述

释放由 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 分配的资源。释放时资源必须不在使用中，即之前要调用适当的函数（例如对于 IRQ 调用 bus_teardown_intr(9)）。

- `dev` 是拥有资源的设备。
- `r` 是指向 `struct resource` 的指针，即 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 返回的资源本身。

## 返回值

如果设备 `dev` 没有父设备，返回 `EINVAL`，否则返回 `0`。如果无法释放资源，内核将 panic。

## 实例

```c
	/* 停用 IRQ */
	bus_teardown_intr(dev, foosoftc->irqres, foosoftc->irqid);
	/* 释放 IRQ 资源 */
	bus_release_resource(dev, foosoftc->irqres);
	/* 释放 I/O 端口资源 */
	bus_release_resource(dev, foosoftc->portres);
```

## 参见

[bus_alloc_resource(9)](bus_alloc_resource.9.md), [device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Alexander Langer <alex@big.endian.de> 编写。
