# BUS_ADD_CHILD.9

`BUS_ADD_CHILD` — 以给定优先级向设备树添加设备节点

## 名称

`BUS_ADD_CHILD`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
device_t
BUS_ADD_CHILD(device_t dev, int order, const char *name,
    int unit)
```

## 描述

`BUS_ADD_CHILD` 方法由驱动程序的 identify 例程使用，用于向设备树添加设备。它也可用于在其他上下文中向实现了此例程的总线添加子设备，但其行为因总线而异。详见 [device_add_child(9)](device_add_child.9.md)。其接口与 [device_add_child(9)](device_add_child.9.md) 相同，但调用的是总线的 `BUS_ADD_CHILD` 方法。

实现 `BUS_ADD_CHILD` 的总线应使用 [device_add_child(9)](device_add_child.9.md) 将设备插入设备树，然后再向该设备添加诸如自身的实例变量和资源列表等内容。[device_add_child(9)](device_add_child.9.md) 不会调用 `BUS_ADD_CHILD`。相反，`BUS_ADD_CHILD` 会调用 [device_add_child(9)](device_add_child.9.md)。

对未实现 `BUS_ADD_CHILD` 的总线调用此方法将导致 panic。某些总线需要调用特定的总线专用例程，而非 `BUS_ADD_CHILD`。

## 返回值

`BUS_ADD_CHILD` 方法返回添加到设备树的 `device_t`，或返回 `NULL` 表示失败。

## 参见

[device(9)](device.9.md), [device_add_child(9)](device_add_child.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 M. Warner Losh 编写。
