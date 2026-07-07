# snd_solo(4)

`snd_solo` — ESS Solo-1/1E PCI 桥设备驱动

## 名称

`snd_solo`

## 概要

`device sound device snd_solo`

## 描述

`snd_solo` 桥驱动允许通用音频驱动 sound(4) 附加到 ESS Solo-1x PCI 卡。

## 硬件

`snd_solo` 驱动支持以下声卡：

- ESS Solo-1（ES1938 芯片组）
- ESS Solo-1E（ES1946 芯片组）

## 参见

sound(4)

## 历史

`snd_solo` 设备驱动首次出现于 FreeBSD 4.1。

## 作者

Cameron Grant <cg@FreeBSD.org>
