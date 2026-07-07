# BUS_PRINT_CHILD(9)

`BUS_PRINT_CHILD` — 打印设备信息

## 名称

`BUS_PRINT_CHILD`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
int
BUS_PRINT_CHILD(device_t dev, device_t child)
```

## 描述

`BUS_PRINT_CHILD` 方法由打印设备描述的系统代码调用。它应描述子设备与父设备的附加关系。例如，TurboLaser 总线会打印设备附加到哪个节点。关于 `BUS_PRINT_CHILD` 打印消息的正确格式，详见 [bus_generic_print_child(9)](bus_generic_print_child.9.md)。

## 返回值

返回输出的字符数。

## 参见

[device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Doug Rabson 编写。
