# hwt(4)

`hwt` — 硬件跟踪框架

## 名称

`hwt`

## 概要

`options HWT_HOOKS device hwt`

`至少需要以下之一： device intel_pt (amd64) device coresight (arm64) device spe (arm64)`

`在 rc.conf(5) 中： kld_list="hwt"`

## 描述

`hwt` 框架为硬件辅助跟踪提供基础设施。它收集有关软件执行的详细信息，并以高度压缩的格式将其作为事件存储到 DRAM 中。事件涵盖有关程序控制流变化的信息，包括分支是否被采用、异常是否被触发、时序信息、经过的周期数等。收集的信息允许在无明显性能影响的情况下重建给定应用程序的完整程序流。

## 硬件

该框架支持 `arm64` 和 `amd64` 系统上的多种跟踪技术：

- ARM Coresight
- ARM 统计分析扩展（SPE）
- Intel 处理器跟踪（PT）

`hwt` 框架支持两种操作模式：

***CPU** 模式* 在内核模式下采集 CPU 活动。

***Thread** 模式* 在用户模式下采集进程每个线程的活动。

## 管理

加载到内核后，`hwt` 框架提供 `/dev/hwt` 字符设备。它接受的唯一 ioctl(2) 请求是 `HWT_IOC_ALLOC`。此请求根据请求的操作模式、CPU 集合和/或 pid 分配内核跟踪上下文（CTX）。

CTX 分配成功后，ioctl 返回 CTX 标识号（ident）。

然后每个 CTX 通过其自己的专用字符设备进行管理，设备路径为 `/dev/hwt_${ident}_${d}`，其中 ident 是跟踪上下文的唯一标识号，d 是 cpu_id（在 HWT CPU 模式下）或进程 pid（在 HWT Thread 模式下）。

## 钩子

在跟踪目标进程期间，HWT 记录线程创建、exec 和 mmap 系统调用等运行时事件。这些事件作为"记录"记录在与被跟踪进程关联的特定 CTX 中。

此外，如果用户请求，HWT 可以在 exec 或 mmap 系统调用时暂停目标线程。此暂停允许用户空间工具在执行继续之前检索记录并调整跟踪设置。此功能在启用地址范围过滤时特别有用，允许跟踪目标可执行文件或动态库中的特定函数。

## 内核选项

内核配置文件中的以下选项是必需的，与 `hwt` 操作相关：

**`HWT_HOOKS`** 启用内核钩子。

## IOCTL 接口

CTX 分配后，其管理字符设备接受多个 ioctl(2) 请求：

**`HWT_IOC_START`** 开始跟踪。在 HWT CPU 模式下，跟踪实际上由此 ioctl(2) 请求启动。在 Thread 模式下，设置跟踪"运行"标志，但跟踪在调度器将目标线程切换到 CPU 并返回用户模式后才开始。

**`HWT_IOC_STOP`** 停止特定 CTX 的跟踪。

**`HWT_IOC_RECORD_GET`** 将钩子调用期间收集的与此 CTX 关联的全部或部分记录复制到用户空间。

**`HWT_IOC_BUFPTR_GET`** 获取缓冲区中由跟踪单元实时填充的当前指针。

**`HWT_IOC_SET_CONFIG`** 设置架构特定配置（可选）。

**`HWT_IOC_WAKEUP`** 唤醒被 HWT 框架钩子置于睡眠状态的线程。

**`HWT_IOC_SVC_BUF`** 仅适用于 SPE，内核等待用户空间通知其已将缓冲区复制出去，以避免数据丢失/覆盖缓冲区。

## 参见

[tracing(7)](../man7/tracing.7.md), hwt(8)

## 历史

`hwt` 框架最早出现在 FreeBSD 15.0 中。

## 作者

Ruslan Bukin <br@FreeBSD.org> Bojan Novković <bnovkov@freebsd.org> Zachary Leaf <zachary.leaf@arm.com>
