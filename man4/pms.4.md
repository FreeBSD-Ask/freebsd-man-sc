# pms.4

`pms` — PMC-Sierra PM8001/8081/8088/8089/8074/8076/8077 SAS/SATA HBA 控制器驱动

## 名称

`pms`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device pmspcv

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
pmspcv_load="YES"
```

## 描述

`pms` 驱动为 PMC-Sierra PM8001/8081/8088/8089/8074/8076/8077 系列的 SAS/SATA HBA 控制器提供支持。

## 硬件

`pms` 驱动支持以下硬件：

- Tachyon TS 光纤通道卡
- Tachyon TL 光纤通道卡
- Tachyon XL2 光纤通道卡
- Tachyon DX2 光纤通道卡
- Tachyon DX2+ 光纤通道卡
- Tachyon DX4+ 光纤通道卡
- Tachyon QX2 光纤通道卡
- Tachyon QX4 光纤通道卡
- Tachyon DE4 光纤通道卡
- Tachyon QE4 光纤通道卡
- Tachyon XL10 光纤通道卡
- PMC Sierra SPC SAS-SATA 卡
- PMC Sierra SPC-V SAS-SATA 卡
- PMC Sierra SPC-VE SAS-SATA 卡
- PMC Sierra SPC-V 16 端口 SAS-SATA 卡
- PMC Sierra SPC-VE 16 端口 SAS-SATA 卡
- PMC Sierra SPC-V SAS-SATA 卡 12Gig
- PMC Sierra SPC-VE SAS-SATA 卡 12Gig
- PMC Sierra SPC-V 16 端口 SAS-SATA 卡 12Gig
- PMC Sierra SPC-VE 16 端口 SAS-SATA 卡 12Gig
- Adaptec Hialeah 4/8 端口 SAS-SATA HBA 卡 6Gig
- Adaptec Hialeah 4/8 端口 SAS-SATA RAID 卡 6Gig
- Adaptec Hialeah 8/16 端口 SAS-SATA HBA 卡 6Gig
- Adaptec Hialeah 8/16 端口 SAS-SATA RAID 卡 6Gig
- Adaptec Hialeah 8/16 端口 SAS-SATA HBA 加密卡 6Gig
- Adaptec Hialeah 8/16 端口 SAS-SATA RAID 加密卡 6Gig
- Adaptec Delray 8 端口 SAS-SATA HBA 卡 12Gig
- Adaptec Delray 8 端口 SAS-SATA HBA 加密卡 12Gig
- Adaptec Delray 16 端口 SAS-SATA HBA 卡 12Gig
- Adaptec Delray 16 端口 SAS-SATA HBA 加密卡 12Gig

## 参见

cam(4), [camcontrol(8)](../man8/camcontrol.8.md)

## 历史

`pms` 设备驱动首次出现于 FreeBSD 10.2。
