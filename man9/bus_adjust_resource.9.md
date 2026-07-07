# bus_adjust_resource(9)

`bus_adjust_resource` — 调整从父总线分配的资源

## 名称

`bus_adjust_resource`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <machine/bus.h>
#include <sys/rman.h>
#include <machine/resource.h>

int
bus_adjust_resource(device_t dev, struct resource *r, rman_res_t start,
    rman_res_t end)
```

## 描述

此函数用于请求父总线调整分配给已分配资源的资源范围。资源 `r` 应由先前调用 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 分配。新的资源范围必须与 `r` 的现有范围重叠。

注意，`bus_adjust_resource` 不检查原始分配请求的任何约束，如对齐或边界限制。强制执行任何此类要求是调用者的责任。

## 返回值

`bus_adjust_resource` 方法成功时返回零，失败时返回错误代码。

## 实例

将现有内存资源扩展 4096 字节。

```c
	struct resource *res;
	int error;
	error = bus_adjust_resource(dev, res, rman_get_start(res),
	    rman_get_end(res) + 0x1000);
```

## 错误

`bus_adjust_resource` 在以下情况下失败：

**[`EINVAL`]** `dev` 设备没有父设备。

**[`EINVAL`]** `r` 资源是共享资源。

**[`EINVAL`]** 新地址范围与 `r` 的现有地址范围不重叠。

**[`EBUSY`]** 新地址范围与另一个已分配资源冲突。

## 参见

[bus_alloc_resource(9)](bus_alloc_resource.9.md), [bus_release_resource(9)](bus_release_resource.9.md), [device(9)](device.9.md), [driver(9)](driver.9.md)
