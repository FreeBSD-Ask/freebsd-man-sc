# bus_generic_detach.9

`bus_generic_detach` — 总线 `DEVICE_DETACH` 的通用实现

## 名称

`bus_generic_detach`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
bus_generic_detach(device_t dev)
```

## 描述

此函数提供 [DEVICE_DETACH(9)](DEVICE_DETACH.9.md) 方法的实现，可供大多数总线代码使用。它使用 bus_detach_children(9) 从所有子设备分离驱动程序，让它们有机会否决分离请求。如果 `bus_detach_children` 成功，`bus_generic_detach` 调用 [device_delete_children(9)](device_delete_children.9.md) 删除所有子设备。

## 返回值

成功时返回零，否则返回适当的错误。

## 参见

bus_detach_children(9), [device(9)](device.9.md), [device_delete_children(9)](device_delete_children.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Doug Rabson 编写。
