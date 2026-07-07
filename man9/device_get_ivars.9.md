# device_get_ivars(9)

`device_get_ivars` — 访问总线私有变量

## 名称

`device_get_ivars`, `device_set_ivars`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

void *
device_get_ivars(device_t dev);

void
device_set_ivars(device_t dev, void *ivar);
```

## 描述

`device_get_ivars` 函数返回设备的总线特定实例变量。

`device_set_ivars` 函数设置设备的总线特定实例变量。

通常只有总线驱动程序会使用这些函数。内核假定总线驱动程序会管理此内存，不会自动进行内存分配或释放。客户端驱动程序应通过 [BUS_READ_IVAR(9)](bus_read_ivar.9.md) 接口访问 ivars。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
