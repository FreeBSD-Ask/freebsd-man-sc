# cd.4

`cd` — SCSI CD-ROM 驱动

## 名称

`cd`

## 概要

`device cd`

## 描述

`cd` 驱动为 SCSI CD-ROM（Compact Disc-Read Only Memory，光盘只读存储器）驱动器提供支持。为使其呈现为常规磁盘，`cd` 驱动会合成分区表，其中一个分区覆盖整个 CD-ROM。可以使用 disklabel(8) 修改此分区表，但修改仅在 CD-ROM 卸载之前有效。总体而言，其接口与 [ada(4)](ada.4.md) 和 [da(4)](da.4.md) 中描述的类似。

在引导期间探测 SCSI 适配器时，系统会扫描 SCSI 总线以查找设备。任何应答为 CDROM（类型 5）或 WORM（类型 4）类型的设备会附加到 `cd` 驱动。在 FreeBSD 2.1 之前，第一个找到的设备附加为 `cd0`，下一个为 `cd1`，依此类推。从 FreeBSD 2.1 起，可以指定设备以何种 cd 单元号上线；有关内核配置的详细信息，请参见 [scsi(4)](scsi.4.md)。

系统工具 disklabel(8) 可用于读取合成的磁盘标签结构，其中包含 CD-ROM 大小的正确数据，以备需要时使用。

## 内核配置

不论系统配置如何，均可附加任意数量的 CD-ROM 设备，因为所有资源都是动态分配的。

## ioctl

以下适用于 SCSI CD-ROM 驱动器的 ioctl(2) 调用定义在头文件

`#include <sys/cdio.h>`

和

`#include <sys/disklabel.h>`

中。

```sh
struct ioc_play_track
{
	u_char	start_track;
	u_char	start_index;
	u_char	end_track;
	u_char	end_index;
};
```

```sh
struct ioc_play_blocks
{
	int	blk;
	int	len;
};
```

```sh
struct ioc_play_msf
{
	u_char	start_m;
	u_char	start_s;
	u_char	start_f;
	u_char	end_m;
	u_char	end_s;
	u_char	end_f;
};
```

```sh
struct ioc_read_subchannel {
	u_char address_format;
#define CD_LBA_FORMAT	1
#define CD_MSF_FORMAT	2
	u_char data_format;
#define CD_SUBQ_DATA		0
#define CD_CURRENT_POSITION	1
#define CD_MEDIA_CATALOG	2
#define CD_TRACK_INFO		3
	u_char track;
	int	data_len;
	struct  cd_sub_channel_info *data;
};
```

```sh
struct ioc_toc_header {
	u_short len;
	u_char  starting_track;
	u_char  ending_track;
};
```

```sh
struct ioc_read_toc_entry {
	u_char	address_format;
	u_char	starting_track;
	u_short	data_len;
	struct  cd_toc_entry *data;
};
```

```sh
struct ioc_patch {
	u_char	patch[4];
	/* 每个通道一个 */
};
```

```sh
struct	ioc_vol
{
	u_char	vol[4];
	/* 每个通道一个 */
};
```

**`CDIOCPLAYTRACKS`** (`struct ioc_play_track`) 根据给定的轨道地址和长度开始音频播放。该结构定义如下：

**`CDIOCPLAYBLOCKS`** (`struct ioc_play_blocks`) 根据给定的块地址和长度开始音频播放。该结构定义如下：

**`CDIOCPLAYMSF`** (`struct ioc_play_msf`) 根据给定的“分-秒-帧”地址和长度开始音频播放。该结构定义如下：

**`CDIOCREADSUBCHANNEL`** (`struct ioc_read_subchannel`) 从此结构指定位置的子通道读取信息：

**`CDIOREADTOCHEADER`** (`struct ioc_toc_header`) 返回已挂载 CD-ROM 目录表的摘要信息。信息返回到以下结构中：

**`CDIOREADTOCENTRYS`** (`struct ioc_read_toc_entry`) 返回所提及的目录表条目信息。（是的，此命令名称拼写有误。）参数结构定义如下：请求数据被写入大小为 `data_len` 的区域，并由 `data` 指向。

**`CDIOCSETPATCH`** (`struct ioc_patch`) 将各音频通道连接到各输出通道。参数结构定义如下：

**`CDIOCGETVOL`**

**`CDIOCSETVOL`** (`struct ioc_vol`) 获取（设置）输出通道的音量设置信息。参数结构如下：

**`CDIOCSETMONO`** 将所有输出通道连接到所有源通道。

**`CDIOCSETSTEREO`** 将左源通道连接到左输出通道，右源通道连接到右输出通道。

**`CDIOCSETMUTE`** 在不更改音量设置的情况下静音输出。

**`CDIOCSETLEFT`**

**`CDIOCSETRIGHT`** 将两个输出通道都连接到左（右）源通道。

**`CDIOCSETDEBUG`**

**`CDIOCCLRDEBUG`** 为相应设备打开（关闭）调试。

**`CDIOCPAUSE`**

**`CDIOCRESUME`** 暂停（恢复）音频播放，而不重置读取头的位置。

**`CDIOCRESET`** 重置驱动器。

**`CDIOCSTART`**

**`CDIOCSTOP`** 通知驱动器启动（停止）CD-ROM 主轴旋转。

**`CDIOCALLOW`**

**`CDIOCPREVENT`** 通知驱动器允许（阻止）手动弹出 CD-ROM 光盘。并非所有驱动器都支持此功能。

**`CDIOCEJECT`** 弹出 CD-ROM。

**`CDIOCCLOSE`** 通知驱动器关闭其仓门并加载介质。并非所有驱动器都支持此功能。

## 注释

当由 `cd` 驱动控制的驱动器中的 CD-ROM 更换时，更换介质的操作会使磁盘标签和内核中保存的信息失效。为防止数据损坏，对设备的所有访问都会丢弃，直到没有更多打开的文件描述符引用该设备。在此期间，所有新的打开尝试都会拒绝。当没有更多打开的文件描述符引用该设备时，下一次打开将加载该驱动器的新参数集（包括磁盘标签）。

`cd` 驱动中的音频代码仅支持 SCSI-2 标准音频命令。由于许多 CD-ROM 制造商未遵循标准，有许多 CD-ROM 驱动器无法正常播放音频。计划对一些较为常见的“不合规”CD-ROM 驱动器提供支持，但目前尚未着手实施。

## sysctl 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**kern.cam.cd.retry_count** 此变量决定 `cd` 驱动重试 READ 或 WRITE 命令的次数。这不会影响探测期间或 `cd` 驱动转储例程使用的重试次数。此值当前默认为 4。

**kern.cam.cd.%d.minimum_cmd_size** `cd` 驱动会尝试自动判断所通信的驱动器是否支持 6 字节或 10 字节的 MODE SENSE/MODE SELECT 操作。许多 SCSI 驱动器仅支持 6 字节命令，而 ATAPI 驱动器仅支持 10 字节命令。`cd` 驱动首先通过发出 CAM Path Inquiry CCB 来尝试判断所使用的协议是否通常支持 6 字节命令，然后据此默认使用 6 字节或 10 字节命令。此后，`cd` 驱动默认使用 6 字节命令（假设驱动器所使用的协议声称支持 6 字节命令），直到某次命令以 SCSI ILLEGAL REQUEST 错误失败。然后它会尝试该命令的 10 字节版本以查看是否可行。用户可按驱动器的 sysctl 变量和 loader 可调参数更改默认值。其中“%d”是相应驱动器的单元号。有效的最小命令大小为 6 和 10。任何大于 6 的值会舍入为 10，任何小于 6 的值会舍入为 6。

## 文件

**`/dev/cd[0-9][a-h]`** raw 模式 CD-ROM 设备

## 诊断

无。

## 参见

cam(4), [cd9660(4)](cd9660.4.md), [da(4)](da.4.md), disklabel(8), [cd(9)](../man9/cd.9.md)

## 历史

本 `cd` 驱动基于 Julian Elischer 编写的 `cd` 驱动，后者出现于 386BSD。`cd` 驱动的 CAM 版本由 Kenneth Merry 编写，首次出现于 FreeBSD 3.0。

## 缺陷

用作 Fn ioctl 第三个参数的结构名称选择不当，且 Fn ioctl 命令的名称中遗留了若干拼写错误。
