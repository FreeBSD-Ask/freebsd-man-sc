# ng_nat(4)

`ng_nat` — NAT netgraph 节点类型

## 名称

`ng_nat`

## 概要

`#include <netgraph/ng_nat.h>`

## 描述

`ng_nat` 节点对通过它的 IPv4 数据包执行网络地址转换（NAT）。`nat` 节点使用 libalias(3) 引擎进行数据包别名处理。

## 钩子

本节点类型有两个钩子：

**`out`** 在此钩子上接收的数据包被视为传出数据包，将被伪装为配置的地址。

**`in`** 在此钩子上接收的数据包被视为传入数据包，将被解除别名。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

```sh
struct ng_nat_mode {
	uint32_t	flags;
	uint32_t	mask;
};
/* 支持的标志： */
#define NG_NAT_LOG			0x01
#define NG_NAT_DENY_INCOMING		0x02
#define NG_NAT_SAME_PORTS		0x04
#define NG_NAT_UNREGISTERED_ONLY	0x10
#define NG_NAT_RESET_ON_ADDR_CHANGE	0x20
#define NG_NAT_PROXY_ONLY		0x40
#define NG_NAT_REVERSE			0x80
#define NG_NAT_UNREGISTERED_CGN		0x100
#define NG_NAT_UDP_EIM			0x200
```

```sh
#define NG_NAT_DESC_LENGTH	64
struct ng_nat_redirect_port {
	struct in_addr	local_addr;
	struct in_addr	alias_addr;
	struct in_addr	remote_addr;
	uint16_t	local_port;
	uint16_t	alias_port;
	uint16_t	remote_port;
	uint8_t		proto;
	char		description[NG_NAT_DESC_LENGTH];
};
```

```sh
struct ng_nat_redirect_addr {
	struct in_addr	local_addr;
	struct in_addr	alias_addr;
	char		description[NG_NAT_DESC_LENGTH];
};
```

```sh
struct ng_nat_redirect_proto {
	struct in_addr	local_addr;
	struct in_addr	alias_addr;
	struct in_addr	remote_addr;
	uint8_t		proto;
	char		description[NG_NAT_DESC_LENGTH];
};
```

```sh
struct ng_nat_add_server {
	uint32_t	id;
	struct in_addr	addr;
	uint16_t	port;
};
```

```sh
struct ng_nat_listrdrs_entry {
	uint32_t	id;		/* 除零外的任何值 */
	struct in_addr	local_addr;
	struct in_addr	alias_addr;
	struct in_addr	remote_addr;
	uint16_t	local_port;
	uint16_t	alias_port;
	uint16_t	remote_port;
	uint16_t	proto;		/* 有效 proto 或 NG_NAT_REDIRPROTO_ADDR */
	uint16_t	lsnat;		/* LSNAT 服务器计数 */
	char		description[NG_NAT_DESC_LENGTH];
};
struct ng_nat_list_redirects {
	uint32_t		total_count;
	struct ng_nat_listrdrs_entry redirects[];
};
#define NG_NAT_REDIRPROTO_ADDR	(IPPROTO_MAX + 3)
```

```sh
struct ng_nat_libalias_info {
	uint32_t	icmpLinkCount;
	uint32_t	udpLinkCount;
	uint32_t	tcpLinkCount;
	uint32_t	sctpLinkCount;
	uint32_t	pptpLinkCount;
	uint32_t	protoLinkCount;
	uint32_t	fragmentIdLinkCount;
	uint32_t	fragmentPtrLinkCount;
	uint32_t	sockCount;
};
```

`#include <net/bpf.h>`

**`NGM_NAT_SET_IPADDR`** (`setaliasaddr`) 为节点配置别名地址。在两个钩子都已连接且别名地址已配置后，节点即可进行别名操作。

**`NGM_NAT_SET_MODE`** (`setmode`) 使用提供的 `struct ng_nat_mode` 设置节点的操作模式。相应的 libalias 标志可通过将 `NG_NAT` 前缀替换为 `PKT_ALIAS` 找到。

**`NGM_NAT_SET_TARGET`** (`settarget`) 为节点配置目标地址。当与任何先前存在的别名链无关的传入数据包到达主机时，它将被发送到指定地址。

**`NGM_NAT_REDIRECT_PORT`** (`redirectport`) 将到达给定端口的传入连接重定向到另一主机和端口。必须提供以下 `struct ng_nat_redirect_port` 作为参数。重定向会分配一个唯一 ID，作为对此消息的响应返回，重定向信息会添加到静态重定向列表中，稍后可通过 `NGM_NAT_LIST_REDIRECTS` 消息检索。

**`NGM_NAT_REDIRECT_ADDR`** (`redirectaddr`) 将公共 IP 地址的流量重定向到本地网络上的机器。此功能称为*静态 NAT*。必须提供以下 `struct ng_nat_redirect_addr` 作为参数。此重定向的唯一 ID 作为对此消息的响应返回。

**`NGM_NAT_REDIRECT_PROTO`** (`redirectproto`) 将协议 `proto`（参见 [protocols(5)](../man5/protocols.5.md)）的传入 IP 数据包重定向到本地网络上的机器。必须提供以下 `struct ng_nat_redirect_proto` 作为参数。此重定向的唯一 ID 作为对此消息的响应返回。

**`NGM_NAT_REDIRECT_DYNAMIC`** (`redirectdynamic`) 将指定 ID 的重定向标记为动态，即它将仅服务于下一个连接，然后会自动从内部链路表中删除。只有完全指定的链路才能设为动态。具有此 ID 的重定向也会立即从用户可见的静态重定向列表中删除（可通过 `NGM_NAT_LIST_REDIRECTS` 消息访问）。

**`NGM_NAT_REDIRECT_DELETE`** (`redirectdelete`) 删除指定 ID 的重定向（当前活动连接不受影响）。

**`NGM_NAT_ADD_SERVER`** (`addserver`) 向池中添加另一台服务器。用于透明地卸载单个服务器上的网络负载并跨服务器池分发负载，也称为 *LSNAT*（RFC 2391）。必须提供以下 `struct ng_nat_add_server` 作为参数。首先，通过 `NGM_NAT_REDIRECT_PORT` 或 `NGM_NAT_REDIRECT_ADDR` 设置重定向。然后，使用该重定向的 ID 在多个 `NGM_NAT_ADD_SERVER` 消息中添加所需数量的服务器。对于由 `NGM_NAT_REDIRECT_ADDR` 创建的重定向，`port` 被忽略，可以是任何值。使用 `NGM_NAT_ADD_SERVER` 后，原始重定向参数 `local_addr` 和 `local_port` 也会被忽略（它们实际上被服务器池替换）。

**`NGM_NAT_LIST_REDIRECTS`** (`listredirects`) 以 `struct ng_nat_list_redirects` 形式返回已配置的静态重定向列表。返回的 `redirects` 数组条目以统一格式呈现所有重定向类型。仅当协议为 TCP 或 UDP 时端口才有意义，而*静态 NAT* 重定向（由 `NGM_NAT_REDIRECT_ADDR` 创建）通过 `proto` 设置为 `NG_NAT_REDIRPROTO_ADDR` 指示。如果 `lsnat` 服务器计数器大于零，则 `local_addr` 和 `local_port` 也无意义。

**`NGM_NAT_PROXY_RULE`** (`proxyrule`) 指定透明代理规则（必须以字符串作为参数提供）。详见 libalias(3)。

**`NGM_NAT_LIBALIAS_INFO`** (`libaliasinfo`) 以 `struct ng_nat_libalias_info` 形式返回 libalias(3) 实例的内部统计信息。如果 `nat` 无法从其 libalias(3) 实例检索某个计数器，相应字段返回 `UINT32_MAX`。

**`NGM_NAT_SET_DLT`** (`setdlt`) 设置 `in` 和 `out` 钩子上的数据链路类型。目前支持的类型有 `DLT_RAW`（原始 IP 数据报，无偏移应用，默认）和 `DLT_EN10MB`（以太网）。DLT_ 定义可在如果你想在 [ipfw(8)](../man8/ipfw.8.md) 级别工作，必须通过指定 `DLT_RAW` 使用无额外偏移。但如果将 `nat` 直接附加到网络接口并指定了 `EN10MB`，则会应用额外偏移以考虑链路层头部。在此模式下，`nat` 还会检查以太网头部中的相应类型字段，并传递任何非 IP 数据包的数据报。

**`NGM_NAT_GET_DLT`** (`getdlt`) 此控制消息返回 `in` 和 `out` 钩子的当前数据链路类型。

在所有重定向消息中，`local_addr` 和 `local_port` 分别表示内部网络中目标机器的地址和端口。如果 `alias_addr` 为零，则使用默认别名地址（由 `NGM_NAT_SET_IPADDR` 设置）。通过使用非零 `remote_addr` 和/或 `remote_port`，还可以限制连接仅从特定外部机器接受。每个重定向都分配一个 ID，稍后可用于单独操作重定向（例如移除）。此 ID 保证在节点关闭之前唯一（删除后不会重用），并在每次创建新重定向后返回给用户，或可在所有重定向的存储列表中找到。`description` 字段在传入和传出节点时保持不变，与 ID 一起提供了一种让多个实体以自动化方式并发操作重定向的方法。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在两个钩子都已断开时关闭。

## 实例

在以下示例中，数据包使用 [ng_ipfw(4)](ng_ipfw.4.md) 节点注入 `nat` 节点。

```sh
# 创建 NAT 节点
ngctl mkpeer ipfw: nat 60 out
ngctl name ipfw:60 nat
ngctl connect ipfw: nat: 61 in
ngctl msg nat: setaliasaddr x.y.35.8
# 将流量分流到 NAT 节点
ipfw add 300 netgraph 61 all from any to any in via fxp0
ipfw add 400 netgraph 60 all from any to any out via fxp0
# 让数据包在（解除）别名后继续
sysctl net.inet.ip.fw.one_pass=0
```

`nat` 节点可以插入图中 [ng_iface(4)](ng_iface.4.md) 节点之后。在以下示例中，我们对使用 HDLC 封装的串行线路执行伪装。

```sh
/usr/sbin/ngctl -f- <<-SEQ
	mkpeer cp0: cisco rawdata downstream
	name cp0:rawdata hdlc
	mkpeer hdlc: nat inet in
	name hdlc:inet nat
	mkpeer nat: iface out inet
	msg nat: setaliasaddr x.y.8.35
SEQ
ifconfig ng0 x.y.8.35 x.y.8.1
```

`nat` 节点也可以通过图中的 [ng_ether(4)](ng_ether.4.md) 节点直接附加到物理接口。在以下示例中，我们对连接到公共网络的以太网接口执行伪装。

```sh
ifconfig igb0 inet x.y.8.35 netmask 0xfffff000
route add default x.y.0.1
/usr/sbin/ngctl -f- <<-SEQ
        mkpeer igb0: nat lower in
        name igb0:lower igb0_NAT
        connect igb0: igb0_NAT: upper out
        msg igb0_NAT: setdlt 1
        msg igb0_NAT: setaliasaddr x.y.8.35
SEQ
```

## 参见

libalias(3), [ng_ipfw(4)](ng_ipfw.4.md), [natd(8)](../man8/natd.8.md), ng_ether(8), ngctl(8)

## 历史

`nat` 节点类型实现于 FreeBSD 6.0。

## 作者

Gleb Smirnoff <glebius@FreeBSD.org>
