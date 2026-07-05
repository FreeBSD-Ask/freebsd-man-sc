# ng_pipe.4

`ng_pipe` — 流量操控 netgraph 节点类型

## 名称

`ng_pipe`

## 概要

`#include <netgraph/ng_pipe.h>`

## 描述

`pipe` 节点类型通过模拟带宽和延迟以及随机丢包来操控流量。

## 钩子

此节点类型支持以下钩子：

**`upper`** 通向上层协议的钩子。

**`lower`** 通向下层协议的钩子。

从 `upper` 流向 `lower` 的流量被视为**下游**流量。从 `lower` 流向 `upper` 的流量被视为**上游**流量。

## 操作模式

在钩子上接收的数据——无论是上游还是下游方向——都会被放入入站队列。如果入站队列已满，则根据丢弃策略（从队首或队尾）丢弃一帧。

输入队列有三种互斥的模式：

**`First In First Out (FIFO)`** 单个队列按时间顺序保存数据包。

**`Weighted fair queuing (WFQ)`** 为不同流（基于 IPv4 IP）设置多个队列。必要时会截断最长的队列。此方法假设停滞的流是当前持有数据包最多的流。

**`Deficit Round Robin (DRR)`** 此模式类似 WFQ，但数据包并非严格按时间顺序取出。原则上最旧的数据包先出，但同一流的数据包不会一次性取出过多。

可以配置复制概率。在投掷决定下，当前活动的数据包保留在队列中，同时发送该数据包的一个副本。没有任何机制阻止数据包被多次复制。

如果配置了 `ber`（误码率），数据包会根据其大小以递增的概率被丢弃。

存活的数据包会被延迟该数据包通过所配置带宽的链路所需的时间。如果出站队列已满，则丢弃该数据包。

## 控制消息

此节点类型支持通用控制消息及以下特定消息。

```sh
struct ng_pipe_cfg {
  u_int64_t  bandwidth;     /* 每秒比特数 */
  u_int64_t  delay;         /* 附加延迟，微秒 */
  u_int32_t  header_offset; /* IP 头部偏移（字节） */
  u_int32_t  overhead;      /* 假定的 L2 开销（字节） */
  struct ng_pipe_hookcfg  downstream;
  struct ng_pipe_hookcfg  upstream;
};
/* 单个钩子的配置结构 */
struct ng_pipe_hookcfg {
  u_int64_t  bandwidth;       /* 每秒比特数 */
  u_int64_t  ber;             /* 位错误之间的平均间隔（1 / BER） */
  u_int32_t  qin_size_limit;  /* 队列项数 */
  u_int32_t  qout_size_limit; /* 队列项数 */
  u_int32_t  duplicate;       /* 概率（百分比） */
  u_int32_t  fifo;            /* 0 = 关闭，1 = 开启 */
  u_int32_t  drr;             /* 0 = 关闭，1 = 2048 字节，或 x 字节 */
  u_int32_t  wfq;             /* 0 = 关闭，1 = 开启 */
  u_int32_t  droptail;        /* 0 = 关闭，1 = 开启 */
  u_int32_t  drophead;        /* 0 = 关闭，1 = 开启 */
};
```

```sh
/* 单个钩子的统计结构 */
struct ng_pipe_hookstat {
  u_int64_t  fwd_octets;
  u_int64_t  fwd_frames;
  u_int64_t  in_disc_octets;
  u_int64_t  in_disc_frames;
  u_int64_t  out_disc_octets;
  u_int64_t  out_disc_frames;
};
/* NGM_PIPE_GET_STATS 返回的统计结构 */
struct ng_pipe_stats {
  struct ng_pipe_hookstat  downstream;
  struct ng_pipe_hookstat  upstream;
};
```

```sh
/* 单个钩子的运行时结构 */
struct ng_pipe_hookrun {
  u_int32_t  fifo_queues;
  u_int32_t  qin_octets;
  u_int32_t  qin_frames;
  u_int32_t  qout_octets;
  u_int32_t  qout_frames;
};
/* NGM_PIPE_GET_RUN 返回的运行时结构 */
struct ng_pipe_run {
  struct ng_pipe_hookrun  downstream;
  struct ng_pipe_hookrun  upstream;
};
```

**`NGM_PIPE_SET_CFG`**（`setcfg`）将节点配置设置为 `struct ng_pipe_cfg` 中指定的值。注意：要将值设为零，请指定 -1。这样允许省略不应修改的配置值。

**`NGM_PIPE_GET_CFG`**（`getcfg`）以 `struct ng_pipe_cfg` 形式返回当前节点配置。

**`NGM_PIPE_GET_STATS`**（`getstats`）以 `struct ng_pipe_stats` 形式返回节点统计信息。

**`NGM_PIPE_CLR_STATS`**（`clrstats`）清零节点统计信息。

**`NGM_PIPE_GETCLR_STATS`**（`getclrstats`）原子地返回并清零节点统计信息。

**`NGM_PIPE_GET_RUN`**（`getrun`）以 `struct ng_pipe_run` 形式返回节点统计信息。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在所有钩子均已断开时关闭。

## 实例

将 fxp0 以太网接口的出站数据速率在 fifo 模式下限制为 20Mbps，入站数据在 drr 模式下限制为 50kbps，并设置 2% 的复制概率。

```sh
/usr/sbin/ngctl -f- <<-SEQ
  mkpeer fxp0: pipe lower lower
  name fxp0:lower fxp0_pipe
  connect fxp0: fxp0_pipe: upper upper
  msg fxp0_pipe: setcfg { downstream={ bandwidth=20000000 fifo=1 } }
  msg fxp0_pipe: setcfg { upstream={ bandwidth=500000 drr=1 duplicate=2 } }
SEQ
```

## 参见

[netgraph(4)](netgraph.4.md), ngctl(8)

## 作者

Lutz Donnerhacke <lutz@donnerhacke.de>（手册页）

## 缺陷

缺少对内存问题的错误处理。如果无法立即分配内核内存，将触发内核崩溃。如果 mbuf 在传输头部内被分片，也会发生同样的情况。
