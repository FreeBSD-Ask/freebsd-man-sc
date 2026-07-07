# device_enable(9)

`device_enable` — 操作设备启用标志

## 名称

`device_enable`, `device_disable`, `device_is_enabled`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

void
device_enable(device_t dev)

void
device_disable(device_t dev)

int
device_is_enabled(device_t dev)
```

## 描述

每个设备都有一个关联的启用标志。设备在创建时默认启用，但可以被禁用（例如，为了防止破坏性或耗时的探测尝试）。要禁用设备，调用 `device_disable`；要重新启用它，调用 `device_enable`；要测试设备是否启用，调用 `device_is_enabled`。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
