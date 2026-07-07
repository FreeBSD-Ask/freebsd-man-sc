# spkr(4)

`speaker` — 控制台扬声器设备驱动

## 名称

`speaker`, `spkr`

## 概要

`device speaker`

`#include <dev/speaker/speaker.h>`

## 描述

扬声器设备驱动允许应用程序在运行 FreeBSD 的 IBM-PC 兼容机上控制 PC 控制台扬声器。

写入设备的内容被解释为以简单 ASCII 旋律记谱法表示的“播放字符串”。也支持通过 ioctl(2) 请求在任意频率上生成音调。

一次只能播放一个字符串。来自不同线程或进程的并发 write(2) 和 ioctl(2) 调用按字符串进行串行化。

声音生成不会独占处理器；事实上，当 PC 硬件发出音调时，驱动大部分时间都在睡眠。在驱动运行期间，其他进程可以发出蜂鸣声。

应用程序可对扬声器文件描述符调用 ioctl(2) 以直接控制扬声器驱动；ioctl(2) 接口的定义位于

`#include <dev/speaker/speaker.h>`

这些调用中使用的 `tone_t` 结构有两个字段，分别指定频率（单位为 Hz）和持续时间（单位为 1/100 秒）。频率为零被解释为休止。

目前有两个这样的 ioctl(2) 调用。`SPKRTONE` 接受指向单个音调结构的指针作为第三个参数并播放它。`SPKRTUNE` 接受指向音调结构数组首元素的指针并按连续序列播放它们；该数组必须以一个持续时间为零的成员结尾。

播放字符串语言是自 1970 年代以来各种计算机和游戏系统中使用的音乐标记语言（Music Markup Language，MML）的一种方言。它是 IBM Advanced BASIC 2.0、MS BASICA 和 GW-BASIC 中 PLAY 语句所支持的 MML 变体以及 MS QBasic 中支持的标准音乐表达式（Standard Musical Expression，SMX）的子集。MML/SMX 的 `MB`、`MF` 和 `X` 原语不受支持。“音域跟踪”特性和连音标记是 FreeBSD 实现所特有的。

共有 84 个可访问的音符，编号为 1-84，分布在 7 个八度中，每个八度从 C 到 B，编号为 0-6；音阶采用 A440 等律，第 3 八度从中音 C 开始。默认情况下，播放函数发出持续半秒的音符，最后 1/16 秒为“休止时间”。

播放字符串从左到右被解释为一系列播放命令组；字母大小写被忽略。播放命令组如下：

```sh
        	Tempo    	Beats Per Minute
very slow	Larghissimo
        	Largo    	40-60
         	Larghetto    	60-66
        	Grave
        	Lento
        	Adagio       	66-76
slow    	Adagietto
        	Andante   	76-108
medium   	Andantino
        	Moderato	108-120
fast    	Allegretto
        	Allegro   	120-168
        	Vivace
        	Veloce
        	Presto    	168-208
very fast	Prestissimo
```

**`CDEFGAB`** 字母 A 到 G 使当前八度中相应的音符被播放。音符字母后可选地跟一个“*升降号*”，即 # + 或 - 中的一个；前两个使其升半音，最后一个使其降半音。其后还可跟一个时值数字和延音点（见下文）。时值的解释与下文的 L 命令相同。

**`O`** **n** 如果 **n** 是数字，则设置当前八度。**n** 也可为 `L` 或 `N` 以启用或禁用音域跟踪（默认禁用）。启用音域跟踪时，一对字母音符的解释会在必要时改变八度，以使音符之间的跳跃尽可能小。因此 ``olbc'' 将被演奏为``olb>c''，而 ``olcb'' 被演奏为``olc<b''。在 >、< 和 O[0123456] 之后的单个字母音符会暂时禁用音域锁定。IBM 和 MS BASIC 方言不支持音域锁定特性。

**`>`** 将当前八度上移一级。

**`<`** 将当前八度下移一级。

**`N`** **n** 播放音符 **n，** **n** 为 1 到 84，或为 0 表示按当前时值休止。其后可跟延音点。

**`L`** **n** 设置音符的当前时值。默认为 `L4`，即四分音符或四分音符。最低可取值为 1；最高可接受至 64。`L1` 设置全音符，`L2` 设置二分音符，`L4` 设置四分音符，依此类推。

**`P`** **n** 暂停（休止），**n** 的解释与 `L` **n** 相同。其后可跟延音点。也可写作 `~`。

**`T`** **n** 设置每分钟四分音符的数量；默认为 120。常见速度的音乐术语名称为：

**`M[LNS]`** 设置 articulation。`MN`（`N` 表示正常）为默认值；音符时值的最后 1/8 为休止时间。可设 `ML` 以连奏（无休止间隔）或 `MS` 以断奏（1/4 休止间隔）。

音符（即 `CDEFGAB` 或 `N` 命令字符组）后可跟延音点。每个点使音符的时值延长其一半。因此，加一个点的音符持续其无点时值的 3/2；加两个点持续 9/4；加三个点则为 27/8。

音符及其延音点后还可跟一个连音标记（下划线）。这会填补音符之后的正常微休止，将其连音到下一个音符。IBM 和 MS BASIC 方言不支持连音特性。

播放字符串中的空白字符会被直接跳过，可用于分隔旋律段落。

## 文件

**`/dev/speaker`** 扬声器设备文件

## 参见

spkrtest(8)

关于 MML 的更多信息：

> "IBM Personal Computer BASIC manual", IBM Corporation, 1982.

> "BASICA manual", Microsoft Corporation, 1982.

> "GW-BASIC manual", Microsoft Corporation, 1987.

> "QBasic manual", Microsoft Corporation, 1991.

> Eleanor Selfridge-Field, "Beyond MIDI: the handbook of musical codes", MIT Press, 1997.

- Lk <https://electronicmusic.fandom.com/wiki/Music_Macro_Language> The Electronic Music Wiki - Music Macro Language
-
-
-
-
-

## 历史

`spkr` 设备出现于 FreeBSD 1.0。

在 FreeBSD 16 之前，只有一个文件描述符可以保持设备打开。

## 作者

`spkr` 驱动由 Eric S. Raymond <<esr@snark.thyrsus.com> in> 于 1990 年 6 月编写，并由 Andrew A. Chernov <ache@astral.msk.su> 移植。并发打开支持由 Raphael Poss <knz@thaumogen.net> 添加。

## 缺陷

由于音高表中的舍入以及音调生成和定时硬件中的误差（两者都不是为精度而设计的），音高精度和定时都无法在数学上精确。没有音量控制。

两个或更多延音点的作用不反映标准乐谱，标准乐谱中每个点增加前一个点修饰符值的一半，而不是已修改音符值的一半。因此，加一个点的音符持续其无点时值的 3/2；加两个点持续 7/4；加三个点则为 15/8。然而，乘以 3/2 的解释在 IBM BASIC 手册中有规定，为兼容性而保留。

在非常长（长于系统物理 I/O 块）的播放字符串中，音符后缀或数字偶尔可能因跨越块边界而被错误解析。
