# snd_t4dwave(4)

`snd_t4dwave` — Trident 4DWave 桥设备驱动

## 名称

`snd_t4dwave`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_t4dwave

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_t4dwave_load="YES"
```

## 描述

`snd_t4dwave` 桥驱动允许通用音频驱动 sound(4) 附加到 Trident 4DWave 音频设备。

## 硬件

`snd_t4dwave` 驱动支持以下音频设备：

- Acer Labs M5451
- SIS 7018
- Trident 4DWave DX
- Trident 4DWave NX

## 参见

sound(4)

## 历史

`snd_t4dwave` 设备驱动首次出现于 FreeBSD 4.0。

## 作者

本手册页由 Joel Dahl <joel@FreeBSD.org> 编写。
