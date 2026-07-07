# wlan_wep(4)

`wlan_wep` — 802.11 设备的 WEP 加密支持

## 名称

`wlan_wep`

## 概要

`device wlan_wep`

## 描述

`wlan_wep` 模块处理 802.11 协议的 WEP 加密要求。它对 WEP 编码的 802.11 帧进行封装和解封装，并可选地计算 WEP 密码。`wlan_wep` 模块是一个 802.11 加密插件模块，供 [wlan(4)](wlan.4.md) 模块使用。如果使用 [ifconfig(8)](../man8/ifconfig.8.md) 配置了 WEP 密钥，此模块会自动加载。如果底层网络设备无法在硬件中执行 WEP 计算，则由 `wlan_wep` 模块完成该工作。

## 参见

[wlan(4)](wlan.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_gcmp(4)](wlan_gcmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md)

## 标准

更多信息可在 IEEE 802.11 标准中找到。

## 历史

`wlan_wep` 驱动最早出现在 FreeBSD 6.0 中。
