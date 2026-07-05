# snd_emu10k1.4

`snd_emu10k1` — SoundBlaster Live! 和 Audigy PCI 桥设备驱动

## 名称

`snd_emu10k1`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_emu10k1

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_emu10k1_load="YES"
```

## 描述

`snd_emu10k1` 桥驱动允许通用音频驱动 sound(4) 附加到 SoundBlaster Live! 和 Audigy 声卡。

默认支持数字输出。

## 硬件

`snd_emu10k1` 驱动支持以下声卡：

- Creative SoundBlaster Live!（EMU10K1 芯片组）
- Creative SoundBlaster Audigy（EMU10K2 芯片组）
- Creative SoundBlaster Audigy 2（EMU10K2 芯片组）
- Creative SoundBlaster Audigy 2（EMU10K3 芯片组）

## 参见

sound(4)

## 历史

`snd_emu10k1` 设备驱动首次出现于 FreeBSD 4.1。

## 作者

David O'Brien <obrien@FreeBSD.org> Orlando Bassotto <orlando.bassotto@ieo-research.it> Cameron Grant <cg@FreeBSD.org>

## 缺陷

不支持 DD5.1 输出等高级功能。
