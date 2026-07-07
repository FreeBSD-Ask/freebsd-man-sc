# snd_uaudio(4)

`snd_uaudio` — USB 音频与 MIDI 设备驱动

## 名称

`snd_uaudio`

## 概要

`device sound device usb device snd_uaudio`

`在 rc.conf(5) 中：kld_list="snd_uaudio"`

`在 sysctl.conf(5) 中：hw.usb.uaudio.buffer_ms hw.usb.uaudio.default_bits hw.usb.uaudio.default_channels hw.usb.uaudio.default_rate hw.usb.uaudio.handle_hid hw.usb.uaudio.debug`

## 描述

USB 音频设备由多个组件构成：输入终端（例如 USB 数字输入）、输出终端（例如扬声器）以及位于其间的多个单元（例如音量控制）。

如果设备支持多种配置，且用户未通过 [sysctl(8)](../man8/sysctl.8.md) 接口指定任何值，则驱动在附加时将选择设备所支持的最为匹配的配置。“最佳”是指具备最多声道且在采样率和样本大小方面具有最高质量的配置。

更多信息请参阅 `USB Audio Class Specification`。

## 硬件

`snd_uaudio` 驱动为 USB 音频类设备和 USB MIDI 类设备提供支持。

## SYSCTL 变量

以下设置可在 [loader(8)](../man8/loader.8.md) 提示符下输入或写入 loader.conf(5)，也可在运行时通过 [sysctl(8)](../man8/sysctl.8.md) 命令更改。要在运行时让更改生效，必须重新附加设备。

**0** 禁用。

**1** 启用。

**`hw.usb.uaudio.buffer_ms`** 一次处理的音频数据周期，以毫秒为单位，取值范围 1 至 8（默认为 4）。值越小延迟越低，但可能因频繁唤醒 CPU 而导致可听见的间隙。

**`hw.usb.uaudio.default_bits`** 首选的样本大小（以位为单位），取值范围 0 至 32（默认为 0）。值为 0 时将样本大小设为所支持的最大样本大小。如果设备支持多种样本大小，可设置此项以选择更小的样本大小。

**`hw.usb.uaudio.default_channels`** 首选的样本声道数，取值范围 0 至 64（默认为 0）。由于带宽限制，USB 1.1 设备最多只能使用 4 个声道，除非显式请求更高的值。值为 0 时将声道数设为所支持的最大声道数。如果设备支持多种声道配置，可设置此项以选择更小的声道数。

**`hw.usb.uaudio.default_rate`** 首选的采样率（单位为 Hz，默认为 0）。如果设为 0，将使用设备所支持的最高采样率。注意，如果启用了 VCHAN，采样率将被 `dev.pcm.%d.[play|rec].vchanrate` 覆盖（参见 sound(4)），后者也可用于在运行时调整采样率。如果 `hw.usb.uaudio.default_rate` 不为零，`dev.pcm.%d.[play|rec].vchanrate` 将使用它作为最大允许值。

**`hw.usb.uaudio.handle_hid`** 让 `snd_uaudio` 处理 HID 音量键（如果有，默认为 1）。

如果 [usb(4)](usb.4.md) 在编译时启用了 `USB_DEBUG`，则还可使用以下设置：

**`hw.usb.uaudio.debug`** 调试输出级别（默认为 0）。

## 参见

sound(4), [usb(4)](usb.4.md), loader.conf(5), [loader(8)](../man8/loader.8.md), [sysctl(8)](../man8/sysctl.8.md)

> "USB Audio Class Specifications".

## 历史

`snd_uaudio` 驱动首次出现于 FreeBSD 4.7。

## 作者

本手册页改编自 NetBSD 1.6，由 Hiten Pandya <hmp@FreeBSD.org> 为 FreeBSD 修改。

## 缺陷

FreeBSD 的 PCM 框架目前并不支持全部 USB 音频混音器控制。某些混音器控制只能通过 `dev.pcm.%d.mixer` sysctl 访问。
