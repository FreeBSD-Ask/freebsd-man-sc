# targ(4)

`targ` — SCSI 目标模拟器驱动程序

## 名称

`targ`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device targ

## 描述

`targ` 驱动为用户态程序提供模拟 SCSI 目标设备的接口。在 **`/usr/share/examples/scsi_target`** 中可以找到一个模拟磁盘驱动器（类似于 [da(4)](da.4.md)）的示例程序。

`targ` 驱动提供控制设备 **`/dev/targ`** 。打开设备后，文件描述符必须绑定到特定的总线/目标/LUN，并使用 `TARGIOCENABLE` ioctl 启用以处理 CCB。然后进程使用 write(2) 将 CCB 发送到 SIM，并使用 poll(2) 或 kqueue(2) 查看响应是否就绪。指向已完成 CCB 的指针通过 read(2) 返回。用户 CCB 请求的任何数据传输都通过零拷贝 IO 完成。

## IOCTL

以下 ioctl(2) 调用定义于头文件

`#include <cam/scsi/scsi_targetio.h>`

```sh
struct ioc_enable_lun {
	path_id_t	path_id;
	target_id_t	target_id;
	lun_id_t	lun_id;
	int		grp6_len;
	int		grp7_len;
};
```

**`TARGIOCENABLE`**（`struct ioc_enable_lun`）按以下结构在指定 LUN 上启用目标模式：所选的路径（总线）、目标和 LUN 必须未被使用，否则返回 Er EADDRINUSE。如果 `grp6_len` 或 `grp7_len` 非零，则启用接收厂商特定命令。

**`TARGIOCDISABLE`** 禁用目标模式并中止所有挂起的 CCB。CCB 可选择在完成时读取。然后可调用 `TARGIOCENABLE` 激活不同的 LUN。多次禁用调用无效。如果已启用，close(2) 系统调用会自动禁用目标模式。

**`TARGIOCDEBUG`**（`int`）如果参数非零，则启用 `CAM_PERIPH` 调试，否则禁用。

## 文件

**cam/scsi/scsi_targetio.h** 描述用户态接口。
**`/sys/cam/scsi/scsi_target.c`** 是驱动源文件。
**`/dev/targ`** 是控制设备。

## 参见

**`/usr/share/examples/scsi_target`**, [ahc(4)](ahc.4.md), [isp(4)](isp.4.md), [scsi(4)](scsi.4.md)

> “FreeBSD Target Information”。

## 作者

`targ` 驱动首次出现于 FreeBSD 3.0，由 Justin T. Gibbs 编写。在 FreeBSD 5.0 中由 Nate Lawson <nate@root.org> 重写。

## 缺陷

目前，只有 [ahc(4)](ahc.4.md) 和 [isp(4)](isp.4.md) 驱动完全支持目标模式。

[ahc(4)](ahc.4.md) 驱动在目标模式下不支持标记队列。
