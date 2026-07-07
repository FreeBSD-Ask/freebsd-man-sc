# devclass_get_softc(9)

`devclass_get_softc` — 将单元号转换为驱动程序私有结构

## 名称

`devclass_get_softc`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

void *
devclass_get_softc(devclass_t dc, int unit)
```

## 描述

此函数检索具有给定单元号的设备的驱动程序私有实例变量并返回它。

## 返回值

如果设备存在，则返回其驱动程序私有变量，否则返回 NULL。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
