# pcm.4

`sound` — FreeBSD PCM 音频设备基础设施

## 名称

`sound`, `pcm`, `snd` FreeBSD PCM 音频设备基础设施

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound

## 描述

`snd` 驱动是 FreeBSD 声音系统的主要组件。它与所支持设备上的桥设备驱动协同工作，并在附加后提供 PCM 音频录制和播放。每个桥设备驱动支持一组特定的音频芯片组，需要与 `snd` 驱动一起启用。PCI 和 ISA PnP 音频设备会自我标识，因此通常无需用户向 **/boot/device.hints** 中添加任何内容。

`snd` 驱动的一些主要特性包括：多声道音频、按应用程序音量控制、通过虚拟声道进行的动态混音、真正的全双工操作、bit-perfect 音频、速率转换和低延迟模式。

`snd` 驱动默认启用，并附带若干桥设备驱动。未默认启用的驱动可在运行时使用 [kldload(8)](../man8/kldload.8.md) 加载，或在引导时通过 loader.conf(5) 加载。可用的桥设备驱动有：

- [snd_ai2s(4)](snd_ai2s.4.powerpc.md)
- [snd_als4000(4)](snd_als4000.4.md)
- [snd_atiixp(4)](snd_atiixp.4.md)
- [snd_cmi(4)](snd_cmi.4.md)
- [snd_cs4281(4)](snd_cs4281.4.md)
- [snd_csa(4)](snd_csa.4.md)
- [snd_davbus(4)](snd_davbus.4.powerpc.md)
- [snd_emu10k1(4)](snd_emu10k1.4.md)
- [snd_emu10kx(4)](snd_emu10kx.4.md)
- [snd_envy24(4)](snd_envy24.4.md)
- [snd_envy24ht(4)](snd_envy24ht.4.md)
- [snd_es137x(4)](snd_es137x.4.md)
- [snd_fm801(4)](snd_fm801.4.md)
- [snd_hda(4)](snd_hda.4.md)
- [snd_hdsp(4)](snd_hdsp.4.md)
- [snd_hdspe(4)](snd_hdspe.4.md)
- [snd_ich(4)](snd_ich.4.md)
- [snd_maestro3(4)](snd_maestro3.4.md)
- [snd_neomagic(4)](snd_neomagic.4.md)
- [snd_solo(4)](snd_solo.4.md)
- [snd_spicds(4)](snd_spicds.4.md)
- [snd_uaudio(4)](snd_uaudio.4.md)
- [snd_via8233(4)](snd_via8233.4.md)
- [snd_via82c686(4)](snd_via82c686.4.md)
- [snd_vibes(4)](snd_vibes.4.md)

各桥设备驱动的特定设置和信息请参阅对应的手册页。

### 引导变量

通常，模块 `snd_foo` 对应于 `device snd_foo`，可由引导 [loader(8)](../man8/loader.8.md) 通过 loader.conf(5) 加载，或使用 [kldload(8)](../man8/kldload.8.md) 实用程序从命令行加载。可在 **/boot/loader.conf** 中指定的选项包括：

**`snd_driver_load`** （“`NO`”）若设为“`YES`”，此选项会加载所有可用驱动。

**`snd_hda_load`** （“`NO`”）若设为“`YES`”，仅加载 Intel High Definition Audio 桥设备驱动及其依赖模块。

**`snd_foo_load`** （“`NO`”）若设为“`YES`”，加载卡/芯片组 foo 的驱动。

要为不同混音器通道定义默认值，可使用 hints 将通道设为期望值，例如：`hint.pcm.0.line`="" `0`。这会默认静音输入通道。

### 多声道音频

多声道音频，通常被称为“环绕声”，受支持并默认启用。FreeBSD 多声道矩阵处理器支持最多 18 个交错声道，但目前限制设为 8 个声道（常用于 7.1 环绕声）。内部矩阵映射可处理声道的缩减、扩展或重路由。这为相关的多声道 Fn ioctl 支持提供了基础接口。多声道音频在有无 VCHAN 时均可工作。

大多数桥设备驱动仍缺少多声道矩阵支持，但在大多数情况下，实现起来应很简单。可使用 `dev.pcm.%d.[play|rec].vchanformat` [sysctl(8)](../man8/sysctl.8.md) 调整所使用的声道数。当前的多声道交错结构和排列方式是通过研究各种流行的 UNIX 应用程序实现的。由于没有单一标准，因此尽管每个应用程序都有自己的冲突标准，仍尽力尝试满足每种可能的场景。

### EQ

参数软件均衡器（EQ）支持使用“音调”控制（低音和高音）。常用于由于硬件质量差异较大而进行的声音修饰或频率补偿。

### VCHAN

每个设备可选择性地通过使用“虚拟声道”（VCHAN）支持比物理硬件提供的更多的播放和录制声道。VCHAN 选项可通过 [sysctl(8)](../man8/sysctl.8.md) 接口配置，但只能在设备非活动状态下进行操作。

### VPC

FreeBSD 为每个活动应用程序支持独立且个别的音量控制，而不会影响主 `snd` 音量。这有时被称为按通道音量（Volume Per Channel，VPC）。

### 运行时配置

有许多 [sysctl(8)](../man8/sysctl.8.md) 变量可在运行时修改。这些值也可存储在 **/etc/sysctl.conf** 中，以便在引导过程中自动设置。`hw.snd.*` 为全局设置，`dev.pcm.*` 为设备特定设置。

**-1** 强制禁用 PROT_EXEC mmap(2) 请求，即使是 Linux 应用程序。

**0** 仅允许 Linux 应用程序的 PROT_EXEC mmap(2) 请求。

**0** 不自动分配默认声音单元。

**1** 根据设备的播放和录制能力使用最佳可用声音设备。

**2** 使用最近附加的设备。

**0** 零阶保持（ZOH）。速度非常快，但质量较差。

**1** 线性插值。速度快，质量因人而异。但由于缺乏抗混叠滤波，技术上质量较差。

**2** 带限 SINC 插值器。实现多相滤波以提高转换速度，代价是内存使用量增加，并使用多个高质量多项式插值器来提高转换精度。100% 定点运算，64 位累加器配合 32 位系数和高精度采样缓冲。质量值为 100dB 阻带、8 抽头和 85% 带宽。

**3** 带限 SINC 插值器的延续，质量值为 100dB 阻带、36 抽头和 90% 带宽。

**4** 带限 SINC 插值器的延续，质量值为 100dB 阻带、164 抽头和 97% 带宽。

**0** 已安装的设备及其分配的总线资源。

**1** 每个设备的播放、录制、虚拟声道数和标志。

**2** 每个设备的通道信息，包括通道的当前格式、速度以及伪设备统计信息（如缓冲区溢出和缓冲区欠载）。

**3** 当前加载的声音模块的文件名和版本。

**4** 用于调试的各种消息。

**s16le:1.0** 单声道。

**s16le:2.0** 立体声，2 声道（左、右）。

**s16le:2.1** 3 声道（左、右、LFE）。

**s16le:3.0** 3 声道（左、右、后中置）。

**s16le:4.0** 四声道，4 声道（前/后左和右）。

**s16le:4.1** 5 声道（4.0 + LFE）。

**s16le:5.0** 5 声道（4.0 + 中置）。

**s16le:5.1** 6 声道（4.0 + 中置 + LFE）。

**s16le:6.0** 6 声道（4.0 + 前/后中置）。

**s16le:6.1** 7 声道（6.0 + LFE）。

**s16le:7.1** 8 声道（4.0 + 中置 + LFE + 左右侧）。

**fixed** 通道混音使用固定格式/速率进行。数字直通等高级操作将无法工作。可视为“传统”模式。这是缺乏数字格式支持的硬件声道的默认模式。

**passthrough** 通道混音使用固定格式/速率进行，但数字直通等高级操作也可工作。所有声道将照常发出声音，直到请求播放数字格式。发生此情况时，所有其他声道将被静音，并允许最新传入的数字格式不受干扰地通过。支持多个并发数字流，但最新流将优先并静音所有其他流。

**adaptive** 工作方式类似于“passthrough”模式，但更智能一些，特别是对于具有不同格式/速率的多个 `snd` 声道。当新声道即将启动时，将扫描整个虚拟声道列表，并选择具有最佳格式/速率（通常为最高/最大）的声道。这确保混音质量取决于最佳声道。缺点是需要重启硬件 DMA 模式，可能引起令人烦恼的爆音或咔嗒声。

**`hw.snd.compat_linux_mmap`** 此 [sysctl(8)](../man8/sysctl.8.md) 变量仅在 Linux 应用程序支持被编译进内核时才可用，并且仅影响 Linux 二进制文件。它是一种权宜之计，用于解决如下情况：对于 i386 仿真，[linux(4)](linux.4.md) 在 mmap(2) 调用期间设置 PROT_READ 或 PROT_WRITE 时会自动设置 PROT_EXEC，而 FreeBSD 不会。支持以下值（默认为 -1）：

**`hw.snd.default_auto`** 自动分配默认声音单元。支持以下值（默认为 1）：

**`hw.snd.default_unit`** 具有多个声卡的系统的默认声卡。使用 [devfs(4)](devfs.4.md) 时，`/dev/dsp` 的默认设备。等价于从 `/dev/dsp` 到 `/dev/dsp``${hw.snd.default_unit}` 的符号链接。

**`hw.snd.feeder_eq_exact_rate`** 仅某些速率允许进行精确处理。但默认行为是允许对所有速率进行宽松处理，即使是不支持的速率。启用以切换此要求，仅允许对支持的速率进行处理。

**`hw.snd.feeder_rate_max`** 允许的最大采样速率。

**`hw.snd.feeder_rate_min`** 允许的最小采样速率。

**`hw.snd.feeder_rate_polyphase_max`** 调整以设置在构建重采样滤波器过程中允许的最大多相条目数。禁用多相重采样可减少内存使用量，代价是转换速度更慢且质量更低。仅在使用 SINC 插值器时适用。默认值为 183040。设为 0 可禁用多相重采样。

**`hw.snd.feeder_rate_quality`** 采样速率转换器质量。默认值为 1，线性插值。可用选项包括：

**`hw.snd.feeder_rate_round`** 采样速率舍入阈值，以牺牲精度为代价避免大质数除法。所有请求的采样速率将被舍入到最近的阈值值。可能值介于 0（禁用）和 500 之间。默认为 25。

**`hw.snd.latency`** 配置缓冲延迟。仅影响未显式请求块大小/片段的应用程序。此可调参数提供比 `hw.snd.latency_profile` 可调参数更细的粒度。可能值介于 0（最低延迟）和 10（最高延迟）之间。

**`hw.snd.latency_profile`** 为 `hw.snd.latency` 可调参数定义一组缓冲延迟转换表。值为 0 将使用低且激进的延迟配置文件，如果应用程序无法跟上快速的中断速率（特别是在高工作负载下），可能导致欠载。默认值为 1，被视为适度/安全的延迟配置文件。

**`hw.snd.vchans_enable`** 全局 VCHAN 设置，用于启用（1）或禁用（0）VCHAN。可通过使用 `dev.pcm.%d.[play|rec].vchans` 可调参数为单个设备覆盖此设置。默认启用。

**`hw.snd.report_soft_formats`** 如果可用，则透明地控制内部格式转换到应用程序软件。当禁用或不可用时，应用程序只能选择设备原生支持的格式。

**`hw.snd.report_soft_matrix`** 即使硬件不支持，也启用无缝声道矩阵。使得即使是简单的立体声卡也能播放多声道流。

**`hw.snd.verbose`** `/dev/sndstat` 设备的详细程度级别。较高的值包含更多输出，在报告问题时应使用最高级别（即四级）。其他选项包括：

**`hw.snd.vpc_0db`** `snd` 音量的默认值。增大以给衰减控制留出更多空间。减小以获得更多放大，但可能导致声音削波。

**`hw.snd.vpc_autoreset`** 当声道关闭时，声道音量将重置为 0db。这意味着对音量的任何更改都将丢失。启用此项将保留音量，但代价是当应用程序尝试重新打开同一设备时可能会产生混淆。

**`hw.snd.vpc_reset`** 启用以将所有声道音量恢复为默认值 0db。

**`dev.pcm.%d.bitperfect`** 启用或禁用 bitperfect 模式。启用时，声道将跳过所有 dsp 处理，如声道矩阵、速率转换和均衡。纯净的 `snd` 流将直接馈送到硬件。如果启用了 VCHAN，bitperfect 模式将使用 VCHAN 格式/速率作为确定的格式/速率目标。使用 bitperfect 模式的推荐方法是禁用 VCHAN 并启用此 sysctl。默认禁用。

**`dev.pcm.%d.eq`** 设为 1 或 0 以启用（1）或禁用（0）均衡器。默认禁用。启用后，可使用混音器低音和高音控制，以及 `dev.pcm.%d.eq_preamp` 可调参数。

**`dev.pcm.%d.eq_preamp`** 均衡器前置放大器（以 dB 为单位）。必须启用 `dev.pcm.%d.eq` 此可调参数才生效。请阅读可调参数描述以查看可用值范围。

**`dev.pcm.%d.[play|rec].vchans`** 启用（1）或禁用（0）VCHAN。默认启用。

**`dev.pcm.%d.[play|rec].vchanformat`** VCHAN 混音的格式。所有播放路径将在混音过程开始之前转换为此格式。默认仅启用 2 个声道。可用选项包括：

**`dev.pcm.%d.[play|rec].vchanmode`** VCHAN 格式/速率选择。可用选项包括：

**`dev.pcm.%d.[play|rec].vchanrate`** VCHAN 混音的采样速率。所有播放路径将在混音过程开始之前转换为此采样速率。

**`dev.pcm.%d.polling`** 实验性轮询模式支持，驱动通过使用 [callout(9)](../man9/callout.9.md) 机制在每个时钟滴答上查询设备状态来运行。默认禁用，目前仅对少数设备驱动可用。

### 统计信息

声道统计信息仅在设备打开时才保留。因此，对于涉及溢出和欠载的情况，请在出错的应用程序打开并运行时考虑输出。

### IOCTL 支持

驱动支持大多数 OSS Fn ioctl 函数，大多数应用程序无需修改即可工作。存在一些差异，内存映射播放原生支持和 Linux 仿真中均支持，但由于 VM 系统设计，不支持内存映射录制。因此，某些应用程序可能需要使用稍加修改的音频模块重新编译。参见

`#include <sys/soundcard.h>`

以获取支持的 Fn ioctl 函数的完整列表。

### kqueue 支持

`kevent` 结构的字段定义如下：

- 计算等待时间并调用 clock_nanosleep(2)。
- 调用 ioctl(2) 执行 `SNDCTL_DSP_GETIPTR` 或 `SNDCTL_DSP_GETOPTR` 以获取内存映射缓冲区中新数据起始处的指针。
- 调用 ioctl(2) 执行 `SNDCTL_DSP_GETERROR` 以获取溢出/欠载并处理它们。

- `ext[0]` 对于使用 mmap(2) 的设备，它包含录制时 `SNDCTL_DSP_GETIPTR` 报告的 `count_info.ptr` 字段或播放时 `SNDCTL_DSP_GETOPTR` 报告的字段，而对于不使用 mmap(2) 的设备，它包含录制时 `SNDCTL_DSP_CURRENT_IPTR` 报告的 `oss_count_t.fifo_samples` 字段或播放时 `SNDCTL_DSP_CURRENT_OPTR` 报告的字段。
- `ext[1]` 包含录制事件的 `audio_errinfo.rec_overruns` 字段或播放事件的 `audio_errinfo.play_underruns` 字段，由 `SNDCTL_DSP_GETERROR` 报告。这允许单个 `kevent` 报告数据已就绪、可读取或写入的字节数、当前缓冲区位置和当前错误计数。这对于使用 mmap(2) 的场景特别有用，因为如果没有 kqueue(2)，典型的处理循环包括：

**`ident`** 设备的文件描述符。

**`filter`** 用于处理事件的内核过滤器。对于录制为 `EVFILT_READ`，对于播放为 `EVFILT_WRITE`。

**`data`** 可读取或写入的字节数。

**`ext`**

## 文件

`snd` 驱动可能创建以下设备节点：

**`/dev/dsp%d`** 音频设备。该数字表示设备的单元号。
**`/dev/dsp`** `/dev/dsp${hw.snd.default_unit}` 的别名。仅在设置了 `hw.snd.basename_clone` 时可用。
**`/dev/sndstat`** 当前 `snd` 状态，包括所有声道和驱动。

所有 `snd` 设备都列在 `/dev/sndstat` 中。在探测和附加设备时有时会记录额外消息，可使用 [dmesg(8)](../man8/dmesg.8.md) 实用程序查看这些消息。

用户必须是 audio 组的成员才能访问 `snd` 创建的任何设备节点，以及设备驱动和 virtual_oss(8)。

## 实例

使用 sound 元驱动一次性加载所有 `snd` 桥设备驱动（例如，当不清楚应使用哪个驱动时）：

```sh
kldload snd_driver
```

加载特定的桥设备驱动，此处为 Intel High Definition Audio 驱动：

```sh
kldload snd_hda
```

检查所有检测到的 `snd` 设备的状态：

```sh
cat /dev/sndstat
```

更改默认声音设备，此处更改为第二个设备。当有多个 `snd` 设备可用时很方便：

```sh
mixer -d pcm1
```

## 诊断

- pcm%d:play:%d:dsp%d.p%d: play interrupt timeout, channel dead 硬件未生成中断以处理传入（播放）或传出（录制）数据。
- unsupported subdevice XX 设备节点未正确创建。

## 参见

[devfs(4)](devfs.4.md), [snd_ai2s(4)](snd_ai2s.4.powerpc.md), [snd_als4000(4)](snd_als4000.4.md), [snd_atiixp(4)](snd_atiixp.4.md), [snd_cmi(4)](snd_cmi.4.md), [snd_cs4281(4)](snd_cs4281.4.md), [snd_csa(4)](snd_csa.4.md), [snd_davbus(4)](snd_davbus.4.powerpc.md), [snd_emu10k1(4)](snd_emu10k1.4.md), [snd_emu10kx(4)](snd_emu10kx.4.md), [snd_envy24(4)](snd_envy24.4.md), [snd_envy24ht(4)](snd_envy24ht.4.md), [snd_es137x(4)](snd_es137x.4.md), [snd_fm801(4)](snd_fm801.4.md), [snd_hda(4)](snd_hda.4.md), [snd_hdsp(4)](snd_hdsp.4.md), [snd_hdspe(4)](snd_hdspe.4.md), [snd_ich(4)](snd_ich.4.md), [snd_maestro3(4)](snd_maestro3.4.md), [snd_neomagic(4)](snd_neomagic.4.md), [snd_solo(4)](snd_solo.4.md), [snd_spicds(4)](snd_spicds.4.md), snd_t4dwave(4), [snd_uaudio(4)](snd_uaudio.4.md), [snd_via8233(4)](snd_via8233.4.md), [snd_via82c686(4)](snd_via82c686.4.md), [snd_vibes(4)](snd_vibes.4.md), [device.hints(5)](../man5/device.hints.5.md), loader.conf(5), [dmesg(8)](../man8/dmesg.8.md), [kldload(8)](../man8/kldload.8.md), mixer(8), [sysctl(8)](../man8/sysctl.8.md), virtual_oss(8)

> "Cookbook formulae for audio EQ biquad filter coefficients (Audio-EQ-Cookbook.txt), by Robert Bristow-Johnson".

> "Julius O'Smith's Digital Audio Resampling".

> "Polynomial Interpolators for High-Quality Resampling of Oversampled Audio, by Olli Niemitalo".

> "The OSS API".

## 历史

`snd` 设备驱动首次出现于 FreeBSD 2.2.6，名为 `pcm`，由 Luigi Rizzo 编写。后来在 FreeBSD 4.0 中由 Cameron Grant 重写。API 演变自 VOXWARE 标准，后者后来成为 OSS 标准。

## 作者

Luigi Rizzo <luigi@iet.unipi.it> 最初编写了 `pcm` 设备驱动和本手册页。Cameron Grant <gandalf@vilnya.demon.co.uk> 后来为 FreeBSD 4.0 修订了设备驱动。Seigo Tanimura <tanimura@r.dl.itc.u-tokyo.ac.jp> 修订了本手册页。之后为 FreeBSD 5.2 重写。

## 缺陷

某些声卡功能（例如全局音量控制）可能并非在所有设备上都受支持。

某些音频设备可能拒绝正常工作，除非为录制和播放配置相同的采样速率，即使仅使用单工模式。参见 `dev.pcm.%d.[play|rec].vchanrate` sysctl。
