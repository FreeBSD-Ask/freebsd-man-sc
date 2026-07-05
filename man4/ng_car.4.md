# ng_car.4

`ng_car` — 承诺访问速率 netgraph 节点类型

## 名称

`ng_car`

## 概要

`#include <netgraph/ng_car.h>`

## 描述

`car` 节点类型使用以下方法限制流经它的流量：

- 单速率三色标记（如 RFC 2697 所述），
- 双速率三色标记（如 RFC 2698 所述），
- Cisco 使用的类 RED 速率限制算法，
- 使用 RED 的流量整形。

## 钩子

此节点类型支持以下钩子：

**`upper`** 通向上层协议的钩子。

**`lower`** 通向下层协议的钩子。

从 `upper` 流向 `lower` 的流量视为**下游**流量。从 `lower` 流向 `upper` 的流量视为**上游**流量。

## 操作模式

每个钩子可在以下模式之一中操作：

**`NG_CAR_SINGLE_RATE`** 如 RFC 2697 所述的单速率三色标记。承诺突发数据包计为绿色，扩展突发数据包计为黄色，超出数据包计为红色。承诺突发以 CIR（承诺信息速率）速度补充。当它满时，扩展突发被补充。

**`NG_CAR_DOUBLE_RATE`** 如 RFC 2698 所述的双速率三色标记。承诺突发数据包计为绿色，峰值突发数据包计为黄色，超出数据包计为红色。承诺突发以 CIR 速度补充。同时峰值突发以 PIR（峰值信息速率）速度补充。

**`NG_CAR_RED`** 类似于 `NG_CAR_SINGLE_RATE`，但对扩展突发有不同理解。当正常突发超出且使用扩展突发时，数据包以等于已消耗扩展突发部分的概率计为红色。扩展突发先被补充。当它满时，承诺突发被补充。此行为类似于 RED 主动队列管理算法。此算法对 TCP 流量比 NG_CAR_SINGLE_RATE 更温和。

**`NG_CAR_SHAPE`** 承诺突发数据包计为绿色，超出数据包由带 RED 管理的队列延迟并计为黄色。被队列丢弃的数据包计为红色。队列参数是硬编码的：长度 99 个数据包，min_th 8 个数据包，max_p 100%。流量整形对 TCP 流量比在带宽 × 延迟乘积小于 6-8 个 TCP 段的链路上进行速率限制更温和，但它消耗额外的系统资源用于队列处理。

默认情况下，所有信息速率以比特每秒为单位测量，突发以字节为单位测量。但当启用 NG_CAR_COUNT_PACKETS 选项时，速率以包每秒为单位测量，突发以包为单位。

## 控制消息

此节点类型支持通用控制消息和以下特定消息。

```sh
struct ng_car_hookconf {
	uint64_t cbs;		/* 承诺突发大小（字节） */
	uint64_t ebs;		/* 超出/峰值突发大小（字节） */
	uint64_t cir;		/* 承诺信息速率（比特/秒） */
	uint64_t pir;		/* 峰值信息速率（比特/秒） */
	uint8_t  green_action;	/* 绿色数据包的动作 */
	uint8_t  yellow_action;	/* 黄色数据包的动作 */
	uint8_t  red_action;	/* 红色数据包的动作 */
	uint8_t  mode;		/* 单/双速率等 */
	uint8_t  opt;		/* 色感知或色盲 */
};
/* 可能的动作（..._action） */
enum {
    NG_CAR_ACTION_FORWARD = 1,
    NG_CAR_ACTION_DROP,
    NG_CAR_ACTION_MARK
};
/* 操作模式（mode） */
enum {
    NG_CAR_SINGLE_RATE = 0,
    NG_CAR_DOUBLE_RATE,
    NG_CAR_RED,
    NG_CAR_SHAPE
};
/* 模式选项（opt 的位） */
#define NG_CAR_COLOR_AWARE	1
#define NG_CAR_COUNT_PACKETS	2
struct ng_car_bulkconf {
	struct ng_car_hookconf upstream;
	struct ng_car_hookconf downstream;
};
```

```sh
struct ng_car_hookstats {
	uint64_t passed_pkts;	/* 通过的数据包计数器 */
	uint64_t dropped_pkts;	/* 丢弃的数据包计数器 */
	uint64_t green_pkts;	/* 绿色数据包计数器 */
	uint64_t yellow_pkts;	/* 黄色数据包计数器 */
	uint64_t red_pkts;	/* 红色数据包计数器 */
	uint64_t errors;	/* 操作错误计数器 */
};
struct ng_car_bulkstats {
	struct ng_car_hookstats upstream;
	struct ng_car_hookstats downstream;
};
```

**`NGM_CAR_SET_CONF`** (`setconf`) 将节点配置设置为 `struct ng_car_bulkconf` 中指定的值

**`NGM_CAR_GET_CONF`** (`getconf`) 返回当前节点配置，作为 `struct ng_car_bulkconf`

**`NGM_CAR_GET_STATS`** (`getstats`) 返回节点统计信息，作为 `struct ng_car_bulkstats`

**`NGM_CAR_CLR_STATS`** (`clrstats`) 清除节点统计信息。

**`NGM_CAR_GETCLR_STATS`** (`getclrstats`) 原子性地返回并清除节点统计信息。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或当所有钩子都已断开时关闭。

## 实例

将 fxp0 以太网接口上的传出数据速率限制为 20Mbit/s，传入数据包速率限制为 5000pps。

```sh
/usr/sbin/ngctl -f- <<-SEQ
	mkpeer fxp0: car lower lower
	name fxp0:lower fxp0_car
	connect fxp0: fxp0_car: upper upper
	msg fxp0_car: setconf { downstream={ cir=20000000 cbs=2500000 ebs=2500000 greenAction=1 yellowAction=1 redAction=2 mode=2 } upstream={ cir=5000 cbs=100 ebs=100 greenAction=1 yellowAction=1 redAction=2 mode=2 opt=2 } }
SEQ
```

## 参见

[netgraph(4)](netgraph.4.md), ngctl(8)

> J. Heinanen, "A Single Rate Three Color Marker", RFC 2697.

> J. Heinanen, "A Two Rate Three Color Marker", RFC 2698.

## 作者

Nuno Antunes <nuno.antunes@gmail.com> Alexander Motin <mav@FreeBSD.org>

## 缺陷

目前仅实现了 DROP 和 FORWARD 动作。
