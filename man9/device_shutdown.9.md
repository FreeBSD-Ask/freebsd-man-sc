# DEVICE\_SHUTDOWN.9

`DEVICE_SHUTDOWN` — 在系统关闭期间调用

## 名称

`DEVICE_SHUTDOWN`

## 概要

```c
#include <sys/param.h>

#include <sys/bus.h>

int
DEVICE_SHUTDOWN(device_t dev)
```

## 描述

`DEVICE_SHUTDOWN` 方法在系统关闭期间调用，允许驱动程序将硬件置于一致的状态以便重启计算机。

## 返回值

成功时返回零，否则返回错误。

## 参见

[device(9)](device.9.md), [DEVICE_ATTACH(9)](device_attach.9.md), [DEVICE_DETACH(9)](device_detach.9.md), [DEVICE_IDENTIFY(9)](device_identify.9.md), [DEVICE_PROBE(9)](device_probe.9.md)

## 作者

本手册页由 Doug Rabson 编写。
