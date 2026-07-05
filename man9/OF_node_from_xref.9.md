# OF\_node\_from\_xref.9

`OF_node_from_xref` — 在内核 phandle 和有效 phandle 之间转换

## 名称

`OF_node_from_xref`, `OF_xref_from_node`

## 概要

```c
#include <dev/ofw/ofw_bus.h>
#include <dev/ofw/ofw_bus_subr.h>

phandle_t
OF_node_from_xref(phandle_t xref)

phandle_t
OF_xref_from_node(phandle_t node)
```

## 描述

某些 OpenFirmware 实现（FDT、IBM）具有有效 phandle 或 xref 的概念。它们用于交叉引用设备树节点。例如，帧缓冲控制器可能引用控制背光的 GPIO 控制器和引脚。在此示例中，GPIO 节点将具有一个 cell（32 位整数）属性，其保留名称如 "phandle" 或 "linux,phandle"，其值唯一标识该节点。实际名称取决于实现。帧缓冲节点将具有一个由设备绑定（设备特定的属性集合）描述的名称的属性。它可以是 cell 属性，也可以是一个组合属性，其中一部分为 cell。帧缓冲节点属性的值将与 GPIO "phandle" 属性的值相同，因此可以说帧缓冲节点引用了 GPIO 节点。内核使用内部逻辑为设备树节点分配唯一标识符，这些值与 "phandle" 属性的值不匹配。`OF_node_from_xref` 和 `OF_xref_from_node` 用于在这两种节点标识符之间进行转换。

`OF_node_from_xref` 返回有效 phandle `xref` 对应的内核 phandle。如果找不到或 OpenFirmware 实现不支持有效 phandle，则函数返回输入值。

`OF_xref_from_node` 返回内核 phandle `node` 对应的有效 phandle。如果找不到或 OpenFirmware 实现不支持有效 phandle，则函数返回输入值。

## 实例

```c
phandle_t panelnode, panelxref;
char *model;
if (OF_getencprop(node, "lcd-panel", &panelxref) <= 0)
    return;
panelnode = OF_node_from_xref(panelxref);
if (OF_getprop_alloc(hdminode, "model", (void **)&model) <= 0)
    return;
```

## 参见

[OF_device_from_xref(9)](OF_device_from_xref.9.md), [OF_device_register_xref(9)](OF_device_from_xref.9.md)

## 作者

本手册页由 Oleksandr Tymoshenko <gonzo@FreeBSD.org> 编写。
