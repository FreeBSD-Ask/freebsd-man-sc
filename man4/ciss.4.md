# ciss(4)

`ciss` — Common Interface for SCSI-3 Support 驱动

## 名称

`ciss`

## 概要

要将此驱动编译进内核，请在你的内核配置文件中加入以下行：

> device scbus
> device ciss

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
ciss_load="YES"
```

## 描述

`ciss` 驱动声称在通用 SCSI 传输和智能主机适配器之间提供公共接口。

`ciss` 驱动支持 Compaq Computer Corporation 于 2000/11/27 发布的题为“CISS Command Interface for SCSI-3 Support Open Specification, Version 1.04, Valence Number 1”文档中所定义的 *CISS*。

我们在 `ciss` 接口和 CAM(4) 之间提供了 shim 层，将大部分排队和作为磁盘的职责交给 CAM 处理。通过 PCI 总线附加 Fn ciss_probe、Fn ciss_attach 等以及通过 CAM 接口 Fn ciss_cam_action 和 Fn ciss_cam_poll 进入驱动。Compaq `ciss` 适配器需要伪造的响应才能获得合理的行为。此外，`ciss` 命令集远不足以支持 RAID 控制器的功能，因此所支持的 Compaq 适配器利用了早期 Compaq 适配器系列的控制协议的某些部分。

目前 `ciss` 支持“simple”和“performant”传输层。

非磁盘设备（如内部 DAT 和连接到外部 SCSI 总线的设备）作为普通 CAM 设备受到支持，前提是它们由控制器固件导出且未被标记为已屏蔽。通过在引导时将 `hw.ciss.expose_hidden_physical` 可调参数设为非零值，可以暴露被屏蔽的设备。直接访问设备（如磁盘驱动器）仅作为 [pass(4)](pass.4.md) 设备暴露。支持设备的热插拔，通知消息将报告到控制台和日志。

适配器冻结并显示消息“ADAPTER HEARTBEAT FAILED”的问题，可能通过更新固件和/或在引导时将 `hw.ciss.nop_message_heartbeat` 可调参数设为非零值来解决。

## 硬件

`ciss` 驱动支持实现了 Common Interface for SCSI-3 Support Open Specification v1.04 的控制器，包括：

- Compaq Smart Array 5300（仅 simple 模式）
- Compaq Smart Array 532
- Compaq Smart Array 5i
- HP Smart Array 5312
- HP Smart Array 6i
- HP Smart Array 641
- HP Smart Array 642
- HP Smart Array 6400
- HP Smart Array 6400 EM
- HP Smart Array E200
- HP Smart Array E200i
- HP Smart Array E500
- HP Smart Array H240
- HP Smart Array H240ar
- HP Smart Array H240nr
- HP Smart Array H241
- HP Smart Array H244br
- HP Smart Array P212
- HP Smart Array P220i
- HP Smart Array P222
- HP Smart Array P230i
- HP Smart Array P240nr
- HP Smart Array P244br
- HP Smart Array P246br
- HP Smart Array P400
- HP Smart Array P400i
- HP Smart Array P410
- HP Smart Array P410i
- HP Smart Array P411
- HP Smart Array P420
- HP Smart Array P420i
- HP Smart Array P421
- HP Smart Array P430
- HP Smart Array P430i
- HP Smart Array P431
- HP Smart Array P440
- HP Smart Array P440ar
- HP Smart Array P441
- HP Smart Array P530
- HP Smart Array P531
- HP Smart Array P542d
- HP Smart Array P600
- HP Smart Array P700m
- HP Smart Array P712m
- HP Smart Array P721m
- HP Smart Array P731m
- HP Smart Array P741m
- HP Smart Array P800
- HP Smart Array P812
- HP Smart Array P822
- HP Smart Array P830
- HP Smart Array P830i
- HP Smart Array P840
- HP Smart Array P840ar
- HP Smart Array P841
- HP Modular Smart Array 20（MSA20）
- HP Modular Smart Array 500（MSA500）

此外，若干 HP Smart Array 控制器仅通过 PCI 子设备 ID 提供支持，因为无法获知其型号名称：0x3220、0x3222、0x3230、0x3231、0x3232、0x3233、0x3236、0x3238、0x3239、0x323A、0x323B、0x323C 和 0x324B（PCI 子厂商均为 0x103C）。

## 参见

cam(4), [pass(4)](pass.4.md), [xpt(4)](xpt.4.md), loader.conf(5), [camcontrol(8)](../man8/camcontrol.8.md)

> "CISS Command Interface for SCSI-3 Support Open Specification, Version 1.04, Valence Number 1", 2000/11/27.

## 作者

`ciss` 驱动由 Mike Smith <msmith@FreeBSD.org> 编写。

本手册页基于其注释编写，由 Tom Rhodes <trhodes@FreeBSD.org> 撰写。
