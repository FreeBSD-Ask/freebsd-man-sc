# snd_hdspe(4)

`snd_hdspe` — RME HDSPe 桥设备驱动

## 名称

`snd_hdspe`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_hdspe

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_hdspe_load="YES"
```

## 描述

`snd_hdspe` 桥驱动允许通用音频驱动 sound(4) 附加到 RME HDSPe 音频设备。

## 硬件

`snd_hdspe` 驱动支持以下音频设备：

- RME HDSPe AIO（可选 AO4S-192 和 AI4S-192 扩展板）
- RME HDSPe RayDAT

默认情况下，每个 [pcm(4)](pcm.4.md) 设备对应声卡上的一个物理端口。对于 ADAT 端口，支持 8 声道、4 声道和 2 声道格式。ADAT 声道的有效数量在单倍速率（32kHz-48kHz）下为 8 声道，在双倍速率（64kHz-96kHz）下为 4 声道，在四倍速率（128kHz-192kHz）下为 2 声道。根据所选的采样速率和声道格式，并非所有 pcm 声道都能映射到 ADAT 声道，反之亦然。

## 加载器可调参数

这些设置可在 [loader(8)](../man8/loader.8.md) 提示符下或 loader.conf(5) 中输入。

**`hw.hdspe.unified_pcm`** 如果设为 1，所有物理端口合并为一个统一的 pcm 设备。在多声道音频软件中打开时，这使所有端口同时可用且完全同步。生成的声道数请参阅下表：

| 声卡 | 单倍速率 Play \| Rec | 双倍速率 Play \| Rec | 四倍速率 Play \| Rec |
| ---- | -------------------- | -------------------- | -------------------- |
| HDSPe AIO | 20 \| 18 | 16 \| 14 | 14 \| 12 |
| HDSPe RayDAT | 36 \| 36 | 20 \| 20 | 12 \| 12 |

## SYSCTL 可调参数

这些设置和信息值可在运行时使用 [sysctl(8)](../man8/sysctl.8.md) 命令访问。如果安装了多张 RME HDSPe 声卡，每个设备都有单独的配置。要为特定声卡调整以下 sysctl 标识符，请将相应的设备号替换 `0`。

**`dev.hdspe.0.sample_rate`** 设置从 32000、44100、48000 直至 192000 的固定采样速率。这通常用于数字连接（AES、S/PDIF、ADAT）。默认值 0 根据 pcm 设备设置调整采样速率。

**`dev.hdspe.0.period`** 每次中断处理的采样数，从 32、64、128 直至 4096。设置较低值可减少延迟，但由于频繁的中断处理会增加系统负载。极端值可能导致音频间断和故障。

**`dev.hdspe.0.clock_list`** 列出可同步的可能时钟源，具体取决于硬件型号。这包括内部和外部主时钟以及传入的数字音频信号，如 AES、S/PDIF 和 ADAT。

**`dev.hdspe.0.clock_preference`** 从时钟列表中选择首选时钟源。HDSPe 卡在可用时将同步到此时钟源，但回退到自动同步它们接收的任何其他数字时钟信号。如果 HDSPe 卡应作为主时钟，请将此项设为 `internal`。

**`dev.hdspe.0.clock_source`** 显示使用中的实际时钟源（只读）。在自动同步模式下，这与设置为时钟首选项的值不同。

**`dev.hdspe.0.sync_status`** 显示所有外部时钟源的当前同步状态。状态指示为 `none` 表示完全没有信号，`lock` 表示存在有效信号，`sync` 表示准确同步的信号（录制数字音频所需）。

以下可调参数仅适用于 HDSPe AIO 设备：

**`dev.hdspe.0.input_level`** 选择模拟线路输入的灵敏度。输入信号的可用参考电平为 `LowGain`、`+4dBu` 和 `-10dBV`。

**`dev.hdspe.0.output_level`** 选择模拟线路输出的增益电平。输出信号的可用参考电平为 `HighGain`、`+4dBu` 和 `-10dBV`。

**`dev.hdspe.0.phones_level`** 单独调整耳机输出的增益电平，与模拟线路输出分开。输出信号的可用参考电平为 `HighGain`、`+4dBu` 和 `-10dBV`。

在适当情况下，这些 sysctl 值以其他平台上的官方 RME 软件为模型，并采用其术语。请查阅 RME 用户手册以获取更多信息。

## 参见

sound(4)

## 历史

`snd_hdspe` 设备驱动首次出现于 FreeBSD 10.0。

## 作者

`snd_hdspe` 驱动由 Ruslan Bukin <br@bsdpad.com> 编写。Florian Walpen <dev@submerge.ch> 贡献了时钟源设置并重构了 pcm 设备映射。
