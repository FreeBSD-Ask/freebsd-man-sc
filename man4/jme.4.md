# jme(4)

`jme` — JMicron 千兆/快速以太网驱动

## 名称

`jme`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device jme

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_jme_load="YES"
```

## 描述

`jme` 设备驱动为 JMicron JMC25x PCI Express 千兆以太网控制器和 JMicron JMC26x PCI Express 快速以太网控制器提供支持。

`jme` 驱动支持的所有 LOM 在发送和接收方向均具有 TCP/UDP/IP 校验和卸载、TCP 分段卸载（TSO）、硬件 VLAN 标签剥离/插入功能、网络唤醒（WOL）、中断合并/调制机制以及 64 位多播哈希过滤器。

JMC25x 还支持 Jumbo 帧（最大 9216 字节），可通过接口 MTU 设置进行配置。使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具选择大于 1500 字节的 MTU 可将适配器配置为接收和发送 Jumbo 帧。

`jme` 驱动支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。

**`1000baseTX`** 设置通过双绞线进行的 1000baseTX 操作。

`jme` 驱动支持以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`jme` 设备驱动为以下以太网控制器提供支持：

- JMicron JMC250 PCI Express 千兆以太网控制器
- JMicron JMC251 PCI Express 带读卡器主机的千兆以太网控制器
- JMicron JMC260 PCI Express 快速以太网控制器
- JMicron JMC261 PCI Express 带读卡器主机的千兆以太网控制器

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.jme.msi_disable`** 此可调参数禁用以太网硬件上的 MSI 支持。默认值为 0。

**`hw.jme.msix_disable`** 此可调参数禁用以太网硬件上的 MSI-X 支持。默认值为 0。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数提供：

**`dev.jme.%d.tx_coal_to`** 此变量设置在发送 Tx 完成中断前延迟的最长时间，以微秒为单位。接受范围为 1 至 65535；默认值为 100（100 微秒）。

**`dev.jme.%d.tx_coal_pkt`** 此变量设置可合并到单个 Tx 完成中断中的最大传出数据包数。接受范围为 1 至 255；默认值为 8。

**`dev.jme.%d.rx_coal_to`** 此变量设置在触发 Rx 完成中断前等待额外数据包到达（用于可能的数据包合并）的最长时间，以微秒为单位。接受范围为 1 至 65535；默认值为 100（100 微秒）。

**`dev.jme.%d.rx_coal_pkt`** 此变量设置可合并到单个 Rx 完成中断中的最大传入数据包数。接受范围为 1 至 255；默认值为 2。

**`dev.jme.%d.process_limit`** 此变量设置在处理程序重新入队到 taskqueue 之前，单批处理中要处理的最大事件数。接受范围为 10 至 255；默认值为 128 个事件。更改此值后无需将接口关闭再重新打开即可生效。

## 参见

altq(4), arp(4), miibus(4), netintro(4), ng_ether(4), vlan(4), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`jme` 驱动由 Pyun YongHyeon <yongari@FreeBSD.org> 编写。最早出现于 FreeBSD 7.1。

## 注意事项

`jme` 驱动尽量避免对使用 eFuse 存储站地址的控制器进行不必要的站地址重编程。eFuse 可安全重编程的次数最多为 16 次。此外，一旦通过 eFuse 重编程了站地址，就无法恢复出厂默认的站地址。强烈建议不要重编程站地址，管理员有责任在更改站地址时将原始站地址存储在安全的地方。

JMC25x 存在两个已知的 1000baseT 链路建立问题。如果 JMC25x 控制器的全掩码修订号小于或等于 4，且链路伙伴启用了 IEEE 802.3az 节能以太网功能，则控制器将无法建立 1000baseT 链路。此外，如果电缆长度超过 120 米，控制器也无法建立 1000baseT 链路。这些问题的已知解决方法是使用 100baseTX 强制手动链路配置，而非依赖自动协商。控制器的全掩码修订号可通过详细的内核引导选项查看。使用芯片修订号的低四位来获取控制器的全掩码修订号。
