# devclass.9

`devclass` — 表示一类设备的对象

## 名称

`devclass`

## 概要

```c
typedef struct devclass *devclass_t;
```

## 描述

`devclass` 对象在系统中有两个主要功能。第一是管理设备实例的单元号分配，第二是保存特定总线类型的设备驱动程序列表。每个 `devclass` 都有一个名称，并且不能有两个同名的 devclass。这确保了向设备实例分配唯一的单元号。所有同名实例都被视为相同。

当不需要特定单元号时，使用 `DEVICE_UNIT_ANY`。

## 参见

[devclass_add_driver(9)](devclass_add_driver.9.md), [devclass_delete_driver(9)](devclass_delete_driver.9.md), [devclass_find(9)](devclass_find.9.md), [devclass_find_driver(9)](devclass_find_driver.9.md), [devclass_get_device(9)](devclass_get_device.9.md), [devclass_get_devices(9)](devclass_get_devices.9.md), [devclass_get_maxunit(9)](devclass_get_maxunit.9.md), [devclass_get_name(9)](devclass_get_name.9.md), [devclass_get_softc(9)](devclass_get_softc.9.md), [device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
