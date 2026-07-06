# bus_attach_children.9

`bus_attach_children` — 管理总线设备的子设备

## 名称

`bus_attach_children`, `bus_delayed_attach_children`, `bus_detach_children`, `bus_enumerate_hinted_children`, `bus_identify_children`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

void
bus_attach_children(device_t dev)

void
bus_delayed_attach_children(device_t bus)

int
bus_detach_children(device_t dev)

void
bus_enumerate_hinted_children(device_t bus)

void
bus_identify_children(device_t dev)
```

## 描述

这些函数管理 `dev` 的子设备的状态转换。

`bus_enumerate_hinted_children` 遍历内核环境以识别描述附加到 `dev` 的设备的任何设备提示。对于每组匹配的提示，调用 [BUS_HINTED_CHILD(9)](bus_hinted_child.9.md) 方法。此函数通常从总线驱动程序的 [DEVICE_ATTACH(9)](DEVICE_ATTACH.9.md) 方法中调用以添加提示设备。注意，大多数总线驱动程序不使用提示来识别子设备。这通常用于不提供设备枚举机制的旧式总线，如 ISA。

`bus_identify_children` 遍历 `dev` 子设备的所有合格设备驱动程序，调用 [DEVICE_IDENTIFY(9)](device_identify.9.md) 方法。这允许设备驱动程序添加通过替代机制（如固件表）枚举的子设备。此函数通常从总线驱动程序的 [DEVICE_ATTACH(9)](DEVICE_ATTACH.9.md) 方法中调用。

`bus_attach_children` 将设备驱动程序附加到 `dev` 的所有子设备。此函数在每个子设备上调用 [device_probe_and_attach(9)](device_probe_and_attach.9.md) 并忽略错误。它尽最大努力将设备驱动程序附加到所有子设备。子设备按递增顺序附加。具有相同顺序的子设备按通过 [device_add_child(9)](device_add_child.9.md) 创建设备时的 FIFO 顺序附加。此函数通常从总线驱动程序的 [DEVICE_ATTACH(9)](DEVICE_ATTACH.9.md) 方法中在添加设备后调用。

`bus_delayed_attach_children` 在中断启用后将设备驱动程序附加到 `dev` 的所有子设备。此函数通过 config_intrhook_establish(9) 在中断启用后调度调用 `bus_attach_children`。如果中断已启用（例如，启动后加载设备驱动程序时），立即调用 `bus_attach_children`。

`bus_detach_children` 通过在每个子设备上调用 device_detach(9) 从 `dev` 的所有子设备分离设备驱动程序。与 `bus_attach_children` 不同，此函数不进行尽力而为的遍历。如果子设备分离失败，`bus_detach_children` 立即失败并返回子设备分离失败的错误。子设备以与 `bus_attach_children` 相反的顺序分离。即，子设备按递减顺序分离，具有相同顺序的子设备按 LIFO 顺序分离。分离的设备不会被删除。

`bus_detach_children` 通常在总线驱动程序的 [DEVICE_DETACH(9)](DEVICE_DETACH.9.md) 方法开始时调用，让子设备有机会否决分离请求。它通常与稍后调用 `device_delete_children(9)` 删除子设备配对使用。如果两个函数调用之间不需要额外逻辑，总线驱动程序可以使用 [bus_generic_detach(9)](bus_generic_detach.9.md) 分离和删除子设备。

## 参见

config_intrhook_establish(9), [device_add_child(9)](device_add_child.9.md), [DEVICE_ATTACH(9)](DEVICE_ATTACH.9.md), [device_delete_children(9)](device_delete_children.9.md), [DEVICE_DETACH(9)](DEVICE_DETACH.9.md), device_detach(9), [DEVICE_IDENTIFY(9)](device_identify.9.md), [device_probe_and_attach(9)](device_probe_and_attach.9.md)

## 历史

`bus_enumerate_hinted_children` 首次出现于 FreeBSD 6.2。

`bus_delayed_attach_children` 首次出现于 FreeBSD 12.2。

`bus_identify_children` 首次出现于 FreeBSD 15.0。其功能在旧版本中通过已弃用的 `bus_generic_probe` 提供。

`bus_attach_children` 首次出现于 FreeBSD 15.0。其功能在旧版本中通过已弃用的 `bus_generic_attach` 提供。

`bus_detach_children` 首次出现于 FreeBSD 15.0。其功能在旧版本中通过 `bus_generic_detach` 提供。
