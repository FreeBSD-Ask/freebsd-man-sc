# device_delete_children.9

`device_delete_children` — 删除给定设备的所有子设备

## 名称

`device_delete_children`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
device_delete_children(device_t dev)
```

## 描述

`device_delete_children` 函数使用 `device_delete_child` 函数删除给定设备 `dev` 的所有子设备（如果有）。如果子设备无法删除，此函数将返回错误代码。

## 返回值

成功时返回零，非零返回值表示失败。

## 参见

[device_delete_child(9)](device_delete_child.9.md)

## 作者

本手册页由 Jeroen Ruigrok van der Werven 编写。
