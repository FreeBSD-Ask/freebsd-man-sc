# bus_child_present(9)

`bus_child_present` — 询问总线驱动程序此设备是否仍然实际存在

## 名称

`bus_child_present`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <machine/bus.h>
#include <sys/rman.h>
#include <machine/resource.h>

int
bus_child_present(device_t dev)
```

## 描述

`bus_child_present` 函数请求 `dev` 的父设备驱动程序检查 `dev` 所代表的硬件此时是否仍然可以物理访问。虽然可访问的概念因总线而异，但通常不可访问的硬件无法通过 `bus_space*` 方法访问，而该方法原本用于访问设备。

这不询问"此设备是否有子设备？"的问题，该问题可通过 [device_get_children(9)](device_get_children.9.md) 更好地回答。

## 返回值

零返回值表示设备不在系统中。非零返回值表示设备在系统中，或者设备状态无法确定。

## 实例

以下是示例代码。仅在 [dc(4)](../man4/dc.4.md) 设备实际存在时才调用 stop。

```c
device_t dev;
dc_softc *sc;
sc = device_get_softc(dev);
if (bus_child_present(dev))
	dc_stop(sc);
```

## 参见

[device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Warner Losh <imp@FreeBSD.org> 编写。
