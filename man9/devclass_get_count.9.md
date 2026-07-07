# devclass_get_count(9)

`devclass_get_count` — 获取 devclass 中的设备数量

## 名称

`devclass_get_count`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
devclass_get_count(devclass_t dc)
```

## 描述

返回指定 `devclass` 中的设备实例数量。

## 参见

[devclass(9)](devclass.9.md), [device(9)](device.9.md)

## 作者

本手册页由 Nate Lawson 编写。
