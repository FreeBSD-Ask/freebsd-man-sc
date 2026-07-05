# aq.4

`aq` — Aquantia/Marvell AQ1xx 10 千兆以太网驱动

## 名称

`aq`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device aq

要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_aq_load="YES"
```

## 描述

`aq` 设备驱动为基于 Aquantia（现为 Marvell）AQtion AQC1xx 以太网控制器的 PCIe 1/2.5/5/10 千兆以太网适配器提供支持。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

`aq` 驱动是实验性的，存在许多注意事项和限制。

## 硬件

`aq` 驱动支持以下 10 千兆以太网 PCIe 控制器：

- aQuantia AQC107
- aQuantia AQC108
- aQuantia AQC109
- aQuantia AQC111
- aQuantia AQC112

## 参见

arp(4), [miibus(4)](miibus.4.md), [ifconfig(8)](../man8/ifconfig.8.md)
