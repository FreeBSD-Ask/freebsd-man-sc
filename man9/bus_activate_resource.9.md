# bus_activate_resource(9)

`bus_activate_resource` — 激活或停用资源

## 名称

`bus_activate_resource`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <machine/bus.h>
#include <sys/rman.h>
#include <machine/resource.h>

int
bus_activate_resource(device_t dev, struct resource *r)

int
bus_deactivate_resource(device_t dev, struct resource *r)
```

## 描述

这些函数激活或停用先前分配的资源。通常，资源在驱动程序访问之前必须激活。总线驱动程序可能执行额外操作以确保资源准备就绪可供访问。例如，PCI 总线驱动程序在激活内存资源时启用 PCI 设备命令寄存器中的内存解码。

参数如下：

**`dev`** 请求资源所有权的设备。分配前，资源由父总线拥有。

**`r`** 指向 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 返回的 `struct resource` 的指针。

### 资源映射

可由 [bus_space(9)](bus_space.9.md) 标签和句柄映射供 CPU 访问的资源在激活时将创建整个资源的映射。此映射的标签和句柄存储在 `r` 中，可通过 rman_get_bustag(9) 和 rman_get_bushandle(9) 检索。这些可与 [bus_space(9)](bus_space.9.md) API 一起使用，以访问 `r` 描述的设备寄存器或内存。如果映射与虚拟地址关联，可通过 rman_get_virtual(9) 检索该虚拟地址。

可通过向 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 传递 `RF_UNMAPPED` 标志禁用此隐式映射。如果驱动程序希望使用 [bus_map_resource(9)](bus_map_resource.9.md) 分配自己的资源映射，可使用此标志。

还提供了 [bus_space(9)](bus_space.9.md) 的包装 API，接受关联资源作为第一个参数以替代 [bus_space(9)](bus_space.9.md) 标签和句柄。此包装 API 中的函数命名与 [bus_space(9)](bus_space.9.md) API 类似，只是名称中移除了"_space"。例如，`bus_read_4` 可替代 `bus_space_read_4` 使用。新驱动程序中推荐使用包装 API。

以下两条语句都读取资源起始处的 32 位寄存器：

```c
	bus_space_read_4(rman_get_bustag(res), rman_get_bushandle(res), 0);
	bus_read_4(res, 0);
```

## 返回值

成功时返回零，否则返回错误。

## 参见

[bus_alloc_resource(9)](bus_alloc_resource.9.md), [bus_map_resource(9)](bus_map_resource.9.md), [bus_space(9)](bus_space.9.md), [device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Warner Losh <imp@FreeBSD.org> 编写。
