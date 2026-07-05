# felix.4.aarch64

`felix` — Microchip Ocelot Felix 交换机驱动程序

## 名称

`felix`

## 概要

`要将本驱动程序编译进内核，内核配置文件中必须包含以下行： options SOC_NXP_LS device pci device fdt device mdio device enetc device etherswitch device felix`

## 描述

`felix` 驱动程序为 NXP LS1028A SoC 中所集成的 Microchip Ocelot Felix 交换机（VSC9959）提供管理接口。它是一个 PCI 设备，属于更大的 ENETC 根复合体的一部分。本驱动程序使用 [etherswitch(4)](etherswitch.4.md) 框架。

本驱动程序仅支持 dot1q vlan。dot1q 支持基于端口的 addtag、striptag、dropuntagged、dropuntagged。

## 实例

通过 etherswitchcfg 命令配置 dot1q vlan。

```sh
# etherswitchcfg config vlan_mode dot1q
```

将端口 5 配置为标记端口。

```sh
# etherswitchcfg port5 addtag
```

取消端口 5 的标记端口配置。

```sh
# etherswitchcfg port5 -addtag
```

## 参见

[etherswitch(4)](etherswitch.4.md), etherswitchcfg(8)

## 历史

`felix` 设备驱动程序首次出现于 FreeBSD 14.0。

## 作者

`felix` 驱动程序由 Kornel Duleba (<mindal@semihalf.com>) 和 Lukasz Hajec (<lha@semihalf.com>) 编写。
