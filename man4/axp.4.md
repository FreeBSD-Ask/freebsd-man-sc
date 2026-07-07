# axp(4)

`axp` — Advanced Micro Devices 10G 以太网驱动

## 名称

`axp`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device iflib
> device axp

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_axp_load="YES"
```

## 描述

`axp` 驱动启用 AMD EPYC 处理器内置的基于 PCI-E 的 10G 以太网控制器。

支持以下特性：

- 1G/10G SFP+ 链路
- Jumbo 帧（9000 字节）
- 发送和接收校验和卸载
- TCP 分段卸载（TSO）
- VLAN 标签插入/提取
- VLAN 校验和卸载
- VLAN TSO
- 接收端导向（RSS）
- 支持 IPV4 和 IPV6
- MSI-X 中断
- 拆分头部

以上所有特性默认启用。

关于硬件相关问题，请参阅 AMD EPYC 处理器附带的相关文档。

## SYSCTL 变量

以下变量可作为 [sysctl(8)](../man8/sysctl.8.md) 变量使用：

- xpcs
- xgmac
- xprop
- xi2c

**`dev.ax.X.mac_stats`** 转储控制器的发送和接收统计计数器值。包括每个发送和接收队列的统计信息。

**`dev.ax.X.channels_info`** 转储允许的及默认配置的发送和接收通道信息。

**`dev.ax.X.ringparam_info`** 转储允许的及默认配置的发送和接收队列描述符信息。

**`dev.ax.X.link_ksettings_info`** 转储当前链路设置，如链路模式、速度和双工设置。

**`dev.ax.X.pauseparam_info`** 转储当前流控设置。

**`dev.ax.X.coalesce_info`** 转储当前中断合并设置。

**`dev.ax.X.link_info`** 转储链路的当前状态。

**`dev.ax.X.drv_info`** 转储驱动程序和控制器固件版本信息。

**`dev.ax.X.YYYY_register`**

**`dev.ax.X.YYYY_register_values`** 用于从控制器特定块转储特定寄存器的 sysctl。YYYY 指定块。支持以下块。将寄存器偏移设置到第一个变量，然后通过读取第二个变量来读取寄存器的值。

**`dev.ax.X.axgbe_debug_level`** 配置驱动的日志级别。默认为 0。支持 0-3。

**`dev.ax.X.link_workaround`** 此变量启用对间歇性链路问题的规避措施。当链路长时间无法建立时，可将此变量设置为 1 以重置 PHY 并建立链路。

## 加载器可调参数

以下变量可作为 loader.conf(5) 可调参数使用。

**`dev.ax.X.sph_enable`** 此变量控制接口的拆分头部特性。默认为 1，表示启用拆分头部支持。此变量必须在加载驱动之前设置，可通过 loader.conf(5) 或通过 [kenv(1)](../man1/kenv.1.md)。驱动加载后无法修改。在 loader.conf(5) 中设置此变量需要重启系统才能生效。使用 [kenv(1)](../man1/kenv.1.md) 时，使用包装变量 `dev.ax.sph_enable`，它将为所有 `axp` 接口配置（启用/禁用）拆分头部支持。要将 netmap 与此设备一起使用，必须禁用拆分头部支持（将此变量设置为 0）。

## 参见

arp(4), [iflib(4)](iflib.4.md), [netmap(4)](netmap.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`axp` 设备驱动首次出现于 FreeBSD 13.0。

FreeBSD 中已存在另一版本的驱动。此驱动早期命名为 "axgbe"，现已更名为 "axa"。此驱动用于早期/旧版本硬件上基于 ACPI 的以太网控制器。此驱动由 <andrew@FreeBSD.org> 编写。

## 作者

`axp` 设备驱动由 Advanced Micro Devices Inc. 编写。

如有任何问题和支持需求，请将详情通过电子邮件发送至 <rajesh1.kumar@amd.com>。
