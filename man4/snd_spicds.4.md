# snd_spicds.4

`snd_spicds` — I2S SPI 音频编解码器驱动

## 名称

`snd_spicds`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device snd_spicds

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_spicds_load="YES"
```

## 描述

`snd_spicds` I2S 编解码器驱动被多个使用所支持编解码器芯片的声卡的音频驱动使用。

## 硬件

`snd_spicds` 驱动支持以下编解码器：

- AK4358
- AK4381
- AK4396
- AK4524
- AK4528
- WM8770

## 参见

[snd_envy24(4)](snd_envy24.4.md), [snd_envy24ht(4)](snd_envy24ht.4.md), sound(4)

## 历史

`snd_spicds` 设备驱动首次出现于 FreeBSD 6.3。

## 作者

`snd_spicds` 驱动由 Konstantin Dimitrov 编写，基于 [snd_envy24(4)](snd_envy24.4.md) 驱动。本手册页由 Alexander Leidinger <netchild@FreeBSD.org> 编写。
