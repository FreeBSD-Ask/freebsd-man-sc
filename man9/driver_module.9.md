# DRIVER_MODULE(9)

`DRIVER_MODULE` — 内核驱动声明宏

## 名称

`DRIVER_MODULE`, `DRIVER_MODULE_ORDERED`, `EARLY_DRIVER_MODULE`, `EARLY_DRIVER_MODULE_ORDERED`

## 概要

```c
#include <sys/param.h>

#include <sys/kernel.h>

#include <sys/bus.h>

#include <sys/module.h>

DRIVER_MODULE(name, busname, driver_t driver, modeventhand_t evh, void *arg)

DRIVER_MODULE_ORDERED(name, busname, driver_t driver, modeventhand_t evh,
    void *arg, int order)

EARLY_DRIVER_MODULE(name, busname, driver_t driver, modeventhand_t evh,
    void *arg, int pass)

EARLY_DRIVER_MODULE_ORDERED(name, busname, driver_t driver, modeventhand_t evh,
    void *arg, enum sysinit_elem_order order, int pass)
```

## 描述

`DRIVER_MODULE` 宏声明一个内核驱动。`DRIVER_MODULE` 展开为真正的驱动声明，其中 `name` 用作驱动及其函数的命名前缀。注意它以纯文本形式提供，而不是 `char` 或 `char *`。

`busname` 是驱动的父总线（PCI、ISA、PPBUS 等），例如 `pci`、`isa` 或 `ppbus`。

`DRIVER_MODULE` 中使用的标识符可以与驱动名不同。此外，相同的驱动标识符可以存在于不同的总线上，这是一种相当简洁的方式，可在相同或不同总线上使用同一驱动为不同卡制作前端。例如，以下用法是允许的：

```c
DRIVER_MODULE(foo, isa, foo_driver, NULL, NULL);

DRIVER_MODULE(foo, pci, foo_driver, NULL, NULL);
```

`driver` 是 `driver_t` 类型的驱动，包含驱动信息，因此是 `DRIVER_MODULE` 调用中两个最重要的部分之一。

`evh` 参数是在驱动（或模块）加载或卸载时调用的事件处理程序（参见 [module(9)](module.9.md)）。

`arg` 目前未使用，应为 `NULL` 指针。

`DRIVER_MODULE_ORDERED` 宏允许按特定顺序注册驱动。如果单个内核模块包含多个相互依赖的驱动，这会很有用。`order` 参数应为 [SYSINIT(9)](sysinit.9.md) 初始化排序常量（`SI_ORDER_*`）之一。驱动模块的默认顺序为 `SI_ORDER_MIDDLE`。通常，模块会为单个驱动指定 `SI_ORDER_ANY` 顺序，以确保它最后注册。

`EARLY_DRIVER_MODULE` 宏允许为特定 pass 级别注册驱动。引导时的探测和附加过程会对设备树进行多次遍历。某些提供其他设备所需基本服务的关键驱动会在较早的遍历中附加。大多数驱动在最后的通用遍历中附加。在早期遍历中附加的驱动必须通过 `pass` 参数注册特定的 pass 级别（`BUS_PASS_*`）。驱动一旦注册，即可在所有后续遍历中附加到设备。

`EARLY_DRIVER_MODULE_ORDERED` 宏允许按特定顺序和特定 pass 级别注册驱动。

## 参见

[device(9)](device.9.md), [driver(9)](driver.9.md), [module(9)](module.9.md), [MODULE_PNP_INFO(9)](module_pnp_info.9.md), [SYSINIT(9)](sysinit.9.md)

## 历史

在 FreeBSD 14.0 之前，这些宏接受 `driver` 之后的额外 `devclass_t` 参数。

## 作者

本手册页由 Alexander Langer <alex@FreeBSD.org> 编写。
