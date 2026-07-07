# ieee80211_beacon(9)

`ieee80211_beacon` — 802.11 信标支持

## 名称

`ieee80211_beacon`

## 概要

```c
#include <net80211/ieee80211_var.h>
```

```c
struct mbuf *
ieee80211_beacon_alloc(struct ieee80211_node *,
    struct ieee80211_beacon_offsets *)

int
ieee80211_beacon_update(struct ieee80211_node *,
    struct ieee80211_beacon_offsets *, struct mbuf *, int mcast)

void
ieee80211_beacon_notify(struct ieee80211vap *, int what)
```

## 描述

`net80211` 软件层为驱动程序提供了支持框架，包括基于模板的机制，用于在 hostap、adhoc 和 mesh 操作模式下动态更新传输的信标帧。驱动程序应使用 `ieee80211_beacon_alloc` 创建初始信标帧。`ieee80211_beacon_offsets` 结构保存有关信标内容的信息，用于优化通过 `ieee80211_beacon_update` 完成的更新。

只有在影响信标帧内容的变化发生时才应进行更新调用。当这种情况发生时，会调用 `iv_update_beacon` 方法，驱动程序提供的例程必须正确处理。对于需要主机传输每个信标帧的设备，此工作可能只是标记 `ieee80211_beacon_offsets` 结构中的一位：

```c
static void
ath_beacon_update(struct ieee80211vap *vap, int item)
{
        struct ieee80211_beacon_offsets *bo = &ATH_VAP(vap)->av_boff;
	setbit(bo->bo_flags, item);
}
```

然后在发送下一个信标之前完成 `ieee80211_beacon_update` 调用。

卸载信标生成的设备可以选择使用此回调立即将更新推送到设备。具体如何实现未指定。一种可能性是更新信标帧内容并提取适当的信息元素，但其他方案也是可能的。

## 多 VAP 信标调度

支持多个可各自发送信标的 vap 的驱动程序需要考虑如何调度信标帧。目前有两种可能性：在 TBTT 处*突发*所有信标，或在信标间隔内*错开信标*。突发信标帧可能导致非周期性传递，影响关联站的省电操作。应用一些抖动（例如通过随机排序突发帧）可能足以解决此问题，通常这不是问题，除非站使用积极的省电技术如 U-APSD（有时由 VoIP 电话采用）。错开帧需要更多中断和可能不可用的设备支持。错开信标帧通常优于突发帧，最多约八个 vap，超过此数量开销变得显著，信道也明显变得繁忙。

## 参见

[ieee80211(9)](ieee80211.9.md)
