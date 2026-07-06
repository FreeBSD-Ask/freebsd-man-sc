# device\_probe\_and\_attach.9

`device_attach` — 管理设备与设备驱动程序的连接

## 名称

`device_attach`, `device_detach`, `device_probe`, `device_probe_and_attach`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
device_attach(device_t dev);

int
device_detach(device_t dev);

int
device_probe(device_t dev);

int
device_probe_and_attach(device_t dev);
```

## 描述

这些函数管理设备与设备驱动程序之间的关系。

`device_probe` 调用每个合适驱动程序的 [DEVICE_PROBE(9)](DEVICE_PROBE.9.md) 方法，以找到与 `dev` 最匹配的驱动程序。若找到匹配的驱动程序，`dev` 会被设置为 `DS_ALIVE` 状态并返回 0。若 `dev` 已经 attach 到设备驱动程序或已通过 [device_disable(9)](device_disable.9.md) 被禁用，则不会对其进行探测并返回 -1。

`device_attach` 将设备驱动程序完全 attach 到 `dev`。此函数会打印设备的描述并调用 [DEVICE_ATTACH(9)](DEVICE_ATTACH.9.md) 方法。若 [DEVICE_ATTACH(9)](DEVICE_ATTACH.9.md) 方法成功，`dev` 会被设置为 `DS_ATTACHED` 状态并返回 0。若 [DEVICE_ATTACH(9)](DEVICE_ATTACH.9.md) 方法失败，会调用 [BUS_CHILD_DETACHED(9)](BUS_CHILD_DETACHED.9.md) 并返回一个错误值。

若设备名和单元被 hint 禁用，`device_attach` 会禁用该设备，将其降级到 `DS_NOTPRESENT` 状态，并返回 `ENXIO`。该设备保留其设备名和单元，可以通过 [devctl(8)](../man8/devctl.8.md) 重新启用。

`device_probe_and_attach` 是 `device_probe` 和 `device_attach` 的封装函数，用于完全初始化一个设备。若 `dev` 已经 attach 或被禁用，`device_probe_and_attach` 保持设备不变并返回 0。否则，使用 `device_probe` 为 `dev` 标识一个设备驱动程序，并由 `device_attach` 完成将驱动程序 attach 到 `dev` 的操作。设备驱动程序通常应使用此函数来初始化设备，而非直接调用 `device_probe` 和 `device_attach`。

`device_detach` 将设备驱动程序从 `dev` 分离。此函数调用 [DEVICE_DETACH(9)](DEVICE_DETACH.9.md) 方法来拆除 `dev` 的设备驱动程序状态。若该方法失败，返回其错误值且 `dev` 保持 attach 状态。若方法成功，则调用 [BUS_CHILD_DETACHED(9)](BUS_CHILD_DETACHED.9.md)，将设备设置为 `DS_NOTPRESENT` 状态，并返回 0。若设备处于 busy 状态，`device_detach` 会失败并返回 `EBUSY`，且 `dev` 保持不变。

## 返回值

成功时返回 0，否则返回相应的错误值。此外，若 `dev` 被禁用或已经 attach，`device_probe` 返回 -1。

## 参见

[devctl(8)](../man8/devctl.8.md), [BUS_CHILD_DETACHED(9)](BUS_CHILD_DETACHED.9.md), [device(9)](device.9.md), [DEVICE_ATTACH(9)](DEVICE_ATTACH.9.md), [DEVICE_DETACH(9)](DEVICE_DETACH.9.md), [DEVICE_PROBE(9)](DEVICE_PROBE.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Doug Rabson 编写。
