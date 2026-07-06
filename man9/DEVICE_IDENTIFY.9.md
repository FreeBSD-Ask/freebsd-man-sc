# DEVICE_IDENTIFY.9

`DEVICE_IDENTIFY` — 识别并注册新的子设备

## 名称

`DEVICE_IDENTIFY`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
void
DEVICE_IDENTIFY(driver_t *driver, device_t parent)
```

## 描述

设备驱动程序的 identify 方法用于添加无法通过总线设备上的标准方法枚举的设备。设备可以通过多种方式枚举，包括访问非歧义设备寄存器和解析固件表。纯软件伪设备也通常通过 identify 方法枚举。

对于每个新识别的设备，应通过调用 [BUS_ADD_CHILD(9)](bus_add_child.9.md) 方法创建新的设备实例。如果 identify 方法能够发现新设备的其他属性，也应一并设置。例如，应通过为每个资源调用 [bus_set_resource(9)](bus_set_resource.9.md) 将设备资源添加到设备中。

identify 方法可能被多次调用。如果设备驱动程序被卸载并重新加载，identify 方法将在重新加载后被第二次调用。因此，identify 方法应避免重复设备。由 identify 方法添加的设备通常使用固定的设备名，在这种情况下，可以使用 [device_find_child(9)](device_find_child.9.md) 来检测现有设备。

## 实例

以下伪代码展示了一个函数示例，该函数探测一块硬件并将其及其资源（一个 I/O 端口）注册到父总线设备。

```c
void
foo_identify(driver_t *driver, device_t parent)
{
	device_t child;
	retrieve_device_information;
	if (devices matches one of your supported devices &&
	    device_find_child(parent, "foo", DEVICE_UNIT_ANY) == NULL) {
		child = BUS_ADD_CHILD(parent, 0, "foo", DEVICE_UNIT_ANY);
		bus_set_resource(child, SYS_RES_IOPORT, 0, FOO_IOADDR, 1);
	}
}
```

## 参见

[BUS_ADD_CHILD(9)](bus_add_child.9.md), bus_identify_children(9), [bus_set_resource(9)](bus_set_resource.9.md), [device(9)](device.9.md), [device_find_child(9)](device_find_child.9.md)

## 作者

本手册页由 Alexander Langer <alex@FreeBSD.org> 编写。
