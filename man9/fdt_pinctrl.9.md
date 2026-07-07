# fdt_pinctrl(9)

`fdt_pinctrl` — FDT 引脚复用控制器驱动的辅助函数

## 名称

`fdt_pinctrl`

## 概要

```c
#include <dev/fdt/fdt_pinctrl.h>

int
fdt_pinctrl_configure(device_t client, u_int index)

int
fdt_pinctrl_configure_by_name(device_t client, const char * name)

int
fdt_pinctrl_register(device_t pinctrl, const char *pinprop)

int
fdt_pinctrl_configure_tree(device_t pinctrl)
```

## 描述

[fdt_pinctrl(4)](../man4/fdt_pinctrl.4.md) 提供了一组 API，用于操作引脚复用控制器和引脚复用客户端上的 I/O 引脚配置。在控制器侧，实现了标准的 newbus 探测和附加方法。作为处理附加的一部分，它调用 `fdt_pinctrl_register` 函数将自身注册为引脚复用控制器。然后使用 `fdt_pinctrl_configure_tree` 遍历设备树，并为所有活动设备配置由 `pinctrl-0` 属性指定的引脚。该驱动程序还实现了 `fdt_pinctrl_configure` 方法，允许客户端设备在启动后更改其引脚配置。如果客户端设备在其生命周期的某个时刻需要更改引脚配置，则使用 `fdt_pinctrl_configure` 或 `fdt_pinctrl_configure_by_name` 函数。

`fdt_pinctrl_configure` 由客户端设备 `client` 用于请求由索引为 `index` 的 `pinctrl-N` 属性描述的引脚配置。

`fdt_pinctrl_configure_by_name` 由客户端设备 `client` 用于请求名为 `name` 的引脚配置。

`fdt_pinctrl_register` 注册一个 pinctrl 驱动，使其可被调用 `fdt_pinctrl_configure` 或 `fdt_pinctrl_configure_by_name` 的其他设备使用。它还注册 pinctrl 驱动节点下每个包含名为 `pinprop` 属性的子节点。如果 `pinprop` 为 `NULL`，则注册每个后代节点。驱动程序可通过多次调用 `fdt_pinctrl_register` 为多种引脚属性类型注册自身为引脚复用控制器。

`fdt_pinctrl_configure_tree` 遍历设备树中已启用的设备。如果 `pinctrl-0` 属性包含对指定 pinctrl 设备子节点的引用，则配置它们的引脚。

## 实例

```c
static int
foo_configure_pins(device_t dev, phandle_t cfgxref)
{
	phandle_t cfgnode;
	uint32_t *pins, *functions;
	int npins, nfunctions;
	cfgnode = OF_node_from_xref(cfgxref);
	pins = NULL;
	npins = OF_getencprop_alloc_multi(cfgnode, "foo,pins", sizeof(*pins),
	    (void **)&pins);
	functions = NULL;
	nfunctions = OF_getencprop_alloc_multi(cfgnode, "foo,functions",
	    sizeof(*functions), (void **)&functions);
	...
}
static int
foo_is_gpio(device_t dev, device_t gpiodev, bool *is_gpio)
{
	return (foo_is_pin_func_gpio(is_gpio));
}
static int
foo_set_flags(device_t dev, device_t gpiodev, uint32_t pin, uint32_t flags)
{
	int rv;
	rv = foo_is_pin_func_gpio(is_gpio);
	if (rv != 0)
		return (rv);
	foo_set_flags(pin, flags);
	return (0);
}
static int
foo_get_flags(device_t dev, device_t gpiodev, uint32_t pin, uint32_t *flags)
{
	int rv;
	rv = foo_is_pin_func_gpio(is_gpio);
	if (rv != 0)
		return (rv);
	foo_get_flags(pin, flags);
	return (0);
}
static int
foo_attach(device_t dev)
{
	...
	fdt_pinctrl_register(dev, "foo,pins");
	/*
	 * 可以注册多个 pinprop 处理程序
	 */
	fdt_pinctrl_register(dev, "bar,pins");
	fdt_pinctrl_configure_tree(dev);
	return (0);
}
static device_method_t foo_methods[] = {
	...
	/* fdt_pinctrl 接口 */
	DEVMETHOD(fdt_pinctrl_configure, foo_configure_pins),
	DEVMETHOD(fdt_pinctrl_is_gpio, foo_is_gpio),
	DEVMETHOD(fdt_pinctrl_set_flags, foo_set_flags),
	DEVMETHOD(fdt_pinctrl_get_flags, foo_get_flags),
	/* 终止方法列表 */
	DEVMETHOD_END
};
DRIVER_MODULE(foo, simplebus, foo_driver, foo_devclass, NULL, NULL);
```

## 参见

[fdt_pinctrl(4)](../man4/fdt_pinctrl.4.md)

## 作者

本手册页由 Oleksandr Tymoshenko 编写。
