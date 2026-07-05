# BUS_CHILD_DELETED.9

`BUS_CHILD_DELETED` — 通知总线设备子设备将被删除

## 名称

`BUS_CHILD_DELETED`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
void
BUS_CHILD_DELETED(device_t dev, device_t child)
```

## 描述

`BUS_CHILD_DELETED` 方法在设备被删除时由 new-bus 框架调用。总线驱动程序可以实现此方法，以释放与设备关联的总线专用资源（如实例变量）。

## 参见

[BUS_ADD_CHILD(9)](BUS_ADD_CHILD.9.md), [device(9)](device.9.md)

## 历史

`BUS_CHILD_DELETED` 方法首次出现于 FreeBSD 10.0。
