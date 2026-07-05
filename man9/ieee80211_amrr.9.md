# ieee80211_amrr.9

`ieee80211_amrr` — 802.11 网络驱动程序发送速率控制支持

## 名称

`ieee80211_amrr`

## 概要

```c
#include <net80211/ieee80211_amrr.h>
```

```c
void
ieee80211_amrr_init(struct ieee80211_amrr *, struct ieee80211vap *,
    int amin, int amax, int interval)
void
ieee80211_amrr_cleanup(struct ieee80211_amrr *)
void
ieee80211_amrr_setinterval(struct ieee80211_amrr *, int interval)
void
ieee80211_amrr_node_init(struct ieee80211_amrr *,
    struct ieee80211_amrr_node *, struct ieee80211_node *)
int
ieee80211_amrr_choose(struct ieee80211_node *, struct ieee80211_amrr_node *)
void
ieee80211_amrr_tx_complete(struct ieee80211_amrr_node *, int ok, int retries)
void
ieee80211_amrr_tx_update(struct ieee80211_amrr_node *, int txnct, int success,
    int retrycnt)
```

## 描述

`ieee80211_amrr` 是 AMRR 发送速率控制算法的实现，用于使用 `net80211` 软件层的驱动程序。速率控制算法负责为每个帧选择发送速率。为最大化吞吐量，算法尝试使用适合操作条件的最高速率。速率会随条件变化而变化；两个站点之间的距离可能改变，可能存在影响信号质量的瞬时噪声等。`net80211` 使用来自驱动程序的非常简单的信息来完成其工作：帧是否成功交付以及进行了多少次发送尝试。虽然这使其几乎可用于任何无线设备，但也限制了其有效性——不要期望它在困难环境中表现良好和/或快速响应变化条件。

`net80211` 需要为其选择速率的每个 vap 状态和每个站点状态。API 设计用于驱动程序在每个 vap 和节点的驱动程序私有扩展区域中预分配状态。例如 [ral(4)](../man4/ral.4.md) 驱动程序将 vap 定义为：

```c
struct rt2560_vap {
        struct ieee80211vap     ral_vap;
        struct ieee80211_beacon_offsets ral_bo;
        struct ieee80211_amrr   amrr;
        int      (*ral_newstate)(struct ieee80211vap *,
                      enum ieee80211_state, int);
};
```

`amrr` 结构成员保存 `net80211` 的每 vap 状态，[ral(4)](../man4/ral.4.md) 在 vap create 方法中使用以下代码初始化它：

```c
ieee80211_amrr_init(&rvp->amrr, vap,
    IEEE80211_AMRR_MIN_SUCCESS_THRESHOLD,
    IEEE80211_AMRR_MAX_SUCCESS_THRESHOLD,
    500 /* ms */);
```

节点定义为：

```c
struct rt2560_node {
        struct ieee80211_node   ni;
        struct ieee80211_amrr_node amrr;
};
```

在驱动程序的 `iv_newassoc` 方法中完成初始化：

```c
static void
rt2560_newassoc(struct ieee80211_node *ni, int isnew)
{
        struct ieee80211vap *vap = ni->ni_vap;
        ieee80211_amrr_node_init(&RT2560_VAP(vap)->amrr,
            &RT2560_NODE(ni)->amrr, ni);
}
```

一旦设置了 `net80211` 状态，在发送路径中调用 `ieee80211_amrr_choose` 请求发送速率；例如：

```c
tp = &vap->iv_txparms[ieee80211_chan2mode(ni->ni_chan)];
if (IEEE80211_IS_MULTICAST(wh->i_addr1)) {
	rate = tp->mcastrate;
} else if (m0->m_flags & M_EAPOL) {
	rate = tp->mgmtrate;
} else if (tp->ucastrate != IEEE80211_FIXED_RATE_NONE) {
	rate = tp->ucastrate;
} else {
	(void) ieee80211_amrr_choose(ni, &RT2560_NODE(ni)->amrr);
	rate = ni->ni_txrate;
}
```

注意仅当未配置固定发送速率时才为单播数据帧选择速率；其他情况由 `net80211` 发送参数处理。还应注意 `ieee80211_amrr_choose` 将所选速率写入 `ni_txrate`；这消除了复制值的需要，因为它导出给用户应用程序以便它们在状态中显示当前发送速率。

驱动程序必须完成的剩余工作是在帧发送完成时使用 `ieee80211_amrr_tx_complete` 向 `net80211` 反馈状态。轮询设备以检索统计信息的驱动程序可使用 `ieee80211_amrr_tx_update`（替代或附加）。

## 参见

[ieee80211(9)](ieee80211.9.md), [ieee80211_output(9)](ieee80211_output.9.md)
