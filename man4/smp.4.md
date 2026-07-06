# smp.4

`SMP` — FreeBSD 对称多处理器内核说明

## 名称

`SMP`

## 概要

`options SMP`

## 描述

`SMP` 内核实现对对称多处理器的支持。

通过将 loader 可调参数 `kern.smp.disabled` 设置为 1 可以禁用 `SMP` 支持。

系统检测到的 CPU 数量可在只读 sysctl 变量 `hw.ncpu` 中获取。

每个 CPU 核心的在线线程数可在只读 sysctl 变量 `kern.smp.threads_per_core` 中获取。系统检测到的物理 CPU 核心数可在只读 sysctl 变量 `kern.smp.cores` 中获取。

FreeBSD 允许禁用多处理器系统上的特定 CPU。这可以通过 `hint.lapic.X.disabled` 可调参数完成，其中 X 是 CPU 的 APIC ID。将此可调参数设置为 1 将导致相应的 CPU 被禁用。

FreeBSD 在 x86 和 powerpc 平台上支持同步多线程。在 x86 上，可以通过将 `machdep.hyperthreading_allowed` 可调参数设置为零来禁用逻辑 CPU。

[sched_ule(4)](sched_ule.4.md) 调度器实现了 CPU 拓扑检测，并调整调度算法以更好地利用现代多核 CPU。sysctl 变量 `kern.sched.topology_spec` 以可解析的 XML 格式反映检测到的 CPU 硬件。顶层 XML 标签是 <groups>，它包含一个或多个 <group> 标签，其中包含关于各个 CPU 组的数据。CPU 组包含被检测为“紧密”在一起的 CPU，通常是因为它们是单个多核处理器中的核心。<group> 标签中可用的属性有“level”，对应 CPU 组的嵌套级别，以及“cache-level”，对应组中 CPU 共享的 CPU 缓存级别。<group> 标签包含 <cpu> 和 <flags> 标签。<cpu> 标签描述组中的 CPU。其属性有“count”，对应组中 CPU 的数量，以及“mask”，对应整数二进制掩码，其中每个设置为 1 的位代表一个属于该组的 CPU。<cpu> 标签的内容（CDATA）是 CPU 索引的逗号分隔列表（派生自“mask”属性）。<flags> 标签包含描述组中 CPU 关系的特殊标签（如果有）。目前可能的标志是“HTT”和“SMT”，对应硬件多线程的各种实现。由两个四核处理器组成的系统的 topology_spec 输出示例如下：

```sh
<groups>
  <group level="1" cache-level="0">
    <cpu count="8" mask="0xff">0, 1, 2, 3, 4, 5, 6, 7</cpu>
    <flags></flags>
    <children>
      <group level="2" cache-level="0">
        <cpu count="4" mask="0xf">0, 1, 2, 3</cpu>
        <flags></flags>
      </group>
      <group level="2" cache-level="0">
        <cpu count="4" mask="0xf0">4, 5, 6, 7</cpu>
        <flags></flags>
      </group>
    </children>
  </group>
</groups>
```

内核在内部使用此信息，将相关任务调度到紧密组合在一起的 CPU 上。

## 兼容性

FreeBSD 的所有 Tier-1 和 Tier-2 架构都支持多处理器系统。目前包括 x86、powerpc、mips、arm 和 arm64。使用 `options SMP` 启用支持。在非 SMP 硬件上使用 SMP 内核配置是允许的。

## I386 注意事项

对于 i386 系统，`SMP` 内核支持遵循 Intel MP 规范版本 1.4 的主板。除了 `options SMP` 外，i386 还需要 `device apic`。可以使用 mptable(1) 命令查看多处理器支持的状态。

## 参见

cpuset(1), mptable(1), [sched_4bsd(4)](sched_4bsd.4.md), [sched_ule(4)](sched_ule.4.md), [loader(8)](../man8/loader.8.md), [sysctl(8)](../man8/sysctl.8.md), [condvar(9)](../man9/condvar.9.md), msleep(9), [mtx_pool(9)](../man9/mtx_pool.9.md), [mutex(9)](../man9/mutex.9.md), [rwlock(9)](../man9/rwlock.9.md), [sema(9)](../man9/sema.9.md), [sx(9)](../man9/sx.9.md)

## 历史

`SMP` 内核的早期历史没有（正式）记录。它在独立的 CVS 分支中开发，直到 1997 年 4 月 26 日，此时它被合并到 3.0-current 中。在此日期之前，3.0-current 已经与 Lite2 内核代码合并。

FreeBSD 5.0 引入了对许多新同步原语的支持，并朝着细粒度内核锁定发展，而不是依赖 Giant 内核锁。SMPng 项目严重依赖 BSDi 的支持，他们提供了来自 BSD/OS 中细粒度 SMP 实现的参考源代码

FreeBSD 5.0 还引入了 sparc64 架构上的 SMP 支持。

## 作者

Steve Passe <fsmp@FreeBSD.org>

## 注意事项

`kern.smp.threads_per_core` 和 `kern.smp.cores` sysctl 变量是尽力而为的猜测。如果某个架构或平台添加了 SMT 而 FreeBSD 尚未实现检测，报告的值可能不准确。在这种情况下，`kern.smp.threads_per_core` 将报告 `1`，`kern.smp.cores` 将报告与 `hw.ncpu` 相同的值。
