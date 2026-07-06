# bus_generic_shutdown.9

`bus_generic_shutdown` — 总线 `DEVICE_SHUTDOWN` 的通用实现

## 名称

`bus_generic_shutdown`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
bus_generic_shutdown(device_t dev)
```

## 描述

此函数提供 [DEVICE_SHUTDOWN(9)](DEVICE_SHUTDOWN.9.md) 方法的实现，可供大多数总线代码使用。它简单地调用附加到总线的每个子设备的 [DEVICE_SHUTDOWN(9)](DEVICE_SHUTDOWN.9.md) 方法。

## 返回值

成功时返回零，否则返回适当的错误。

## 参见

[device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Doug Rabson 编写。
