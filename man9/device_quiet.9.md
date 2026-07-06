# device\_quiet.9

`device_quiet` — 操作设备静默标志

## 名称

`device_quiet`, `device_verbose`, `device_is_quiet`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

void
device_quiet(device_t dev);

void
device_verbose(device_t dev);

int
device_is_quiet(device_t dev);
```

## 描述

每个设备都关联一个静默（quiet）标志。设备在创建时默认为 verbose（详细）模式，但可以将其静默以防止在 attach 时打印设备标识字符串，以及在 detach 时打印消息。要静默一个设备，在设备驱动程序 probe 例程中调用 `device_quiet`。要重新启用探测消息，调用 `device_verbose`。要测试一个设备是否被静默，调用 `device_is_quiet`。

驱动程序 detach 后，设备会被隐式标记为 verbose。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
