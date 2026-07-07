# thunderbolt(4)

`thunderbolt` — Thunderbolt / USB4 原生主控制器驱动程序

## 名称

`thunderbolt`

## 概要

`device thunderbolt`

## 描述

`thunderbolt` 驱动附加到 Intel 和 AMD 平台上发现的 Thunderbolt 和通用 USB4 原生主控制器（NHI）。NHI 是管理 Thunderbolt 和 USB4 路由器通信的主机端控制器。

该驱动初始化 NHI 硬件，可以读写其配置空间以挂起或恢复它。

*此驱动不提供可工作的 Thunderbolt 或 USB4 支持。* 加载此驱动的主要目的是允许系统声明对 NHI 设备的所有权，以便 PCI 电源管理可以将其置于低功耗状态。在支持 S0ix 的平台上（如 S0i3），未挂起的 NHI 将阻止进入最深空闲状态，且 NHI 由 pre-OS 连接管理器在引导时置于活动状态。加载 `thunderbolt` 可防止此阻塞。不需要 S0ix 空闲状态的用户暂时无需加载此驱动。

## 硬件

`thunderbolt` 驱动仅附加到通用 USB4 控制器，即匹配 PCI 类 `PCIC_SERIALBUS`、子类 `PCIS_SERIALBUS_USB` 和编程接口 `PCIP_SERIALBUS_USB_USB4` 的设备。

## 历史

`thunderbolt` 驱动出现于 FreeBSD 16.0。

## 注意事项

此驱动正在积极开发中，功能尚不完整。接口和行为可能随时更改，恕不另行通知。不要依赖此驱动进行 Thunderbolt 或 USB4 设备连接。
