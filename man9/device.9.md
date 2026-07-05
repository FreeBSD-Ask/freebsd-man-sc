# device.9

`device` — 设备的抽象表示

## 名称

`device`

## 概要

```c
typedef struct _device *device_t;
```

## 描述

设备对象表示连接到系统的一件硬件，例如扩展卡、该卡所插入的总线、连接到该扩展卡的磁盘驱动器等。系统定义了一个设备 `root_bus`，所有其他设备都在自动配置期间动态创建。通常，代表系统中顶级总线（ISA、PCI 等）的设备将直接附加到 `root_bus`，而其他设备将作为其相关总线的子设备添加。

系统中的设备形成一棵树。除 `root_bus` 外的所有设备都有父设备（参见 [device_get_parent(9)](device_get_parent.9.md)）。此外，任何设备都可以有附加到其上的子设备（参见 [device_add_child(9)](device_add_child.9.md)、device_add_child_ordered(9)、[device_find_child(9)](device_find_child.9.md)、[device_get_children(9)](device_get_children.9.md) 和 [device_delete_child(9)](device_delete_child.9.md)）。

已成功探测并附加到系统的设备还将有一个驱动程序（参见 [device_get_driver(9)](device_get_driver.9.md) 和 [driver(9)](driver.9.md)）和一个 devclass（参见 [device_get_devclass(9)](device_get_devclass.9.md) 和 [devclass(9)](devclass.9.md)）。设备的其他各种属性包括单元号（参见 [device_get_unit(9)](device_get_unit.9.md)）、详细描述（通常由驱动程序提供，参见 [device_set_desc(9)](device_set_desc.9.md) 和 device_get_desc(9)）、一组总线特定的变量（参见 [device_get_ivars(9)](device_get_ivars.9.md)）以及一组驱动程序特定的变量（参见 [device_get_softc(9)](device_get_softc.9.md)）。

设备可以处于以下几种状态之一：

**`DS_NOTPRESENT`** 设备尚未探测存在性或探测失败

**`DS_ALIVE`** 设备探测成功但尚未附加

**`DS_ATTACHED`** 设备已成功附加

**`DS_BUSY`** 设备当前已打开

可以通过调用 [device_get_state(9)](device_get_state.9.md) 来确定设备的当前状态。

## 参见

[devclass(9)](devclass.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Doug Rabson 编写。
