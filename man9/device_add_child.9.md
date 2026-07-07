# device_add_child(9)

`device_add_child` — 将新设备作为现有设备的子设备添加

## 名称

`device_add_child`, `device_add_child_ordered`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

device_t
device_add_child(device_t dev, const char *name, int unit)

device_t
device_add_child_ordered(device_t dev, int order, const char *name,
    int unit)
```

## 描述

创建 `dev` 的新子设备。`name` 和 `unit` 参数指定设备的名称和单元号。如果名称未知，调用者应传递 `NULL`。如果单元号未知，调用者应传递 `DEVICE_UNIT_ANY`，系统将选择下一个可用的单元号。

设备的名称用于确定哪些驱动程序可能适合该设备。如果指定了名称，则仅探测该名称的驱动程序。如果未指定名称，则探测所属总线的所有驱动程序。无论哪种情况，仅存储设备的名称，以便可以安全地卸载/加载绑定到该名称的驱动程序。

这允许能够唯一标识设备实例的总线（如 PCI）允许每个驱动程序检查每个设备实例以寻找匹配。对于依赖所提供的探测提示、且只有一个驱动程序有机会探测设备的总线，应将驱动程序名称指定为设备名称。

通常单元号由系统自动选择，应给出 `DEVICE_UNIT_ANY` 的单元号。当需要特定的单元号时（例如，将特定硬件连接到预配置的单元号），应传递该单元号。如果指定的单元号已分配，将分配一个新单元号并打印诊断消息。

如果附加到总线的设备必须按特定顺序探测（例如，对于 ISA 总线，某些设备对不相关驱动程序的失败探测尝试敏感，因此必须先探测），应使用 `device_add_child_ordered` 的 `order` 参数指定部分排序。新设备将在任何具有更大顺序值的现有设备之前添加。如果使用 `device_add_child`，则新子设备的添加就像其顺序值为零一样。

在 [DEVICE_IDENTIFY(9)](device_identify.9.md) 例程的上下文中添加设备时，应使用 [device_find_child(9)](device_find_child.9.md) 例程来确保该设备尚未添加到树中。由于设备名称和 `devclass_t` 在探测时（而非子设备添加时）关联，驱动程序的先前实例（例如在后来卸载的模块中）可能已经添加了该实例。总线驱动程序的作者在加载和卸载时添加子设备时同样必须小心，以避免子设备重复。

将子设备添加到另一个设备节点时（例如在 identify 例程中），应使用 [BUS_ADD_CHILD(9)](bus_add_child.9.md) 而不是 `device_add_child`。[BUS_ADD_CHILD(9)](bus_add_child.9.md) 将调用 `device_add_child` 并向新子设备添加适当的总线特定数据。`device_add_child` 不会调用 [BUS_ADD_CHILD(9)](bus_add_child.9.md)。

## 返回值

成功时返回新设备，否则返回 NULL。

## 参见

[BUS_ADD_CHILD(9)](bus_add_child.9.md), [device(9)](device.9.md), [device_delete_child(9)](device_delete_child.9.md), [device_find_child(9)](device_find_child.9.md), [DEVICE_IDENTIFY(9)](device_identify.9.md)

## 作者

本手册页由 Doug Rabson 编写。
