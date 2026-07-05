# ng_patch.4

`ng_patch` — 简易 mbuf 数据修改 netgraph 节点类型

## 名称

`ng_patch`

## 概要

`#include <netgraph/ng_patch.h>`

## 描述

`patch` 节点对穿过它的数据包执行数据修改。修改操作仅限于对 8、16、32 或 64 位无符号整数执行 C 语言运算的子集，包括：赋新值（=）、加法（+=）、减法（-=）、乘法（\*=）、除法（/=）、取负（=-）、按位与（&=）、按位或（|=）、按位异或（^=）、左移（<<=）、右移（>>=）。取负操作是个例外：整数被视为有符号数，且不使用第二操作数（即 `value`）。如果有多个修改操作，它们会按用户指定的顺序依次应用于数据包。数据包的数据负载被视为字节数组，零偏移对应于数据包头的第一个字节，而从 `offset` 开始、长度为 `length` 字节的字段被视为一个网络字节序的整数。在配置时还可选择性地请求一个附加偏移量，以应对不同的数据包类型。

## 钩子

此节点类型有两个钩子：

**`in`** 在此钩子上接收的数据包将按配置中指定的规则进行修改，然后转发到 `out` 钩子（如果存在）。否则，它们会被反射回 `in` 钩子。

**`out`** 在此钩子上接收的数据包将被原样转发到 `in` 钩子。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

`#include <net/bpf.h>`

```sh
struct ng_patch_op {
	uint32_t	offset;
	uint16_t	length; /* 1,2,4 或 8 字节 */
	uint16_t	mode;
	uint64_t	value;
};
/* 修改模式 */
#define NG_PATCH_MODE_SET	1
#define NG_PATCH_MODE_ADD	2
#define NG_PATCH_MODE_SUB	3
#define NG_PATCH_MODE_MUL	4
#define NG_PATCH_MODE_DIV	5
#define NG_PATCH_MODE_NEG	6
#define NG_PATCH_MODE_AND	7
#define NG_PATCH_MODE_OR	8
#define NG_PATCH_MODE_XOR	9
#define NG_PATCH_MODE_SHL	10
#define NG_PATCH_MODE_SHR	11
struct ng_patch_config {
	uint32_t	count;
	uint32_t	csum_flags;
	uint32_t	relative_offset;
	struct ng_patch_op ops[];
};
```

**`NGM_PATCH_SETDLT`**（`setdlt`）设置 `in` 钩子上的数据链路类型（用于辅助计算相对偏移）。当前支持的类型包括 `DLT_RAW`（原始 IP 数据报，不应用附加偏移，默认值）和 `DLT_EN10MB`（以太网）。DLT_ 定义可在以下文件中找到：如果你想在链路层头部上操作，必须通过指定 `DLT_RAW` 来不使用附加偏移。如果指定了 `EN10MB`，则可选的附加偏移会将以太网头部以及存在的 QinQ 头部计算在内。

**`NGM_PATCH_GETDLT`**（`getdlt`）此控制消息返回 `in` 钩子的数据链路类型。

**`NGM_PATCH_SETCONFIG`**（`setconfig`）此命令设置将应用于钩子上传入数据的修改操作序列。必须以下面的 `struct ng_patch_config` 作为参数：`csum_flags` 可以设置为 CSUM_IP、CSUM_TCP、CSUM_SCTP 和 CSUM_UDP 的任意组合（其他值将被忽略），用于指示 IP 协议栈在输出接口上传输数据包前重新计算相应的校验和。`patch` 节点本身不进行任何校验和修正。默认情况下，`ng_patch_op` 结构中的 `offset` 值从零开始计算（即数据包头的第一个字节）。如果在配置时启用了 `relative_offset`（设置为 1），则操作会基于数据链路类型将一个附加量添加到偏移值上。

**`NGM_PATCH_GETCONFIG`**（`getconfig`）此控制消息以 `struct ng_patch_config` 的形式返回当前的修改操作集合。

**`NGM_PATCH_GET_STATS`**（`getstats`）以 `struct ng_patch_stats` 的形式返回节点统计信息。

**`NGM_PATCH_CLR_STATS`**（`clrstats`）清零节点统计信息。

**`NGM_PATCH_GETCLR_STATS`**（`getclrstats`）此命令与 `NGM_PATCH_GET_STATS` 相同，但同时会原子地清零统计信息。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在所有钩子均已断开时关闭。

## 实例

`patch` 节点最初用于修改 IP 数据包中的 TTL 和 TOS/DSCP 字段。举例来说，假设你有两条相邻的简易链路通往远程网络（例如卫星），那么在两者之间过期的数据包将产生不需要的 ICMP 回复，而这些回复必须前进而非返回。因此，你需要将进入链路的每个数据包的 TTL 提升 2，以确保 TTL 在那里不会变为零。为此，你可以设置一条 [ipfw(8)](../man8/ipfw.8.md) 规则，使用 `netgraph` 动作将前往简易链路的数据包注入到 patch 节点中，使用如下 ngctl(8) 脚本：

```sh
/usr/sbin/ngctl -f- <<-SEQ
	mkpeer ipfw: patch 200 in
	name ipfw:200 ttl_add
	msg ttl_add: setconfig { count=1 csum_flags=1 ops=[	e
		{ mode=2 value=3 length=1 offset=8 } ] }
SEQ
/sbin/ipfw add 150 netgraph 200 ip from any to simplex.remote.net
```

此处名为“`ttl_add`”的 `patch` 类型节点被配置为对单字节 TTL 字段（即 IP 数据包头的第 9 个字节）加上（模式 `NG_PATCH_MODE_ADD`）`value` 值 3。

另一个示例是对数据包 TOS 字段进行两次连续修改：假设你需要清除 `IPTOS_THROUGHPUT` 位并设置 `IPTOS_MINCOST` 位。可以这样做：

```sh
/usr/sbin/ngctl -f- <<-SEQ
	mkpeer ipfw: patch 300 in
	name ipfw:300 tos_chg
	msg tos_chg: setconfig { count=2 csum_flags=1 ops=[	e
		{ mode=7 value=0xf7 length=1 offset=1 }		e
		{ mode=8 value=0x02 length=1 offset=1 } ] }
SEQ
/sbin/ipfw add 160 netgraph 300 ip from any to any not dst-port 80
```

此处首先执行 `NG_PATCH_MODE_AND` 清除第四位，然后执行 `NG_PATCH_MODE_OR` 设置第三位。

在以上两个示例中，`csum_flags` 字段表示在传输前应重新计算 IP 校验和（但不包括 TCP 或 UDP 校验和）。

注意：应通过设置相应的 [sysctl(8)](../man8/sysctl.8.md) 变量，确保数据包在 [netgraph(4)](netgraph.4.md) 内部处理后能够返回到 ipfw：

```sh
sysctl net.inet.ip.fw.one_pass=0
```

## 参见

[netgraph(4)](netgraph.4.md), [ng_ipfw(4)](ng_ipfw.4.md), ngctl(8)

## 历史

`patch` 节点类型实现于 FreeBSD 8.1。

## 作者

Maxim Ignatenko <gelraen.ua@gmail.com>.

相对偏移代码由 DMitry Vagin 编写

本手册页由 Vadim Goncharov <vadimnuclight@tpu.ru> 编写。

## 缺陷

该节点会盲目地尝试对每个数据包应用每项 patching 操作（偏移大于数据包长度的除外），因此请务必仅向其提供正确的数据包（例如，本应作用于 IP 头部的字节如果被作用于 ARP 数据包，可能会损坏数据包并导致你的机器在网络中不可达）。

*!!! 警告 !!!*

IP 协议栈的输出路径假定数据包中的字段和长度均正确——将其更改为错误的值可能导致不可预测的后果，包括内核崩溃。
