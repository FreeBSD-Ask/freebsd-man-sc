# snd_atiixp.4

`snd_atiixp` — ATI IXP 桥设备驱动

## 名称

`snd_atiixp`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_atiixp

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_atiixp_load="YES"
```

## 描述

`snd_atiixp` 桥驱动允许通用音频驱动 sound(4) 附加到 ATI IXP 音频设备。此驱动支持 16 位播放和录制，以及 32 位原生播放和录制。

### 运行时配置

除了所有 sound(4) 设备可用的变量之外，还提供以下 [sysctl(8)](../man8/sysctl.8.md) 变量：

**`dev.pcm.%d.polling`** 实验性轮询模式，驱动通过使用 [callout(9)](../man9/callout.9.md) 在每个时钟滴答上查询设备状态来运行。轮询默认禁用。除非你遇到奇怪的中断问题，或者设备完全无法生成中断，否则不要启用它。

## 硬件

`snd_atiixp` 驱动支持以下音频芯片组：

- ATI IXP 200
- ATI IXP 300
- ATI IXP 400

## 参见

sound(4)

## 历史

`snd_atiixp` 设备驱动首次出现于 FreeBSD 6.1。

## 作者

本手册页由 Joel Dahl <joel@FreeBSD.org> 编写。

## 缺陷

`snd_atiixp` 驱动不支持 S/PDIF，但如果有合适的硬件，实现起来应该相当容易。

在某些硬件上 32 位原生录制无法正常工作。
