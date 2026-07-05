# ieee80211_node.9

`ieee80211_node` — 软件 802.11 栈节点管理函数

## 名称

`ieee80211_node`

## 概要

```c
#include <net80211/ieee80211_var.h>
```

```c
struct ieee80211_node *
ieee80211_find_rxnode(struct ieee80211com *,
    const struct ieee80211_frame_min *)

struct ieee80211_node *
ieee80211_find_rxnode_withkey(struct ieee80211com *,
    const struct ieee80211_frame_min *, ieee80211_keyix)

struct ieee80211_node *
ieee80211_ref_node(struct ieee80211_node *)

void
ieee80211_free_node(struct ieee80211_node *)

void
ieee80211_iterate_nodes(struct ieee80211_node_table *,
    ieee80211_iter_func *f, void *arg)

void
ieee80211_dump_nodes(struct ieee80211_node_table *)

void
ieee80211_dump_node(struct ieee80211_node *)
```

## 描述

支持 802.11 设备驱动程序的 `net80211` 层维护一个称为"节点表"的对等站数据库，位于 `ieee80211com` 结构的 `ic_sta` 条目中。站模式 vap 为站关联的接入点创建条目。AP 模式 vap 为关联站创建条目。Adhoc 和 mesh 模式 vap 为邻居站创建条目。WDS 模式 vap 为对等站创建条目。所有 vap 的站驻留在同一表中；每个节点条目有一个 `ni_vap` 字段标识创建它的 vap。在某些情况下，一个条目被多个 vap 使用（例如对于动态 WDS，关联到 ap vap 的站也可能是 WDS vap 的对等方）。

节点表条目采用引用计数。也就是说，有一个所有长期引用的计数，决定何时可以回收条目。每个发送到站的在途帧都持有引用，以确保在帧排队或被驱动程序持有时条目不会被回收。查找表条目的例程返回"持有的引用"（即指向引用计数已递增的表条目的指针）。`ieee80211_ref_node` 调用显式递增节点的引用计数。`ieee80211_free_node` 递减节点的引用计数，如果计数归零则回收表条目。

站表及其条目通过多种方式暴露给驱动程序。每个传输到站的帧在 `m_pkthdr.rcvif` 字段中包含对关联节点的引用。驱动程序在传输处理完成时必须回收此引用。对于每个接收到的帧，驱动程序必须查找表条目以用于"向上栈"调度帧。此查找隐式获取对表条目的引用，驱动程序必须在帧处理完成时回收引用。否则，驱动程序在处理状态机变化时经常检查 `iv_bss` 节点内容，因为数据结构中维护了重要信息。

节点表对驱动程序是不透明的。可以使用预定义 API 之一查找条目，或使用 `ieee80211_iterate_nodes` 调用遍历所有条目以进行每节点处理或实现某些非标准搜索机制。注意，`ieee80211_iterate_nodes` 按设备单线程处理，所涉及的工作处理相当可观，因此应谨慎使用。

提供了两个例程用于将节点内容打印到控制台以进行调试：`ieee80211_dump_node` 显示单个节点的内容，`ieee80211_dump_nodes` 显示指定节点表的内容。也可以使用 [ddb(4)](../man4/ddb.4.md) 的"show node"指令显示节点，站节点表可以用"show statab"显示。

## 驱动程序私有状态

节点数据结构可以由驱动程序扩展以包含驱动程序私有状态。这通过覆盖用于分配节点表条目的 `ic_node_alloc` 方法完成。驱动程序方法必须分配一个作为 `ieee80211_node` 结构扩展的结构。例如 [iwi(4)](../man4/iwi.4.md) 驱动程序定义私有节点结构为：

```c
struct iwi_node {
        struct ieee80211_node   in_node;
	int                     in_station;
};
```

然后提供一个执行此操作的私有分配例程：

```c
static struct ieee80211_node *
iwi_node_alloc(struct ieee80211vap *vap,
    const uint8_t mac[IEEE80211_ADDR_LEN])
{
        struct iwi_node *in;
        in = malloc(sizeof(struct iwi_node), M_80211_NODE,
		M_NOWAIT | M_ZERO);
        if (in == NULL)
                return NULL;
        in->in_station = -1;
        return &in->in_node;
}
```

注意，回收驱动程序分配的节点时，必须调用"父方法"以确保 `net80211` 状态被回收；例如：

```c
static void
iwi_node_free(struct ieee80211_node *ni)
{
        struct ieee80211com *ic = ni->ni_ic;
        struct iwi_softc *sc = ic->ic_ifp->if_softc;
        struct iwi_node *in = (struct iwi_node *)ni;
        if (in->in_station != -1)
                free_unr(sc->sc_unr, in->in_station);
        sc->sc_node_free(ni);	/* 调用 net80211 释放处理程序 */
}
```

注意必须小心避免持有可能导致节点无法回收的引用。`net80211` 会在其数据结构中最后一个引用被回收时回收节点。但如果驱动程序持有额外引用，`net80211` 将无法识别这一点，表条目将不会被回收。如果驱动程序覆盖了 `ic_node_cleanup` 和/或 `ic_node_free` 方法，则不需要此类引用。

## 密钥表支持

节点表查找通常使用站 MAC 地址的哈希完成。接收帧时，这足以找到发送方的节点表条目。但某些设备还在随每个帧接收的设备状态中标识发送站，此数据可用于使用称为"keytab"的配套表优化接收查找。此表记录一个单独的节点表引用，可以使用表索引在无任何锁定的情况下获取。此逻辑通过 `ieee80211_find_rxnode_withkey` 调用处理：如果使用指定索引找到 keytab 条目，则直接返回；否则进行正常查找，并使用指定索引写入 keytab 条目。如果指定索引为 `IEEE80211_KEYIX_NONE`，则进行正常查找而不更新表。

## 参见

[ddb(4)](../man4/ddb.4.md), [ieee80211(9)](ieee80211.9.md), [ieee80211_proto(9)](ieee80211_proto.9.md)
