# ofw_bus_is_compatible.9.md

`ofw_bus_is_compatible` — 检查设备树节点与驱动程序的兼容性

## 名称

`ofw_bus_is_compatible`, `ofw_bus_is_compatible_strict`, `ofw_bus_node_is_compatible`, `ofw_bus_search_compatible`

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
int
ofw_bus_is_compatible(device_t dev, const char *compatstr)

int
ofw_bus_is_compatible_strict(device_t dev, const char *compatstr)

int
ofw_bus_node_is_compatible(phandle_t node, const char *compatstr)

const struct ofw_compat_data *
ofw_bus_search_compatible(device_t dev, const struct ofw_compat_data *compat)
```

## 描述

设备树节点的 "compatible" 属性用于标识该节点所代表的设备类型。该属性是一个或多个字符串的列表，表示设备兼容的硬件类型。此类字符串的通用格式为 "vendor,hardware"，其中 "vendor" 是制造商的缩写名称，"hardware" 是设备标识符，例如 "fsl" 代表 "Freescale"，"imx6ul-i2c" 代表 I2C 控制器。为了与驱动程序的旧版本兼容，需要多个字符串。如果硬件修订版 B 向后兼容修订版 A，设备树节点可以通过在 "compatible" 属性值中同时提供 "vndr,hrdwrA" 和 "vndr,hrdwrB" 字符串来表示此兼容性。这样，旧驱动程序可以使用仅修订版 A 中可用的功能，而新版本的驱动程序可以利用修订版 B 的功能集。

`ofw_bus_is_compatible` 在与设备 `dev` 关联的设备树节点的 "compatible" 属性列表中出现 `compatstr` 值时返回 1，否则返回 0。

`ofw_bus_is_compatible_strict` 在与设备 `dev` 关联的设备树节点的 "compatible" 属性仅包含一个字符串且该字符串等于 `compatstr` 时返回 1，否则返回 0。

`ofw_bus_node_is_compatible` 在设备树节点 `node` 的 "compatible" 属性列表中出现 `compatstr` 值时返回 1，否则返回 0。

`ofw_bus_search_compatible` 返回 `compat` 表中 ocd_str 字段在与设备 `dev` 关联的设备树节点的 "compatible" 属性中出现的第一个条目的指针。`compat` 表是一个 struct ofw_compat_data 元素数组，定义如下：

```c
struct ofw_compat_data {
	const char *ocd_str;
	uintptr_t  ocd_data;
};
```

`compat` 表必须以 ocd_str 设置为 NULL 的条目终止。如果设备树节点与任何条目都不兼容，函数返回指向终止条目的指针。

## 实例

```c
static struct ofw_compat_data compat_data[] = {
	{"arm,hrdwrA",		FEATURE_A},
	{"arm,hrdwrB",		FEATURE_A | FEATURE_B},
	{NULL,			0}
};
static int
hrdwr_probe(device_t dev)
{
	...
	if (!ofw_bus_search_compatible(dev, compat_data)->ocd_data)
		return (ENXIO);
	...
}
static int
hrdwr_attach(device_t dev)
{
	...
	sc = device_get_softc(dev);
	sc->sc_features = ofw_bus_search_compatible(dev, compat_data)->ocd_data;
	...
}
```

## 参见

ofw_bus_find_compatible(9)

## 作者

本手册页由 Oleksandr Tymoshenko 编写。
