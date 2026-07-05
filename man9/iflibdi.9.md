# iflibdi.9

`iflibdi` — 设备无关配置函数

## 名称

`iflibdi`

## 概要

```c
#include <ifdi_if.h>
```

### 设备无关函数

```c
int
iflib_device_attach(device_t dev)

int
iflib_device_detach(device_t dev)

int
iflib_device_suspend(device_t dev)

int
iflib_device_resume(device_t dev)

int
iflib_device_register(device_t dev, void *softc,
    if_shared_ctx_t sctx, if_ctx_t *ctxp)

int
iflib_device_deregister(if_ctx_t ctx)

int
iflib_irq_alloc(if_ctx_t ctx, if_irq_t irq_info, int rid,
    driver_filter_t filter, void *filter_arg,
    driver_intr_t handler, void *arg, char *name)

int
iflib_irq_alloc_generic(if_ctx_t ctx, if_irq_t irq, int rid,
    intr_type_t type, driver_filter_t *filter, void *filter_arg,
    int qid, char *name)

void
iflib_led_create(if_ctx_t ctx)

void
iflib_tx_intr_deferred(if_ctx_t ctx, int txqid)

void
iflib_rx_intr_deferred(if_ctx_t ctx, int rxqid)

void
iflib_link_intr_deferred(if_ctx_t ctx)

void
iflib_link_state_change(if_ctx_t ctx, int linkstate)

void
iflib_add_int_delay_sysctl(if_ctx_t ctx, const char *,
    const char *, if_int_delay_info_t, int, int)
```

### 全局变量

```c
extern struct if_txrx
```

## 数据结构

if_ctx_t 结构是设备无关数据结构，包含用于发送和接收数据包的统计信息和标识信息。该接口与按顺序分配的队列数组相关联。每个队列都有其自己的发送（iflib_txq_t）和接收（iflib_rxq_t）队列。发送队列用于在接口发送另一个数据包时保存数据包。接收队列用于接收等待处理的数据包。

### if_ctx_t 结构

`struct if_ctx_t` 的字段如下：

**`if_softc`** (`void`) 指向驱动程序私有状态块的指针。

**`ifc_dev`** (`device_t`) 底层设备结构。

**`ifc_ip`** (`if_t`) 指回接口结构的链接。

**`ifc_cpus`** (`cpuset_t`)

**`ifc_mutex`** (`struct mtx`) 用于维护数据完整性的互斥锁。

**`ifc_mtx_name`** (`char *`) 互斥锁的名称。

**`ifc_txqs`** (`iflib_txq_t`) 由 iflib 内部维护的设备无关发送队列。

**`ifc_rxqs`** (`iflib_rxq_t`) 由 iflib 内部维护的设备无关接收队列。

**`ifc_qsets`** (`iflib_qset_t`) 包含单个发送（ifc_txq_t）和接收（ifc_rxq_t）队列的输出队列。

**`ifc_if_flags`** (`uint32_t`) 描述接口操作参数的标志。

**`ifc_in_detach`** (`int`)

**`ifc_link_state`** (`int`) 描述以太网接口的当前链路状态。其可能值为活动或非活动。

**`ifc_link_irq`** (`int`)

**`ifc_vlan_attach_event`** (`eventhandler_tag`)

**`ifc_vlan_detach_event`** (`eventhandler_tag`)

**`ifc_pause_frames`** (`int`)

**`ifc_watchdog_events`** (`int`)

**`ifc_mac`** (`uint8_t`)

**`ifc_msix_mem`** (`struct resource *`)

**`ifc_legacy_irq`** (`struct if_irq`)

**`ifc_admin_task`** (`struct grouptask`) 为接口链路状态变更事件调度的 taskqueue 任务。

**`ifc_filter_info`** (`struct iflib_filter_info`) 与接口设备过滤器相关的统计信息和信息。

**`ifc_media`** (`struct ifmedia`)

**`ifc_txrx`** (`struct if_txrx`)

## 函数

上述命名函数仅存在于 iflib 中。它们独立于底层硬件类型或配置。

### 设备无关函数

**`iflib_device_attach`** 此函数启动向 iflib 框架的设备注册。它调用 iflib_register 函数，该函数负责分配和初始化 if_ctx_t 结构。

**`iflib_device_detach`** 关闭并分离设备。注销 vlan 事件，排空所有依赖任务，并释放 irq、pci 和 msix 内存。

**`iflib_device_suspend`** 通过调用设备相关的挂起函数和 bus_generic_suspend 来挂起设备。

**`iflib_device_resume`** 通过调用设备相关的恢复函数、iflib_init_locked 函数和 bus_generic_resume 来恢复设备。

**`iflib_device_register`** 向 iflib 框架注册设备。分配并初始化 if_ctx_t 结构。如有必要，设置并初始化 MSI 或 MSI/X 中断队列。为队列和 qset 结构设置分配内存。

**`iflib_irq_alloc`** 为给定的 rid 值分配具有关联过滤器和处理函数的中断资源。

**`iflib_irq_alloc_generic`** 执行与 iflib_device_irq_alloc 相同的功能，并附加添加 taskgroup 的功能。数据字段和回调函数由中断类型决定，如 `IFLIB_INTR_TX`、`IFLIB_INTR_RX` 和 `IFLIB_INTR_ADMIN`。

**`iflib_led_create`** 调用 led_create 来初始化 ctx->ifc_led_dev 字段。

**`iflib_tx_intr_deferred`** 调用 GROUPTASK_ENQUEUE 将传输队列 ift_task 入队。

**`iflib_rx_intr_deferred`** 调用 GROUPTASK_ENQUEUE 将接收队列 ifr_task 入队。

**`iflib_link_intr_deferred`** 调用 GROUPTASK_ENQUEUE 将链路任务入队。

**`iflib_link_state_change`** 将接口链路状态更改为由函数的第二个参数指定的 `LINK_STATE_UP` 或 `LINK_STATE_DOWN`。*接口链路状态* 当前定义了以下链路状态：

**`LINK_STATE_UP`** 链路已建立。

**`LINK_STATE_DOWN`** 链路已断开。

**`iflib_add_int_delay_sysctl`** 修改给定变量集的设置为用户定义的值。

## 参见

[iflibdd(9)](iflibdd.9.md), [iflibtxrx(9)](iflibtxrx.9.md)

## 作者

本手册页由 Nicole Graziano 编写。
