# vlan.4

`vlan` — IEEE 802.1Q VLAN 网络接口

## 名称

`vlan`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device vlan

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_vlan_load="YES"
```

## 描述

`vlan` 驱动将按照 IEEE 802.1Q 标准打标签的帧解复用到逻辑 `vlan` 网络接口中，这允许通过单个交换机中继端口在多个 VLAN 之间进行路由/桥接。

每个 `vlan` 接口在运行时通过接口克隆创建。最简单的方法是使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `create` 命令，或使用 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `cloned_interfaces` 变量。

要正常工作，必须使用 [ifconfig(8)](../man8/ifconfig.8.md) 为 `vlan` 接口分配父接口和数字 VLAN 标签。只要标签不同，可将单个父接口分配给多个 `vlan` 接口。父接口很可能是连接到正确配置的交换机端口的以太网卡。VLAN 标签应与交换网络中设置的标签之一匹配。

`vlan` 最初假定已标记和未标记帧的最小长度相同。此模式通过将 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.link.vlan.soft_pad` 设置为 0（默认）来选择。但是，有些网络设备在帧长度因去标签而低于允许的最小值时无法调整帧长度。将 `net.link.vlan.soft_pad` 的值更改为 1 后，此类设备应能与 `vlan` 互操作。在后一种模式下，`vlan` 会在打标签之前填充短帧，使其在不符合规范的设备去除标签后长度不小于最小值。

## 硬件

`vlan` 驱动支持在能够协助处理 VLAN 的父接口上高效运行。此类接口会因其能力被自动识别。根据物理接口的复杂程度，它可以执行完整的 VLAN 处理，或仅能接收和发送长帧（最多 1522 字节，包括以太网头和 FCS）。这些能力可由 [ifconfig(8)](../man8/ifconfig.8.md) 的相应参数 `vlanhwtag` 和 `vlanmtu` 由用户控制。但是，物理接口不一定对此做出反应：它可能永久启用某项能力而无法关闭。整个问题非常特定于具体设备及其驱动程序。

目前，以下设备能够在硬件中执行完整的 VLAN 处理：[ae(4)](ae.4.md), [age(4)](age.4.md), [alc(4)](alc.4.md), [ale(4)](ale.4.md), [bce(4)](bce.4.md), [bge(4)](bge.4.md), [bxe(4)](bxe.4.md), [cxgb(4)](cxgb.4.md), [cxgbe(4)](cxgbe.4.md), [em(4)](em.4.md), igb(4), [ix(4)](ix.4.md), [jme(4)](jme.4.md), [liquidio(4)](liquidio.4.md), [msk(4)](msk.4.md), [mxge(4)](mxge.4.md), [nge(4)](nge.4.md), [re(4)](re.4.md), [sge(4)](sge.4.md), [stge(4)](stge.4.md), [ti(4)](ti.4.md) 和 [vge(4)](vge.4.md)。

其他以太网接口可通过 `vlan` 驱动中的软件模拟来运行 VLAN。但是，有些接口缺乏发送和接收长帧的能力。将此类接口指定为 `vlan` 的父接口会导致相应 `vlan` 接口上的 MTU 减小。在当今的互联网中，由于大量不当的 [icmp(4)](icmp.4.md) 过滤破坏了路径 MTU 发现机制，这很可能导致 [tcp(4)](tcp.4.md) 连接问题。

这些接口原生支持 `vlan` 的长帧：[axe(4)](axe.4.md), [bfe(4)](bfe.4.md), [cas(4)](cas.4.md), [dc(4)](dc.4.md), [et(4)](et.4.md), [fwe(4)](fwe.4.md), [fxp(4)](fxp.4.md), [gem(4)](gem.4.md), le(4), [nfe(4)](nfe.4.md), [rl(4)](rl.4.md), [sis(4)](sis.4.md), [sk(4)](sk.4.md), [ste(4)](ste.4.md), [vr(4)](vr.4.md), [vte(4)](vte.4.md) 和 [xl(4)](xl.4.md)。

`vlan` 驱动会自动识别原生支持 `vlan` 使用长帧的设备，并根据父接口的能力计算适当的帧 MTU。其他未在上面列出的接口可能能处理长帧，但不会声明此能力。如果与这样的父接口一起使用，可手动校正 `vlan` 上的 MTU 设置。

## 参见

[ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md)
