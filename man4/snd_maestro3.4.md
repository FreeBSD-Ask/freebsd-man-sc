# snd_maestro3(4)

`snd_maestro3` — ESS Maestro3/Allegro-1 桥设备驱动

## 名称

`snd_maestro3`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_maestro3

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_maestro3_load="YES"
```

## 描述

`snd_maestro3` 驱动在 PCM 框架下为 ESS Maestro3 和 Allegro-1 声音芯片提供支持。这些芯片主要见于笔记本电脑，具有 AC97 混音器、一个可在硬件中混合最多四个数字音频流的多声道采样速率转换器、录制支持以及外部音量控制按钮。

声音处理器的固件采用 GNU 公共许可证授权，因此此驱动不包括在默认的 `GENERIC` 内核中。

## 硬件

`snd_maestro3` 驱动支持以下音频设备：

- ESS Technology Allegro-1
- ESS Technology Maestro3

## 诊断

硬件音量控制按钮可连接到芯片上两组不同的引脚（GPIO 或 GD），具体取决于制造商。驱动无法确定此配置，因此可使用提示覆盖默认猜测。硬件音量控制的默认设置假定 GD 引脚连接到硬件音量。对于 GPIO 引脚连接到硬件音量控制按钮的系统，请在文件 **/boot/device.hints** 中添加“`hint.pcm.0.hwvol_config="0"`”行以覆盖默认设置。

## 参见

sound(4), loader.conf(5)

## 历史

`snd_maestro3` 驱动首次出现于 FreeBSD 4.3。

## 作者

Scott Long <scottl@FreeBSD.org> Darrel Anderson <anderson@cs.duke.edu>
