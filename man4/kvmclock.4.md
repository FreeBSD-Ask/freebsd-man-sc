# kvmclock.4

`kvmclock` — 用于 x86 KVM 客户机的半虚拟化时钟驱动

## 名称

`kvmclock`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device kvm_clock

## 描述

此驱动从 Linux 主机上 KVM hypervisor 提供的半虚拟化时钟设备读取计时信息。`kvmclock` 驱动仅在 i386 和 amd64 平台上实现。它作为 timecounters(4) 设备运行，并在可用时优先于时间戳计数器（TSC）。驱动通过 `/dev/pvclock` 导出计时信息，使得无需进入内核即可实现 clock_gettime(2) 和相关函数。

`kvmclock` 驱动通过访问 hypervisor 维护的每 vCPU 计时结构来工作。它结合使用 TSC 读取和共享结构中的信息，生成在 vCPU 迁移和实时 VM 迁移等 hypervisor 事件下保持不变的高分辨率时间计数器。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数提供：

**`dev.kvmclock.0.vdso_enable_without_rdtscp`** 默认情况下，仅当（虚拟）CPU 宣布支持“rdtscp”指令时，计时信息才导出到用户空间。将此 sysctl 设置为 1 可覆盖此行为，即使没有“rdtscp”支持也允许导出计时信息。但是，这会破坏与 FreeBSD 14.0 之前发布的 `/lib/libc.so.7` 副本以及嵌入系统 C 库副本的静态链接二进制文件的兼容性。因此，如果系统可能执行早于 FreeBSD 14.0 的二进制文件，则不应更改此 sysctl 值。

**`dev.kvmclock.0.vdso_force_unstable`** 将时间计数器标记为对用户空间消费者不稳定。这主要用于调试驱动和用户空间计时代码，通常不应改动。

## 参见

timecounters(4)

## 历史

`kvmclock` 驱动最早出现于 FreeBSD 13.1。
