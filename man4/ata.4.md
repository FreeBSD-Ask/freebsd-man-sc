# ata.4

`ata` — 通用 ATA/SATA 控制器驱动

## 名称

`ata`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device scbus
> device ata

或者，要在引导时以模块集合形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下若干行：

```sh
ata_load="YES"
ataisa_load="YES"
atapci_load="YES"
ataacard_load="YES"
ataacerlabs_load="YES"
ataamd_load="YES"
ataati_load="YES"
atacenatek_load="YES"
atacypress_load="YES"
atacyrix_load="YES"
atahighpoint_load="YES"
ataintel_load="YES"
ataite_load="YES"
atajmicron_load="YES"
atamarvell_load="YES"
atamicron_load="YES"
atanational_load="YES"
atanetcell_load="YES"
atanvidia_load="YES"
atapromise_load="YES"
ataserverworks_load="YES"
atasiliconimage_load="YES"
atasis_load="YES"
atavia_load="YES"
```

第一行用于硬件无关的公共代码，是其他模块的前提条件。接下来三行是通用的总线相关驱动。其余为厂商特定的 PCI 驱动。

以下可调参数可从 [loader(8)](../man8/loader.8.md) 设置：

**hw.ata.ata_dma_check_80pin** 设为 0 可禁用 80 针电缆检测（默认为 1，即检测电缆）。

**hint.atapci.X.msi** 设为 1 允许指定的 PCI ATA 控制器在支持时使用消息信号中断（MSI）。

**hint.ata.X.devX.mode** 限制指定通道上指定设备的初始 ATA 模式。

**hint.ata.X.mode** 限制指定通道上所有设备的初始 ATA 模式。

**hint.ata.X.pm_level** 控制指定通道的 SATA 接口电源管理，允许以增加命令延迟为代价节省部分功耗。可能取值：

**0** 禁用接口电源管理。此为默认值。

**1** 允许设备发起 PM 状态更改；主机为被动方。

**hint.ata.X.devX.sata_rev** 限制指定通道上指定设备的初始 SATA 版本（速度）。值 1、2 和 3 分别对应 1.5、3 和 6Gbps。

**hint.ata.X.sata_rev** 同上，但作用于指定通道上的所有设备。

## 描述

`ata` 驱动使 CAM(4) 子系统能够访问许多通用控制器的 ATA（IDE）和 SATA 端口。根据控制器的不同，每个 PATA（IDE）端口或每一两个 SATA 端口会作为带有一个或两个目标设备的独立总线呈现给 CAM。大多数总线管理细节由 CAM 的 ATA/SATA 专用传输层处理。已连接的 ATA 磁盘由 ATA 协议磁盘外围驱动 [ada(4)](ada.4.md) 处理。ATAPI 设备由 SCSI 协议外围驱动 [cd(4)](cd.4.md)、[da(4)](da.4.md)、[sa(4)](sa.4.md) 等处理。

此驱动支持 ATA，并且对大多数控制器支持 ATAPI 设备。不支持命令队列和 SATA 端口倍增器。仅在部分控制器上支持设备热插拔和 SATA 接口电源管理。

`ata` 驱动可在系统运行期间更改传输模式。参见 [camcontrol(8)](../man8/camcontrol.8.md) 的 `negotiate` 子命令。

`ata` 驱动默认设置为硬件支持的最高传输模式。但 `ata` 驱动有时会警告：“**DMA limited to UDMA33, non-ATA66 cable or device**”。这表示 `ata` 驱动检测到所需的 80 芯电缆不存在或无法正确检测，或者通道上的某个设备最高仅支持 UDMA2/ATA33。可将 `hw.ata.ata_dma_check_80pin` 可调参数设为 0 以禁用此检测。

## 硬件

`ata` 驱动支持以下 ATA/SATA 控制器上的 IDE 接口：

**Acard：** ATP850P、ATP860A、ATP860R、ATP865A、ATP865R。
**ALI：** M5228、M5229、M5281、M5283、M5287、M5288、M5289。
**AMD：** AMD756、AMD766、AMD768、AMD8111、CS5536。
**ATI：** IXP200、IXP300、IXP400、IXP600、IXP700、IXP800。
**CMD：** CMD646、CMD646U2、CMD648、CMD649。
**Cypress：** Cypress 82C693。
**Cyrix：** Cyrix 5530。
**HighPoint：** HPT302、HPT366、HPT368、HPT370、HPT371、HPT372、HPT372N、HPT374。
**Intel：** 6300ESB、31244、PIIX、PIIX3、PIIX4、ESB2、ICH、ICH0、ICH2、ICH3、ICH4、ICH5、ICH6、ICH7、ICH8、ICH9、ICH10、SCH、PCH。
**ITE：** IT8211F、IT8212F、IT8213F。
**JMicron：** JMB360、JMB361、JMB363、JMB365、JMB366、JMB368。
**Marvell** 88SE6101、88SE6102、88SE6111、88SE6121、88SE6141、88SE6145。
**National：** SC1100。
**NetCell：** NC3000、NC5000。
**nVidia：** nForce、nForce2、nForce2 MCP、nForce3、nForce3 MCP、nForce3 Pro、nForce4、MCP51、MCP55、MCP61、MCP65、MCP67、MCP73、MCP77、MCP79、MCP89。
**Promise：** PDC20246、PDC20262、PDC20263、PDC20265、PDC20267、PDC20268、PDC20269、PDC20270、PDC20271、PDC20275、PDC20276、PDC20277、PDC20318、PDC20319、PDC20371、PDC20375、PDC20376、PDC20377、PDC20378、PDC20379、PDC20571、PDC20575、PDC20579、PDC20580、PDC20617、PDC20618、PDC20619、PDC20620、PDC20621、PDC20622、PDC40518、PDC40519、PDC40718、PDC40719。
**ServerWorks：** HT1000、ROSB4、CSB5、CSB6、K2、Frodo4、Frodo8。
**Silicon** Image：SiI0680、SiI3112、SiI3114、SiI3512。
**SiS：** SIS180、SIS181、SIS182、SIS5513、SIS530、SIS540、SIS550、SIS620、SIS630、SIS630S、SIS633、SIS635、SIS730、SIS733、SIS735、SIS745、SIS961、SIS962、SIS963、SIS964、SIS965。
**VIA：** VT6410、VT6420、VT6421、VT82C586、VT82C586B、VT82C596、VT82C596B、VT82C686、VT82C686A、VT82C686B、VT8231、VT8233、VT8233A、VT8233C、VT8235、VT8237、VT8237A、VT8237S、VT8251、CX700、VX800、VX855、VX900。

上述部分芯片可配置为 AHCI 模式。这种情况下改由 [ahci(4)](ahci.4.md) 驱动支持。

未知的 ATA 芯片组以 PIO 模式支持；如果标准总线主控 DMA 寄存器存在且包含有效设置，也会启用 DMA，但最高模式被限制为 UDMA33，因为无法确定芯片组的能力及如何编程。

## 注意事项

请记住，要使用 UDMA4/ATA66 及以上模式，你*必须*使用 80 芯电缆。请确保排线长度不超过 45cm。对于圆形 ATA 电缆，长度取决于电缆质量。按规范 SATA 电缆最长可达 1m。外部 SATA 电缆可达 2m 或更长，但并非所有控制器在长电缆下都能正常工作，尤其是在高速模式下。

## 参见

[ada(4)](ada.4.md), [ahci(4)](ahci.4.md), cam(4), [cd(4)](cd.4.md), [mvs(4)](mvs.4.md), [siis(4)](siis.4.md), [camcontrol(8)](../man8/camcontrol.8.md)

## 历史

`ata` 驱动首次出现于 FreeBSD 4.0。在 FreeBSD 9.0 中被改造为 CAM(4) 接口模块。

## 作者

Alexander Motin <mav@FreeBSD.org> 与 Søren Schmidt <sos@FreeBSD.org>
