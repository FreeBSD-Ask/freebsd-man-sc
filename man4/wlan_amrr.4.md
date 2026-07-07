# wlan_amrr(4)

`wlan_amrr` — 802.11 设备的 AMRR 速率自适应算法支持

## 名称

`wlan_amrr`

## 概要

`device wlan_amrr`

## 描述

`wlan_amrr` 模块实现 Adaptive Multi-Rate Retry 发送速率控制算法，供 802.11 设备驱动使用。

## 参见

[bwi(4)](bwi.4.md), [iwn(4)](iwn.4.md), [ral(4)](ral.4.md), [rum(4)](rum.4.md), [ural(4)](ural.4.md), [wlan(4)](wlan.4.md), [wpi(4)](wpi.4.md), [zyd(4)](zyd.4.md)

## 标准

更多信息可在描述 *AMRR* 算法的论文中找到，地址为 `http://hal.inria.fr/inria-00070784/en/`。

## 历史

`wlan_amrr` 驱动最早出现在 FreeBSD 6.0 中。
