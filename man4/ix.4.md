# ix(4)

`ix` — Intel 10Gb 以太网驱动

## 名称

`ix`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device iflib
> device ix

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_ix_load="YES"
```

## 描述

`ix` 驱动为 Intel(R) 10Gb 以太网 PCIe 适配器提供支持。该驱动支持 Jumbo 帧、MSIX、TSO 和 RSS。

有关硬件需求的问题，请参阅 Intel 10GbE 适配器附带的文档。列出的所有硬件需求均适用于 FreeBSD。

通过接口 MTU 设置提供对 Jumbo 帧的支持。使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具选择大于 1500 字节的 MTU 可将适配器配置为接收和发送 Jumbo 帧。Jumbo 帧的最大 MTU 大小为 9710。

此驱动版本支持 VLAN。有关启用 VLAN 的信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`ix` 驱动支持 Intel 10Gb 以太网 PCIe 适配器，包括：

- Intel(R) Ethernet E610
- Intel(R) Ethernet X553
- Intel(R) Ethernet X552
- Intel(R) Ethernet X550
- Intel(R) Ethernet X540 Bypass
- Intel(R) Ethernet X540
- Intel(R) Ethernet X520 Bypass (82599)
- Intel(R) Ethernet X520 (82599)
- Intel(R) 10 Gigabit Server Adapter (82598EB)

## 加载器可调参数

`ix` 驱动支持以下加载器可调参数：

**`hw.ix.max_interrupt_rate`** 每秒最大中断数。

**`hw.ix.flow_control`** 用于所有适配器的默认流控制。

**`hw.ix.advertise_speed`** 用于所有适配器的默认通告速度。

**`hw.ix.enable_msix`** 启用消息信号中断（MSI-X）。

**`hw.ix.allow_unsupported_sfp`** 允许不受支持的小型可插拔（SFP）模块。使用风险自负。

**`hw.ix.enable_fdir`** 启用 Flow Director。Flow Director 将以太网数据包定向到消耗该数据包的进程、应用程序、容器或微服务运行所在的核心。

**`hw.ix.enable_rss`** 启用接收端缩放（RSS）。启用 RSS 后，特定 TCP 连接的所有接收数据处理会在多个处理器或处理器核心之间共享。不启用 RSS 时，所有处理由单个处理器执行，导致系统缓存利用率低效。如果你的系统只有一个处理单元，则无效果。

**`hw.ix.enable_aim`** 启用自适应中断节流（AIM）。根据该中断向量的流量随时间变化中断速率。

## SYSCTL 变量

`ix` 驱动支持以下 [sysctl(8)](../man8/sysctl.8.md) 变量：

**0** 除可管理性事务外的所有集群
**0x1** 链路集群
**0x2** 除 RCW 寄存器外的完整 CSR 空间

**0** 无
**1** 错误
**2** 警告
**3** 常规
**4** 详细

**`dev.ix.?.debug.dump.clusters`** 指定位掩码以选择要包含在调试转储中的固件事件集群。可能的值包括：此功能仅在 E610 设备上支持。

**`dev.ix.?.debug.dump.dump`** 指定 1 以生成每设备调试快照。输出必须重定向到文件并由 Intel 客户支持解码。此功能仅在 E610 上支持。

**`dev.ix.?.debug.fw_log.severity.<module>`** 为指定模块指定固件日志详细级别。可用级别包括：支持的模块：general、ctrl、link、link_topo、dnl、i2c、sdp、mdio、adminq、hdma、lldp、dcbx、dcb、xlr、nvm、auth、vpd、iosf、parser、sw、scheduler、txq、acl、post、watchdog、task_dispatch、mng、synce、health、tsdrv、pfreg、mdlver。此功能仅在 E610 设备上支持。

**`dev.ix.?.debug.fw_log.register`** 指定 1 以应用每设备固件日志配置。此功能仅在 E610 设备上支持。

**`dev.ix.?.debug.fw_log.on_load`** 通过 [kenv(1)](../man1/kenv.1.md) 设置时，在驱动初始化期间启用固件日志。此功能仅在 E610 设备上支持。

## 诊断

- ix%d: Unable to allocate bus resource: memory 发生了致命的初始化错误。
- ix%d: Unable to allocate bus resource: interrupt 发生了致命的初始化错误。
- ix%d: watchdog timeout -- resetting 设备已停止响应网络，或网络连接（线缆）存在问题。

## 支持

如需一般信息和支持，请访问 Intel 支持网站：`http://support.intel.com`。

如果使用受支持的内核和受支持的适配器发现已发布源代码的问题，请将与问题相关的具体信息发送邮件至 <freebsd@intel.com>。

## 参见

[altq(4)](altq.4.md), arp(4), [iflib(4)](iflib.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`ix` 设备驱动最早出现于 FreeBSD 7.0。

## 作者

`ix` 驱动由 Intel Corporation <freebsd@intel.com> 编写。

## 注意事项

Intel(R) Flow Director 支持目前在 FreeBSD 中未完全实现，需要额外工作才能支持这些功能。

启用 Flow Director 可能使流量路由到 NIC 的错误 RX 队列，导致接收端性能次优。
