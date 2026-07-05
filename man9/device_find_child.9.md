# device_find_child.9

`device_find_child` — 搜索设备的子设备

## 名称

`device_find_child`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

device_t
device_find_child(device_t dev, const char *classname, int unit)
```

## 描述

此函数查找 `dev` 的具有给定 `classname` 和 `unit` 的特定子设备。如果 `unit` 为 -1，则返回 `dev` 的第一个具有匹配 `classname` 的子设备（即单元号最低的那个）。

## 返回值

如果存在，则返回子设备，否则返回 NULL。

## 参见

[device_add_child(9)](device_add_child.9.md)

## 作者

本手册页由 Doug Rabson 编写。
