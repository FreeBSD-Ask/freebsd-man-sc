# BUS_HINTED_CHILD.9

`BUS_HINTED_CHILD` — 通知总线设备有关由提示标识的潜在子设备

## 名称

`BUS_HINTED_CHILD`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
void
BUS_HINTED_CHILD(device_t dev, const char *dname, int dunit)
```

## 描述

`BUS_HINTED_CHILD` 方法由 bus_enumerate_hinted_children(9) 函数为每组其“at”提示与总线设备 `dev` 匹配的命名提示调用。通常，此方法应确定给定设备名称和单元的提示集是否充分描述了一个新设备。如果是，应通过 [BUS_ADD_CHILD(9)](BUS_ADD_CHILD.9.md) 添加新设备。

## 参见

[BUS_ADD_CHILD(9)](BUS_ADD_CHILD.9.md), bus_enumerate_hinted_children(9), [device(9)](device.9.md)

## 历史

`BUS_HINTED_CHILD` 方法首次出现于 FreeBSD 6.2。
