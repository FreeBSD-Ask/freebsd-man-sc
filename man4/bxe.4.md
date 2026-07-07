# bxe(4)

`bxe` — QLogic NetXtreme II 10Gb PCIe 以太网适配器驱动

## 名称

`bxe`

## 概要

要将此驱动编译进内核，请在你的内核配置文件中加入以下行：

> device bxe

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_bxe_load="YES"
```

## 描述

`bxe` 驱动为基于 QLogic NetXtreme II 系列 10Gb 芯片的 PCIe 10Gb 以太网适配器提供支持。该驱动支持 Jumbo 帧、VLAN 标记、校验和卸载（IPv4、TCP、UDP、IPv6-TCP、IPv6-UDP）、MSI-X 中断、TCP 分段卸载（TSO）、大接收卸载（LRO）以及接收端缩放（RSS）。

## 硬件

`bxe` 驱动为基于 QLogic NetXtreme II 系列 10Gb 以太网控制器芯片的各类网卡提供支持，包括以下型号：

- QLogic NetXtreme II BCM57710 10Gb
- QLogic NetXtreme II BCM57711 10Gb
- QLogic NetXtreme II BCM57711E 10Gb
- QLogic NetXtreme II BCM57712 10Gb
- QLogic NetXtreme II BCM57712-MF 10Gb
- QLogic NetXtreme II BCM57800 10Gb
- QLogic NetXtreme II BCM57800-MF 10Gb
- QLogic NetXtreme II BCM57810 10Gb
- QLogic NetXtreme II BCM57810-MF 10Gb
- QLogic NetXtreme II BCM57840 10Gb / 20Gb
- QLogic NetXtreme II BCM57840-MF 10Gb

## 配置

可以通过设置若干配置参数来调整驱动行为。这些参数可通过 loader.conf(5) 文件设置，在下次系统引导时生效。以下参数影响该驱动的所有实例。

**`hw.bxe.debug`** 默认值 = 0。设置驱动的默认日志级别。详见下文的诊断与调试章节。

**`hw.bxe.interrupt_mode`** 默认值 = 2。设置默认中断模式：0=IRQ，1=MSI，2=MSIX。如果设置为 MSIX 且分配失败，驱动将回退并尝试分配 MSI。如果 MSI 分配失败，驱动将回退并尝试分配固定电平 IRQ。如果 IRQ 分配也失败，则驱动加载失败。使用 MSI/MSIX 时，除了一个用于默认处理的中断向量外，驱动还会为每个队列分配一个中断向量。

**`hw.bxe.queue_count`** 默认值 = 4。设置快速路径数据包处理队列的默认数量。注意每个队列会分配一个 MSI/MSIX 中断向量。

**`hw.bxe.max_rx_bufs`** 默认值 = 0。设置每个队列分配的最大接收缓冲区数。零（0）表示为每个缓冲区描述符分配一个接收缓冲区。默认情况下，这相当于每个队列 4080 个缓冲区，也是此配置参数的最大值。

**`hw.bxe.hc_rx_ticks`** 默认值 = 25。设置接收路径中主机中断合并的 tick 数。

**`hw.bxe.hc_tx_ticks`** 默认值 = 50。设置发送路径中主机中断合并的 tick 数。

**`hw.bxe.rx_budget`** 默认值 = 0xffffffff。设置在一次中断中处理的最大接收数据包数。如果达到预算，剩余/待处理的数据包将在调度的 taskqueue 中处理。

**`hw.bxe.max_aggregation_size`** 默认值 = 32768。设置最大 LRO 聚合字节数。值越大，硬件聚合的数据包越多。最大值为 65K。

**`hw.bxe.mrrs`** 默认值 = -1。设置 PCI MRRS：-1=自动，0=128B，1=256B，2=512B，3=1KB

**`hw.bxe.autogreeen`** 默认值 = 0。设置 AutoGrEEEN：0=HW_DEFAULT，1=FORCE_ON，2=FORCE_OFF

**`hw.bxe.udp_rss`** 默认值 = 0。启用/禁用 UDP 的四元组 RSS：0=DISABLED，1=ENABLED

修改队列数和接收缓冲区数时需特别小心。FreeBSD 会对 [mbuf(9)](../man9/mbuf.9.md) 分配进行限制。如果缓冲区分配失败，接口初始化将失败，接口将无法使用。驱动对缓冲区分配不做尽力而为的处理，而是全有或全无。

你可以使用 [sysctl(8)](../man8/sysctl.8.md) 调整 [mbuf(9)](../man9/mbuf.9.md) 分配上限，并使用 [netstat(1)](../man1/netstat.1.md) 查看当前用量，方法如下：

```sh
# netstat -m
# sysctl kern.ipc.nmbclusters
# sysctl kern.ipc.nmbclusters=<#>
```

还有一些可按实例设置的配置参数，可动态覆盖默认配置。下文中的“#”需替换为驱动实例/接口单元号：

**`dev.bxe.#.debug`** 默认值 = 0。设置该驱动实例的默认日志级别。详见上文的 `hw.bxe.debug` 及下文的诊断与调试章节。

**`dev.bxe.#.rx_budget`** 默认值 = 0xffffffff。设置该驱动实例在一次中断中处理的最大接收数据包数。详见上文的 `hw.bxe.rx_budget`。

还可使用 [ifconfig(8)](../man8/ifconfig.8.md) 配置其他选项：

**`MTU - 最大传输单元`** 默认值 = 1500。范围 = 46-9184。

```sh
# ifconfig bxe# mtu <n>
```

**`混杂模式`** 默认值 = OFF。

```sh
# ifconfig bxe# [ promisc | -promisc ]
```

**`Rx/Tx 校验和卸载`** 默认值 = RX/TX CSUM ON。注意 Rx 和 Tx 设置不是独立的。

```sh
# ifconfig bxe# [ rxcsum | -rxcsum | txcsum | -txcsum ]
```

**`TSO - TCP 分段卸载`** 默认值 = ON。

```sh
# ifconfig bxe# [ tso | -tso | tso6 | -tso6 ]
```

**`LRO - TCP 大接收卸载`** 默认值 = ON。

```sh
# ifconfig bxe# [ lro | -lro ]
```

## 诊断与调试

`bxe` 通过 [sysctl(8)](../man8/sysctl.8.md) 暴露了大量统计信息。

转储默认驱动配置：

```sh
# sysctl -a | grep hw.bxe
```

转储每个实例的配置和详细统计信息：

```sh
# sysctl -a | grep dev.bxe
```

转储单个实例的信息（将“#”替换为驱动实例/接口单元号）：

```sh
# sysctl -a | grep dev.bxe.#
```

转储单个实例所有队列的信息：

```sh
# sysctl -a | grep dev.bxe.#.queue
```

转储单个实例中某个队列的信息（将额外的“#”替换为队列号）：

```sh
# sysctl -a | grep dev.bxe.#.queue.#
```

`bxe` 驱动能够向系统日志输出大量调试信息。默认日志级别可通过 `hw.bxe.debug` [sysctl(8)](../man8/sysctl.8.md) 设置。使用此设置时需谨慎，因为它可能导致输出过多日志。由于此参数是默认参数，会影响每个实例，并会显著改变驱动的时序。辅助调试的更好方法是使用 `dev.bxe.#.debug` [sysctl(8)](../man8/sysctl.8.md) 动态更改特定实例的调试级别，这样可以在运行时开启/关闭各调试组的日志。

可切换的不同调试组如下：

```sh
DBG_LOAD   0x00000001 /* 加载与卸载    */
DBG_INTR   0x00000002 /* 中断处理       */
DBG_SP     0x00000004 /* 慢路径处理      */
DBG_STATS  0x00000008 /* 统计更新       */
DBG_TX     0x00000010 /* 数据包发送      */
DBG_RX     0x00000020 /* 数据包接收      */
DBG_PHY    0x00000040 /* PHY/链路处理    */
DBG_IOCTL  0x00000080 /* ioctl 处理     */
DBG_MBUF   0x00000100 /* 转储 mbuf 信息  */
DBG_REGS   0x00000200 /* 寄存器访问      */
DBG_LRO    0x00000400 /* LRO 处理       */
DBG_ASSERT 0x80000000 /* 调试断言       */
DBG_ALL    0xFFFFFFFF /* 全部           */
```

例如，要调试 bxe0 上接收路径的问题：

```sh
# sysctl dev.bxe.0.debug=0x22
```

完成后将日志关闭：

```sh
# sysctl dev.bxe.0.debug=0
```

## 支持

如需支持，请联系你的 QLogic 授权经销商或 QLogic 技术支持，网址 `http://support.qlogic.com`，或发送电子邮件至 <support@qlogic.com>。

## 参见

[netstat(1)](../man1/netstat.1.md), [altq(4)](altq.4.md), arp(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`bxe` 设备驱动首次出现于 FreeBSD 9.0。

## 作者

`bxe` 驱动由 Eric Davis <edavis@broadcom.com>、David Christensen <davidch@broadcom.com> 和 Gary Zambrano <zambrano@broadcom.com> 编写。
