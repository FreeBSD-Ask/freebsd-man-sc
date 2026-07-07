# snd_envy24ht(4)

`snd_envy24ht` — VIA Envy24HT 及兼容桥设备驱动

## 名称

`snd_envy24ht`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_envy24ht
> device snd_spicds

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_envy24ht_load="YES"
```

## 描述

`snd_envy24ht` 桥驱动允许通用音频驱动 sound(4) 附加到 VIA Envy24HT（ICE1724 或 VT1724 芯片组）及兼容音频设备。

## 硬件

`snd_envy24ht` 驱动支持以下音频设备：

- Audiotrak Prodigy 7.1
- Audiotrak Prodigy 7.1 LT
- Audiotrak Prodigy 7.1 XT
- Audiotrak Prodigy HD2
- ESI Juli@
- ESI Juli@ XTe
- M-Audio Audiophile 192
- M-Audio Revolution 5.1
- M-Audio Revolution 7.1
- Terratec Aureon 5.1 Sky
- Terratec Aureon 7.1 Space
- Terratec Aureon 7.1 Universe
- Terratec PHASE 22
- Terratec PHASE 28

仅支持模拟播放。不支持录制和这些卡的其他功能。

## 参见

sound(4)

## 历史

`snd_envy24ht` 设备驱动首次出现于 FreeBSD 6.3。

## 作者

`snd_envy24ht` 驱动由 Konstantin Dimitrov 编写，基于 [snd_envy24(4)](snd_envy24.4.md) 驱动。本手册页由 Alexander Leidinger <netchild@FreeBSD.org> 编写。
