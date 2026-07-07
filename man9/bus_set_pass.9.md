# bus_set_pass(9)

`bus_set_pass` — 提升总线 pass 级别

## 名称

`bus_set_pass`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

void
bus_set_pass(int pass)
```

## 描述

`bus_set_pass` 函数在启动期间调用，将总线 pass 级别提升到 `pass`。此函数将为当前 pass 级别和新级别之间具有至少一个关联驱动程序的每个 pass 级别重新扫描设备树。设备树重新扫描通过在根总线设备上调用 [BUS_NEW_PASS(9)](bus_new_pass.9.md) 方法实现。

## 参见

[BUS_NEW_PASS(9)](bus_new_pass.9.md), [device(9)](device.9.md)
