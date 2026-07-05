# pwmbus.9

`pwmbus` — PWMBUS 方法

## 名称

`pwmbus`, `PWMBUS_CHANNEL_CONFIG`, `PWMBUS_CHANNEL_COUNT`, `PWMBUS_CHANNEL_ENABLE`, `PWMBUS_CHANNEL_GET_CONFIG`, `PWMBUS_CHANNEL_GET_FLAGS`, `PWMBUS_CHANNEL_IS_ENABLED`, `PWMBUS_CHANNEL_SET_FLAGS`, `PWMBUS_GET_BUS`

## 概要

```c
device pwm
```

```c
#include <pwmbus_if.h>
```

```c
int
PWMBUS_CHANNEL_CONFIG(device_t bus, u_int channel, u_int period, u_int duty)

int
PWMBUS_CHANNEL_COUNT(device_t bus, u_int *nchannel)

int
PWMBUS_CHANNEL_ENABLE(device_t bus, u_int channel, bool enable)

int
PWMBUS_CHANNEL_GET_CONFIG(device_t bus, u_int channel, u_int *period, u_int *duty)

int
PWMBUS_CHANNEL_GET_FLAGS(device_t bus, u_int channel, uint32_t *flags)

int
PWMBUS_CHANNEL_IS_ENABLED(device_t bus, u_int channel, bool *enabled)

int
PWMBUS_CHANNEL_SET_FLAGS(device_t bus, u_int channel, uint32_t flags)
```

## 描述

PWMBUS（脉宽调制）接口允许设备驱动程序注册到全局总线，以便内核中的其他设备可以通用方式使用它们。

对于所有 `PWMBUS_GET_BUS` 方法，`period` 参数是一个完整的开关周期持续时间（以纳秒为单位），`duty` 参数是该周期中导通部分的持续时间（以纳秒为单位）。

某些 PWM 硬件组织为具有多个通道的单个控制器。通道号从零开始计数。当存在多个通道时，它们有时共享公共时钟或其他资源。在这种情况下，更改任一通道的周期或占空比可能会影响共享相同资源的硬件中的其他通道。有关共享资源的通道的详细信息，请查阅底层 PWM 硬件设备驱动程序的文档。

## 接口

**`PWMBUS_CHANNEL_CONFIG`** `bus` `channel` `period` `duty` 配置总线上 PWM 控制器中指定通道的周期和占空比（以纳秒为单位）。成功返回 0，如果控制器不支持这些值则返回 `EINVAL`，如果 PWMBUS 控制器正在使用中且不支持动态更改值则返回 `EBUSY`。

**`PWMBUS_CHANNEL_COUNT`** `bus` `nchannel` 获取控制器支持的通道数。

**`PWMBUS_CHANNEL_ENABLE`** `bus` `channel` `enable` 启用 PWM 通道。

**`PWMBUS_CHANNEL_GET_CONFIG`** `bus` `channel` `period` `duty` 获取指定通道的周期和占空比的当前配置。

**`PWMBUS_CHANNEL_GET_FLAGS`** `bus` `channel` `flags` 获取通道的当前标志。如果驱动程序或控制器不支持此功能，默认方法返回标志值为零。

**`PWMBUS_CHANNEL_IS_ENABLED`** `bus` `channel` `enable` 测试 PWM 通道是否已启用。

**`PWMBUS_CHANNEL_SET_FLAGS`** `bus` `channel` `flags` 设置通道的标志（如反极性）。如果驱动程序或控制器不支持此功能，则使用空操作的默认方法。

## 历史

`pwmbus` 接口首次出现在 FreeBSD 13.0 中。`pwmbus` 接口和手册页由 Emmanuel Vadot <manu@FreeBSD.org> 编写。
