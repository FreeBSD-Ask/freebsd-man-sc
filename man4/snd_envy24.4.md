# snd_envy24.4

`snd_envy24` — VIA Envy24 及兼容桥设备驱动

## 名称

`snd_envy24`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_envy24
> device snd_spicds

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_envy24_load="YES"
```

## 描述

`snd_envy24` 桥驱动允许通用音频驱动 sound(4) 附加到 VIA Envy24（ICE1724 或 VT1724 芯片组）及兼容音频设备。

## 硬件

`snd_envy24` 驱动支持以下音频设备：

- M-Audio Audiophile 2496
- M-Audio Delta Dio 2496
- Terratec DMX 6fire

仅支持模拟播放。不支持录制和这些卡的其他功能。

## 参见

sound(4)

## 历史

`snd_envy24` 设备驱动首次出现于 FreeBSD 6.3。

## 作者

`snd_envy24` 驱动由 Katsurajima Naoto 编写。本手册页由 Alexander Leidinger <netchild@FreeBSD.org> 编写。
