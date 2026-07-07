# snd_cs4281(4)

`snd_cs4281` — Crystal Semiconductor CS4281 PCI 桥设备驱动

## 名称

`snd_cs4281`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_cs4281

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_cs4281_load="YES"
```

## 描述

`snd_cs4281` 桥驱动允许通用音频驱动 sound(4) 附加到 CS4281 声卡。

## 硬件

`snd_cs4281` 驱动支持以下声卡：

- Crystal Semiconductor CS4281

## 参见

sound(4)

## 历史

`snd_cs4281` 设备驱动首次出现于 FreeBSD 4.3。

## 作者

Orion Hodson <O.Hodson@cs.ucl.ac.uk>
