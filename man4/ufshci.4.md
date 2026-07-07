# ufshci(4)

`ufshci` — 通用闪存存储主机控制器接口驱动

## 名称

`ufshci`

## 概要

要将此驱动编译进内核，请将以下行加入内核配置文件：

> device ufshci

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
ufshci_load="YES"
```

## 描述

通用闪存存储（UFS）是一种低功耗、高性能的存储标准，由一个主机控制器和单个目标设备组成。

该驱动目前提供：

- 主机控制器和目标设备的初始化
- UFS 互连（UIC）命令的处理
- 对 UTP 传输请求（UTR）和 UTP 任务管理请求（UTMR）的支持
- 对 SCSI 命令集的支持
- 以传统单门铃队列模式运行
- 对 PCI Express 总线的支持

初始化完成后，控制器会注册到 cam(4) 子系统，其逻辑单元显示为设备节点 **`/dev/daX`**。

该驱动正在积极开发中；后续工作包括完整的 UFS 4.1 特性覆盖、更多电源管理模式，以及基于 ACPI/FDT 的附加支持。

## 硬件

`ufshci` 驱动支持实现通用闪存存储主机控制器接口 4.1 及更早版本的主机控制器和设备。

## 配置

`ufshci` 驱动目前以单门铃（单个 I/O 队列）方式运行，因此任何更改队列数的可调参数都会被忽略。当加入多循环队列（MCQ）支持并使多个队列可用时，以下队列数可调参数值将生效。

若要强制所有 CPU 共享单个 I/O 队列对，请在 loader.conf(5) 中设置以下可调参数：

```sh
hw.ufshci.per_cpu_io_queues=0
```

若要为每个 I/O 队列对分配多个 CPU，从而减少设备消耗的 MSI-X 向量数，请在 loader.conf(5) 中设置以下可调参数：

```sh
hw.ufshci.min_cpus_per_ioq=X
```

若要更改 I/O 命令超时值（单位为秒），请在 loader.conf(5) 中设置以下可调参数：

```sh
hw.ufshci.timeout_period=X
```

若要更改 I/O 命令重试次数，请在 loader.conf(5) 中设置以下可调参数：

```sh
hw.ufshci.retry_count=X
```

若要强制驱动使用传统 INTx 中断，请在 loader.conf(5) 中设置以下可调参数：br（注意：在 MCQ 支持可用之前，驱动始终使用传统 INTx，因此此值实际上保持为 1）

```sh
hw.ufshci.force_intx=1
```

## SYSCTL 变量

以下控制器级 [sysctl(8)](../man8/sysctl.8.md) 节点目前已实现：

**`dev.ufshci.0.num_failures`** (R) 整个控制器的命令失败次数。

**`dev.ufshci.0.num_retries`** (R) 整个控制器的命令重试次数。

**`dev.ufshci.0.num_intr_handler_calls`** (R) 中断处理程序被调用的次数。

**`dev.ufshci.0.num_cmds`** (R) 控制器发出的命令总数。

**`dev.ufshci.0.timeout_period`** (RW) 配置的超时周期（单位为秒）。

**`dev.ufshci.0.cap`** (R) 主机控制器能力寄存器值。

**`dev.ufshci.0.num_io_queues`** (R) I/O 队列对数。

**`dev.ufshci.0.io_queue_mode`** (R) 指示单门铃模式或多循环队列模式。

**`dev.ufshci.0.minor_version`** (R) 主机控制器次版本号。

**`dev.ufshci.0.major_version`** (R) 主机控制器主版本号。

**`dev.ufshci.0.wb_enabled`** (R) WriteBooster 启用/禁用。

**`dev.ufshci.0.wb_flush_enabled`** (R) WriteBooster 刷新启用/禁用。

**`dev.ufshci.0.wb_buffer_type`** (R) WriteBooster 类型。

**`dev.ufshci.0.wb_buffer_size_mb`** (R) WriteBooster 缓冲区大小（单位为 MB）。

**`dev.ufshci.0.wb_user_space_config_option`** (R) WriteBooster 保留用户空间模式。

**`dev.ufshci.0.auto_hibernation_supported`** (R) 设备自动休眠支持。

**`dev.ufshci.0.auto_hibernate_idle_timer_value`** (R) 自动休眠空闲计时器值（单位为微秒）。

**`dev.ufshci.0.power_mode_supported`** (R) 设备电源模式支持。

**`dev.ufshci.0.power_mode`** (R) 当前设备电源模式。

**`dev.ufshci.0.tx_rx_power_mode`** (R) 当前 TX/RX PA_PWRMode 值。

**`dev.ufshci.0.max_tx_lanes`** (R) 最大可用 TX 数据通道数。

**`dev.ufshci.0.max_rx_lanes`** (R) 最大可用 RX 数据通道数。

**`dev.ufshci.0.tx_lanes`** (R) 活动 TX 数据通道数。

**`dev.ufshci.0.rx_lanes`** (R) 活动 RX 数据通道数。

**`dev.ufshci.0.max_rx_hs_gear`** (R) 最大可用 RX HS 齿轮。

**`dev.ufshci.0.hs_gear`** (R) 活动 HS 齿轮。

**`dev.ufshci.0.utmrq.num_failures`** (R) 失败的 UTP 任务管理请求数。

**`dev.ufshci.0.utmrq.num_retries`** (R) 重试的 UTP 任务管理请求数。

**`dev.ufshci.0.utmrq.num_intr_handler_calls`** (R) 由 UTP 任务管理请求导致的中断处理程序调用次数。

**`dev.ufshci.0.utmrq.num_cmds`** (R) 发出的 UTP 任务管理请求数。

**`dev.ufshci.0.utmrq.cq_head`** (R) UTP 任务管理完成队列头的当前位置。

**`dev.ufshci.0.utmrq.sq_tail`** (R) UTP 任务管理提交队列尾的当前位置。

**`dev.ufshci.0.utmrq.sq_head`** (R) UTP 任务管理提交队列头的当前位置。

**`dev.ufshci.0.utmrq.num_trackers`** (R) UTP 任务管理队列中的追踪器数。

**`dev.ufshci.0.utmrq.num_entries`** (R) UTP 任务管理队列中的条目数。

**`dev.ufshci.0.ioq.0.num_failures`** (R) 失败的 UTP 传输请求数。

**`dev.ufshci.0.ioq.0.num_retries`** (R) 重试的 UTP 传输请求数。

**`dev.ufshci.0.ioq.0.num_intr_handler_calls`** (R) 由 UTP 传输请求导致的中断处理程序调用次数。

**`dev.ufshci.0.ioq.0.num_cmds`** (R) 发出的 UTP 传输请求数。

**`dev.ufshci.0.ioq.0.cq_head`** (R) UTP 传输完成队列头的当前位置。

**`dev.ufshci.0.ioq.0.sq_tail`** (R) UTP 传输提交队列尾的当前位置。

**`dev.ufshci.0.ioq.0.sq_head`** (R) UTP 传输提交队列头的当前位置。

**`dev.ufshci.0.ioq.0.num_trackers`** (R) UTP 传输队列中的追踪器数。

**`dev.ufshci.0.ioq.0.num_entries`** (R) UTP 传输队列中的条目数。

## 参见

cam(4), [pci(4)](pci.4.md), [disk(9)](../man9/disk.9.md)

## 历史

`ufshci` 驱动首次出现于 FreeBSD 15.0。

## 作者

`ufshci` 驱动由三星电子开发，最初由 Jaeyoon Choi <j_yoon.choi@samsung.com> 编写。

本手册页由 Jaeyoon Choi <j_yoon.choi@samsung.com> 编写。
