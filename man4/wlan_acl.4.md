# wlan_acl(4)

`wlan_acl` — 802.11 设备的基于 MAC 的 ACL 支持

## 名称

`wlan_acl`

## 概要

`device wlan_acl`

## 描述

`wlan_acl` 模块为作为接入点工作的 802.11 设备实现基于 MAC 的访问控制插件。必须加载 `wlan_acl` 才能使 [ifconfig(8)](../man8/ifconfig.8.md) 处理 `mac:*` 请求。

## 参见

[wlan(4)](wlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 标准

更多信息可在 IEEE 802.11 标准中找到。

## 历史

`wlan_acl` 驱动最早出现在 FreeBSD 6.0 中。
