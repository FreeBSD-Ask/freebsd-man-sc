# snd_ai2s(4)

`snd_ai2s` — Apple I2S 音频设备驱动

## 名称

`snd_ai2s`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_ai2s

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_ai2s_load="YES"
```

## 描述

`snd_ai2s` 驱动为 G4 和 G5 机器中常见的 Apple I2S 音频控制器以及 snapper 和 tumbler 编解码器提供支持。某些机器（例如 Mac Mini）没有可配置的编解码器，因此缺少硬件音量控制。

## 硬件

`snd_ai2s` 驱动支持的芯片包括：

- Apple Tumbler Audio
- Apple Snapper Audio

## 参见

[snd_davbus(4)](snd_davbus.4.powerpc.md), sound(4)

## 历史

`snd_ai2s` 设备驱动首次出现于 NetBSD 2.0，后来出现于 FreeBSD 8.0。

## 作者

`snd_ai2s` 驱动由 Tsubai Masanari <tsubai@netbsd.org> 编写，并由 Marco Trillo <marcotrillo@gmail.com> 移植到 FreeBSD。

## 缺陷

目前不支持录制和非 44.1 kHz 音频操作。
