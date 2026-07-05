# sk.4

`sk` — SysKonnect SK-984x 和 SK-982x PCI 千兆以太网适配器驱动

## 名称

`sk`

## 概要

`要将此驱动编译进内核，请将以下行添加到你的内核配置文件中：`

> device miibus
> device sk

`或者，要在引导时以模块形式加载此驱动，请将以下行添加到 loader.conf(5) 中：`

```sh
if_sk_load="YES"
```

## 描述

`sk` 驱动为 SysKonnect SK-984x 和 SK-982x 系列 PCI 千兆以太网适配器提供支持。

SysKonnect 适配器由两个主要组件组成：XaQti Corp. XMAC II 千兆 MAC 和 SysKonnect GEnesis 控制器 ASIC。XMAC 提供千兆 MAC 和 PHY 支持，而 GEnesis 提供到 PCI 总线的接口、DMA 支持、数据包缓冲和仲裁。GEnesis 可同时控制最多两个 XMAC，支持双端口 NIC 配置。

SK-982x 1000baseT 适配器还包括一个 Broadcom BCM5400 1000baseTX PHY，用于替代 XMAC 的内部 PHY。Broadcom PHY 通过其 GMII 端口连接到 XMAC。

`sk` 驱动配置双端口 SysKonnect 适配器时，将每个 XMAC 视为独立的逻辑网络接口。两个端口可彼此独立运行，并连接到不同的网络。SysKonnect 驱动软件目前仅将双端口适配器上的第二个端口用于故障转移：如果主端口链路发生故障，SysKonnect 驱动会自动将流量切换到第二个端口。

还支持 Marvell Semiconductor 88E100* 千兆 PHY。

XaQti XMAC II 支持带自动协商的全双工和半双工操作。XMAC 还支持无限帧大小。通过接口 MTU 设置提供对 jumbo 帧的支持。使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具选择大于 1500 字节的 MTU 即可配置适配器收发 jumbo 帧。使用 jumbo 帧可显著提高某些任务（如文件传输和数据流）的性能。

`sk` 驱动支持以下媒体类型：

**autoselect** 启用媒体类型和选项的自动选择。用户可通过在 **`/etc/rc.conf`** 文件中添加媒体选项来手动覆盖自动选择的模式。

**1000baseTX** 设置通过双绞线的 1000baseTX 操作。仅适用于具有 1000baseT 端口的 SK-982x 系列适配器。支持 `full-duplex` 和 `half-duplex` 模式。

**1000baseSX** 设置 1000Mbps（千兆以太网）操作。支持 `full-duplex` 和 `half-duplex` 模式。

`sk` 驱动支持以下媒体选项：

**full-duplex** 强制全双工操作。

**half-duplex** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`sk` 驱动支持的适配器包括：

- 3Com 3C940 单端口，1000baseT 适配器
- 3Com 3C2000-T 单端口，1000baseT 适配器
- Belkin F5D5005 单端口，1000baseT 适配器
- D-Link DGE-530T 单端口，1000baseT 适配器
- Linksys（修订版 2）单端口，1000baseT 适配器
- SK-9521 SK-NET GE-T 单端口，1000baseT 适配器
- SK-9821 SK-NET GE-T 单端口，1000baseT 适配器
- SK-9822 SK-NET GE-T 双端口，1000baseT 适配器
- SK-9841 SK-NET GE-LX 单端口，单模光纤适配器
- SK-9842 SK-NET GE-LX 双端口，单模光纤适配器
- SK-9843 SK-NET GE-SX 单端口，多模光纤适配器
- SK-9844 SK-NET GE-SX 双端口，多模光纤适配器
- SMC 9452TX 单端口，1000baseT 适配器

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.skc.jumbo_disable`** 禁用 jumbo 帧支持。内存较少的系统可将此设为非零值以节省内存。默认值为 0。

## SYSCTL 变量

以下变量既可作为 [sysctl(8)](../man8/sysctl.8.md) 变量，也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`dev.skc.%d.int_mod`** 此变量控制中断节流。接受范围为 10 到 10000。默认值为 100 微秒。更改需将接口关闭再重新启动才能生效。

## 诊断

- sk%d: couldn't map memory 已发生致命初始化错误。
- sk%d: couldn't map ports 已发生致命初始化错误。
- sk%d: couldn't map interrupt 已发生致命初始化错误。
- sk%d: no memory for softc struct! 驱动在初始化期间未能为每设备实例信息分配内存。
- sk%d: failed to enable memory mapping! 驱动未能初始化 PCI 共享内存映射。这可能发生在卡不在总线主控插槽中的情况。
- sk%d: no memory for jumbo buffers! 驱动在初始化期间未能为 jumbo 帧分配内存。
- sk%d: watchdog timeout 设备已停止响应网络，或网络连接存在问题（电缆）。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "XaQti XMAC II datasheet"。

> "SysKonnect GEnesis programming manual"。

## 历史

`sk` 设备驱动最早出现于 FreeBSD 3.0。

## 作者

`sk` 驱动由 Bill Paul <wpaul@ctr.columbia.edu> 编写。
