# snd_als4000.4

`snd_als4000` — Avance Logic ALS4000 PCI 桥设备驱动

## 名称

`snd_als4000`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_als4000

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_als4000_load="YES"
```

## 描述

`snd_als4000` 桥驱动允许通用音频驱动 sound(4) 附加到 ALS4000 声卡。

## 硬件

`snd_als4000` 驱动支持以下声卡：

- Avance Logic ALS4000

## 参见

sound(4)

## 历史

`snd_als4000` 设备驱动首次出现于 FreeBSD 4.4。

## 作者

Orion Hodson <oho@acm.org>
