# BUS_GET_PROPERTY(9)

`BUS_GET_PROPERTY` — 获取子设备的特定属性

## 名称

`BUS_GET_PROPERTY`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
ssize_t
BUS_GET_PROPERTY(device_t dev, device_t child, const char *propname,
    void *propvalue, size_t size, device_property_type_t type)
```

## 描述

`BUS_GET_PROPERTY` 方法由需要访问存储在总线上的子设备特定数据的驱动程序代码调用。属性具有名称和关联的值。实现应向 `propvalue` 复制至多 `size` 个字节。

`BUS_GET_PROPERTY` 支持通过 `type` 参数指定的不同属性类型。`size` 保证是底层属性类型的整数倍。如果不支持某种类型，`BUS_GET_PROPERTY` 应返回 -1。

## 注意事项

如果 `propvalue` 为 `NULL` 或 `size` 为零，实现应仅返回属性的大小。

## 返回值

成功时返回属性大小，否则返回 -1。

## 参见

[device(9)](device.9.md), [device_get_property(9)](device_get_property.9.md)

## 作者

本手册页由 Bartlomiej Grzesik 编写。
