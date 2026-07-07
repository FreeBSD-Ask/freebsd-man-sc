# device_get_unit(9)

`device_get_unit` — 访问设备的单元号

## 名称

`device_get_unit`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
device_get_unit(device_t dev);
```

## 描述

返回设备的单元号。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
