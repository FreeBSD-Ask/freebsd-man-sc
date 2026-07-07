# enetc(4)

`enetc` — Freescale ENETC PCIe 千兆以太网驱动

## 名称

`enetc`

## 概要

`若要将此驱动编译进内核，内核配置文件中必须包含以下行： sp options SOC_NXP_LS device pci device fdt device iflib device enetc`

## 描述

`enetc` 驱动为 LS1028A SoC 中集成的 ENETC 千兆以太网 NIC 提供支持。使用 [iflib(9)](../man9/iflib.9.md) 与内核其余部分通信。支持物理端口以及连接到内部交换机的虚拟接口。

此版本驱动中已实现以下硬件卸载：

```sh
- 接收 IP 校验和验证。
- VLAN 标签插入和提取。
- 基于 VLAN 标签的数据包过滤。
```

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 参见

[vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md), [iflib(9)](../man9/iflib.9.md)

## 历史

`enetc` 驱动首次出现于 FreeBSD 14.0。
