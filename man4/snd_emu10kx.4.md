# snd_emu10kx(4)

`snd_emu10kx` — Creative SoundBlaster Live! 和 Audigy 声卡设备驱动

## 名称

`snd_emu10kx`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_emu10kx

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_emu10kx_load="YES"
```

## 描述

`snd_emu10kx` 桥驱动允许通用音频驱动 sound(4) 附加到基于 EMU10K1、CA0100、CA0101、CA0102 和 CA0108 DSP 的 Creative 声卡。

`snd_emu10kx` 声卡具有 PCM 部分（可通过一至五个 [pcm(4)](pcm.4.md) 设备访问，详见多声道播放章节），以及可通过 midi 设备访问的 MPU401 兼容 MIDI I/O 控制器。不支持波表合成器。

## 硬件

`snd_emu10kx` 驱动支持以下声卡：

- Creative Sound Blaster Live!（EMU10K1 芯片组）。PCM 和 MIDI 接口均可用。
- Creative Sound Blaster Audigy（CA0100 和 CA0101 芯片组）。PCM 和两个 MIDI 接口可用。
- Creative Sound Blaster Audigy 2 和 Creative Sound Blaster Audigy 4（CA0102 芯片组）。PCM 支持仅限于 48kHz/16 位立体声（不支持此芯片组的 192kHz/24 位部分）。
- Creative Sound Blaster Audigy 2 Value（CA0108 芯片组）。PCM 支持仅限于 48kHz/16 位立体声（不支持此芯片组的 192kHz/24 位部分）。此卡没有 MIDI 支持。

`snd_emu10kx` 驱动**不**支持以下声卡（尽管它们的名字与某些受支持的声卡相似）：

- Creative Sound Blaster Live! 24-Bit，FreeBSD 将其标识为 "" `emu10k1x Soundblaster Live! 5.1`。
- Creative Sound Blaster Audigy LS / ES，FreeBSD 将其标识为 "" `CA0106-DAT Audigy LS`。
- 所有其他带有 -DAT 芯片组的 Creative 声卡。
- 所有 Creative X-Fi 系列声卡。

## 多声道播放

默认情况下，`snd_emu10kx` 驱动加载时启用多声道播放功能。如果不在 loader.conf(5) 配置文件中设置 `hint.emu10kx.0.multichannel_disabled` 选项，将获得最多五个 DSP 设备，每个声卡输出对应一个。可使用附加软件（如 *Ports Collection* 中的 *audio/pulseaudio*）进行音频流解复用。只有“FRONT”输出可以播放和录制来自外部源（如线路或 S/PDIF 输入）的音频。

## 多声道录制

默认情况下，加载 `snd_emu10kx` 驱动时不会启用多声道录制功能。如果在 loader.conf(5) 中启用 `hint.emu10kx.0.multichannel_recording` 选项，将获得一个额外的 DSP 设备，其速率锁定为 48kHz/16bit/单声道。实际上在 SB Live! 卡上是 48kHz/16bit/32 声道，在 Audigy 卡上是 48kHz/16bit/64 声道，但当前的声音子系统实现不支持如此多的 PCM 声道。此设备无法打开读取，从而会使许多应用程序感到困惑。

在多声道流中，前半部分（0-15 或 0-31）是所有 DSP 输出的副本，后半部分（15-30 或 32-63）是某些 DSP 输入的副本。在 Live! 卡上，最后一个子流（31）用作同步流，始终设置为 0xc0de。Audigy 卡不需要此类同步数据，因为流始终从子流 0 开始。

### SB Live! 子流映射（按字节偏移，每个子流为 2 字节 LE）

**`偏移`** 子流

**+0x00..+0x1E** PCM 流 0..15

**+0x20,** +0x22 空

**+0x24..+0x2A** PCM 输入：前左、前右、后左、后右、中置、低音

**+0x2C..+0x3C** DSP 输入 0..8：

**+0x3E** 同步子流（0xc0de）

### Audigy 子流映射（按字节偏移，每个子流为 2 字节 LE）

**`偏移`** 子流

**+0x00..+0x3E** PCM 流 0..31

**+0x40..+0x5E** PCM 输入：前 LR、后 LR、中置、低音、...

**+0x60..+0x7E** DSP 输入 0..16

## OSS 混音器控制

这些是通过标准 OSS 编程接口可用的控制。可使用 mixer(8) 来更改它们。

在基于 EMU10K1 的卡上，OSS 混音器直接控制 AC97 编解码器。在较新的卡上，OSS 混音器控制 AC97 编解码器的某些参数以及某些基于 DSP 的混音器控制。

**"vol"** 总体音量的混音器控制。

**"pcm"** PCM 播放音量的混音器控制。在多声道模式下仅控制前输出音量，在单声道模式下控制所有输出音量。

**"rec"** 混音器控制在 EMU10K1 和其他卡上的行为截然不同。在 EMU10K1 卡上，它控制 AC97 编解码器录制电平。在非 EMU10K1 卡上，它控制进入 DSP 的 AC97“立体声混音”量。AC97 录制电平和 AC97 录制源在 CA0100、CA0101、CA0102 和 CA0108 卡上是固定的。AC97 录制电平始终设为最大，录制源始终为 “`stereo mix`”。

**"dig1"** 是 CD S/PDIF（板载）音量控制

**"dig2"** 是 AudigyDrive S/PDIF（Audigy 系列）或 TOSLink（SB Live! 系列）音量控制

**"dig3"** 是板载 S/PDIF 音量控制

**"line2"** 是 AudigyDrive“Line In 2”音量控制

**"line3"** 是 AudigyDrive“AUX In 2”音量控制

其他 OSS 混音器控制用于控制 AC97 编解码器的输入。

## 私有设备控制

可通过 `dev.emu10kx.`<`X`> sysctl 控制 EMU10Kx 的某些操作和配置参数。这些 [sysctl(8)](../man8/sysctl.8.md) 值是临时的，不应依赖。

## 驱动配置

加载器可调参数用于设置驱动配置。可在引导内核前在 [loader(8)](../man8/loader.8.md) 提示符下设置可调参数，也可将其存储在 **/boot/loader.conf** 中。这些可调参数在引导后无法从机器 [sysctl(8)](../man8/sysctl.8.md) 入口更改，但可在加载 `snd_emu10kx` 驱动之前使用 [kenv(1)](../man1/kenv.1.md) 更改。

**0** 不启用任何附加调试选项

**1** 启用连接所有 DSP 输出，即使在特定卡上已知未使用的输出。

**2** 将打印有关驱动程序内事件的附加调试消息。

**2** 内存分配失败时将打印附加调试消息。

**`hint.emu10kx.`** <`X` >`.disabled`> 禁用加载驱动实例。

**`hint.emu10kx.`** <`X` >`.multichannel_disabled`> 禁用多声道播放支持，当一张卡表示为多个 PCM 设备时。

**`hint.emu10kx.`** <`X` >`.multichannel_recording`> 启用实验性多声道录制支持。

**`hint.emu10kx.`** <`X` >`.debug`> 设置调试输出级别。

## 文件

**`/dev/emu10kx?`** `snd_emu10kx` 管理接口

## 参见

sound(4)

## 历史

`snd_emu10kx` 设备驱动首次出现于 FreeBSD 7.0。

## 作者

该驱动的 PCM 部分基于 Cameron Grant <cg@FreeBSD.org> 编写的 [snd_emu10k1(4)](snd_emu10k1.4.md) SB Live! 驱动。MIDI 接口基于 Mathew Kanner <matk@FreeBSD.org> 编写的 [snd_emu10k1(4)](snd_emu10k1.4.md) MIDI 接口代码。`snd_emu10kx` 设备驱动和本手册页由 Yuriy Tsibizov 编写。

## 缺陷

驱动不会检测丢失的 S/PDIF 信号，并在 S/PDIF 未连接且 S/PDIF 音量不为零时产生噪声。

PCM 驱动无法检测 Live!Drive 或 AudigyDrive 转接盒的存在，并尝试使用它们（并在混音器中列出其连接器）。

MIDI 驱动无法检测 Live!Drive 或 AudigyDrive 转接盒的存在，并无论如何都尝试启用其上的 IR 接收器。
