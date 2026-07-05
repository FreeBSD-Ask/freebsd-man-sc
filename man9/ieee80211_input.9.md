# ieee80211_input.9

`ieee80211_input` — 软件 802.11 栈输入函数

## 名称

`ieee80211_input`

## 概要

```c
#include <net80211/ieee80211_var.h>
```

```c
void
ieee80211_input(struct ieee80211_node *, struct mbuf *, int rssi, int noise)

void
ieee80211_input_all(struct ieee80211com *, struct mbuf *, int rssi, int noise)
```

## 描述

支持 802.11 设备驱动程序的 `net80211` 层要求接收处理是单线程的。通常使用专用的驱动程序 [taskqueue(9)](taskqueue.9.md) 线程完成。`ieee80211_input` 和 `ieee80211_input_all` 处理接收到的 802.11 帧，设计用于该上下文；例如，不得持有任何驱动程序锁。

在 `mbuf` 中传递上来的帧必须在前部具有 802.11 协议头；所有设备特定信息和/或 PLCP 必须移除。任何 CRC 必须从帧末尾剥离。802.11 协议头应 32 位对齐以获得最佳性能，但接收处理不要求如此。如果帧持有有效载荷且未对齐到 32 位边界，则有效载荷将被重新对齐，使其适合 [ip(4)](../man4/ip.4.md) 等协议处理。

如果设备（如 [ath(4)](../man4/ath.4.md)）在 802.11 头之后插入填充以将有效载荷对齐到 32 位边界，则必须设置 `IEEE80211_C_DATAPAD` 能力。否则，头和有效载荷在 mbuf 链中被视为连续的。

如果接收到的帧必须通过 A-MPDU 接收重排序缓冲区，则 mbuf 必须标记 `M_AMPDU` 标志。注意，目前要求来自 Block ACK 流处于活动状态的站和 TID 的所有帧都如此，而不仅仅是 A-MPDU 聚合。检查站节点表条目的 `ni_flags` 中的 `IEEE80211_NODE_HT` 即可，任何不需要重排序处理的帧将以最小开销调度。

`rssi` 参数是以 0.5dBm 为单位相对于噪声底测量的帧接收信号强度指示。`noise` 参数是接收帧时噪声底的最佳近似值（以 dBm 为单位）。RSSI 和噪声由 `net80211` 层用于在站模式下做出扫描和漫游决策，以及在 hostap 和类似模式下进行自动信道选择。否则，这些值对用户应用程序可用（rssi 表示为最近十个值的过滤平均值，噪声底为最后报告的值）。

## 参见

[ieee80211(9)](ieee80211.9.md)
