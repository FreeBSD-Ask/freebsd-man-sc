# snd_ich(4)

`snd_ich` — Intel ICH AC'97 及兼容桥设备驱动

## 名称

`snd_ich`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_ich

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_ich_load="YES"
```

## 描述

`snd_ich` 桥驱动允许通用音频驱动 sound(4) 附加到 Intel ICH AC'97 及兼容音频设备。

某些较新的芯片，如 ICH6/ICH7，根据接线可能实现较新的 Intel HD Audio 规范，由 [snd_hda(4)](snd_hda.4.md) 驱动支持。

## 硬件

`snd_ich` 驱动支持以下音频设备：

- AMD 768
- AMD 8111
- Intel 443MX
- Intel ICH
- Intel ICH revision 1
- Intel ICH2
- Intel ICH3
- Intel ICH4
- Intel ICH5
- Intel ICH6
- Intel ICH7
- NVIDIA nForce
- NVIDIA nForce2
- NVIDIA nForce2 400
- NVIDIA nForce3
- NVIDIA nForce3 250
- NVIDIA nForce4
- SiS 7012

## 参见

[snd_hda(4)](snd_hda.4.md), sound(4)

## 历史

`snd_ich` 设备驱动首次出现于 FreeBSD 4.2。

## 作者

本手册页由 Jorge Mario G. Mazo <jgutie11@eafit.edu.co> 编写。
