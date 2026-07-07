# mouse(4)

`mouse` — 鼠标和指向设备驱动

## 名称

`mouse`

## 概要

`#include <sys/mouse.h>`

## 描述

鼠标驱动 [psm(4)](psm.4.md)、[ums(4)](ums.4.md) 和 [sysmouse(4)](sysmouse.4.md) 为用户程序提供鼠标的移动和按钮状态信息。目前针对总线鼠标、InPort 鼠标、PS/2 鼠标和 USB 鼠标有专用设备驱动。串口鼠标不由专用驱动直接支持，但可通过串口设备驱动或通过 [moused(8)](../man8/moused.8.md) 和 [sysmouse(4)](sysmouse.4.md) 访问。

用户程序只需通过 open(2) 调用打开鼠标设备，并通过 read(2) 从设备读取鼠标数据。移动和按钮状态通常以定长数据包编码。某些鼠标设备可能发送变长数据包。每个驱动使用的实际协议（数据格式）差异很大。

鼠标驱动可具有 ``非阻塞'' 属性，当鼠标数据不可用时，驱动将立即返回。

鼠标设备驱动通常提供若干操作级别。当前操作级别可通过 ioctl(2) 命令查看和更改。级别零为最低级别，驱动在该级别向用户程序提供基本服务。大多数驱动在该级别提供鼠标的水平和垂直移动以及最多三个按钮的状态。在级别一（如果驱动支持），鼠标数据按标准格式 `MOUSE_PROTO_SYSMOUSE` 编码，如下所示：

**bit** 7 始终为一。
**bit** 6..3 始终为零。
**bit** 2 左键状态；按下时清除，否则置位。
**bit** 1 中键状态；按下时清除，否则置位。如果设备没有中键，则始终为一。
**bit** 0 右键状态；按下时清除，否则置位。

**Byte** 1
**Byte** 2 水平移动计数的前半部分，以二进制补码表示；范围为 -128 到 127。
**Byte** 3 垂直移动计数的前半部分，以二进制补码表示；范围为 -128 到 127。
**Byte** 4 水平移动计数的后半部分，以二进制补码表示；范围为 -128 到 127。要获取完整的水平移动计数，请将字节 2 和字节 4 相加。
**Byte** 5 垂直移动计数的后半部分，以二进制补码表示；范围为 -128 到 127。要获取完整的垂直移动计数，请将字节 3 和字节 5 相加。
**Byte** 6 bit 7 始终为零。低 7 位编码 Z 轴移动计数的前半部分，以二进制补码表示；范围为 -64 到 63。
**Byte** 7 bit 7 始终为零。低 7 位编码 Z 轴移动计数的后半部分，以二进制补码表示；范围为 -64 到 63。要获取完整的 Z 轴移动计数，请将字节 6 和字节 7 相加。
**Byte** 8 bit 7 始终为零。bit 0 至 bit 6 反映按钮 4 至按钮 10 的状态。如果某个按钮被按下，对应的位被清除。否则该位置位。

此格式的前 5 个字节与 MouseSystems 格式兼容。额外的 3 个字节的最高有效位始终为零。因此，如果用户程序能够解释 MouseSystems 数据格式，并尝试通过检测位模式 10000xxxb 来找到格式的第一个字节，它将丢弃额外的字节，从而能够正确解码 x、y 以及 3 个按钮的状态。

设备驱动可提供高于级别一的操作级别。详情请参阅各个驱动的手册页。

## IOCTLS

为鼠标驱动定义了以下 ioctl(2) 命令。各驱动对这些命令的支持程度不一。本节给出命令的一般描述。具体细节请参阅各个驱动的手册页。

```sh
typedef struct mousehw {
    int buttons;    /* 按钮数量 */
    int iftype;     /* 接口类型 */
    int type;       /* 鼠标/轨迹球/触摸板... */
    int model;      /* 依赖于接口的型号 ID */
    int hwid;       /* 依赖于接口的硬件 ID */
} mousehw_t;
```

```sh
typedef struct mousemode {
    int protocol;    /* MOUSE_PROTO_XXX */
    int rate;        /* 报告速率（每秒次数） */
    int resolution;  /* MOUSE_RES_XXX，未知则为 -1 */
    int accelfactor; /* 加速因子 */
    int level;       /* 驱动操作级别 */
    int packetsize;  /* 数据包长度 */
    unsigned char syncmask[2]; /* 同步位 */
} mousemode_t;
```

```sh
typedef struct mousedata {
    int len;        /* 缓冲区中的数据量 */
    int buf[16];    /* 数据缓冲区 */
} mousedata_t;
```

```sh
typedef struct mousestatus {
    int flags;      /* 状态变化标志 */
    int button;     /* 按钮状态 */
    int obutton;    /* 上一次按钮状态 */
    int dx;         /* x 移动 */
    int dy;         /* y 移动 */
    int dz;         /* z 移动 */
} mousestatus_t;
```

**`MOUSE_GETLEVEL`** `int *level`
**`MOUSE_SETLEVEL`** `int *level` 这些命令用于操作鼠标驱动的操作级别。
**`MOUSE_GETHWINFO`** `mousehw_t *hw` 返回所连接设备的硬件信息。除 `iftype` 字段外，设备驱动可能并不总是用正确的值填充该结构。详情请参阅各个驱动的手册页。`buttons` 字段保存驱动检测到的按钮数量。如果无法确定确切数量，驱动可在此字段中放置任意值，例如二。`iftype` 是接口类型：`MOUSE_IF_SERIAL`、`MOUSE_IF_BUS`、`MOUSE_IF_INPORT`、`MOUSE_IF_PS2`、`MOUSE_IF_USB`、`MOUSE_IF_SYSMOUSE` 或 `MOUSE_IF_UNKNOWN`。`type` 表示设备类型：`MOUSE_MOUSE`、`MOUSE_TRACKBALL`、`MOUSE_STICK`、`MOUSE_PAD` 或 `MOUSE_UNKNOWN`。`model` 可为 `MOUSE_MODEL_GENERIC` 或 `MOUSE_MODEL_XXX` 常量之一。`hwid` 是指向设备返回的 ID 值。它取决于接口类型；可能取值请参阅具体鼠标驱动的手册页。
**`MOUSE_GETMODE`** `mousemode_t *mode` 该命令报告鼠标驱动的当前操作参数。`protocol` 字段表示用户程序读取鼠标数据时返回设备状态的格式。它为 `MOUSE_PROTO_XXX` 常量之一。`rate` 字段是设备向主机发送移动报告的状态报告速率（报告/秒）。若未知或不适用则为 -1。`resolution` 字段保存指定指向设备分辨率的值。它为正值或 `MOUSE_RES_XXX` 常量之一。`accelfactor` 字段保存用于控制加速功能的值。它必须为零或更大。若为零则禁用加速。`packetsize` 字段表示定长数据包的长度或变长数据包定长部分的长度。该长度取决于接口类型、设备类型和型号、协议以及驱动的操作级别。`syncmask` 数组保存用于检测数据包首字节的位掩码和模式。`syncmask[0]` 是用于与字节进行 AND 运算的位掩码。如果结果等于 `syncmask[1]`，则该字节很可能是数据包的首字节。注意，这种检测首字节的方法并非 100% 可靠，因此应仅作为参考措施。
**`MOUSE_SETMODE`** `mousemode_t *mode` 该命令按 `mode` 所指定更改鼠标驱动的当前操作参数。仅 `rate`、`resolution`、`level` 和 `accelfactor` 可修改。在其他字段中设置值不会产生错误，也无效果。若不想更改某字段的当前设置，可在此字段中放入 -1。也可在 `resolution` 和 `rate` 中放入零，将使用这些字段的默认值。
**`MOUSE_READDATA`** `mousedata_t *data` 该命令从设备读取原始数据。调用进程必须在 `len` 字段中填入要读入缓冲区的字节数。此命令可能并非所有驱动都支持。
**`MOUSE_READSTATE`** `mousedata_t *state` 该命令从设备读取原始状态数据。它使用与上述相同的结构。此命令可能并非所有驱动都支持。
**`MOUSE_GETSTATUS`** `mousestatus_t *status` 该命令返回按钮的当前状态和移动计数，结构如下。`button` 和 `obutton` 字段分别保存鼠标按钮的当前状态和上一次状态。当按钮被按下时，对应的位被置位。鼠标驱动最多支持 31 个按钮，对应 bit 0 至 bit 31。少数按钮位被定义为 `MOUSE_BUTTON1DOWN` 至 `MOUSE_BUTTON8DOWN`。前三个按钮对应左、中、右键。如果某按钮的状态自上次 `MOUSE_GETSTATUS` 调用以来发生了变化，`flags` 字段中对应的位将被置位。如果鼠标自上次调用以来发生了移动，`flags` 字段中的 `MOUSE_POSCHANGED` 位也将被置位。其他字段保存自上次 `MOUSE_GETSTATUS` 调用以来的移动计数。每次调用此命令后，内部计数器将被重置。

## 文件

**`/dev/cuau%d`** 串口
**`/dev/psm%d`** PS/2 鼠标设备
**`/dev/sysmouse`** 虚拟鼠标设备
**`/dev/ums%d`** USB 鼠标设备

## 参见

[ioctl(2)](../sys/ioctl.2.md), [psm(4)](psm.4.md), [sysmouse(4)](sysmouse.4.md), [ums(4)](ums.4.md), [moused(8)](../man8/moused.8.md)

## 作者

本手册页由 Kazutaka Yokota <yokota@FreeBSD.org> 编写。
