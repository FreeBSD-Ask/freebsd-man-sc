# hptiop(4)

`hptiop` — HighPoint RocketRAID 3xxx/4xxx 设备驱动

## 名称

`hptiop`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device hptiop
> device scbus
> device da

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
hptiop_load="YES"
```

## 描述

`hptiop` 驱动为 HighPoint RocketRAID 3xxx/4xxx 系列的 SAS 和 SATA RAID 控制器提供支持。

## 硬件

`hptiop` 驱动支持以下 SAS 和 SATA RAID 控制器：

- HighPoint RocketRAID 4522
- HighPoint RocketRAID 4521
- HighPoint RocketRAID 4520
- HighPoint RocketRAID 4322
- HighPoint RocketRAID 4321
- HighPoint RocketRAID 4320
- HighPoint RocketRAID 4311
- HighPoint RocketRAID 4310
- HighPoint RocketRAID 3640
- HighPoint RocketRAID 3622
- HighPoint RocketRAID 3620

`hptiop` 驱动还支持以下已停产的 SAS 和 SATA RAID 控制器：

- HighPoint RocketRAID 4211
- HighPoint RocketRAID 4210
- HighPoint RocketRAID 3560
- HighPoint RocketRAID 3540
- HighPoint RocketRAID 3530
- HighPoint RocketRAID 3522
- HighPoint RocketRAID 3521
- HighPoint RocketRAID 3520
- HighPoint RocketRAID 3511
- HighPoint RocketRAID 3510
- HighPoint RocketRAID 3410
- HighPoint RocketRAID 3320
- HighPoint RocketRAID 3220
- HighPoint RocketRAID 3122
- HighPoint RocketRAID 3120
- HighPoint RocketRAID 3020

## 注释

`hptiop` 驱动仅在 i386 和 amd64 平台上经过测试。

## 参见

cam(4), [hptmv(4)](hptmv.4.md)

## 历史

`hptiop` 设备驱动最早出现在 FreeBSD 7.0 中。

## 作者

`hptiop` 驱动由 HighPoint Technologies, Inc. 编写。
