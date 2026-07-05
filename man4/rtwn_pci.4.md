# rtwn_pci.4

`rtwn_pci` — Realtek 无线 rtwn 网络驱动程序的 PCI/PCIe 支持

## 名称

`rtwn_pci`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device rtwn
> device rtwn_pci
> device pci
> device wlan

## 描述

`rtwn_pci` 驱动为 [rtwn(4)](rtwn.4.md) 驱动提供对 PCIe 无线网络设备的支持。

RTL8188CE 和 RTL8188EE 都是高度集成的 802.11n 适配器，将 MAC、支持 1T1R 的基带和 RF 集成在单芯片中。它们仅在 2GHz 频段工作。

## 硬件

`rtwn_pci` 驱动支持以下 PCIe Wi-Fi 设备：

- Realtek 802.11n wireless 8188 (RTL8188EE)
- Realtek 802.11n wireless 8192 (RTL8192CE)

## 参见

[pci(4)](pci.4.md), [rtwn(4)](rtwn.4.md), [rtwn_usb(4)](rtwn_usb.4.md), [rtwnfw(4)](rtwnfw.4.md)
