# ath_hal.4

`ath_hal` — Atheros 硬件访问层（HAL）

## 名称

`ath_hal`

## 概要

`device ath_hal` 或 `device ath_ar5210 device ath_ar5211 device ath_ar5212 device ath_rf2413 device ath_rf2417 device ath_rf2425 device ath_rf5111 device ath_rf5112 device ath_rf5413 device ath_ar5416 device ath_ar9160 device ath_ar9280 device ath_ar9285 device ath_ar9287 device ath_ar9300`

## 描述

HAL 为基于 Atheros AR5210、AR5211、AR5212、AR5213、AR2413、AR2417、AR2425、AR5413、AR5416、AR5418、AR5424、AR9160、AR9220、AR9280、AR9285、AR9287、AR9380、AR9390、AR9580、AR9590、AR9562 和 QCA9565 芯片（及配套的 RF/基带部件）的无线网络适配器提供硬件支持。此代码是 [ath(4)](ath.4.md) 驱动的一部分，但单独配置以便对所支持芯片集合进行细粒度控制。选择 `ath_hal` 将启用对所有 PCI 和 Cardbus 设备的支持。

部分设备采用 Cardbus/MiniPCI/PCI 形式。其他设备（例如 AR2413、AR2427、AR5418、AR9280、AR9285、AR9287）采用 PCIe、Mini-PCIe 或 ExpressCard 形式。

历史上此代码曾以纯二进制形式发布并打包为独立模块。随着 HAL 源代码的发布，这种情况已改变，代码已与驱动紧密集成。

## 硬件

以下卡片属于 `ath_hal` 模块所支持的设备：

| 卡片 | 芯片 | 总线 | 标准 |
| --- | --- | --- | --- |
| Aztech WL830PC | AR5212 | CardBus | b/g |
| D-Link DWL-A650 | AR5210 | CardBus | a |
| D-Link DWL-AB650 | AR5211 | CardBus | a/b |
| D-Link DWL-A520 | AR5210 | PCI | a |
| D-Link DWL-AG520 | AR5212 | PCI | a/b/g |
| D-Link DWL-AG650 | AR5212 | CardBus | a/b/g |
| D-Link DWL-G520B | AR5212 | PCI | b/g |
| D-Link DWL-G650B | AR5212 | CardBus | b/g |
| Elecom LD-WL54AG | AR5212 | Cardbus | a/b/g |
| Elecom LD-WL54 | AR5211 | Cardbus | a |
| Fujitsu E5454 | AR5212 | Cardbus | a/b/g |
| Fujitsu FMV-JW481 | AR5212 | Cardbus | a/b/g |
| Fujitsu E5454 | AR5212 | Cardbus | a/b/g |
| HP NC4000 | AR5212 | PCI | a/b/g |
| I/O Data WN-AB | AR5212 | CardBus | a/b |
| I/O Data WN-AG | AR5212 | CardBus | a/b/g |
| I/O Data WN-A54 | AR5212 | CardBus | a |
| Linksys WMP55AG | AR5212 | PCI | a/b/g |
| Linksys WPC51AB | AR5211 | CardBus | a/b |
| Linksys WPC55AG | AR5212 | CardBus | a/b/g |
| NEC PA-WL/54AG | AR5212 | CardBus | a/b/g |
| Netgear WAG311 | AR5212 | PCI | a/b/g |
| Netgear WAB501 | AR5211 | CardBus | a/b |
| Netgear WAG511 | AR5212 | CardBus | a/b/g |
| Netgear WG311 (aka WG311v1) | AR5212 | PCI | b/g |
| Netgear WG311v2 | AR5212 | PCI | b/g |
| Netgear WG311T | AR5212 | PCI | b/g |
| Netgear WG511T | AR5212 | CardBus | b/g |
| Orinoco 8480 | AR5212 | CardBus | a/b/g |
| Orinoco 8470WD | AR5212 | CardBus | a/b/g |
| Proxim Skyline 4030 | AR5210 | CardBus | a |
| Proxim Skyline 4032 | AR5210 | PCI | a |
| Samsung SWL-5200N | AR5212 | CardBus | a/b/g |
| SMC SMC2735W | AR5210 | CardBus | a |
| Sony PCWA-C700 | AR5212 | Cardbus | a/b |
| Sony PCWA-C300S | AR5212 | Cardbus | b/g |
| Sony PCWA-C500 | AR5210 | Cardbus | a |
| 3Com 3CRPAG175 | AR5212 | CardBus | a/b/g |
| TP-LINK TL-WDN4800 | AR9380 | PCIe | a/b/g/n |

## 参见

[ath(4)](ath.4.md)

## 历史

`ath_hal` 模块首次出现于 FreeBSD 5.2。

## 缺陷

已知缺陷参见 [ath(4)](ath.4.md)。
