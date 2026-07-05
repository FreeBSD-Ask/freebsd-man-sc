# device_delete_child.9

`device_delete_child` — 从设备中删除子设备

## 名称

`device_delete_child`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
device_delete_child(device_t dev, device_t child)
```

## 描述

将指定设备从 `dev` 中移除并删除。如果设备当前已附加，则首先通过 device_detach(9) 分离。如果 `device_detach` 失败，则返回其错误值。否则，删除 `child` 的所有后代设备并返回零。

对每个被删除的设备调用 [BUS_CHILD_DELETED(9)](BUS_CHILD_DELETED.9.md) 方法。这允许父设备的驱动程序拆除与子设备关联的任何状态，如 ivars。

## 返回值

成功时返回零，否则返回错误。

## 参见

[BUS_CHILD_DELETED(9)](BUS_CHILD_DELETED.9.md), [device_add_child(9)](device_add_child.9.md)

## 作者

本手册页由 Doug Rabson 编写。
