# bus_alloc_resource(9)

`bus_alloc_resource` — 从父总线分配资源

## 名称

`bus_alloc_resource`, `bus_alloc_resource_any`, `bus_alloc_resource_anywhere`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <machine/bus.h>
#include <sys/rman.h>
#include <machine/resource.h>

struct resource *
bus_alloc_resource(device_t dev, int type, int rid, rman_res_t start,
    rman_res_t end, rman_res_t count, u_int flags)

struct resource *
bus_alloc_resource_any(device_t dev, int type, int rid, u_int flags)

struct resource *
bus_alloc_resource_anywhere(device_t dev, int type, int rid,
    rman_res_t count, u_int flags)
```

## 描述

这是资源管理函数的简便接口。它隐藏了通过父方法表间接调用的过程。此函数通常应在 attach 中调用，但（除某些罕见情况外）绝不应在更早时调用。

`bus_alloc_resource_any` 和 `bus_alloc_resource_anywhere` 函数是 `bus_alloc_resource` 的便利包装器。`bus_alloc_resource_any` 将 `start`、`end` 和 `count` 设置为默认资源（参见下面对 `start` 的描述）。`bus_alloc_resource_anywhere` 将 `start` 和 `end` 设置为默认资源并使用提供的 `count` 参数。

参数如下：

- `dev` 是请求资源所有权的设备。分配前，资源由父总线拥有。
- `type` 是要分配的资源类型。可以是以下之一：
  - `PCI_RES_BUS` 用于 PCI 总线号
  - `SYS_RES_IRQ` 用于 IRQ
  - `SYS_RES_DRQ` 用于 ISA DMA 线
  - `SYS_RES_IOPORT` 用于 I/O 端口
  - `SYS_RES_MEMORY` 用于 I/O 内存
- `rid` 是标识要分配的资源的总线特定句柄。对于 ISA，这是由 PnP 机制或通过提示机制为此设备设置的资源数组的索引。对于 PCCARD，这是 PC Card 的 CIS 条目描述的资源数组的索引。对于 PCI，这是 PCI 配置空间中具有用于访问资源的 BAR 的偏移量。
- `start` 和 `end` 是资源的起始/结束地址。如果为 `start` 指定 0ul，为 `end` 指定 ~0ul，为 `count` 指定 1，则计算总线的默认值。
- `count` 是资源的大小。例如，I/O 端口的大小通常为 1 字节（但某些设备会覆盖此值）。如果为 `start` 和 `end` 指定了默认值，则当 `count` 小于默认值时使用总线的默认值，当 `count` 大于默认值时使用 `count`。
- `flags` 设置资源的标志。可以设置零个或多个以下标志：
  - `RF_ACTIVE` 原子地激活资源。
  - `RF_PREFETCHABLE` 资源可预取。
  - `RF_SHAREABLE` 资源允许同时共享。除非知道资源不能共享，否则应始终设置。如果总线不支持共享，总线驱动程序负责过滤掉此标志。
  - `RF_UNMAPPED` 通过 [bus_activate_resource(9)](bus_activate_resource.9.md) 激活时不建立隐式映射。

## 返回值

成功时返回指向 `struct resource` 的指针，否则返回空指针。

## 实例

以下是分配 32 字节 I/O 端口范围和 IRQ 的示例代码。

```c
	struct resource *portres, *irqres;
	portres = bus_alloc_resource(dev, SYS_RES_IOPORT, 0,
			0ul, ~0ul, 32, RF_ACTIVE);
	irqres = bus_alloc_resource_any(dev, SYS_RES_IRQ, 0,
			RF_ACTIVE | RF_SHAREABLE);
```

## 参见

[bus_activate_resource(9)](bus_activate_resource.9.md), [bus_adjust_resource(9)](bus_adjust_resource.9.md), [bus_map_resource(9)](bus_map_resource.9.md), [bus_release_resource(9)](bus_release_resource.9.md), [device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Alexander Langer <alex@big.endian.de> 编写，部分由 Warner Losh <imp@FreeBSD.org> 编写。
