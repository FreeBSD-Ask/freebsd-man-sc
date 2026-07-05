# `snd_davbus(4)`

`snd_davbus` — Apple Davbus 音频设备驱动

## 名称

`snd_davbus`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_davbus

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_davbus_load="YES"
```

## 描述

`snd_davbus` 驱动为许多 G3 时代 Apple 机器中常见的 Apple Davbus 音频控制器提供支持。

## 硬件

`snd_davbus` 驱动支持的芯片包括：

- Apple Burgundy Audio
- Apple Screamer Audio

## 参见

[snd_ai2s(4)](snd_ai2s.4.powerpc.md), sound(4)

## 历史

`snd_davbus` 设备驱动首次出现于 FreeBSD 8.0。

## 作者

`snd_davbus` 驱动由 Marco Trillo <marcotrillo@gmail.com> 编写。

## 缺陷

目前不支持录制。
