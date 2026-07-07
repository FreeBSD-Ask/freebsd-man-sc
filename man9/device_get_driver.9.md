# device_get_driver(9)

`device_get_driver` — 访问设备的当前驱动程序

## 名称

`device_get_driver`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

driver_t *
device_get_driver(device_t dev);
```

## 描述

返回与该设备关联的当前驱动程序。若设备没有驱动程序，则返回 `NULL`。

## 参见

[device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Doug Rabson 编写。
