# mlx.4

`mlx` — Mylex DAC 系列 Parallel SCSI RAID 驱动

## 名称

`mlx`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device pci
> device mlx

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
mlx_load="YES"
```

## 描述

`mlx` 驱动为 Mylex DAC 系列 PCI 到 SCSI RAID 控制器提供支持，包括被 Digital/Compaq 重新贴牌的版本。

## 硬件

`mlx` 驱动支持以下 Parallel SCSI RAID 控制器：

- Mylex DAC960P（Wide Fast SCSI-2）
- Mylex DAC960PD / DEC KZPSC（Wide Fast SCSI-2）
- Mylex DAC960PDU（Ultra SCSI-3）
- Mylex DAC960PL（Wide Fast SCSI-2）
- Mylex DAC960PJ（Wide Ultra SCSI-3）
- Mylex DAC960PG（Wide Ultra SCSI-3）
- Mylex DAC960PU / DEC PZPAC（Wide Ultra SCSI-3）
- Mylex AcceleRAID 150（DAC960PRL）（Wide Ultra2 SCSI）
- Mylex AcceleRAID 250（DAC960PTL1）（Wide Ultra2 SCSI）
- Mylex eXtremeRAID 1100（DAC1164P）（Wide Ultra2 SCSI）
- RAIDarray 230 控制器，即 Ultra-SCSI DEC KZPAC-AA（1 通道，4MB 缓存）、KZPAC-CA（3 通道，4MB）、KZPAC-CB（3 通道，8MB 缓存）

## 诊断

### 控制器初始化阶段

- mlx%d: controller initialisation in progress...
- mlx%d: initialisation complete 控制器固件正在执行/已完成初始化。
- mlx%d: physical drive %d:%d not responding 位于 channel:target 的驱动器未响应；可能已发生故障或被移除。
- mlx%d: spinning up drives... 驱动器正在启动；这可能需要几分钟时间。
- mlx%d: configuration checksum error 阵列配置已损坏。
- mlx%d: mirror race recovery in progress
- mlx%d: mirror race on a critical system drive
- mlx%d: mirror race recovery failed 这些错误代码未公开文档。
- mlx%d: physical drive %d:%d COD mismatch 位于 channel:target 的驱动器上的配置数据与阵列其余部分不匹配。
- mlx%d: system drive installation aborted 出现错误导致一个或多个系统驱动器无法配置。
- mlx%d: new controller configuration found 控制器在磁盘上检测到一份配置，该配置优先于其非易失性内存中的配置。控制器将重置并使用新配置启动。
- mlx%d: FATAL MEMORY PARITY ERROR 固件检测到致命内存错误；驱动将不会尝试附加到此控制器。
- mlx%d: unknown firmware initialisation error %x:%x:%x 初始化期间发生未知错误；该错误将被忽略。

### 驱动初始化/关闭阶段：

- mlx%d: can't allocate scatter/gather DMA tag
- mlx%d: can't allocate buffer DMA tag
- mlx%d: can't allocate s/g table
- mlx%d: can't make initial s/g list mapping
- mlx%d: can't make permanent s/g list mapping
- mlx%d: can't allocate interrupt
- mlx%d: can't set up interrupt 初始化驱动时发生资源分配错误；初始化失败，驱动将不会附加到此控制器。
- mlx%d: error fetching drive status 无法获取所有系统驱动器的当前状态；系统驱动器的附加将被中止。
- mlx%d: device_add_child failed 创建系统驱动器实例失败；一个或多个系统驱动器的附加可能已被中止。
- mlxd%d: detaching... 所指示的系统驱动器正在分离。
- mlxd%d: still open, can't detach 所指示的系统驱动器仍处于打开或挂载状态；无法分离该控制器。
- mlx%d: flushing cache... 在分离或关闭之前正在刷新控制器缓存。

### 操作诊断：

- mlx%d: ENQUIRY failed - %s
- mlx%d: ENQUIRY2 failed
- mlx%d: ENQUIRY_OLD failed
- mlx%d: FLUSH failed - %s
- mlx%d: CHECK ASYNC failed - %s
- mlx%d: REBUILD ASYNC failed - %s
- mlx%d: command failed - %s 控制器因所给原因拒绝了某条命令。
- mlx%d: I/O beyond end of unit (%u,%d > %u)
- mlx%d: I/O error - %s 控制器报告了 I/O 错误。
- mlx%d: periodic enquiry failed - %s 由于所给原因，尝试轮询控制器状态失败。
- mlx%d: mlx_periodic_enquiry: unknown command %x 周期性状态轮询发出了一条已损坏的命令。
- mlxd%d: drive offline
- mlxd%d: drive online
- mlxd%d: drive critical 所指示的系统磁盘已改变状态。
- mlx%d: physical drive %d:%d reset
- mlx%d: physical drive %d:%d killed %s
- mlx%d: physical drive %d:%d error log: sense = %d asc = %x asq = %x
- mlx%d: info %4D csi %4D 位于 channel:target 的驱动器已被重置、因所给原因被禁用，或发生了 SCSI 错误。
- mlx%d: unknown log message type %x
- mlx%d: error reading message log - %s 尝试读取控制器的消息日志时发生错误。
- mlxd%d: consistency check started
- mlx%d: consistency check completed 用户发起的一致性检查已开始/完成。
- mlx%d: drive rebuild started for %d:%d
- mlx%d: drive rebuild completed 用户发起的物理驱动器重建已开始/完成。
- mlx%d: background check/rebuild operation started
- mlx%d: background check/rebuild operation completed 自动系统驱动器一致性检查或物理驱动器重建已开始/完成。
- mlx%d: channel %d pausing for %d seconds
- mlx%d: channel %d resuming
- mlx%d: pause command failed - %s
- mlx%d: pause failed for channel %d
- mlx%d: resume command failed - %s
- mlx%d: resume failed for channel %d 控制器/通道暂停操作通知。（目前任何控制器都不支持通道暂停。）
- mlx%d: controller wedged (not taking commands) 控制器对提交新命令的尝试未作出响应。
- mlx%d: duplicate done event for slot %d
- mlx%d: done event for nonbusy slot %d 控制器上的命令列表或驱动中发生了数据损坏。

## 参见

[mlxcontrol(8)](../man8/mlxcontrol.8.md)

## 作者

`mlx` 驱动由 Michael Smith <msmith@FreeBSD.org> 编写。

本手册页由 Jeroen Ruigrok van der Werven <asmodai@FreeBSD.org> 和 Michael Smith <msmith@FreeBSD.org> 编写。

## 缺陷

DEC KZPSC 的 flash ROM 容量不足，无法容纳任何较新的固件。这给本驱动带来了问题。

该驱动尚不支持 AcceleRAID 352 以及 eXtremeRAID 2000 和 3000 产品中使用的 6.x 版本固件。
