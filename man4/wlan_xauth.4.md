# wlan_xauth(4)

`wlan_xauth` — 802.11 设备的外部认证器支持

## 名称

`wlan_xauth`

## 概要

`device wlan_xauth`

## 描述

`wlan_xauth` 模块是一个 [wlan(4)](wlan.4.md) 认证器插件，用于与用户态认证实现（如 `hostapd`）配合使用。它挂钩到 802.11 层但不做任何事。因此，关联的 802.11 站点在由外部代理授权之前无权收发帧；通常使用 WPA、802.1x 或 802.11i 等协议。

此模块由通常启动 hostapd(8) 的 rc 脚本自动加载。

## 参见

[wlan(4)](wlan.4.md)

## 标准

更多信息可在 IEEE 802.11、WPA 和 802.11i 标准中找到。

## 历史

`hostapd` 驱动最早出现在 FreeBSD 6.0 中。
