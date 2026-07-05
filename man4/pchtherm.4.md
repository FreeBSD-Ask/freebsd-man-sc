# pchtherm.4

`pchtherm` — Intel PCH 热子系统

## 名称

`pchtherm`

## 概要

`device pci device pchtherm`

## 描述

`pchtherm` 驱动提供对 Intel PCH 芯片组中安装的传感器数据和配置的访问。`pchtherm` 配置寄存器。

通过 [sysctl(8)](../man8/sysctl.8.md) 接口访问 `pchtherm` 数据：

```sh
dev.pchtherm.0.ctt: 115.0C
dev.pchtherm.0.temperature: 28.5C
dev.pchtherm.0.t2temp: 91.0C
dev.pchtherm.0.t1temp: 86.0C
dev.pchtherm.0.t0temp: 81.0C
dev.pchtherm.0.tahv: 83.0C
dev.pchtherm.0.talv: 30.0C
dev.pchtherm.0.pmtime: 32
dev.pchtherm.0.pmtemp: 50.0C
dev.pchtherm.0.%parent: pci0
dev.pchtherm.0.%pnpinfo: vendor=0x8086 device=0x9d31 subvendor=0x17aa subdevice=0x2256 class=0x118000
dev.pchtherm.0.%location: slot=20 function=2 dbsf=pci0:0:20:2
dev.pchtherm.0.%driver: pchtherm
dev.pchtherm.0.%desc: Skylake PCH Thermal Subsystem
dev.pchtherm.%parent:
```

**`dev.pchtherm.%d.temperature`** 传感器读取的当前温度的只读值。

**`dev.pchtherm.%d.ctt`** 当系统达到此温度时将关机。当此功能被禁用并锁定时，此项不会出现。

**`dev.pchtherm.%d.t0temp`** 当温度低于此值时，系统将处于 T0 状态。

**`dev.pchtherm.%d.t1temp`** 当温度高于 `t0temp` 且低于此值时，系统将处于 T1 状态。

**`dev.pchtherm.%d.t2temp`** 当温度高于 `t1temp` 且低于此值时，系统将处于 T2 状态。高于此值时，系统将处于 T3 状态。

**`dev.pchtherm.%d.talv`** 低告警值。当传感器使能位被锁定且值为零（将显示 -50.0C）时，此项不会出现。

**`dev.pchtherm.%d.tahv`** 高告警值。当传感器使能位被锁定且值为零（将显示 -50.0C）时，此项不会出现。

**`dev.pchtherm.%d.pmtemp`** 传感器电源管理温度。低于此温度时，传感器将在 `pmtime` 秒内空闲。

**`dev.pchtherm.%d.pmtime`** 低温时传感器的空闲持续时间。

**`dev.pchtherm.%d.pch_hot_level`** 当温度高于此值时，PCHHOT# 引脚将被置位。当此功能被禁用并锁定时，此值不会出现。

更多详情请查阅 PCH 数据手册。

## 注意事项

所有值均为只读。当前不支持事件中断。

## 参见

[sysctl(8)](../man8/sysctl.8.md)

## 历史

`pchtherm` 驱动首次出现于 FreeBSD 13.0。

## 作者

`pchtherm` 驱动及本手册页由 Takanori Watanabe <takawata@FreeBSD.org> 编写。
