# driver(9)

`driver` — 描述设备驱动的结构

## 名称

`driver`

## 概要

```c
#include <sys/param.h>
#include <sys/kernel.h>
#include <sys/bus.h>
#include <sys/module.h>
static int foo_probe(device_t);
static int foo_attach(device_t);
static int foo_detach(device_t);
static int foo_frob(device_t, int, int);
static int foo_twiddle(device_t, char *);
static device_method_t foo_methods[] = {
	/* 来自 device 接口的方法 */
	DEVMETHOD(device_probe,		foo_probe),
	DEVMETHOD(device_attach,	foo_attach),
	DEVMETHOD(device_detach,	foo_detach),
	/* 来自 bogo 接口的方法 */
	DEVMETHOD(bogo_frob,		foo_frob),
	DEVMETHOD(bogo_twiddle,		foo_twiddle),
	/* 终止方法列表 */
	DEVMETHOD_END
};
static driver_t foo_driver = {
	"foo",
	foo_methods,
	sizeof(struct foo_softc)
};
DRIVER_MODULE(foo, bogo, foo_driver, NULL, NULL);
```

## 描述

内核中的每个驱动由一个 `driver_t` 结构描述。该结构包含设备名称、指向方法列表的指针、驱动所实现的设备类型指示，以及驱动需要与设备实例关联的私有数据大小。每个驱动会实现一组或多组方法（称为接口）。示例驱动实现了标准的 "driver" 接口和虚构的 "bogo" 接口。

当驱动向系统注册时（通过 `DRIVER_MODULE` 宏，参见 [DRIVER_MODULE(9)](driver_module.9.md)），它会被添加到其父总线类型的 devclass 所包含的驱动列表中。例如，所有 PCI 驱动会包含在名为 "pci" 的 devclass 中，所有 ISA 驱动会包含在名为 "isa" 的 devclass 中。驱动不存放在父总线的设备对象中是为了处理给定总线类型的多个实例。`DRIVER_MODULE` 宏还会创建以驱动名称命名的 devclass，并可通过指定最后两个参数为额外的模块事件处理器和参数，可选地调用驱动中的额外初始化代码。

## 参见

[devclass(9)](devclass.9.md), [device(9)](device.9.md), [DEVICE_ATTACH(9)](device_attach.9.md), [DEVICE_DETACH(9)](device_detach.9.md), [DEVICE_IDENTIFY(9)](device_identify.9.md), [DEVICE_PROBE(9)](device_probe.9.md), [DEVICE_SHUTDOWN(9)](device_shutdown.9.md), [DRIVER_MODULE(9)](driver_module.9.md)

## 历史

`driver` 框架首次出现于 FreeBSD 2.2.7。

## 作者

本手册页由 Doug Rabson 编写。
