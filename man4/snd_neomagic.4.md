# snd_neomagic.4

`snd_neomagic` — NeoMagic 256AV/ZX 桥设备驱动

## 名称

`snd_neomagic`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_neomagic

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_neomagic_load="YES"
```

## 描述

`snd_neomagic` 桥驱动允许通用音频驱动 sound(4) 附加到 NeoMagic 256AV/ZX 音频设备。这些芯片多见于笔记本电脑。

## 硬件

`snd_neomagic` 驱动支持以下音频设备：

- NeoMagic 256AV
- NeoMagic 256ZX

## 参见

sound(4)

## 历史

`snd_neomagic` 设备驱动首次出现于 FreeBSD 4.0。

## 作者

本手册页由 Joel Dahl <joel@FreeBSD.org> 编写。
