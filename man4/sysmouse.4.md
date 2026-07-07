# sysmouse(4)

`sysmouse` — 虚拟化鼠标驱动程序

## 名称

`sysmouse`

## 概要

`#include <sys/mouse.h>`

`#include <sys/consio.h>`

## 描述

控制台驱动程序与鼠标守护进程 [moused(8)](../man8/moused.8.md) 配合，通过 `sysmouse` 驱动以标准化方式向用户进程提供鼠标数据。这种安排使控制台和用户进程（如 X Window System）能够共享鼠标。

希望使用鼠标操作的用户进程只需通过 open(2) 调用打开 **`/dev/sysmouse`** ，并通过 read(2) 从该设备读取鼠标数据。请确保 [moused(8)](../man8/moused.8.md) 正在运行，否则用户进程不会看到来自鼠标的任何数据。

### 操作级别

`sysmouse` 驱动有两个操作级别。当前操作级别可通过 ioctl 调用查询和更改。

零级，即基本级，是驱动程序向用户程序提供基本服务的最低级别。`sysmouse` 驱动以 MouseSystems 格式提供鼠标的水平、垂直移动以及最多三个按键的状态，如下所示。

**bit** 7 始终为 1。
**bit** 6..3 始终为 0。
**bit** 2 左键状态；按下时清零，否则置位。
**bit** 1 中键状态；按下时清零，否则置位。如果设备没有中键，则始终为 1。
**bit** 0 右键状态；按下时清零，否则置位。

**Byte** 1
**Byte** 2 水平移动计数值的前半部分，以二进制补码表示；范围为 -128 到 127。
**Byte** 3 垂直移动计数值的前半部分，以二进制补码表示；范围为 -128 到 127。
**Byte** 4 水平移动计数值的后半部分，以二进制补码表示；范围为 -128 到 127。要获得完整的水平移动计数，请将字节 2 和 4 相加。
**Byte** 5 垂直移动计数值的后半部分，以二进制补码表示；范围为 -128 到 127。要获得完整的垂直移动计数，请将字节 3 和 5 相加。

在一级，即扩展级，鼠标数据按 [mouse(4)](mouse.4.md) 中定义的标准格式 `MOUSE_PROTO_SYSMOUSE` 进行编码。

## IOCTL

本节描述两类 ioctl(2) 命令：用于 `sysmouse` 驱动本身的命令，以及用于控制台和控制台控制驱动程序的命令。

### Sysmouse IOCTL

鼠标驱动有少量命令。命令的一般描述见 [mouse(4)](mouse.4.md)。以下是 `sysmouse` 驱动特有的功能。

```sh
typedef struct mousehw {
    int buttons;    /* 按键数量 */
    int iftype;     /* 接口类型 */
    int type;       /* 鼠标/轨迹球/触摸板... */
    int model;      /* 依赖于接口的型号 ID */
    int hwid;       /* 依赖于接口的硬件 ID */
} mousehw_t;
```

```sh
typedef struct mousemode {
    int protocol;    /* MOUSE_PROTO_XXX */
    int rate;        /* 报告速率（每秒） */
    int resolution;  /* MOUSE_RES_XXX，未知则为 -1 */
    int accelfactor; /* 加速因子 */
    int level;       /* 驱动操作级别 */
    int packetsize;  /* 数据包长度 */
    unsigned char syncmask[2]; /* 同步位 */
} mousemode_t;
```

***level** 0* 5 字节
***level** 1* 8 字节

**`MOUSE_GETLEVEL`** `int *level`
**`MOUSE_SETLEVEL`** `int *level` 这些命令用于操作鼠标驱动程序的操作级别。
**`MOUSE_GETHWINFO`** `mousehw_t *hw` 返回所连接设备的硬件信息，结构如下。在当前版本的 `sysmouse` 驱动中，只有 `iftype` 字段保证填入正确的值。`buttons` 字段保存驱动检测到的按键数量。`iftype` 始终为 `MOUSE_IF_SYSMOUSE`。`type` 表示设备类型：`MOUSE_MOUSE`、`MOUSE_TRACKBALL`、`MOUSE_STICK`、`MOUSE_PAD` 或 `MOUSE_UNKNOWN`。在操作级别 0 时，`model` 始终为 `MOUSE_MODEL_GENERIC`。在更高的操作级别下，它可能为 `MOUSE_MODEL_GENERIC` 或 `MOUSE_MODEL_XXX` 常量之一。`hwid` 始终为零。
**`MOUSE_GETMODE`** `mousemode_t *mode` 该命令获取鼠标驱动程序的当前操作参数。`protocol` 字段表示当用户程序读取鼠标数据时返回设备状态的格式。在操作级别 0 时为 `MOUSE_PROTO_MSC`。在操作级别 1 时为 `MOUSE_PROTO_SYSMOUSE`。`rate` 始终设为 -1。`resolution` 始终设为 -1。`accelfactor` 始终为 0。`packetsize` 字段指定数据包长度，取决于操作级别。`syncmask` 数组保存用于检测数据包首字节的位掩码和模式。`syncmask[0]` 是要与字节进行 AND 运算的位掩码。如果结果等于 `syncmask[1]`，则该字节很可能是数据包的首字节。注意，这种检测首字节的方法并非 100% 可靠；因此，应仅作为参考措施。
**`MOUSE_SETMODE`** `mousemode_t *mode` 该命令按 `mode` 中指定的方式更改鼠标驱动程序的当前操作参数。只有 `level` 可修改。在其他字段中设置值不会产生错误，也无效果。
**`MOUSE_READDATA`** `mousedata_t *data`
**`MOUSE_READSTATE`** `mousedata_t *state` 这些命令不被 `sysmouse` 驱动支持。
**`MOUSE_GETSTATUS`** `mousestatus_t *status` 该命令以 [mouse(4)](mouse.4.md) 中定义的结构返回按键的当前状态和移动计数。

### 控制台和 Consolectl IOCTL

用户进程向当前虚拟控制台发出控制台 Fn ioctl 调用，以控制鼠标指针。控制台 Fn ioctl 还为用户进程提供了一种方法，在按下按键时接收 signal(3)。

鼠标守护进程 [moused(8)](../man8/moused.8.md) 使用对控制台控制设备 **`/dev/consolectl`** 的 Fn ioctl 调用，向控制台通知鼠标动作，包括鼠标移动和按键状态。

这两类 Fn ioctl 命令都定义为 `CONS_MOUSECTL`，它接受以下参数。

```sh
struct mouse_info {
    int operation;
    union {
        struct mouse_data data;
        struct mouse_mode mode;
        struct mouse_event event;
    } u;
};
```

**`MOUSE_SHOW`** 启用并显示鼠标光标。
**`MOUSE_HIDE`** 禁用并隐藏鼠标光标。
**`MOUSE_MOVEABS`** 将鼠标光标移动到 `u.data` 中提供的位置。
**`MOUSE_MOVEREL`** 将 `u.data` 中提供的位置加到当前位置。
**`MOUSE_GETINFO`** 在 `u.data` 中返回当前虚拟控制台的当前鼠标位置和按键状态。
**`MOUSE_MODE`** 设置当按键按下时向当前进程传递的 signal(3)。要传递的信号在 `u.mode` 中设置。

**`MOUSE_ACTION`**
**`MOUSE_MOTION_EVENT`** 这些操作接受 `u.data` 中的信息并据此执行操作。如果 `sysmouse` 驱动已打开，鼠标数据将被发送到 `sysmouse` 驱动。`MOUSE_ACTION` 还处理按键按下动作，并在被请求时向进程发送信号，或者如果当前控制台是文本界面，则执行剪切和粘贴操作。
**`MOUSE_BUTTON_EVENT`** `u.data` 指定一个按键及其点击次数。如果被请求，控制台驱动将使用此信息进行信号传递，或者如果控制台处于文本模式，则用于剪切和粘贴操作。

```sh
struct mouse_data {
    int x;
    int y;
    int z;
    int buttons;
};
```

```sh
struct mouse_mode {
    int mode;
    int signal;
};
```

`#include <signal.h>`

```sh
struct mouse_event {
    int id;
    int value;
};
```

**`data`** `x`、`y` 和 `z` 表示鼠标沿各方向的移动。`buttons` 表示按键状态。它在位 0 到位 30 中编码最多 31 个按键。如果按键被按下，对应的位被置位。
**`mode`** `signal` 字段指定要传递给进程的信号。它必须是定义于其中的值之一。`mode` 字段当前未使用。
**`event`** `id` 字段按 `u.data.buttons` 的方式指定按键编号。只设置一个位/按键。`value` 字段保存点击次数：用户连续点击该按键的次数。

**`operation`** 可以是上述操作之一。上述操作用于虚拟控制台。下面定义的操作用于控制台控制设备，由 [moused(8)](../man8/moused.8.md) 用于将鼠标数据传递给控制台驱动。`MOUSE_MOTION_EVENT` 和 `MOUSE_BUTTON_EVENT` 是较新的接口，设计为配合使用。它们旨在替代由 `MOUSE_ACTION` 单独执行的功能。
**`u`** 此联合是以下之一

## 文件

**`/dev/consolectl`** 控制控制台的设备
**`/dev/sysmouse`** 虚拟化鼠标驱动程序
**`/dev/ttyv%d`** 虚拟控制台

## 参见

vidcontrol(1), ioctl(2), signal(3), [mouse(4)](mouse.4.md), [moused(8)](../man8/moused.8.md)

## 历史

`sysmouse` 驱动首次出现于 FreeBSD 2.2。

## 作者

本手册页由 John-Mark Gurney <jmg@FreeBSD.org> 和 Kazutaka Yokota <yokota@FreeBSD.org> 编写。
