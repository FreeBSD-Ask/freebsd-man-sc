# bhnd_pmu.4

`bhnd_pmu` — Broadcom 家庭网络部门 PMU 驱动

## 名称

`bhnd_pmu`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device bhnd

要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
bhnd_load="YES"
```

## 描述

`bhnd_pmu` 驱动支持 Broadcom 家庭网络部门网络芯片组和嵌入式系统中使用的电源管理单元（PMU）。

PMU 提供管理设备时钟和电源拓扑的硬件接口。

## 参见

[bhnd(4)](bhnd.4.md), [intro(4)](intro.4.md)

## 历史

`bhnd_pmu` 设备驱动首次出现于 FreeBSD 12.0。

## 作者

`bhnd_pmu` 驱动派生自 Broadcom 的 ISC 许可 Linux PMU 驱动，由 Landon Fuller <landonf@FreeBSD.org> 移植到 FreeBSD 和 [bhnd(4)](bhnd.4.md)。
