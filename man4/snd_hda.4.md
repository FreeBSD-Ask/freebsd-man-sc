# snd_hda.4

`snd_hda` — Intel High Definition Audio 桥设备驱动

## 名称

`snd_hda`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound
> device snd_hda

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_hda_load="YES"
```

## 描述

High Definition (HD) Audio 规范由 Intel 开发，作为旧 AC'97 规范的逻辑继任者，具有多项优势，例如更高的带宽（允许更多声道和更精细的格式）、对多个逻辑音频设备的支持以及通用 DMA 声道。

`snd_hda` 驱动包括 HDA 总线控制器驱动 (hdac)、HDA 编解码器驱动 (hdacc) 和 HDA 编解码器音频功能桥驱动 (hdaa)，允许通用音频驱动 sound(4) 与此硬件一起使用。`snd_hda` 仅支持音频功能。调制解调器和其他可能的功能未实现。

`snd_hda` 驱动支持符合 Intel High Definition Audio 规范 1.0 版本的硬件，并尝试在处理音频设备时表现得类似于 Microsoft Universal Audio Architecture (UAA) 草案（0.7b 版）。

根据 HDA 和 UAA 规范，取决于系统中存在的 HDA 总线和编解码器数量、其音频功能和 BIOS 提供的配置，`snd_hda` 驱动通常提供多个 PCM 音频设备。例如，一个用于主后 7.1 输出和输入的设备，一个用于前面板独立耳机连接器的设备，以及一个用于 SPDIF 或 HDMI 音频输入/输出的设备。音频输入和输出的分配可通过 [device.hints(5)](../man5/device.hints.5.md) 或 [sysctl(8)](../man8/sysctl.8.md) 调整。驱动的详细引导消息提供了大量有关驱动操作和当前音频设置的信息。

默认音频设备可通过设置 `hw.snd.default_unit` sysctl 来调整（如 sound(4) 中所述），或在应用程序设置中显式指定。

### 引导时配置

以下变量可在引导时通过 [device.hints(5)](../man5/device.hints.5.md) 文件使用：

**0** 禁用，
**1** 附加时一次，
**2** 启用。

**`hint.hdac.%d.config`** 配置一系列可能的控制器选项。可能值为：“`64bit`”、“`dmapos`”、“`msi`”。以“`no`”为前缀的选项（如“`nomsi`”）执行相反操作并优先。选项可用空格和逗号分隔。

**`hint.hdac.%d.msi`** 控制 MSI（消息信号中断）支持。

**`hint.hdac.%d.cad%d.nid%d.config`** 同 `hint.hdaa.%d.nid%d.config`

**`hint.hdaa.%d.config`** 配置一系列可能的音频功能选项。可能值为：“`eapdinv`”、“`ivref`”、“`ivref50`”、“`ivref80`”、“`ivref100`”、“`fixedrate`”、“`forcestereo`”、“`ovref`”、“`ovref50`”、“`ovref80`”、“`ovref100`”、“`senseinv`”、“`softpcmvol`”和“`vref`”。以“`no`”为前缀的选项（如“`nofixedrate`”）执行相反操作并优先。选项可用空格和逗号分隔。“`eapdinv`”选项反转外部放大器电源关闭信号。“`fixedrate`”拒绝除 48KHz 外的所有采样速率。“`forcestereo`”拒绝单声道播放/录制。“`senseinv`”选项反转插孔检测逻辑。“`ivref``X`”和“`ovref``X`”选项控制用于为外部麦克风供电的电压。

**`dev.hdaa.%d.init_clear`** 清零系统设置的引脚组件配置。某些系统在清除引脚组件配置后似乎会出现不可用的音频设备。将此值设为 0 以接受 BIOS 设置的默认配置值。

**`hint.hdaa.%d.gpio_config`** 覆盖 BIOS 设置的音频功能 GPIO 引脚配置。可指定为一组以空格分隔的“`num`=`value`”对，其中 `num` 是 GPIO 线号，`value` 为以下之一：“`keep`”、“`set`”、“`clear`”、“`disable`”和“`input`”。“`GPIO`s”是编解码器的通用 I/O 引脚，系统集成商有时使用它们来控制外部静音器、放大器等。如果没有声音或音量不足，可能需要尝试 GPIO 设置以找到系统的最佳配置。

**`hint.hdaa.%d.nid%d.config`** 覆盖 BIOS 设置的音频功能引脚配置。可指定为以“0x”开头的 32 位十六进制值，或一组以空格分隔的“`option`=`value`”对。

**`hint.pcm.%d.rec.autosrc`** 控制自动录制源功能：启用时，驱动会使用插孔存在检测状态自动将混音器的录制源设置为已连接的输入。

引脚配置是 UAA 驱动有关编解码器使用情况的主要信息来源。此信息通常由编解码器制造商提供，并由系统集成商针对特定系统要求进行调整。`snd_hda` 驱动允许用户覆盖它以修复集成商错误或以替代方式使用可用编解码器（例如，获取立体声输出和 2 个输入而非单个 5.1 输出）。

支持以下选项：

**`as`** 关联号。关联用于将各个引脚分组以形成复杂的多引脚设备。例如，将 4 个连接器分组用于 7.1 输入/输出，或将多个输入连接器视为同一输入设备的源。关联号可指定为 0 到 15 的数值。值 0 表示禁用引脚。值 15 是一组独立的非关联引脚。每个关联仅包含同方向（输入/输出）的引脚，并且是原子检测的（所有引脚或无）。每对输入和输出关联创建一个独立的 PCM 音频设备。

**`seq`** 序列号。一个唯一的、按关联的编号，用于对特定关联内的引脚进行排序。序列号可指定为 0 到 15 的数值。序列号 15 对输出关联有特殊含义。具有此编号和设备类型“`Headphones`”的输出引脚将复制（如果支持插孔检测，则自动静音）该关联中的第一个引脚。序列号 14 和 15 对输入关联有特殊含义。它们在关联中的存在分别将其定义为多路复用或混合。如果两者都不存在且关联中有多个引脚，则该关联将提供多声道输入。对于多声道输入/输出关联，序列号编码声道对位置：0 - 前、1 - 中置/低音、2 - 后、3 - 前宽中置、4 - 侧。标准组合有：(0) - 立体声；(0, 2)、(0, 4) - 四声道；(0, 1, 2)、(0, 1, 4) - 5.1；(0, 1, 2, 4) - 7.1。

**`device`** 设备类型。可指定为 0 到 15 的数字或名称：“`Line-out`”、“`Speaker`”、“`Headphones,`” “`CD`”、“`SPDIF-out`”、“`Digital-out`”、“`Modem-line`”、“`Modem-handset`”、“`Line-in`”、“`AUX`”、“`Mic`”、“`Telephony`”、“`SPDIF-in`”、“`Digital-in`”、“`Res.E`”或“`Other`”。设备类型还描述了引脚方向（输入/输出）。例如，“`CD`”始终表示输入引脚，而“`Headphones`”始终表示输出。

**`conn`** 连接类型。可指定为 0 到 3 的数字。连接类型也可指定为特殊名称“`Jack`”、“`None`”、“`Fixed`”或“`Both`”之一。连接类型为“`None`”的引脚被禁用。

**`ctype`** 连接器物理类型。可指定为 0 到 15 的数字。这是仅供参考的值。`snd_hda` 驱动会忽略它。

**`color`** 连接器颜色。可指定为 0 到 15 的数字或以下名称之一：“`Unknown`”、“`Black`”、“`Grey`”、“`Blue`”、“`Green`”、“`Red`”、“`Orange`”、“`Yellow`”、“`Purple`”、“`Pink`”、“`Res.A`”、“`Res.B`”、“`Res.C`”、“`Res.D`”、“`White`”或“`Other`”。这是仅供参考的值。`snd_hda` 驱动会忽略它。

**`loc`** 连接器物理位置。可指定为 0 到 63 的数字。这是仅供参考的值。`snd_hda` 驱动会忽略它。

**`misc`** 杂项位。可指定为 0 到 15 的数字。位 0 有特殊含义。设置时表示硬件中未实现插孔检测。

### 运行时配置

除了所有 sound(4) 设备可用的变量之外，还提供以下 [sysctl(8)](../man8/sysctl.8.md) 变量：

**`dev.hdac.%d.pindump`** 将此值设为非零值会将控制器上所有音频功能的当前引脚配置、主要功能和插孔感测状态转储到控制台和 syslog。

**`dev.hdac.%d.polling`** 启用轮询模式。在此模式下，驱动通过使用 [callout(9)](../man9/callout.9.md) 在时钟滴答上查询设备状态而非中断来运行。轮询默认禁用。除非你遇到奇怪的中断问题，或者设备完全无法生成中断，否则不要启用它。

**`dev.hdaa.%d.config`** `hint.hdaa.%d.config` 可调参数的运行时等效项。

**`dev.hdaa.%d.gpi_state`** GPI 线的当前状态。

**`dev.hdaa.%d.gpio_state`** GPIO 线的当前状态。

**`dev.hdaa.%d.gpio_config`** `hint.hdaa.%d.gpio.config` 可调参数的运行时等效项。

**`dev.hdaa.%d.gpo_state`** GPO 线的当前状态。

**`dev.hdaa.%d.nid%d_config`** `hint.hdaa.%d.nid%d.config` 可调参数的运行时等效项。

**`dev.hdaa.%d.nid%d_original`** BIOS 写入的原始引脚配置。

**`dev.hdaa.%d.reconfig`** 将此值设为非零值会使驱动销毁现有 pcm 设备并处理通过 `dev.hdaa.%d.nid%d_config` 设置的新引脚配置。

**`dev.pcm.%d.play.32bit , dev.pcm.%d.rec.32bit`** HDA 控制器对超过 16 位的所有采样使用 32 位表示。这些变量允许指定 CODEC 应使用这 32 位中的多少位。根据编解码器功能，可能值为 20、24 和 32 位。默认值为 24。

**`dev.pcm.%d.rec.autosrc`** `hint.pcm.%d.rec.autosrc` 可调参数的运行时等效项。

## 硬件

`snd_hda` 驱动支持 PCI 类 04h（多媒体）、子类 03h（HDA）音频控制器以及与 Intel High Definition Audio 1.0 规范兼容的编解码器。

## 实例

以配备 Realtek ALC888 HDA 编解码器的 HP Compaq DX2300 为例。此系统前面板有两个音频连接器，后面板有三个音频连接器，以及一个内置扬声器。根据详细驱动输出和编解码器数据手册，此编解码器有五个立体声 DAC 和两个立体声 ADC，全部可路由到任何编解码器引脚（外部连接器）。所有编解码器引脚都是可逆的（可配置为输入或输出）。

如此高的编解码器统一性和灵活性使驱动能够根据引脚配置描述的请求引脚使用情况，以多种不同方式配置它。当启用详细消息时，驱动会报告此类默认引脚配置：

```sh
hdaa0: nid   0x    as seq device       conn  jack    loc        color   misc
hdaa0: 20 01014020 2  0  Line-out      Jack  1/8     Rear       Green   0
hdaa0: 21 99130110 1  0  Speaker       Fixed ATAPI   Onboard    Unknown 1
hdaa0: 22 411111f0 15 0  Speaker       None  1/8     Rear       Black   1 DISA
hdaa0: 23 411111f0 15 0  Speaker       None  1/8     Rear       Black   1 DISA
hdaa0: 24 01a19830 3  0  Mic           Jack  1/8     Rear       Pink    8
hdaa0: 25 02a1983f 3  15 Mic           Jack  1/8     Front      Pink    8
hdaa0: 26 01813031 3  1  Line-in       Jack  1/8     Rear       Blue    0
hdaa0: 27 0221401f 1  15 Headphones    Jack  1/8     Front      Green   0
hdaa0: 28 411111f0 15 0  Speaker       None  1/8     Rear       Black   1 DISA
hdaa0: 30 411111f0 15 0  Speaker       None  1/8     Rear       Black   1 DISA
hdaa0: 31 411111f0 15 0  Speaker       None  1/8     Rear       Black   1 DISA
```

这里可以看到，ID (nid) 为 25 和 27 的节点是前面板连接器（Jack, Front），nid 20、24 和 26 是后面板连接器（Jack, Rear），nid 21 是内置扬声器（Fixed, Onboard）。nid 为 22、23、28、30 和 31 的引脚将由于 "None" 连接性而被驱动禁用。因此引脚数量和描述与现有连接器匹配。

使用关联 (as) 和序列 (seq) 字段值，引脚被分为 3 个关联：

```sh
hdaa0: Association 0 (1) out:
hdaa0:   Pin nid=21 seq=0
hdaa0:   Pin nid=27 seq=15
hdaa0: Association 1 (2) out:
hdaa0:   Pin nid=20 seq=0
hdaa0: Association 2 (3) in:
hdaa0:   Pin nid=24 seq=0
hdaa0:   Pin nid=26 seq=1
hdaa0:   Pin nid=25 seq=15
```

每个 [pcm(4)](pcm.4.md) 设备使用两个关联：一个用于播放，一个用于录制。关联按数字递增顺序处理并分配给 [pcm(4)](pcm.4.md) 设备。在这种情况下，关联 #0 (1) 将成为 `pcm0` 设备播放，使用内置扬声器和 `Headphones` 插孔，并在耳机插孔连接时自动静音扬声器。关联 #1 (2) 将成为 `pcm1` 播放，使用 `Line-out` 插孔。关联 #2 (3) 将成为 `pcm0` 录制，使用外部麦克风和 `Line-in` 插孔。

`snd_hda` 驱动提供大量详细消息以诊断其操作逻辑并描述当前编解码器配置。

使用 [device.hints(5)](../man5/device.hints.5.md) 可修改现有引脚的配置，从而允许广泛的音频设置范围。以下是此特定硬件可能的一些设置示例：

### 示例 1

设置 [device.hints(5)](../man5/device.hints.5.md) 选项

```sh
hint.hdac.0.cad0.nid20.config="as=1"
hint.hdac.0.cad0.nid21.config="as=2"
```

将交换 line-out 和扬声器功能。因此 `pcm0` 设备将播放到 line-out 和耳机插孔。在耳机插孔连接时 line-out 将被静音。`pcm0` 上的录制将来自两个外部麦克风和 line-in 插孔。`pcm1` 播放将输出到内置扬声器。

### 示例 2

设置 [device.hints(5)](../man5/device.hints.5.md) 选项

```sh
hint.hdac.0.cad0.nid20.config="as=1 seq=15 device=Headphones"
hint.hdac.0.cad0.nid27.config="as=2 seq=0"
hint.hdac.0.cad0.nid25.config="as=4 seq=0"
```

将耳机和其中一个麦克风分离到单独设备。`pcm0` 设备将播放到内置扬声器和 line-out 插孔，并在 line-out 插孔连接时自动静音扬声器。`pcm0` 上的录制将使用来自一个外部麦克风和 line-in 插孔的输入。`pcm1` 设备将完全专用于连接到前面板连接器的耳机（耳机和麦克风）。

### 示例 3

设置 [device.hints(5)](../man5/device.hints.5.md) 选项

```sh
hint.hdac.0.cad0.nid20.config="as=1 seq=0"
hint.hdac.0.cad0.nid26.config="as=2 seq=0"
hint.hdac.0.cad0.nid27.config="as=3 seq=0"
hint.hdac.0.cad0.nid25.config="as=4 seq=0"
hint.hdac.0.cad0.nid24.config="as=5 seq=0 device=Line-out"
hint.hdac.0.cad0.nid21.config="as=6 seq=0"
```

将产生 4 个独立设备：`pcm0`（line-out 和 line-in）、`pcm1`（耳机和麦克风）、`pcm2`（通过重新分配后麦克风插孔的额外 line-out）和 `pcm3`（内置扬声器）。

### 示例 4

设置 [device.hints(5)](../man5/device.hints.5.md) 选项

```sh
hint.hdac.0.cad0.nid20.config="as=1 seq=0"
hint.hdac.0.cad0.nid24.config="as=1 seq=1 device=Line-out"
hint.hdac.0.cad0.nid26.config="as=1 seq=2 device=Line-out"
hint.hdac.0.cad0.nid21.config="as=2 seq=0"
```

将产生 2 个设备：`pcm0` 用于通过 3 个后面板连接器（line-out 和重新分配的麦克风与 line-in）进行 5.1 播放，以及前面板连接器的耳机（耳机和麦克风）。`pcm1` 用于内置扬声器播放。连接耳机时后面板连接器将被静音。

## 混音器控制

根据编解码器配置，这些控制和信号源可能报告给 sound(4)：

**`vol`** 总体输出电平（音量）

**`rec`** 总体录制电平

**`igain`** 输入到输出监听环回电平

**`ogain`** 外部放大器控制

**`pcm`** PCM 播放

**`mix`** 输入混音

**`mic`** 第一个外部或第二个内部麦克风输入

**`monitor`** 第一个内部或第二个外部麦克风输入

**`line`** , `line1`, `line2`, `line3` 模拟（线路）输入

**`dig1`** , `dig2`, `dig3` 数字（S/PDIF、HDMI 或 DisplayPort）输入

**`cd`** CD 输入

**`speaker`** PC 扬声器输入

**`phin`** , `phout`, `radio`, `video` 其他杂项输入

控制具有不同的精度。某些可能只是开/关触发器。大多数控制使用对数刻度。

## 参见

[snd_ich(4)](snd_ich.4.md), sound(4), [device.hints(5)](../man5/device.hints.5.md), loader.conf(5), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`snd_hda` 设备驱动首次出现于 FreeBSD 6.3。

## 作者

`snd_hda` 驱动由 Stephane E. Potvin <sepotvin@videotron.ca>、Ariff Abdullah <ariff@FreeBSD.org> 和 Alexander Motin <mav@FreeBSD.org> 编写。本手册页由 Joel Dahl <joel@FreeBSD.org>、Alexander Motin <mav@FreeBSD.org> 和 Giorgos Keramidas <keramida@FreeBSD.org> 编写。

## 缺陷

某些硬件/OEM 厂商倾向于搞砸 BIOS 设置或使用自定义的不寻常 CODEC 接线，从而给驱动造成问题。这可能导致缺少 pcm 设备，或者 `snd_hda` 驱动似乎附加并工作但不播放声音的情况。某些情况下可通过调整 `loader.conf` 变量来解决。但在此之前，请确保确实存在问题，并且所使用的 PCM 音频设备确实对应于预期的音频连接器。

某些厂商使用编解码器的非标准化通用 I/O (GPIO) 引脚来控制外部放大器。在某些情况下，可能需要设置 GPIO 位的组合才能使声音在特定设备上工作。

HDMI 和 DisplayPort 音频可能还需要视频驱动的支持。
