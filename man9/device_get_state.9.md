# device\_get\_state.9

`device_get_state` — 操作设备状态

## 名称

`device_get_state`, `device_busy`, `device_unbusy`, `device_is_alive`, `device_is_attached`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

device_state_t
device_get_state(device_t dev);

void
device_busy(device_t dev);

void
device_unbusy(device_t dev);

int
device_is_alive(device_t dev);

int
device_is_attached(device_t dev);
```

## 描述

通过调用 `device_get_state` 访问设备的当前状态，该函数返回 `DS_NOTPRESENT`、`DS_ALIVE`、`DS_ATTACHED` 或 `DS_BUSY`（在 [device(9)](device.9.md) 中描述）。要测试设备是否已被成功探测，调用 `device_is_alive`，当状态大于或等于 `DS_ALIVE` 时该函数简单地返回。要测试设备是否已被成功 attach，调用 `device_is_attached`，当状态大于或等于 `DS_ATTACHED` 时该函数简单地返回。

每个设备都有一个 busy 计数，调用 `device_busy` 时递增，调用 `device_unbusy` 时递减。若设备状态小于 `DS_ATTACHED`，这两个函数都会返回错误。

当对处于 `DS_ATTACHED` 状态的设备调用 `device_busy` 时，设备会转为 `DS_BUSY` 状态。当调用 `device_unbusy` 且递减后设备的 busy 计数为零时，设备会转为 `DS_ATTACHED` 状态。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
