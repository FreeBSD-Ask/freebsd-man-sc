# device_get_parent(9)

`device_get_parent` — 返回设备的父设备

## 名称

`device_get_parent`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

device_t
device_get_parent(device_t dev);
```

## 描述

`device_get_parent` 函数返回设备的父设备。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 Warner Losh 编写。
