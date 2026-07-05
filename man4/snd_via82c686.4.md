# snd_via82c686.4

`snd_via82c686` — VIA Technologies 82C686A 桥设备驱动

## 名称

`snd_via82c686`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_via82c686

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_via82c686_load="YES"
```

## 描述

`snd_via82c686` 桥驱动允许通用音频驱动 sound(4) 附加到基于 VIA 82C686A 芯片组的音频设备。

## 硬件

`snd_via82c686` 驱动支持基于以下芯片组的音频设备：

- VIA 82C686A

## 参见

sound(4)

## 历史

`snd_via82c686` 设备驱动首次出现于 FreeBSD 4.2。

## 作者

本手册页由 Joel Dahl <joel@FreeBSD.org> 编写。
