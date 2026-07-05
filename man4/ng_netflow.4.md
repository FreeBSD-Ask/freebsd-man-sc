# ng_netflow.4

`ng_netflow` — Cisco 的 NetFlow 实现

## 名称

`ng_netflow`

## 概要

`#include <sys/types.h>`

`#include <netinet/in.h>`

`#include <netgraph/netflow/ng_netflow.h>`

## 描述

`ng_netflow` 节点在运行 FreeBSD 的路由器上实现 Cisco 的 NetFlow 导出协议。`ng_netflow` 节点监听传入流量并识别其中的唯一流。流通过端点 IP 地址、TCP/UDP 端口号、ToS 和输入接口区分。过期流以 NetFlow 版本 5/9 UDP 数据报形式从节点导出。过期原因可能是以下之一：

- RST 或 FIN TCP 段。
- 活动超时。流不能存活超过指定的时间段。默认为 1800 秒（30 分钟）。
- 非活动超时。流在指定时间段内处于非活动状态。默认为 15 秒。

节点支持 IPv6 计费（仅 NetFlow v9）并感知多个 fib。不同的 fib 映射到 NetFlow V9 中不同的 domain_id 和 NetFlow V5 中不同的 engine_id。

## 钩子

本节点类型最多支持 `NG_NETFLOW_MAXIFACES`（默认 65536）个名为 `iface0`、`iface1` 等的钩子，以及相同数量的名为 `out0`、`out1` 等的钩子，外加两个导出钩子：`export`（用于 NetFlow 版本 5）和 `export9`（用于 NetFlow 版本 9）。可同时对所有支持的导出钩子进行导出。默认情况下（启用入口 NetFlow），节点对 `iface*` 钩子上接收的数据进行 NetFlow 计费。如果相应的 `out` 钩子已连接，未修改的数据会旁路到该钩子，否则数据被释放。如果在 `out` 钩子上收到数据，会旁路到相应的 `iface` 钩子，不进行任何处理（默认禁用出口 NetFlow）。当某个导出协议的完整导出数据报构建完成后，会发送到 `export` 或 `export9` 钩子。在正常操作中，一个（或多个）导出钩子会连接到 [ng_ksocket(4)](ng_ksocket.4.md) 节点的 `inet/dgram/udp` 钩子。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

`#include <net/bpf.h>`

```sh
struct ng_netflow_setdlt {
	uint16_t iface;		/* 哪个 iface dlt 更改 */
	uint8_t  dlt;		/* 来自 bpf.h 的 DLT_XXX */
};
```

```sh
struct ng_netflow_setifindex {
	uint16_t iface;		/* 哪个 iface 索引更改 */
	uint16_t index;		/* 新索引 */
};
```

```sh
struct ng_netflow_settimeouts {
	uint32_t inactive_timeout;	/* 流非活动超时 */
	uint32_t active_timeout;	/* 流活动超时 */
};
```

```sh
struct ng_netflow_setconfig {
	uint16_t iface;		/* 哪个 iface 配置更改 */
	uint32_t conf;		/* 新配置 */
#define NG_NETFLOW_CONF_INGRESS		1
#define NG_NETFLOW_CONF_EGRESS		2
#define NG_NETFLOW_CONF_ONCE		4
#define NG_NETFLOW_CONF_THISONCE	8
#define NG_NETFLOW_CONF_NOSRCLOOKUP	16
#define NG_NETFLOW_CONF_NODSTLOOKUP	32
};
```

```sh
struct ng_netflow_settemplate {
	uint16_t time;		/* 公告之间的最长时间 */
	uint16_t packets;	/* 公告之间的最大数据包数 */
};
```

```sh
struct ng_netflow_setemtu {
	uint16_t mtu;		/* 数据包的 MTU */
};
```

```sh
struct ng_netflow_v9info {
    uint16_t        templ_packets;  /* v9 模板数据包 */
    uint16_t        templ_time;     /* v9 模板时间 */
    uint16_t        mtu;            /* v9 MTU */
};
```

**`NGM_NETFLOW_INFO`** (`info`) 以 `struct ng_netflow_info` 形式返回一些节点统计信息和当前超时值。

**`NGM_NETFLOW_IFINFO`** (`ifinfo`) 返回 `iface``N` 钩子的信息。钩子号作为参数传递。

**`NGM_NETFLOW_SETDLT`** (`setdlt`) 设置 `iface``N` 钩子上的数据链路类型。目前支持的类型有 `DLT_RAW`（原始 IP 数据报）和 `DLT_EN10MB`（以太网）。DLT_ 定义可在头文件中找到。当前使用的值为 1（`DLT_EN10MB`）和 12（`DLT_RAW`）。此消息类型使用 `struct ng_netflow_setdlt` 作为参数：请求的 `iface``N` 钩子必须已连接，否则消息发送操作将返回错误。

**`NGM_NETFLOW_SETIFINDEX`** (`setifindex`) 在某些情况下，`ng_netflow` 可能无法确定数据包的输入接口索引。这可能在流量进入 `ng_netflow` 节点之前就到达系统接口的输入队列时发生。这种设置的一个示例是在同步数据线路和 [ng_iface(4)](ng_iface.4.md) 之间捕获流量。在这种情况下，输入索引应与给定钩子关联。接口的索引可通过用户态的 if_nametoindex(3) 确定。此消息需要 `struct ng_netflow_setifindex` 作为参数：请求的 `iface``N` 钩子必须已连接，否则消息发送操作将返回错误。

**`NGM_NETFLOW_SETTIMEOUTS`** (`settimeouts`) 设置 NetFlow 活动/非活动超时的秒数值。此消息需要 `struct ng_netflow_settimeouts` 作为参数：

**`NGM_NETFLOW_SETCONFIG`** (`setconfig`) 设置指定接口的配置。此消息需要 `struct ng_netflow_setconfig` 作为参数：配置是几个选项的位掩码。默认启用的选项 NG_NETFLOW_CONF_INGRESS 启用入口 NetFlow 生成（用于来自 ifaceX 钩子的数据）。选项 `NG_NETFLOW_CONF_EGRESS` 启用出口 NetFlow（用于来自 outX 钩子的数据）。选项 `NG_NETFLOW_CONF_ONCE` 定义如果数据包多次通过 netflow 节点，只应计费一次。选项 `NG_NETFLOW_CONF_THISONCE` 定义如果数据包多次通过此 netflow 节点，只应计费一次。这两个选项对于在同时启用入口和出口 NetFlow 时避免重复计费很重要。选项 `NG_NETFLOW_CONF_NOSRCLOOKUP` 跳过对用于填充网络掩码的流源地址的 radix 查找。选项 `NG_NETFLOW_CONF_NODSTLOOKUP` 跳过对目的地的 radix 查找（填充出口接口 ID、目的掩码和网关）。如果不需要查找提供的数据，可以禁用它们以减少路由器上的负载。

**`NGM_NETFLOW_SETTEMPLATE`** (`settemplate`) 设置用于公告数据流模板的各种超时（NetFlow v9 特定）。此消息需要 `struct ng_netflow_settemplate` 作为参数：time 字段值表示重新公告数据模板的时间（秒）。packets 字段值表示重新公告数据模板之间的最大数据包计数。

**`NGM_NETFLOW_SETMTU`** (`setmtu`) 设置导出接口 MTU 以构建指定大小的数据包（NetFlow v9 特定）。此消息需要 `struct ng_netflow_setmtu` 作为参数：默认为 1500 字节。

**`NGM_NETFLOW_SHOW`** 此控制消息请求节点转储流缓存的全部内容。它由 flowctl(8) 调用，而非直接从 ngctl(8) 调用。

**`NGM_NETFLOW_V9INFO`** (`v9info`) 以

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在所有钩子都已断开时关闭。

## 实例

最简单的可能配置是一个启用了流收集的以太网接口。

```sh
/usr/sbin/ngctl -f- <<-SEQ
	mkpeer fxp0: netflow lower iface0
	name fxp0:lower netflow
	connect fxp0: netflow: upper out0
	mkpeer netflow: ksocket export inet/dgram/udp
	msg netflow:export connect inet/10.0.0.1:4444
SEQ
```

这是一个更复杂的路由器示例，具有 2 个启用 NetFlow 的接口 `fxp0` 和 `ng0`。注意，此示例中的 `ng0:` 节点连接到 [ng_tee(4)](ng_tee.4.md)。后者向我们发送 IP 数据包的副本，我们进行分析并释放。在 `fxp0:` 上我们不使用 tee，而是将数据包发回任一节点。

```sh
/usr/sbin/ngctl -f- <<-SEQ
	# 将 ng0 的 tee 连接到 iface0 钩子
	mkpeer ng0:inet netflow right2left iface0
	name ng0:inet.right2left netflow
	# 将 DLT 设置为原始模式
	msg netflow: setdlt { iface=0 dlt=12 }
	# 设置接口索引（此示例中为 5）
	msg netflow: setifindex { iface=0 index=5 }
	# 将 fxp0: 连接到 iface1 和 out1 钩子
	connect fxp0: netflow: lower iface1
	connect fxp0: netflow: upper out1
	# 在 export 钩子上创建 ksocket 节点，并配置它
	# 将导出发送到正确的目的地
	mkpeer netflow: ksocket export inet/dgram/udp
	msg netflow:export connect inet/10.0.0.1:4444
SEQ
```

## 参见

setfib(2), [netgraph(4)](netgraph.4.md), [ng_ether(4)](ng_ether.4.md), [ng_iface(4)](ng_iface.4.md), [ng_ksocket(4)](ng_ksocket.4.md), [ng_tee(4)](ng_tee.4.md), flowctl(8), ngctl(8)

> B. Claise, Ed, "Cisco Systems NetFlow Services Export Version 9", RFC 3954.

`http://www.cisco.com/en/US/docs/ios/solutions_docs/netflow/nfwhite.html`

## 作者

`ng_netflow` 节点类型由 Gleb Smirnoff <glebius@FreeBSD.org>、Alexander Motin <mav@FreeBSD.org>、Alexander Chernikov <melifaro@ipfw.ru> 编写。初始代码基于 Roman V. Palagin <romanp@unshadow.net> 编写的 `ng_ipacct`。

## 缺陷

通过 `NGM_NETFLOW_SHOW` 命令获取的缓存快照在严重负载下可能缺少一定百分比的条目。

`ng_ipacct` 节点类型不填充 AS 号。这是由于内核路由表中缺乏必要信息。但此信息可以从路由守护进程（如 GNU Zebra）注入内核。此功能可能在未来的版本中提供。
