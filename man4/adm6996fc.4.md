# adm6996fc(4)

`adm6996fc` — Infineon ADM6996FC 快速以太网交换芯片驱动

## 名称

`adm6996fc`

## 概要

`device mdio device etherswitch device adm6996fc`

`hint.adm6996fc.0.at="mdio0"`

## 描述

`adm6996fc` 设备驱动为 Infineon ADM6996FC 快速以太网交换芯片提供管理接口。此驱动通过以太网接口使用 smi 接口。

此驱动支持 port 和 dot1q vlan。dot1q 支持基于端口的 tag/untag。

## 实例

通过 etherswitchcfg 命令配置 dot1q vlan。

```sh
# etherswitchcfg config vlan_mode dot1q
```

将端口 5 配置为 tagging 端口。

```sh
# etherswitchcfg port5 addtag
```

## 参见

[etherswitch(4)](etherswitch.4.md), etherswitchcfg(8)

## 历史

`adm6996fc` 设备驱动最早出现在 FreeBSD 12.0 中。

## 作者

`adm6996fc` 驱动由 Hiroki Mori 编写。
