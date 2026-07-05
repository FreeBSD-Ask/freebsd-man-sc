# ofw_bus_status_okay.9.md

`ofw_bus_get_status` — 检查设备树节点的状态

## 名称

`ofw_bus_get_status`, `ofw_bus_status_okay`, `ofw_bus_node_status_okay`

## 概要

```c
#include <dev/ofw/openfirm.h>
```

```c
#include <dev/ofw/ofw_bus.h>
```

```c
#include <dev/ofw/ofw_bus_subr.h>
```

```c
const char *
ofw_bus_get_status(device_t dev)

int
ofw_bus_status_okay(device_t dev)

int
ofw_bus_node_status_okay(phandle_t node)
```

## 描述

设备树节点的 "status" 属性指示设备是否已启用。多个硬件版本可能使用相同的基础片上系统（SoC）构建，但启用了不同的功能块集合。通常使用 SoC 设备树，仅为衍生主板启用/禁用设备节点。只有当设备树节点具有 "status" 属性且值设置为 "ok" 或 "okay" 时，才视为已启用。

`ofw_bus_get_status` 返回与设备 `dev` 关联的设备树节点的 "status" 属性值。如果该节点没有 "status" 属性或没有与设备关联的节点，函数返回 NULL。

`ofw_bus_status_okay` 在与设备 `dev` 关联的设备树节点具有 "status" 属性且其值为 "ok" 或 "okay" 时返回 1。

`ofw_bus_node_status_okay` 在设备树节点 `node` 具有 "status" 属性且其值为 "ok" 或 "okay" 时返回 1。

## 作者

本手册页由 Oleksandr Tymoshenko 编写。
