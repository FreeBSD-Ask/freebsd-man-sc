# snd_csa.4

`snd_csa` — Crystal Semiconductor CS461x/462x/4280 PCI 桥设备驱动

## 名称

`snd_csa`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_csa

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_csa_load="YES"
```

## 描述

`snd_csa` 桥驱动允许通用音频驱动 sound(4) 附加到基于 Crystal Semiconductor CS461x/462x/4280 的声卡。

## 硬件

`snd_csa` 驱动支持以下声卡：

- Crystal Semiconductor CS4280
- Crystal Semiconductor CS4610
- Crystal Semiconductor CS4611
- Crystal Semiconductor CS4614
- Crystal Semiconductor CS4615
- Crystal Semiconductor CS4622
- Crystal Semiconductor CS4624
- Crystal Semiconductor CS4630
- Genius Soundmaker 128 Value
- Hercules Game Theatre XP
- Turtle Beach Santa Cruz

某些板载 CS4610 芯片搭配的是 CS423x ISA 编解码器，而非 CS4297 AC97 编解码器。`snd_csa` 驱动尚不支持此类配置。

## 参见

sound(4)

## 历史

`snd_csa` 设备驱动首次出现于 FreeBSD 4.0。

## 作者

Seigo Tanimura <tanimura@r.dl.itc.u-tokyo.ac.jp>
