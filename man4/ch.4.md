# ch.4

`ch` — SCSI 介质更换器（juke box）驱动

## 名称

`ch`

## 概要

`device ch`

## 描述

`ch` 驱动为 *SCSI* 介质更换器提供支持。它允许在多个驱动器之间复用大量介质槽位。更换器设备可选配条形码阅读器，用于读取附在介质上的标签信息。

在配置 SCSI 更换器之前，还必须单独将 SCSI 适配器配置到系统中。

在引导期间探测 SCSI 适配器时，会扫描 *SCSI* 总线以查找设备。任何应答为“Changer”类型的设备将被“附加”到 `ch` 驱动。在 FreeBSD 2.1 之前的版本中，第一个找到的设备将被附加为 *ch0*，下一个为 *ch1*，依此类推。从 2.1 起，可以指定设备以何种 ch 单元号上线；有关内核配置的详细信息，请参见 [scsi(4)](scsi.4.md)。

## 内核配置

只需显式配置一个 `ch` 设备；数据结构会在 SCSI 总线上发现介质更换时动态分配。

## ioctl

用户态程序通过下述若干 ioctl 与更换器驱动通信。内核与更换器设备之间通信所使用的更换器元素地址映射为从零开始的逻辑地址。元素类型规定如下：

**`CHET_MT`** 介质传输元素（抓取器）。

**`CHET_ST`** 存储元素（槽位）。

**`CHET_IE`** 导入/导出元素（端口）。

**`CHET_DT`** 数据传输元素（驱动器）。

以下 ioctl(2) 调用适用于更换器。它们定义在头文件

`#include <sys/chio.h>`

中。

```sh
u_int cm_fromtype; /* 源元素类型 */
u_int cm_fromunit; /* 源元素的逻辑单元 */
u_int cm_totype;   /* 目标元素类型 */
u_int cm_tounit;   /* 目标元素的逻辑单元 */
u_int cm_flags;	   /* 杂项标志 */
```

```sh
u_int ce_srctype;	 /* 源元素类型 */
u_int ce_srcunit;	 /* 源元素的逻辑单元 */
u_int ce_fdsttype; /* 第一目标元素类型 */
u_int ce_fdstunit; /* 第一目标元素的逻辑单元 */
u_int ce_sdsttype; /* 第二目标元素类型 */
u_int ce_sdstunit; /* 第二目标元素的逻辑单元 */
u_int ce_flags;	 /* 杂项标志 */
```

```sh
u_int cp_type;  /* 元素类型 */
u_int cp_unit;  /* 元素的逻辑单元 */
u_int cp_flags; /* 杂项标志 */
```

```sh
u_int cp_npickers; /* 抓取器数量 */
u_int cp_nslots;   /* 槽位数量 */
u_int cp_nportals; /* 导入/导出端口数量 */
u_int cp_ndrives;  /* 驱动器数量 */
```

```sh
u_int                          cesr_element_type;
u_int                          cesr_element_base;
u_int                          cesr_element_count;
u_int                          cesr_flags;
struct changer_element_status *cesr_element_status;
```

```sh
u_int            ces_addr;      /* 介质更换器中的元素地址 */
u_char           ces_flags;     /* 参见下文的 CESTATUS 定义 */
u_char           ces_sensecode; /* 元素的附加检测码 */
u_char           ces_sensequal; /* 附加检测码限定符 */
u_char           ces_invert;    /* 翻转位 */
u_char           ces_svalid;    /* 源地址（ces_source）有效 */
u_short          ces_source;    /* 介质的源地址 */
changer_voltag_t ces_pvoltag;   /* 主卷标 */
changer_voltag_t ces_avoltag;   /* 备用卷标 */
u_char           ces_idvalid;   /* ces_scsi_id 有效 */
u_char           ces_scsi_id;   /* 元素的 SCSI ID（当 ces_idvalid 非零时） */
u_char           ces_lunvalid;  /* ces_scsi_lun 有效 */
u_char           ces_scsi_lun;  /* 元素的 SCSI LUN（当 ces_lunvalid 非零时） */
```

**`CESTATUS_FULL`** 存在介质。

**`CESTATUS_IMPEXP`** 介质由操作员放置（而非由抓取器放置）。

**`CESTATUS_EXCEPT`** 元素处于异常状态（例如条形码标签无效、条形码尚未扫描）。

**`CESTATUS_ACCESS`** 抓取器可访问该元素。

**`CESTATUS_EXENAB`** 该元素支持介质导出。

**`CESTATUS_INENAB`** 该元素支持介质导入。

**`CHIOMOVE`** (`struct changer_move`) 使用当前抓取器将介质从一个元素移动到另一个元素（**MOVE MEDIUM**）。源元素和目标元素在 changer_move 结构中指定，该结构至少包含以下字段：如果 `cm_flags` 字段中设置了 `CM_INVERT`，则指示介质更换器在移动介质时将其翻转。

**`CHIOEXCHANGE`** (`struct changer_exchange`) 将位于源元素中的介质移动到第一目标元素，并将原在第一目标元素中的介质移动到第二目标元素。在简单交换的情况下，源元素和第二目标元素应为同一元素。此操作使用当前抓取器执行。受影响元素的地址在 `changer_exchange` 结构中指定给 ioctl，该结构至少包含以下字段：在 `ce_flags` 中，可设置 `CM_INVERT1` 和/或 `CM_INVERT2`，以在交换操作期间分别翻转第一或第二个介质。*此操作未经测试。*

**`CHIOPOSITION`** (`struct changer_position`) 将当前抓取器定位到指定元素前方。该元素由 changer_position 结构指定，该结构至少包含以下字段：`cp_flags` 字段可设为 `CP_INVERT` 以在操作期间翻转抓取器。

**`CHIOGPICKER`** (`int`) 返回当前抓取器的逻辑地址。

**`CHIOSPICKER`** (`int`) 选择由给定逻辑地址指定的抓取器。

**`CHIOGPARAMS`** (`struct changer_params`) 返回介质更换器的配置参数。此 ioctl 用至少包含以下字段的内容填充用户传入的 changer_params 结构：应用程序可使用此调用在使用 `CHIGSTATUS` ioctl 查询自动点唱机状态之前查询其尺寸。

**`CHIOIELEM`** 对介质更换器设备执行 **INITIALIZE ELEMENT STATUS** 调用。这会强制介质更换器根据已加载的介质更新其内部状态信息。如果配备了标签阅读器，还会扫描任何条形码标签。`ch` 驱动的状态不受此调用影响。

**`CHIOGSTATUS`** (`struct changer_element_status_request`) 对介质更换器设备执行 **READ ELEMENT STATUS** 调用。此调用读取介质更换器的元素状态信息，并将其转换为 `changer_element_status` 结构数组。每次调用 `CHIOGSTATUS` 可查询一种类型的一个或多个元素的状态。应用程序向 `ch` 驱动传递一个 `changer_element_status_request` 结构，其中包含以下字段：驱动读取此结构以确定要返回信息的元素类型、逻辑基址和元素数量，这些信息存放在 `cesr_element_status` 字段所指向的 `changer_element_status` 结构数组中。应用程序必须为 `cesr_element_count` 个状态结构分配足够的内存（见下文）。`cesr_flags` 可选地设为 `CESR_VOLTAGS`，表示要从自动点唱机读取并返回卷标（条形码）信息。`cesr_element_base` 和 `cesr_element_count` 字段必须相对于更换器的物理配置有效。如果无效，`CHIOGSTATUS` ioctl 将返回 Er EINVAL 错误码。有关元素的信息在 `changer_element_status` 结构数组中返回。该结构至少包含以下字段：`ces_addr` 字段包含元素在介质更换器坐标系中的地址。驱动不使用此字段，应仅用于诊断目的。`ces_flags` 字段定义了以下标志：注意并非所有标志对所有元素类型都有效。

## 注释

本版本的 `ch` 驱动已在 DEC TZ875（5 槽位，一个 DLT 驱动器）和 Breece Hill Q47（60 槽位，四个 DLT 驱动器，条形码阅读器）上测试过。

由于可用于测试的设备不支持必要的命令，`ch` 驱动支持的许多功能未经充分测试。这适用于备用卷标、介质翻转、导入/导出元素处理、多抓取器操作等。

## 文件

**`/dev/ch[0-9]`** 设备条目

## 诊断

如果介质更换器不支持 `ch` 驱动所请求的功能，它将产生控制台错误消息，并向上文所述的 ioctl 返回失败码。

## 参见

chio(1), cam(4), [cd(4)](cd.4.md), [da(4)](da.4.md), [sa(4)](sa.4.md)

## 历史

`ch` 驱动出现于 386BSD。

## 作者

`ch` 驱动由 Jason R. Thorpe <thorpej@and.com> 为 And Communications（`http://www.and.com/`）编写。由 Stefan Grefen <grefen@goofy.zdv.uni-mainz.de> 添加到系统中（他显然拥有这样一台设备）。由 Kenneth Merry <ken@FreeBSD.org> 移植到 CAM。由 Hans Huebner <hans@artcom.de> 更新以支持卷标。
