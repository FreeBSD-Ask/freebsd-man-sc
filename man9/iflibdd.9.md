# iflibdd.9

`iflibdd` — 设备相关配置函数

## 名称

`iflibdd`

## 概要

```c
#include <ifdi_if.h>
```

### 软队列设置与拆除函数

#### 必需函数

```c
int
ifdi_tx_queues_alloc(if_ctx_t ctx, caddr_t *vaddrs, uint64_t *paddrs,
    int ntxqs, int ntxqsets)

int
ifdi_rx_queues_alloc(if_ctx_t ctx, caddr_t *vaddrs, uint64_t *paddrs,
    int nrxqs, int nrxqsets)

int
ifdi_queues_free(if_ctx_t ctx)
```

#### 可选函数

```c
int
ifdi_txq_setup(if_ctx_t ctx, uint16_t qid)

int
ifdi_rxq_setup(if_ctx_t ctx, uint16_t qid)
```

### 设备设置与拆除函数

#### 必需函数

```c
int
ifdi_attach_pre(if_ctx_t ctx)

int
ifdi_attach_post(if_ctx_t ctx)

int
ifdi_detach(if_ctx_t ctx)
```

#### 可选函数

```c
void
ifdi_vlan_register(if_ctx_t ctx, uint16_t vtag)

void
ifdi_vlan_unregister(if_ctx_t ctx, uint16_t vtag)

int
ifdi_suspend(if_ctx_t ctx)

int
ifdi_resume(if_ctx_t ctx)
```

### 设备配置函数

#### 必需函数

```c
void
ifdi_init(if_ctx_t ctx)

void
ifdi_stop(if_ctx_t ctx)

void
ifdi_multi_set(if_ctx_t ctx)

int
ifdi_mtu_set(if_ctx_t ctx, uint32_t mtu)

void
ifdi_media_status(if_ctx_t ctx, struct ifmediareq *ifr)

int
ifdi_media_change(if_ctx_t ctx)

void
ifdi_promisc_set(if_ctx_t ctx, int flags)

uint64_t
ifdi_get_counter(if_ctx_t ctx, ift_counter cnt)

void
ifdi_update_admin_status(if_ctx_t ctx)
```

#### 可选函数

```c
void
ifdi_media_set(if_ctx_t ctx)
```

### 中断启用/禁用

#### 必需函数

```c
void
ifdi_intr_enable(if_ctx_t ctx)

void
ifdi_queue_intr_enable(if_ctx_t ctx, uint16_t qid)

void
ifdi_intr_disable(if_ctx_t ctx)
```

### IOV 支持

```c
init
iov_init(if_ctx_t ctx, uint16_t num_vfs, const nvlist_t *params)

void
iov_uinit(if_ctx_t ctx)

void
ifdi_vflr_handle(if_ctx_t ctx)

int
ifdi_vf_add(if_ctx_t ctx, uint16_t vfnum, const nvlist_t *params)
```

#### 可选函数

```c
void
ifdi_link_intr_enable(if_ctx_t ctx)
```

### 可选服务例程

```c
void
ifdi_timer(if_ctx_t ctx)

void
ifdi_watchdog_reset(if_ctx_t ctx)
```

### 附加函数

```c
void
ifdi_led_func(if_ctx_t ctx, int onoff)

int
ifdi_sysctl_int_delay(if_ctx_t ctx, if_int_delay_info_t iidi)

int
ifdi_i2c_req(if_ctx_t ctx, struct ifi2creq *req)
```

## 函数

上述命名函数为设备相关配置函数。驱动程序将这些例程注册到 iflib，相应的 iflib 函数会调用它们来配置设备特定的功能和寄存器。

### 设备相关函数

### 软队列设置与拆除

**`ifdi_tx_queues_alloc`** 必需函数，在 iflib_attach 期间调用以分配发送队列。vaddrs 和 paddrs 分别是硬件发送队列的虚拟地址和物理地址数组。ntxqs 是每个 qset 的队列数。ntxqsets 是 qset 的数量。

**`ifdi_rx_queues_alloc`** 必需函数，在 iflib_attach 期间调用以分配接收队列。vaddrs 和 paddrs 分别是硬件接收队列的虚拟地址和物理地址数组。nrxqs 是每个 qset 的队列数。nrxqsets 是 qset 的数量。

**`ifdi_queues_free`** 必需函数，释放已分配的队列和关联的发送缓冲区。

**`ifdi_txq_setup`** 可选函数，用于每个发送队列的设备特定初始化。

**`ifdi_rxq_setup`** 可选函数，用于每个接收队列的设备特定初始化。

### 设备设置与拆除

**`ifdi_attach_pre`** 必需函数，由驱动程序实现，用于执行中断和队列分配、队列设置以及中断分配之前的任何附加逻辑。

**`ifdi_attach_post`** 必需函数，由驱动程序实现，用于执行 ifdi_attach_pre 以及 iflib 的队列设置和 MSI/MSIX(X) 或传统中断分配之后的任何附加逻辑。

**`ifdi_detach`** 必需函数，释放驱动程序在 ifdi_attach_pre 和 ifdi_attach_post 中分配的所有资源。

**`ifdi_vlan_register`** 可选函数，由 VLAN config 事件处理程序调用。`vtag` 是新的 VLAN 标签。

**`ifdi_vlan_unregister`** 可选函数，由 VLAN unconfig 事件处理程序调用。

**`ifdi_suspend`** 可选函数，挂起驱动程序。

**`ifdi_resume`** 可选函数，恢复驱动程序。

### 设备配置函数

**`ifdi_init`** 必需函数，初始化并启动硬件。例如，它会重置芯片并启用接收单元。它应将接口标记为运行，但不活动（`IFF_DRV_RUNNING`，`~IIF_DRV_OACTIVE`）。

**`ifdi_stop`** 必需函数，应通过在 MAC 上发出全局重置并释放 TX 和 RX 缓冲区来禁用接口上的所有流量。

**`ifdi_multi_set`** 设置接口的多播地址。

**`ifdi_media_status`** 媒体 Ioctl 回调。当用户使用 [ifconfig(8)](../man8/ifconfig.8.md) 查询接口状态时调用此函数。驱动程序在 ifmr->ifm_active 中设置适当的链路类型和速度。

**`ifdi_mtu_set`** 将接口的 mtu 设置为第二个函数参数 mtu 的值。

**`ifdi_media_change`** 当用户使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 media/mediaopt 选项更改速度/双工时调用此函数。

**`ifdi_promisc_set`** 根据 flags 值启用或禁用混杂设置。`flags` 包含接口的 [ifnet(9)](ifnet.9.md) 标志。

**`ifdi_get_counter`** 根据计数器类型返回计数器 cnt 的值。

**`ifdi_update_admin_status`** 根据 OS 链路状态将 link_up 状态设置为 TRUE 或 FALSE。仅在链路中断时才对硬件进行实际检查。

**`ifdi_media_set`** 需要定义。

### 中断启用/禁用

**`ifdi_intr_enable`** 必需函数，启用所有中断。

**`ifdi_intr_disable`** 必需函数，禁用所有中断。

**`ifdi_queue_intr_enable`** 必需函数，启用队列 qid 上的中断。

**`iov_init`** 初始化 num_vfs 个 VF。

**`io_uninit`** 拆除所有 VF 的上下文。

**`ifdi_vflr_handle`** 处理任何通过 Function Level Reset (FLR) 自行重置的 VF。

**`ifdi_vf_add`** 在 VF vfnum 中设置 params 中的参数。

### 服务例程

**`ifdi_timer`** 可选定时器例程，每 500ms 运行一次。

**`ifdi_watchdog_reset`** 可选函数，在发送队列挂起时运行。

### 附加函数

**`ifdi_led_func`**

**`ifdi_sysctl_int_delay`**

**`ifdi_i2c_req`**

## 参见

[ifconfig(8)](../man8/ifconfig.8.md), [iflibdi(9)](iflibdi.9.md), [iflibtxrx(9)](iflibtxrx.9.md), [ifnet(9)](ifnet.9.md)

## 作者

本手册页由 Nicole Graziano 编写。
