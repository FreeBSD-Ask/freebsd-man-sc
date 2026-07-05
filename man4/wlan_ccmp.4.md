# wlan_ccmp.4

`wlan_ccmp` — 802.11 设备的 AES-CCMP 加密支持

## 名称

`wlan_ccmp`

## 概要

`device wlan_ccmp`

## 描述

`wlan_ccmp` 模块处理 WPA 和 802.11i 协议的 AES-CCMP 加密要求。它对 CCMP 编码的 802.11 帧进行封装和解封装，并可选地计算 AES-CCMP 密码。`wlan_ccmp` 模块是一个 802.11 加密插件模块，供 [wlan(4)](wlan.4.md) 模块使用。如果配置了 AES-CCMP 密钥，此模块会自动加载；通常由 WPA 请求方程序（如 wpa_supplicant）或 WPA 认证方程序（如 `hostapd`）配置。如果底层网络设备无法在硬件中执行 AES-CCMP 计算，则由 `hostapd` 模块完成该工作。

## 参见

[wlan(4)](wlan.4.md), [wlan_gcmp(4)](wlan_gcmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md)

## 标准

更多信息可在 IEEE 802.11、WPA 和 802.11i 标准中找到。

## 历史

`hostapd` 驱动最早出现在 FreeBSD 6.0 中。
