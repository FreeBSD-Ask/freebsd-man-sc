# device_get_property(9)

`device_get_property` — 访问设备特定数据

## 名称

`device_get_property`, `device_has_property`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

ssize_t
device_get_property(device_t dev, const char *prop, void *val, size_t sz,
    device_property_type_t type);

bool
device_has_property(device_t dev, const char *prop);
```

## 描述

访问由父总线提供的设备特定数据。驱动程序可以使用这些属性来获取设备能力并设置必要的 quirks。

底层属性类型通过 `type` 参数指定。目前支持以下类型：

**`DEVICE_PROP_BUFFER`** 底层属性为字节串。

**`DEVICE_PROP_ANY`** 通配属性类型。

**`DEVICE_PROP_HANDLE`** 跟随一个引用，底层属性为相应总线的句柄。

**`DEVICE_PROP_UINT32`** 底层属性为无符号 32 位整数数组。`sz` 参数应为 4 的倍数。

**`DEVICE_PROP_UINT64`** 底层属性为无符号 64 位整数数组。`sz` 参数应为 8 的倍数。

## 注释

调用 `device_get_property` 时可以传入 NULL 作为属性值的指针，以获取属性的大小。

目前此接口由 [simplebus(4)](../man4/simplebus.4.md) 和 [acpi(4)](../man4/acpi.4.md) 实现。

## 返回值

`device_get_property` 成功时返回属性的大小，否则返回 -1。

`device_has_property` 在找到给定属性时返回 true。

## 参见

[acpi(4)](../man4/acpi.4.md), [simplebus(4)](../man4/simplebus.4.md), [device(9)](device.9.md)

## 作者

本手册页由 Bartlomiej Grzesik 编写。
