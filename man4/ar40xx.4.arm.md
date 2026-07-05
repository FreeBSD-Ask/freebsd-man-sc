# ar40xx.4.arm

`ar40xx_switch` — Qualcomm IPQ4018/IPQ4019 千兆以太网交换机驱动

## 名称

`ar40xx_switch`

## 概要

`device mdio etherswitch ar40xx_switch`

## 描述

`ar40xx_switch` 驱动支持 Qualcomm IPQ4018/IPQ4019 SoC 内部的千兆以太网交换机。

## 硬件

`ar40xx_switch` 驱动支持以下千兆以太网交换机控制器：

- Qualcomm IPQ 4019 五端口千兆以太网交换机
- Qualcomm IPQ 4018 五端口千兆以太网交换机

## 参见

[etherswitch(4)](etherswitch.4.md), etherswitchcfg(8)

## 注意事项

此驱动目前仅支持 L2 端口/VLAN 映射模式。
