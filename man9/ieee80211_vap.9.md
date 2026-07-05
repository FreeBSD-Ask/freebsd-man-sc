# ieee80211_vap.9

`net80211_vap` — 802.11 网络层虚拟无线电支持

## 名称

`net80211_vap`

## 概要

```c
#include <net80211/ieee80211_var.h>
```

```c
int
ieee80211_vap_setup(struct ieee80211com *,
    struct ieee80211vap *, const char name[IFNAMSIZ],
    int unit, int opmode, int flags,
    const uint8_t bssid[IEEE80211_ADDR_LEN],
    const uint8_t macaddr[IEEE80211_ADDR_LEN])

int
ieee80211_vap_attach(struct ieee80211vap *,
    ifm_change_cb_t media_change, ifm_stat_cb_t media_stat)

void
ieee80211_vap_detach(struct ieee80211vap *)
```

## 描述

`net80211` 软件层为驱动程序提供了一套支持框架，其中包括通过从底层设备克隆的网络接口（即 vap）导出给用户的虚拟无线电 API。这些接口具有一种操作模式（station、adhoc、hostap、wds、monitor 等），在接口的整个生命周期内固定不变。能够支持多个并发接口的设备允许克隆多个 vap。

`net80211` 层定义的虚拟无线电接口意味着驱动程序必须按特定规则进行结构化。任何时候只支持单个接口的驱动程序仍必须遵守这些规则。

虚拟无线电架构将状态划分到一个 per-device 的 `ieee80211com` 结构和一个或多个 `ieee80211vap` 结构之间。vap 通过 `SIOCIFCREATE2` 请求创建。这会导致调用驱动程序的 `ic_vap_create` 方法，驱动程序在此可以决定是否接受该请求。

vap 创建过程分三步完成。首先驱动程序使用 [malloc(9)](malloc.9.md) 分配数据结构。此数据结构的前部必须是 `ieee80211vap` 结构，但通常会扩展以包含驱动程序私有状态。然后通过调用 `ieee80211_vap_setup` 来设置 vap。此请求初始化 `net80211` 状态但不激活接口。驱动程序然后可以覆盖 `net80211` 设置的方法并设置驱动程序资源，最后调用 `ieee80211_vap_attach` 完成整个过程。这两个调用都必须在不持有任何驱动程序锁的情况下进行，因为工作可能需要进程阻塞/睡眠。

当发出 `SIOCIFDESTROY` ioctl 请求或设备分离（导致所有关联的 vap 自动被删除）时，vap 被删除。删除请求会导致调用 `ic_vap_delete` 方法。驱动程序必须在调用 `ieee80211_vap_detach` 以停用 vap 并将其与用户应用程序的请求等活动隔离之前使设备静默。然后驱动程序可以回收 vap 持有的资源并重新启用设备操作。使设备静默的确切过程未规定，但通常涉及阻塞中断和停止发送与接收处理。

## 多 VAP 操作

驱动程序负责决定是否可以创建多个 vap 以及如何管理它们。是否可以支持多个并发 vap 取决于设备的能力。例如，通常可以支持多个 hostap vap，但许多设备不支持为每个 vap 分配唯一的 BSSID。如果设备支持 hostap 操作，通常可以支持并发的 station 模式 vap，但可能会有一些限制，例如失去对硬件 beacon miss 支持的能力。能够进行 hostap 操作并且可以发送和接收 4 地址帧的设备应该能够支持 WDS vap 与 ap vap 一起工作。但相反，一些设备在没有至少一个 ap vap 的情况下无法支持 WDS vap（不过可以通过强制 ap vap 不发送 beacon 帧来巧妙处理）。所有设备都应支持与其他 vap 并发创建任意数量的 monitor 模式 vap，但允许此操作是驱动程序的责任。

支持多个并发 vap 的一个重要后果是，驱动程序的 `iv_newstate` 方法必须编写为能够处理对每个 vap 的调用。在必要的地方，驱动程序必须跟踪所有 vap 的私有状态，而不仅仅是状态正在被更改的那个 vap（例如，对于处理 beacon 定时器，驱动程序可能需要知道所有发送 beacon 的 vap 是否都已停止，然后才能停止硬件定时器）。

## 参见

[ieee80211(9)](ieee80211.9.md), [ifnet(9)](ifnet.9.md), [malloc(9)](malloc.9.md)
