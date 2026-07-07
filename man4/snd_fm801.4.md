# snd_fm801(4)

`snd_fm801` — Forte Media FM801 桥设备驱动

## 名称

`snd_fm801`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_fm801

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_fm801_load="YES"
```

## 描述

`snd_fm801` 桥驱动允许通用音频驱动 sound(4) 附加到基于 Forte Media FM801 芯片组的音频设备。这是 OEM 制造商在各种部件中使用的常见芯片组。

## 硬件

`snd_fm801` 驱动支持基于以下芯片组的音频设备：

- Forte Media FM801

## 参见

sound(4)

## 历史

`snd_fm801` 设备驱动首次出现于 FreeBSD 4.2。

## 作者

本手册页由 Joel Dahl <joel@FreeBSD.org> 编写。

## 缺陷

Forte Media FM801 芯片组是一种 PCI 桥，而非真正的声音控制器，因此可能存在无声卡支持。问题在于带声音支持和不带声音支持的芯片组都使用相同的 PCI ID。这使得无法确定安装的是哪一种。
