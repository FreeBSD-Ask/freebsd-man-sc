# altq(9)

`ALTQ` — 操作网络接口输出队列的内核接口

## 名称

`ALTQ`

## 概要

```c
#include <sys/types.h>
#include <sys/socket.h>
#include <net/if.h>
#include <net/if_var.h>
```

### 入队宏

```c
IFQ_ENQUEUE(struct ifaltq *ifq, struct mbuf *m, int error)
IFQ_HANDOFF(struct ifnet *ifp, struct mbuf *m, int error)
IFQ_HANDOFF_ADJ(struct ifnet *ifp, struct mbuf *m, int adjust, int error)
```

### 出队宏

```c
IFQ_DEQUEUE(struct ifaltq *ifq, struct mbuf *m)
IFQ_POLL_NOLOCK(struct ifaltq *ifq, struct mbuf *m)
IFQ_PURGE(struct ifaltq *ifq)
IFQ_IS_EMPTY(struct ifaltq *ifq)
```

### 驱动管理的出队宏

```c
IFQ_DRV_DEQUEUE(struct ifaltq *ifq, struct mbuf *m)
IFQ_DRV_PREPEND(struct ifaltq *ifq, struct mbuf *m)
IFQ_DRV_PURGE(struct ifaltq *ifq)
IFQ_DRV_IS_EMPTY(struct ifaltq *ifq)
```

### 通用设置宏

```c
IFQ_SET_MAXLEN(struct ifaltq *ifq, int len)
IFQ_INC_LEN(struct ifaltq *ifq)
IFQ_DEC_LEN(struct ifaltq *ifq)
IFQ_INC_DROPS(struct ifaltq *ifq)
IFQ_SET_READY(struct ifaltq *ifq)
```

## 描述

`ALTQ` 系统是管理网络接口排队规则的框架。`ALTQ` 引入新的宏来操作输出队列。输出队列宏用于抽象队列操作，不直接接触输出队列结构的内部字段。这些宏独立于 `ALTQ` 实现，并与传统的 `ifqueue` 宏兼容，便于过渡。

`IFQ_ENQUEUE`、`IFQ_HANDOFF` 和 `IFQ_HANDOFF_ADJ` 将数据包 `m` 入队到队列 `ifq`。底层排队规则可能丢弃数据包。`error` 参数在成功时设置为 0，如果数据包被丢弃则设置为 `ENOBUFS`。成功时由设备驱动程序释放 `m` 指向的数据包，失败时由排队规则释放，因此调用者在入队后不应再操作 `m`。`IFQ_HANDOFF` 和 `IFQ_HANDOFF_ADJ` 将入队操作与统计生成结合，并在成功入队时调用 `if_start` 以启动实际发送。

`IFQ_DEQUEUE` 从队列中出队一个数据包。出队的数据包通过 `m` 返回，如果没有数据包出队则 `m` 设置为 `NULL`。调用者必须始终检查 `m`，因为在速率限制下非空队列也可能返回 `NULL`。

`IFQ_POLL_NOLOCK` 返回下一个数据包但不从队列中移除。调用者在调用 `IFQ_POLL_NOLOCK` 时必须持有队列互斥锁，以保证后续调用 `IFQ_DEQUEUE_NOLOCK` 出队相同的数据包。

`IFQ_*_NOLOCK` 变体（如果可用）始终假设调用者持有队列互斥锁。可以使用 `IFQ_LOCK` 获取锁，使用 `IFQ_UNLOCK` 释放锁。

`IFQ_PURGE` 丢弃队列中的所有数据包。需要清除操作是因为非工作保守队列无法通过出队循环清空。

`IFQ_IS_EMPTY` 可用于检查队列是否为空。注意，如果排队规则是非工作保守的，`IFQ_DEQUEUE` 仍可能返回 `NULL`。

`IFQ_DRV_DEQUEUE` 将最多 `ifq->ifq_drv_maxlen` 个数据包从队列移动到"驱动管理"队列，并通过 `m` 返回第一个。与 `IFQ_DEQUEUE` 一样，即使队列非空，`m` 也可能为 `NULL`。后续调用 `IFQ_DRV_DEQUEUE` 从"驱动管理"队列传递数据包，而无需获取队列互斥锁。调用者有责任防止并发访问。为给定队列启用 `ALTQ` 会将 `ifq_drv_maxlen` 设置为 0，因为 `IFQ_DRV_DEQUEUE` 对较大 `ifq_drv_maxlen` 值执行的"批量出队"对 `ALTQ` 的内部计时有不利影响。注意，驱动程序不得将 `IFQ_DRV_*` 宏与默认出队宏混合使用，因为默认宏不查看"驱动管理"队列，可能导致 mbuf 泄漏。

`IFQ_DRV_PREPEND` 将 `m` 前置到"驱动管理"队列，下次调用 `IFQ_DRV_DEQUEUE` 时将从中获取。

`IFQ_DRV_PURGE` 刷新"驱动管理"队列中的所有数据包，然后调用 `IFQ_PURGE`。

`IFQ_DRV_IS_EMPTY` 检查队列的"驱动管理"部分是否有数据包。如果为空，则转发到 `IFQ_IS_EMPTY`。

`IFQ_SET_MAXLEN` 设置默认 FIFO 队列的长度限制。`ifaltq` 结构的 `ifq_drv_maxlen` 成员控制"驱动管理"队列的长度限制。

`IFQ_INC_LEN` 和 `IFQ_DEC_LEN` 增加或减少当前队列长度（以数据包计）。这主要用于内部目的。

`IFQ_INC_DROPS` 增加丢弃计数器，与 `IF_DROP` 相同。定义它仅为命名一致性。

`IFQ_SET_READY` 设置标志以指示驱动程序已转换为使用新宏。只能在具有此标志的接口上启用 `ALTQ`。

## 兼容性

### `ifaltq` 结构

为了与现有代码保持兼容，新的输出队列结构 `ifaltq` 具有相同的字段。传统的 `IF_*` 宏和直接引用 `if_snd` 中字段的代码仍然适用于 `ifaltq`。

```c
            ##old-style##                           ##new-style##
                                       |
 struct ifqueue {                      | struct ifaltq {
    struct mbuf *ifq_head;             |    struct mbuf *ifq_head;
    struct mbuf *ifq_tail;             |    struct mbuf *ifq_tail;
    int          ifq_len;              |    int          ifq_len;
    int          ifq_maxlen;           |    int          ifq_maxlen;
 };                                    |    /* 驱动队列字段 */
                                       |    ......
                                       |    /* altq 相关字段 */
                                       |    ......
                                       | };
                                       |
```

新结构替换了 `struct ifnet` 中的 `struct ifqueue`。

```c
            ##old-style##                           ##new-style##
                                       |
 struct ifnet {                        | struct ifnet {
     ....                              |     ....
                                       |
     struct ifqueue if_snd;            |     struct ifaltq if_snd;
                                       |
     ....                              |     ....
 };                                    | };
                                       |
```

（简化的）新 `IFQ_*` 宏如下所示：

```c
	#define IFQ_DEQUEUE(ifq, m)			\
		if (ALTQ_IS_ENABLED((ifq))		\
			ALTQ_DEQUEUE((ifq), (m));	\
		else					\
			IF_DEQUEUE((ifq), (m));
```

### 入队操作

入队操作的语义已改变。在新样式中，入队和数据包丢弃合并在一起，因为在许多排队规则中它们不易分离。新的入队操作对应于以下用旧宏编写的宏。

```c
#define	IFQ_ENQUEUE(ifq, m, error)                      \
do {                                                    \
        if (IF_QFULL((ifq))) {                          \
                m_freem((m));                           \
                (error) = ENOBUFS;                      \
                IF_DROP(ifq);                           \
        } else {                                        \
                IF_ENQUEUE((ifq), (m));                 \
                (error) = 0;                            \
        }                                               \
} while (0)
```

`IFQ_ENQUEUE` 执行以下操作：

- 将数据包入队，
- 如果入队操作失败，则丢弃（并释放）数据包。

如果入队操作失败，`error` 设置为 `ENOBUFS`。`m` mbuf 由排队规则释放。调用者在调用 `IFQ_ENQUEUE` 后不应再操作 mbuf，因此调用者可能需要事先复制 `m_pkthdr.len` 或 `m_flags` 字段用于统计。如果只需要默认接口统计和立即调用 `if_start`，可以使用 `IFQ_HANDOFF` 和 `IFQ_HANDOFF_ADJ`。调用者不应使用 `senderr`，因为 mbuf 已被释放。

新样式 `if_output` 如下所示：

```c
            ##old-style##                           ##new-style##
                                       |
 int                                   | int
 ether_output(ifp, m0, dst, rt0)       | ether_output(ifp, m0, dst, rt0)
 {                                     | {
     ......                            |     ......
                                       |
                                       |     mflags = m->m_flags;
                                       |     len = m->m_pkthdr.len;
     s = splimp();                     |     s = splimp();
     if (IF_QFULL(&ifp->if_snd)) {     |     IFQ_ENQUEUE(&ifp->if_snd, m,
                                       |                 error);
         IF_DROP(&ifp->if_snd);        |     if (error != 0) {
         splx(s);                      |         splx(s);
         senderr(ENOBUFS);             |         return (error);
     }                                 |     }
     IF_ENQUEUE(&ifp->if_snd, m);      |
     ifp->if_obytes +=                 |     ifp->if_obytes += len;
                    m->m_pkthdr.len;   |
     if (m->m_flags & M_MCAST)         |     if (mflags & M_MCAST)
         ifp->if_omcasts++;            |         ifp->if_omcasts++;
                                       |
     if ((ifp->if_flags & IFF_OACTIVE) |     if ((ifp->if_flags & IFF_OACTIVE)
         == 0)                         |         == 0)
         (*ifp->if_start)(ifp);        |         (*ifp->if_start)(ifp);
     splx(s);                          |     splx(s);
     return (error);                   |     return (error);
                                       |
 bad:                                  | bad:
     if (m)                            |     if (m)
         m_freem(m);                   |         m_freem(m);
     return (error);                   |     return (error);
 }                                     | }
                                       |
```

## 如何转换现有驱动程序

首先，确保相应的 `if_output` 已转换为新样式。

在驱动程序中查找 `if_snd`。可能需要修改包含 `if_snd` 的行。

### 空检查操作

如果代码检查 `ifq_head` 来判断队列是否为空，使用 `IFQ_IS_EMPTY`。

```c
            ##old-style##                           ##new-style##
                                       |
 if (ifp->if_snd.ifq_head != NULL)     | if (!IFQ_IS_EMPTY(&ifp->if_snd))
                                       |
```

`IFQ_IS_EMPTY` 仅检查队列中是否存储了任何数据包。注意，即使 `IFQ_IS_EMPTY` 为 `FALSE`，如果队列处于速率限制下，`IFQ_DEQUEUE` 仍可能返回 `NULL`。

### 出队操作

用 `IFQ_DEQUEUE` 替换 `IF_DEQUEUE`。始终检查出队的 mbuf 是否为 `NULL`。注意，即使 `IFQ_IS_EMPTY` 为 `FALSE`，由于速率限制，`IFQ_DEQUEUE` 也可能返回 `NULL`。

```c
            ##old-style##                           ##new-style##
                                       |
 IF_DEQUEUE(&ifp->if_snd, m);          | IFQ_DEQUEUE(&ifp->if_snd, m);
                                       | if (m == NULL)
                                       |     return;
                                       |
```

驱动程序应从发送完成中断调用 `if_start`，以触发下一次出队。

### 轮询并出队操作

如果代码轮询队列头部的数据包并在出队前实际使用该数据包，使用 `IFQ_POLL_NOLOCK` 和 `IFQ_DEQUEUE_NOLOCK`。

```c
            ##old-style##                           ##new-style##
                                       |
                                       | IFQ_LOCK(&ifp->if_snd);
 m = ifp->if_snd.ifq_head;             | IFQ_POLL_NOLOCK(&ifp->if_snd, m);
 if (m != NULL) {                      | if (m != NULL) {
                                       |
     /* use m to get resources */      |     /* 使用 m 获取资源 */
     if (something goes wrong)         |     if (something goes wrong)
                                       |         IFQ_UNLOCK(&ifp->if_snd);
         return;                       |         return;
                                       |
     IF_DEQUEUE(&ifp->if_snd, m);      |     IFQ_DEQUEUE_NOLOCK(&ifp->if_snd, m);
                                       |     IFQ_UNLOCK(&ifp->if_snd);
                                       |
     /* kick the hardware */           |     /* 启动硬件 */
 }                                     | }
                                       |
```

保证在与先前 `IFQ_POLL_NOLOCK` 相同的锁下，`IFQ_DEQUEUE_NOLOCK` 返回相同的数据包。注意，它们需要由 `IFQ_LOCK` 保护。

### 消除 `IF_PREPEND`

如果代码使用 `IF_PREPEND`，必须消除它，除非可以使用允许使用 `IFQ_DRV_PREPEND` 作为替代的"驱动管理"队列。`IF_PREPEND` 的常见用法是取消先前的出队操作。必须将逻辑转换为轮询并出队。

```c
            ##old-style##                           ##new-style##
                                       |
                                       | IFQ_LOCK(&ifp->if_snd);
 IF_DEQUEUE(&ifp->if_snd, m);          | IFQ_POLL_NOLOCK(&ifp->if_snd, m);
 if (m != NULL) {                      | if (m != NULL) {
                                       |
     if (something_goes_wrong) {       |     if (something_goes_wrong) {
         IF_PREPEND(&ifp->if_snd, m);  |         IFQ_UNLOCK(&ifp->if_snd);
         return;                       |         return;
     }                                 |     }
                                       |
                                       |     /* 此时，驱动程序
                                       |      * 已承诺发送此
                                       |      * 数据包。
                                       |      */
                                       |     IFQ_DEQUEUE_NOLOCK(&ifp->if_snd, m);
                                       |     IFQ_UNLOCK(&ifp->if_snd);
                                       |
     /* kick the hardware */           |     /* 启动硬件 */
 }                                     | }
                                       |
```

### 清除操作

使用 `IFQ_PURGE` 清空队列。注意，非工作保守队列无法通过出队循环清空。

```c
            ##old-style##                           ##new-style##
                                       |
 while (ifp->if_snd.ifq_head != NULL) {|  IFQ_PURGE(&ifp->if_snd);
     IF_DEQUEUE(&ifp->if_snd, m);      |
     m_freem(m);                       |
 }                                     |
                                       |
```

### 使用驱动管理队列转换

将 `IF_*` 宏转换为等效的 `IFQ_DRV_*`，并在适当的地方使用 `IFQ_DRV_IS_EMPTY`。

```c
            ##old-style##                           ##new-style##
                                       |
 if (ifp->if_snd.ifq_head != NULL)     | if (!IFQ_DRV_IS_EMPTY(&ifp->if_snd))
                                       |
```

确保对 `IFQ_DRV_DEQUEUE`、`IFQ_DRV_PREPEND` 和 `IFQ_DRV_PURGE` 的调用受到某种互斥锁的保护。

### 附加例程

使用 `IFQ_SET_MAXLEN` 将 `ifq_maxlen` 设置为 `len`。如果计划使用 `IFQ_DRV_*` 宏，使用合理的值初始化 `ifq_drv_maxlen`。添加 `IFQ_SET_READY` 以表明此驱动程序已转换为新样式。（用于区分新样式驱动程序。）

```c
            ##old-style##                           ##new-style##
                                       |
 ifp->if_snd.ifq_maxlen = qsize;       | IFQ_SET_MAXLEN(&ifp->if_snd, qsize);
                                       | ifp->if_snd.ifq_drv_maxlen = qsize;
                                       | IFQ_SET_READY(&ifp->if_snd);
 if_attach(ifp);                       | if_attach(ifp);
                                       |
```

### 其他问题

统计的新宏：

```c
            ##old-style##                           ##new-style##
                                       |
 IF_DROP(&ifp->if_snd);                | IFQ_INC_DROPS(&ifp->if_snd);
                                       |
 ifp->if_snd.ifq_len++;                | IFQ_INC_LEN(&ifp->if_snd);
                                       |
 ifp->if_snd.ifq_len--;                | IFQ_DEC_LEN(&ifp->if_snd);
                                       |
```

## 排队规则

排队规则需要维护 `ifq_len`（由 `IFQ_IS_EMPTY` 使用）。排队规则还需要保证，如果 `IFQ_DEQUEUE` 在 `IFQ_POLL` 之后立即调用，则返回相同的 mbuf。

## 参见

[pf(4)](../man4/pf.4.md), [pf.conf(5)](../man5/pf.conf.5.md), pfctl(8)

## 历史

`ALTQ` 系统首次出现于 1997 年 3 月，并在 KAME 项目（https://www.kame.net）中找到归宿。它在 FreeBSD 5.3 中被导入。
