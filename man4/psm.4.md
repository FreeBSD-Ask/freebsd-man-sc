# psm.4

`psm` — PS/2 鼠标风格指点设备驱动程序

## 名称

`psm`

## 概要

`options KBD_RESETDELAY=N options KBD_MAXWAIT=N options PSM_DEBUG=N options KBDIO_DEBUG=N device psm`

在 **`/boot/device.hints`** 中：`hint.psm.0.at="atkbdc" hint.psm.0.irq="12"`

## 描述

`psm` 驱动程序为 PS/2 鼠标风格指点设备提供支持。目前系统中只能有一个 `psm` 设备节点。由于 PS/2 鼠标端口位于键盘控制器的辅助端口，键盘控制器驱动程序 `atkbdc` 也必须在内核中配置。注意，目前无法更改 *irq* 编号。

基本 PS/2 风格指点设备有两个或三个按键。某些设备可能具有滚轮或滚花和/或额外按键。

### 设备分辨率

PS/2 风格指点设备通常具有多档分辨率，即移动灵敏度。典型值为每英寸 25、50、100 和 200 脉冲。某些设备可能具有更高分辨率。当前分辨率可在运行时更改。`atkbdc` 驱动程序允许用户通过驱动程序标志初始设置分辨率（参见“驱动程序配置”章节），或稍后通过 ioctl(2) 命令 `MOUSE_SETMODE` 更改（参见“IOCTLS”章节）。

### 报告速率

设备向主机系统发送移动和按键状态报告的频率，即报告速率，也是可配置的。PS/2 风格指点设备通常支持每秒 10、20、40、60、80、100 和 200 次报告。许多设备的默认值似乎是 60 或 100。注意，当没有移动且没有按键状态变化时，设备不会向主机系统发送任何内容。报告速率可通过 ioctl 调用更改。

### 操作级别

`atkbdc` 驱动程序有三种操作级别。当前操作级别可通过 ioctl 调用设置。

级别 0 提供基本支持；设备驱动程序会报告所连接设备的水平和垂直移动以及最多三个按键的状态。移动和状态编码为一系列定长数据包（参见“数据包格式”章节）。这是默认操作级别，当用户程序打开驱动程序时初始处于此级别。

操作级别 1，即“扩展”级别，支持滚轮（若有）以及最多 11 个按键。滚轮的移动作为沿 Z 轴的移动报告。在此级别下，8 字节数据包会发送给用户程序。

操作级别 2 中，来自指点设备的数据原样传递给用户程序。反过来，来自用户程序的命令也原样传递给指点设备，由用户程序负责状态验证和错误恢复。现代 PS/2 类型指点设备通常使用专有数据格式。因此，在此级别下操作驱动程序时，预期用户程序对特定设备的格式有深入了解。此级别称为“原生”级别。

### 数据包格式

从 `atkbdc` 驱动程序读取的数据包在每个操作级别下的格式不同。

PS/2 鼠标风格指点设备在操作级别 0 下的数据包为三字节长：

**bit** 7 1 表示垂直移动计数溢出。
**bit** 6 1 表示水平移动计数溢出。
**bit** 5 若垂直移动计数为负则置位。
**bit** 4 若水平移动计数为负则置位。
**bit** 3 始终为 1。
**bit** 2 中键状态；按下则置位。对于无中键的设备，此位始终为零。
**bit** 1 右键状态；按下则置位。
**bit** 0 左键状态；按下则置位。

**Byte** 1
**Byte** 2 水平移动计数，二进制补码；-256 到 255。注意符号位在第一字节。
**Byte** 3 垂直移动计数，二进制补码；-256 到 255。注意符号位在第一字节。

在级别 1 下，数据包按 [mouse(4)](mouse.4.md) 中定义的标准格式 `MOUSE_PROTO_SYSMOUSE` 编码。

在级别 2（原生级别）下，数据包的大小和格式没有标准。

### 加速度

`atkbdc` 驱动程序可以在一定程度上“加速”指点设备的移动。你移动设备越快，指针在屏幕上移动得越远。驱动程序有一个内部变量控制加速效果。其值可通过驱动程序标志或 ioctl 调用修改。

## 驱动程序配置

### 内核配置选项

以下内核配置选项可控制 `atkbdc` 驱动程序。可在内核配置文件中设置（参见 [config(8)](../man8/config.8.md)）。

***KBD_RESETDELAY=X** , KBD_MAXWAIT=Y* `atkbdc` 驱动程序会在引导过程中尝试重置指点设备。重置后设备响应有时需要较长时间。这些选项控制驱动程序最终放弃等待前的等待时长。驱动程序最多等待 `X` * `Y` 毫秒。若驱动程序似乎无法检测到你的指点设备，可增大这些值。默认值为 `X` 200 毫秒、`Y` 5。

***PSM_DEBUG=N** , KBDIO_DEBUG=N* 将调试级别设为 `N`。默认调试级别为零。调试日志参见“诊断”章节。

### 驱动程序标志

`atkbdc` 驱动程序接受以下驱动程序标志。在 **`/boot/device.hints`** 中设置（参见下文“实例”）。

***1** （低）* 每英寸 25 脉冲（ppi）
***2** （中低）* 50 ppi
***3** （中高）* 100 ppi
***4** （高）* 200 ppi

```sh
psmintr: out of sync (xxxx != yyyy).
```

**bit** 0..3 RESOLUTION 此标志指定指点设备的分辨率。取值必须为 0 到 4。值越大，设备选择的分辨率越精细。此字段所选实际分辨率因设备型号而异。典型分辨率为：将此标志留零会选择设备的默认分辨率（不论其具体为何）。

**bit** 4..7 ACCELERATION 此标志控制加速效果的强度。此标志值越小，移动越灵敏。允许的最小值，亦即最灵敏设置对应的值为 1。将此标志设为零会完全禁用加速效果。

**bit** 8 NOCHECKSYNC `atkbdc` 驱动程序通过检查字节位模式来尝试识别数据包的第一字节。虽然此方法应适用于大多数 PS/2 指点设备，但对一些与已知设备兼容性不佳的设备可能会产生干扰。如果你认为指点设备未按预期工作，且内核频繁向控制台打印以下消息，可设置此标志以禁用同步检查并查看是否有帮助。

**bit** 9 NOIDPROBE `atkbdc` 驱动程序不会尝试识别指点设备型号，也不会执行型号特定的初始化。在此情况下，设备应始终表现得像标准 PS/2 鼠标。滚轮和额外按键等附加功能将不被 `atkbdc` 驱动程序识别。

**bit** 10 NORESET 设置此标志时，`atkbdc` 驱动程序在初始化设备时不会重置指点设备。如果 FreeBSD 内核在另一个操作系统运行之后启动，指点设备会继承前一操作系统的设置。但由于 `atkbdc` 驱动程序无法得知这些设置，设备与驱动程序可能无法正确工作。在正常情况下此标志应不需要。

**bit** 11 FORCETAP 某些板设备在用户“轻拍”设备表面时会报告如同第四按键被按下（参见“注意事项”）。此标志会使 `atkbdc` 驱动程序假定设备按此方式工作。未设置此标志时，驱动程序仅对 ALPS GlidePoint 型号假定此行为。

**bit** 12 IGNOREPORTERROR 此标志使 `atkbdc` 驱动程序在探测 PS/2 鼠标端口时忽略某些错误条件。正常情况下应不需要。

**bit** 13 HOOKRESUME 某些笔记本电脑的内置 PS/2 指点设备在系统从节能模式“恢复”后无法立即操作，但最终会变得可用。有报告指出，通过执行 I/O 来刺激设备有助于快速唤醒设备。此标志会启用 `atkbdc` 驱动程序中的一段代码，挂钩“resume”事件并对设备执行一些无害的 I/O 操作。

**bit** 14 INITAFTERSUSPEND 此标志对上述问题采取更激烈的措施。它会使 `atkbdc` 驱动程序在“resume”事件之后重置并重新初始化指点设备。

## 加载器可调参数

可在引导时将 `hw.psm.synaptics_support` 设为 *1* 以启用对 Synaptics 触摸板的扩展支持。这会使 `atkbdc` 能够处理来自 guest 设备（指点杆）和额外按键的数据包。类似地，可在引导时将 `hw.psm.trackpoint_support` 或 `hw.psm.elantech_support` 分别设为 *1* 以启用对 IBM/Lenovo TrackPoint 和 Elantech 触摸板的扩展支持。

可在引导时将 `hw.psm.tap_enabled` 设为 *0* 以禁用轻拍和拖放手势。目前，无论扩展支持状态如何，Synaptics 触摸板均支持此功能；Elantech 触摸板在启用扩展支持后也支持。引导后可通过同名 sysctl 修改此行为，并使用 **`/etc/rc.d/moused`** 重启 [moused(8)](../man8/moused.8.md)。

可在引导时将 `hw.psm.mux_disabled` 设为 *1* 以禁用主动多路复用支持。这会阻止 `atkbdc` 启用某些 Synaptics 触摸板所需的主动多路复用模式。

## IOCTLS

鼠标驱动程序有若干 ioctl(2) 命令。这些命令及相关结构和常量定义于：

`#include <sys/mouse.h>`

命令的一般描述见 [mouse(4)](mouse.4.md)。本节说明 `atkbdc` 驱动程序特有的功能。

```sh
typedef struct mousehw {
    int buttons;    /* 按键数量 */
    int iftype;     /* 接口类型 */
    int type;       /* 鼠标/轨迹球/触摸板... */
    int model;      /* 依赖接口的型号 ID */
    int hwid;       /* 依赖接口的硬件 ID */
} mousehw_t;
```

***0*** 鼠标（Microsoft、Logitech 及许多其他厂商）
***2*** Microsoft Ballpoint 鼠标
***3*** Microsoft IntelliMouse

```sh
typedef struct synapticshw {
    int infoMajor;	/* 主要硬件修订版本 */
    int infoMinor;	/* 次要硬件修订版本 */
    int infoRot180;	/* 触摸板已旋转 */
    int infoPortrait;	/* 触摸板为纵向 */
    int infoSensor;	/* 传感器型号 */
    int infoHardware;	/* 硬件型号 */
    int infoNewAbs;	/* 支持 newabs 格式 */
    int capPen;		/* 可检测笔 */
    int infoSimplC;	/* 支持简单命令 */
    int infoGeometry;	/* 触摸板尺寸 */
    int capExtended;	/* 支持扩展数据包 */
    int capSleep;	/* 可挂起/恢复 */
    int capFourButtons;	/* 具有四个按键 */
    int capMultiFinger;	/* 可检测多指 */
    int capPalmDetect;	/* 可检测手掌 */
    int capPassthrough;	/* 可透传 guest 数据包 */
    int capMiddle;	/* 具有物理中键 */
    int nExtendedButtons; /* 具有 N 个额外按键 */
    int nExtendedQueries; /* 支持 N 个扩展查询 */
} synapticshw_t;
```

```sh
typedef struct mousemode {
    int protocol;    /* MOUSE_PROTO_XXX */
    int rate;        /* 报告速率（每秒），未知则为 -1 */
    int resolution;  /* MOUSE_RES_XXX，未知则为 -1 */
    int accelfactor; /* 加速因子 */
    int level;       /* 驱动程序操作级别 */
    int packetsize;  /* 数据包长度 */
    unsigned char syncmask[2]; /* 同步位 */
} mousemode_t;
```

**`MOUSE_RES_LOW`** 25 ppi
**`MOUSE_RES_MEDIUMLOW`** 50 ppi
**`MOUSE_RES_MEDIUMHIGH`** 100 ppi
**`MOUSE_RES_HIGH`** 200 ppi

***level** 0* 3 字节
***level** 1* 8 字节
***level** 2* 取决于设备型号

**`MOUSE_GETLEVEL`** `int *level`
**`MOUSE_SETLEVEL`** `int *level` 这些命令用于操作 `atkbdc` 驱动程序的操作级别。
**`MOUSE_GETHWINFO`** `mousehw_t *hw` 按以下结构返回所连接设备的硬件信息。`buttons` 字段保存设备上的按键数量。`atkbdc` 驱动程序目前可以检测 Logitech 的三键鼠标并相应报告。其他厂商的三键鼠标可能无法正确报告。但这不影响驱动程序的操作。`iftype` 始终为 `MOUSE_IF_PS2`。`type` 表示设备类型：`MOUSE_MOUSE`、`MOUSE_TRACKBALL`、`MOUSE_STICK`、`MOUSE_PAD` 或 `MOUSE_UNKNOWN`。用户不应过分依赖此字段，因为驱动程序可能并不总能识别设备类型，事实上极少能识别。`model` 在操作级别 0 下始终为 `MOUSE_MODEL_GENERIC`。在更高操作级别下可能为 `MOUSE_MODEL_GENERIC` 或某个 `MOUSE_MODEL_XXX` 常量。同样，`atkbdc` 驱动程序可能在此字段中设置也可能不设置适当的值。`hwid` 是设备返回的 ID 值。已知 ID 包括：
**`MOUSE_SYN_GETHWINFO`** `synapticshw_t *synhw` 检索与 Synaptics 触摸板关联的额外信息。仅在检测到受支持设备时可用。关于此结构中各字段的更多信息，参见 *Synaptics TouchPad Interfacing Guide*。
**`MOUSE_GETMODE`** `mousemode_t *mode` 此命令获取鼠标驱动程序的当前操作参数。`protocol` 在操作级别 0 和 2 下为 `MOUSE_PROTO_PS2`，在操作级别 1 下为 `MOUSE_PROTO_SYSMOUSE`。`rate` 是设备向主机发送移动报告的状态报告速率（每秒报告数）。典型支持值为 10、20、40、60、80、100 和 200。某些鼠标也接受其他任意值。`resolution` 必须是某个 `MOUSE_RES_XXX` 常量或正值。值越大，鼠标选择的分辨率越精细。`MOUSE_RES_XXX` 常量所选实际分辨率因鼠标型号而异。典型分辨率为：`accelfactor` 字段保存控制加速功能的值（参见“加速度”章节）。必须为零或正值。若为零则禁用加速。`packetsize` 字段指定数据包长度。它取决于操作级别和指点设备型号。`syncmask` 数组保存用于检测数据包第一字节的位掩码和模式。`syncmask[0]` 是要与字节进行 AND 运算的位掩码。若结果等于 `syncmask[1]`，则该字节很可能是数据包的第一字节。注意，此检测方法并非 100% 可靠，因此仅应作为辅助手段。
**`MOUSE_SETMODE`** `mousemode_t *mode` 此命令按 `mode` 指定更改鼠标驱动程序的当前操作参数。仅 `rate`、`resolution`、`level` 和 `accelfactor` 可修改。在其他字段中设置值不会产生错误，也无效果。若不想更改某字段的当前设置，将其置为 -1。也可在 `resolution` 和 `rate` 中置零，将选择该字段的默认值。
**`MOUSE_READDATA`** `mousedata_t *data`
**`MOUSE_READSTATE`** `mousedata_t *state` 这些命令目前不被 `atkbdc` 驱动程序支持。
**`MOUSE_GETSTATUS`** `mousestatus_t *status` 此命令返回 [mouse(4)](mouse.4.md) 中所述的按键和移动计数的当前状态。

## 文件

**`/dev/psm0`** “非阻塞”设备节点
**`/dev/bpsm0`** “阻塞”设备节点

## 实例

为安装 `atkbdc` 驱动程序，你需要在内核配置文件中加入：

```sh
device atkbdc
```

```sh
device psm
```

并在 **`/boot/device.hints`** 中加入以下行：

```sh
hint.atkbdc.0.at="isa"
```

```sh
hint.atkbdc.0.port="0x060"
```

```sh
hint.psm.0.at="atkbdc"
```

```sh
hint.psm.0.irq="12"
```

若在 **`/boot/device.hints`** 中加入以下语句：

```sh
hint.psm.0.flags="0x2000"
```

你将添加在“resume”事件后刺激指点设备的可选代码。

```sh
hint.psm.0.flags="0x24"
```

上述行会将设备分辨率设为高（4），加速因子设为 2。

## 诊断

在调试级别 0 下，除引导过程中的以下行外，几乎不记录信息：

```sh
psm0: device ID X
```

其中 `X` 是所发现指点设备返回的设备 ID 代码。已知 ID 参见 `MOUSE_GETINFO`。

在调试级别 1 下，驱动程序探测辅助端口（鼠标端口）时会记录更多信息。消息以 LOG_KERN 设施在 LOG_DEBUG 级别记录（参见 syslogd(8)）。

```sh
psm0: current command byte:xxxx
kbdio: TEST_AUX_PORT status:0000
kbdio: RESET_AUX return code:00fa
kbdio: RESET_AUX status:00aa
kbdio: RESET_AUX ID:0000
[...]
psm: status 00 02 64
psm0 irq 12 on isa
psm0: model AAAA, device ID X, N buttons
psm0: config:00000www, flags:0000uuuu, packet size:M
psm0: syncmask:xx, syncbits:yy
```

第一行显示辅助端口被探测前键盘控制器的命令字节值。通常为 40、45、47 或 65，取决于主板 BIOS 上电时如何初始化键盘控制器。

第二行显示键盘控制器对辅助端口接口的测试结果，零表示无错误；但注意，某些控制器即使系统中不存在该端口也会报告无错误。

第三至第五行显示指点设备的重置状态。功能正常的设备应返回 FA AA <ID> 序列。ID 代码如上所述。

第七行显示当前硬件设置。这些字节的格式如下：

**bit** 7 保留。
**bit** 6 0 - 流模式，1 - 远程模式。在流模式下，指点设备在状态变化时发送设备状态。在远程模式下，主机必须请求发送状态。`atkbdc` 驱动程序将设备置于流模式。
**bit** 5 若指点设备当前已启用则置位。否则为零。
**bit** 4 0 - 1:1 缩放，1 - 2:1 缩放。1:1 缩放为默认。
**bit** 3 保留。
**bit** 2 左键状态；按下则置位。
**bit** 1 中键状态；按下则置位。
**bit** 0 右键状态；按下则置位。

**bit** 7 保留。
**bit** 6..0 分辨率代码：0 到 3。分辨率代码对应的实际分辨率因设备而异。

**Byte** 1
**Byte** 2
**Byte** 3 设备向主机发送移动报告的状态报告速率（每秒报告数）。

注意，指点设备在 `atkbdc` 驱动程序被用户程序打开之前不会被启用。

其余行显示设备 ID 代码、检测到的按键数量和内部变量。

在调试级别 2 下，会记录更为详细的信息。

## 参见

ioctl(2), syslog(3), [atkbdc(4)](atkbdc.4.md), [mouse(4)](mouse.4.md), [sysmouse(4)](sysmouse.4.md), [moused(8)](../man8/moused.8.md), syslogd(8)

> "Synaptics TouchPad Interfacing Guide".

## 作者

`atkbdc` 驱动程序基于许多人的工作，包括 Eric Forsberg、Sandi Donno、Rick Macklem、Andrew Herbert、Charles Hannum、Shoji Yuen 和 Kazutaka Yokota 等。

本手册页由 Kazutaka Yokota <yokota@FreeBSD.org> 编写。

## 注意事项

许多板设备在用户“轻拍”板表面时会表现得如同第一（左）按键被按下。相反，某些板产品，例如某些版本的 ALPS GlidePoint 和 Interlink VersaPad，将轻拍动作视为第四按键事件。

据报告，ALPS GlidePoint、Synaptics 触摸板、IBM/Lenovo TrackPoint 和 Interlink VersaPad 需要 *INITAFTERSUSPEND* 标志才能从挂起状态恢复。当 `atkbdc` 驱动程序检测到这些设备之一时会自动设置此标志。

某些 MouseSystems 的 PS/2 鼠标型号需要置于高分辨率模式才能正常工作。使用驱动程序标志设置分辨率。

一旦与数据流失去同步，没有保证的方法能重新与数据包的第一字节同步。但如果你使用 XFree86 服务器并遇到此问题，可以通过切换到虚拟终端再返回 X 服务器来使 X 服务器与鼠标同步，除非 X 服务器通过 [moused(8)](../man8/moused.8.md) 访问鼠标。在不移动鼠标的情况下点击任意按键也可能奏效。

## 缺陷

据报告，启用对 Synaptics 触摸板的扩展支持会在某些（较新的）Synaptics 硬件型号上引发响应性问题，尤其是带有 guest 设备的型号。
