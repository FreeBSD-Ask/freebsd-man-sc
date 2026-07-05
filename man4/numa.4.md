# numa.4

`NUMA` — 非一致性内存访问

## 名称

`NUMA`

## 概要

`options MAXMEMDOM options NUMA`

## 描述

非一致性内存访问（Non-Uniform Memory Access）是一种计算机体系结构设计，涉及给定系统中处理器、内存和 IO 设备之间的不均衡成本。

在 `NUMA` 架构中，访问特定内存或 IO 设备的延迟取决于该内存或设备连接到哪个处理器。访问处理器本地的内存比访问连接到其他处理器的内存更快。FreeBSD 实现了 NUMA 感知的内存分配策略。默认情况下，它尝试确保分配在每个域之间均衡。用户可使用 cpuset(1) 覆盖默认的域选择策略。

当在内核配置文件中指定 `NUMA` 选项时启用 `NUMA` 支持。每个平台定义 `MAXMEMDOM` 常量，指定支持的 NUMA 域的最大数量。此常量可在内核配置文件中指定。可在引导时通过将 `vm.numa.disabled` 可调参数设置为 1 来禁用 `NUMA` 支持。此可调参数的其他值目前被忽略。

线程和进程的 `NUMA` 策略通过 cpuset_getdomain(2) 和 cpuset_setdomain(2) 系统调用控制。cpuset(1) 工具可用于以非默认策略启动进程，或更改现有线程或进程的策略。有关 CPU 到域的映射信息，请参见 SMP(4)。

对 IO 设备具有非一致性访问的系统可以用本地 VM 域标识符标记这些设备。驱动可通过调用 bus_get_domain(9) 获取其本地域信息。

### MIB 变量

`NUMA` 的操作通过以下 [sysctl(8)](../man8/sysctl.8.md) MIB 变量控制和暴露信息：

**`vm.ndomains`** 已检测到的 VM 域数量。

**`vm.phys_locality`** 指示每个 VM 域之间相对成本的表。值为 10 表示成本相同。值为 -1 表示本地性映射不可用或没有本地性信息。

**`vm.phys_segs`** 物理内存映射，按 VM 域分组。

## 实现说明

当前 `NUMA` 实现以 VM 为焦点。硬件 `NUMA` 域被映射到从 0 开始的连续非稀疏 VM 域空间。因此，VM 域信息（例如域标识符）不一定与硬件特定信息中的相同。策略信息在 struct thread 和 struct proc 中均可用。

## 参见

cpuset(1), cpuset_getaffinity(2), cpuset_setaffinity(2), SMP(4), bus_get_domain(9)

## 历史

`NUMA` 首次出现于 FreeBSD 9.0，作为首次访问分配策略，故障转移到轮询分配，且不可配置。随后在 FreeBSD 10.0 中修改为实现轮询分配策略，同样不可配置。

numa_getaffinity(2) 和 numa_setaffinity(2) 系统调用以及 numactl(1) 工具首次出现于 FreeBSD 11.0，在 FreeBSD 12.0 中移除。当前实现出现于 FreeBSD 12.0。

## 作者

本手册页由 Adrian Chadd <adrian@FreeBSD.org> 编写。

## 注释

未保留任何统计信息以指示 `NUMA` 分配策略的成功或失败频率。
