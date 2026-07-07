# bus_map_resource(9)

`bus_map_resource` — 映射或取消映射活动资源

## 名称

`bus_map_resource`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <machine/bus.h>
#include <sys/rman.h>
#include <machine/resource.h>

int
bus_map_resource(device_t dev, struct resource *r,
    struct resource_map_request *args, struct resource_map *map)

int
bus_unmap_resource(device_t dev, struct resource *r,
    struct resource_map *map)

void
resource_init_map_request(struct resource_map_request *args)
```

## 描述

这些函数创建或销毁先前激活资源的映射。映射允许 CPU 通过 [bus_space(9)](bus_space.9.md) API 访问资源。

参数如下：

**`dev`** 拥有资源的设备。

**`r`** 指向 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 返回的 `struct resource` 的指针。

**`args`** 创建映射时要应用的一组可选属性。此参数可设置为 `NULL` 以请求使用默认属性映射整个资源。

**`map`** 要创建或销毁的资源映射。

### 资源映射

资源映射由 `struct resource_map` 对象描述。此结构在 `r_bustag` 和 `r_bushandle` 成员中包含 [bus_space(9)](bus_space.9.md) 标签和句柄，可用于 CPU 访问映射。此结构还包含 `r_vaddr` 成员，如果存在虚拟地址，则包含映射的虚拟地址。

[bus_activate_resource(9)](bus_activate_resource.9.md) 中描述的 `struct resource` 对象包装 API 也可与 `struct resource_map` 一起使用。例如，指向映射对象的指针可作为 `bus_read_4` 的第一个参数传递。此包装 API 优于直接使用 `r_bustag` 和 `r_bushandle` 成员。

### 可选映射属性

在 `args` 中传递的 `struct resource_map_request` 对象可用于指定映射的可选属性。此结构必须通过调用 `resource_init_map_request` 初始化。然后通过设置以下一个或多个成员指定属性：

**`offset`, `length`** 这两个成员指定要映射的资源区域。默认情况下，为整个资源创建映射。`offset` 相对于资源起始位置。

**`memattr`** 指定映射资源时要使用的内存属性。默认情况下，内存映射使用 `VM_MEMATTR_UNCACHEABLE` 属性。

## 返回值

成功时返回零，否则返回错误。

## 实例

以下代码使用写组合内存属性映射 PCI 内存 BAR 并读取第一个 32 位字：

```c
	struct resource *r;
	struct resource_map map;
	struct resource_map_request req;
	uint32_t val;
	int rid;
	rid = PCIR_BAR(0);
	r = bus_alloc_resource_any(dev, SYS_RES_MEMORY, &rid, RF_ACTIVE |
	    RF_UNMAPPED);
	resource_init_map_request(&req);
	req.memattr = VM_MEMATTR_WRITE_COMBINING;
	bus_map_resource(dev, SYS_RES_MEMORY, r, &req, &map);
	val = bus_read_4(&map, 0);
```

## 参见

[bus_activate_resource(9)](bus_activate_resource.9.md), [bus_alloc_resource(9)](bus_alloc_resource.9.md), [bus_space(9)](bus_space.9.md), [device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 John Baldwin <jhb@FreeBSD.org> 编写。
