# snd_via8233(4)

`snd_via8233` — VIA Technologies VT8233 桥设备驱动

## 名称

`snd_via8233`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_via8233

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_via8233_load="YES"
```

## 描述

`snd_via8233` 桥驱动允许通用音频驱动 sound(4) 附加到 VIA VT8233 音频设备。这些音频芯片组集成在许多基于 VIA 的主板的南桥中。

### 运行时配置

除所有 sound(4) 设备都可使用的变量之外，还可使用以下 [sysctl(8)](../man8/sysctl.8.md) 变量：

**`dev.pcm.%d.polling`** 实验性轮询模式，驱动通过使用 [callout(9)](../man9/callout.9.md) 在每个时钟滴答上查询设备状态来运行。默认禁用。除非你遇到奇怪的中断问题或设备根本无法生成中断，否则不要启用此模式。

## 硬件

`snd_via8233` 驱动支持以下音频芯片组：

- VIA VT8233
- VIA VT8233A
- VIA VT8233C
- VIA VT8235
- VIA VT8237
- VIA VT8251

## 参见

sound(4)

## 历史

`snd_via8233` 设备驱动首次出现于 FreeBSD 4.7。

## 作者

本手册页由 Joel Dahl <joel@FreeBSD.org> 编写。

## 缺陷

`snd_via8233` 驱动不支持 S/PDIF。代码中存在部分支持，因此如果有合适的硬件，实现起来应当相当容易。
