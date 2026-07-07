# snd_es137x(4)

`snd_es137x` — Ensoniq AudioPCI ES137x 桥设备驱动

## 名称

`snd_es137x`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_es137x

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_es137x_load="YES"
```

## 描述

`snd_es137x` 桥驱动允许通用音频驱动 sound(4) 附加到 Ensoniq 137x 声卡。

### 运行时配置

除了所有 sound(4) 设备可用的变量之外，还提供以下 [sysctl(8)](../man8/sysctl.8.md) 变量：

**`hw.snd.pcm%d.latency_timer`** 控制 PCI 延迟定时器设置。增大此值可解决大多数爆音和咔嗒声问题（尤其是在 VIA 主板上）。

**`hw.snd.pcm%d.spdif_enabled`** 在主播放声道上启用 S/PDIF 输出。仅当设备已知支持 S/PDIF 输出时，此 [sysctl(8)](../man8/sysctl.8.md) 变量才可用。

**`dev.pcm.%d.polling`** 实验性轮询模式，驱动通过使用 [callout(9)](../man9/callout.9.md) 在每个时钟滴答上查询设备状态来运行。轮询默认禁用。除非你遇到奇怪的中断问题，或者设备完全无法生成中断，否则不要启用它。

## 硬件

`snd_es137x` 驱动支持以下声卡：

- Creative CT5880-A
- Creative CT5880-C
- Creative CT5880-D
- Creative CT5880-E
- Creative SB AudioPCI CT4730
- Ensoniq AudioPCI ES1370
- Ensoniq AudioPCI ES1371-A
- Ensoniq AudioPCI ES1371-B
- Ensoniq AudioPCI ES1373-A
- Ensoniq AudioPCI ES1373-B
- Ensoniq AudioPCI ES1373-8

## 参见

sound(4)

## 历史

`snd_es137x` 设备驱动首次出现于 FreeBSD 4.0。

## 作者

Russell Cattelan <cattelan@thebarn.com> Cameron Grant <cg@FreeBSD.org> Joachim Kuebart Jonathan Noack <noackjr@alumni.rice.edu>
