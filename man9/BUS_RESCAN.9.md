# BUS_RESCAN.9

`BUS_RESCAN` — 重新扫描总线以检查已添加或移除的设备

## 名称

`BUS_RESCAN`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
void
BUS_RESCAN(device_t dev)
```

## 描述

`BUS_RESCAN` 方法用于请求重新扫描总线设备上的子设备。该方法应添加自上次扫描以来新增的设备，并移除删除的设备。此方法不需要重新检查现有设备以确定其属性是否更改。此方法也不需要把重新扫描请求传播给子设备。

## 参见

[device(9)](device.9.md)
