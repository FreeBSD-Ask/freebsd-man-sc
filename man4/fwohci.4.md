# fwohci(4)

`fwohci` — OHCI FireWire 芯片组设备驱动程序

## 名称

`fwohci`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device firewire

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
firewire_load="YES"
```

`要禁用物理访问（详见缺陷章节），请在 loader.conf(5) 中加入以下行：`

```sh
hw.firewire.phydma_enable=0
```

## 硬件

`fwohci` 驱动程序为 PCI/CardBus FireWire 接口卡提供支持。本驱动程序支持以下 IEEE 1394 OHCI 芯片组：

- Adaptec AHA-894x/AIC-5800
- Apple Pangea
- Apple UniNorth
- Intel 82372FB
- IOGEAR GUF320
- Lucent / Agere FW322/323
- NEC uPD72861
- NEC uPD72870
- NEC uPD72871/2
- NEC uPD72873
- NEC uPD72874
- National Semiconductor CS4210
- Ricoh R5C551
- Ricoh R5C552
- Sony CX3022
- Sony i.LINK (CXD3222)
- Texas Instruments PCI4410A
- Texas Instruments PCI4450
- Texas Instruments PCI4451
- Texas Instruments TSB12LV22
- Texas Instruments TSB12LV23
- Texas Instruments TSB12LV26
- Texas Instruments TSB43AA22
- Texas Instruments TSB43AB21/A/AI/A-EP
- Texas Instruments TSB43AB22/A
- Texas Instruments TSB43AB23
- Texas Instruments TSB82AA2
- VIA Fire II (VT6306)

## 参见

[firewire(4)](firewire.4.md), [fwe(4)](fwe.4.md), [fwip(4)](fwip.4.md), [sbp(4)](sbp.4.md), fwcontrol(8), [kldload(8)](../man8/kldload.8.md)

## 历史

`fwohci` 设备驱动程序首次出现于 FreeBSD 5.0。

## 作者

`fwohci` 设备驱动程序由 Katsushi Kobayashi 和 Hidetoshi Shimokawa 编写。

## 缺陷

默认情况下，本驱动程序允许总线上任何节点进行物理访问。这意味着总线上任何设备都可以读取和修改 IEEE 1394 OHCI 芯片所能访问的任何内存空间。这主要是为 [sbp(4)](sbp.4.md) 设备而允许的。应当更改为仅对特定设备允许此访问。但无论如何，FireWire 是一种总线，不应与不可信的设备连接，因为任一节点都可以监视所有流量。
