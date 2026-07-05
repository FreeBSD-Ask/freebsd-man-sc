# atrtc.4

`atrtc` — AT 实时时钟（RTC）驱动

## 名称

`atrtc`

## 概要

此驱动是 i386/amd64 内核的必需部分。

以下可调参数可从 [loader(8)](../man8/loader.8.md) 设置：

**hint.atrtc.X.clock** 控制事件计时器功能支持。设为 0 则禁用。默认值为 1。

**hw.atrtc.enabled** 强制启用或禁用设备。设为 0 禁用，设为 1 启用，绕过任何平台配置提示。默认值为 -1（自动检测）。

## 描述

此驱动使用 RTC 硬件为内核提供 1 秒分辨率的当日时钟和一个事件计时器。此硬件使用 32768Hz 基础频率推进当日时钟并生成周期性中断。中断可由固定数量的频率生成，范围从 2Hz 到 8192Hz，通过将基础频率除以支持的 2 的幂除数之一获得。

该驱动提供的事件计时器与 CPU 电源状态无关。

## 参见

[apic(4)](apic.4.md), [attimer(4)](attimer.4.md), [eventtimers(4)](eventtimers.4.md), [hpet(4)](hpet.4.md)
