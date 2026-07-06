# OF\_device\_from\_xref.9

`OF_device_from_xref` — 管理 xref 与设备之间的映射

## 名称

`OF_device_from_xref`, `OF_xref_from_device`, `OF_device_register_xref`, `OF_device_unregister_xref`

## 概要

```c
#include <dev/ofw/ofw_bus.h>
#include <dev/ofw/ofw_bus_subr.h>

int
OF_device_register_xref(phandle_t xref, device_t dev)

void
OF_device_unregister_xref(phandle_t xref, device_t dev)

device_t
OF_device_from_xref(phandle_t xref)

phandle_t
OF_xref_from_device(device_t dev)
```

## 描述

当一个设备树节点引用另一个节点时，驱动程序可能需要获取与被引用节点关联的 device_t 实例。例如，以太网驱动程序访问 PHY 设备。为实现这一点，内核维护一个将有效句柄映射到 device_t 实例的表。

`OF_device_register_xref` 添加一个从有效 phandle `xref` 到设备 `dev` 的映射条目。如果 `xref` 的映射条目已存在，则替换为新的条目。该函数始终返回 0。

`OF_device_unregister_xref` 移除从有效 phandle `xref` 到设备 `dev` 的映射条目。如果 `xref` 的映射条目不存在，则静默返回。

`OF_device_from_xref` 返回与有效 phandle `xref` 关联的 device_t 实例。如果不存在此类映射，则返回 NULL。

`OF_xref_from_device` 返回与设备 `dev` 关联的有效 phandle。如果不存在此类映射，则返回 0。

## 实例

```c
static int
acmephy_attach(device_t dev)
{
    phandle_t node;
    /* PHY 节点被 eth 设备引用，注册它 */
    node = ofw_bus_get_node(dev);
    OF_device_register_xref(OF_xref_from_node(node), dev);
    return (0);
}
```

## 参见

[OF_node_from_xref(9)](of_node_from_xref.9.md)

## 作者

本手册页由 Oleksandr Tymoshenko <gonzo@FreeBSD.org> 编写。
