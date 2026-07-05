# regulator.9

`regulator` — 调压器方法

## 名称

`regulator`, `regulator_get_by_name`, `regulator_get_by_id`, `regulator_release`, `regulator_get_name`, `regulator_enable`, `regulator_disable`, `regulator_stop`, `regulator_status`, `regulator_get_voltage`, `regulator_set_voltage`, `regulator_check_voltage`, `regulator_get_by_ofw_property`

## 概要

```c
device regulator
```

```c
#include <dev/extres/regulator/regulator.h>
```

```c
int
regulator_get_by_name(device_t cdev, const char *name, regulator_t *regulator)

int
regulator_get_by_id(device_t cdev, device_t pdev, intptr_t id, regulator_t *regulator)

int
regulator_release(regulator_t regulator)

int
regulator_get_name(regulator_t regulator)

int
regulator_enable(regulator_t reg)

int
regulator_disable(regulator_t reg)

int
regulator_stop(regulator_t reg)

int
regulator_status(regulator_t reg, int *status)

int
regulator_get_voltage(regulator_t reg, int *uvolt)

int
regulator_set_voltage(regulator_t reg, int min_uvolt, int max_uvolt)

int
regulator_check_voltage(regulator_t reg, int uvolt)

int
regulator_get_by_ofw_property(device_t dev, phandle_t node, char *name, regulator_t *reg)
```

## 描述

调压器框架允许驱动程序启用、禁用和更改调压器电压。

## 返回值

所有函数成功时返回 0，如果找不到调压器或其某个父级则返回 `ENODEV`。

## 接口

**`REGULATOR_STATUS_ENABLED`** 调压器已启用。

**`REGULATOR_STATUS_OVERCURRENT`** 硬件报告正在消耗过多电流。

**`regulator_get_by_name`** `cdev` `name` `regulator` 根据名称解析调压器。所有调压器名称都是唯一的。这还会递增调压器的引用计数。

**`regulator_get_by_id`** `cdev` `pdev` `id` `regulator` 根据 id 解析调压器。所有调压器 id 都是唯一的。这还会递增调压器的引用计数。

**`regulator_get_by_ofw_property`** `dev` `node` `name` `reg` 根据名为 name 的 fdt 属性解析调压器。如果 node 为 0，则函数将自行获取 ofw 节点。这还会递增调压器的引用计数。成功返回 0，如果 ofw 属性不存在则返回 `ENOENT`。

**`regulator_release`** `regulator` 禁用调压器，递减其引用计数并释放传递的调压器变量。

**`regulator_get_name`** `regulator` 返回调压器的名称。所有调压器名称都是唯一的。

**`regulator_enable`** `reg` 启用调压器。如果调压器支持电压范围，硬件中配置的值将作为输出电压。如果调压器已被另一个驱动程序启用，这仅递增启用计数器。

**`regulator_disable`** `reg` 禁用调压器。如果调压器也已被另一个驱动程序启用，这仅递减启用计数器。如果调压器之前未被启用，将触发 kassert。

**`regulator_stop`** `reg` 在硬件中禁用调压器。这确保即使调压器被引导加载程序启用，也会被禁用。不应在之前已被驱动程序启用的调压器上调用。成功返回 0，如果另一个消费者启用了它则返回 `EBUSY`。

**`regulator_status`** `reg` `status` 获取调压器的硬件状态。status 将包含一个位掩码，可能具有以下值：

**`regulator_get_voltage`** `reg` `uvolt` 获取调压器当前设置的电压（以微伏为单位）。

**`regulator_set_voltage`** `reg` `min_uvolt` `max_uvolt` 更改调压器的电压。如果硬件或驱动程序接受范围，可以提供不同的最小值和最大值。成功返回 0，如果调压器不支持此电压范围则返回 `ERANGE`。

**`regulator_check_voltage`** `reg` `uvolt` 检查调压器是否支持给定电压。成功返回 0，如果调压器不支持此电压范围则返回 `ERANGE`。

## 历史

`regulator` 框架首次出现在 FreeBSD 12.0 中。`regulator` 框架由 Michal Meloun <mmel@FreeBSD.org> 编写。`regulator` 手册页由 Emmanuel Vadot <manu@FreeBSD.org> 编写。
