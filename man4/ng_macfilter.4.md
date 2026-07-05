# ng_macfilter.4

`ng_macfilter` — 使用以太网 MAC 地址的数据包过滤 netgraph 节点

## 名称

`ng_macfilter`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_macfilter.h>`

## 描述

`macfilter` 允许根据发送方 MAC 地址将以太网数据包路由到不同的钩子。

此处理在流量从“ether”钩子通过 `macfilter` 流向某个传出钩子时执行。可以添加和移除传出钩子，并随意命名。默认情况下，存在一个名为 “default” 的钩子，用于 MAC 表中没有 MAC 地址的所有数据包。通过向 MAC 表添加 MAC 地址，来自此主机的流量可以定向到其他钩子输出。`macfilter` 会在 MAC 表中跟踪来自和发往此 MAC 地址的数据包数和字节数。

数据包不会以任何方式被修改。如果钩子未连接，数据包将被丢弃。

## 钩子

本节点类型默认有一个 `ether` 钩子，用于连接到 NIC 的 `lower` 钩子，以及一个 `default` 钩子，用于在表中找不到 MAC 地址时发送数据包。`macfilter` 最多支持 `NG_MACFILTER_UPPER_NUM` 个钩子连接到 NIC 的 upper 钩子。可以插入其他节点以提供额外的处理。所有传出流量可以通过使用 `ng_one2many` 合并回一个。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

```sh
struct ngm_macfilter_direct {
    u_char	ether[ETHER_ADDR_LEN];  	/* MAC 地址 */
    u_char	hookname[NG_HOOKSIZ];   	/* 上层钩子名称 */
};
```

```sh
struct ngm_macfilter_direct_hookid {
    u_char	ether[ETHER_ADDR_LEN];  	/* MAC 地址 */
    u_int16_t	hookid;		        	/* 上层钩子 hookid */
};
```

```sh
struct ngm_macfilter_mac {
    u_char	ether[ETHER_ADDR_LEN];  	/* MAC 地址 */
    u_int16_t	hookid;		        	/* 上层钩子 hookid */
    u_int64_t	packets_in;			/* 从下游进入的数据包数 */
    u_int64_t	bytes_in;			/* 从上游进入的字节数 */
    u_int64_t	packets_out;			/* 向下游出去的数据包数 */
    u_int64_t	bytes_out;			/* 向下游出去的字节数 */
};
struct ngm_macfilter_macs {
    u_int32_t   n;                              /* macs 中的条目数 */
    struct ngm_macfilter_mac macs[];            /* Macs 表 */
};
```

```sh
struct ngm_macfilter_hook {
    u_char	hookname[NG_HOOKSIZ];   	/* 上层钩子名称 */
    u_int16_t	hookid;		        	/* 上层钩子 hookid */
    u_int32_t   maccnt;                         /* 与钩子关联的 mac 地址数 */
};
```

**`NGM_MACFILTER_RESET`** (`reset`) 重置节点中的 MAC 表。

**`NGM_MACFILTER_DIRECT`** (`direct`) 接受以下参数结构：给定的以太网 MAC 地址将通过命名的钩子转发。

**`NGM_MACFILTER_DIRECT_HOOKID`** (`directi`) 接受以下参数结构：给定的以太网 MAC 地址将通过 ID 为 `hookid` 的钩子转发。

**`NGM_MACFILTER_GET_MACS`** (`getmacs`) 以以下结构返回节点中的 MAC 地址列表：

**`NGM_MACFILTER_GETCLR_MACS`** (`getclrmacs`) 同上，但同时原子性地清除表中的 `packets_in`、`bytes_in`、`packets_out` 和 `bytes_out` 字段。

**`NGM_MACFILTER_CLR_STATS`** (`clrmacs`) 将清除每个 MAC 地址的数据包和字节计数器。

**`NGM_MACFILTER_GET_HOOKS`** (`gethooks`) 将以以下结构数组的形式返回钩子及其 hookid 列表：

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在所有钩子都已断开时关闭。

## 实例

以下 netgraph 配置会对通过 “accepted” 钩子路由的每个数据包应用 [ipfw(8)](../man8/ipfw.8.md) 标记 42。图如下所示：

```sh
    /------<one>-[combiner]-<many1>--------\
<upper>               |                    <out>
  /                <many0>                    \
[em0]                 |                    [tagger]
                 <default>                   /
<lower>               |                     <in>
    ----<ether>-[macfilter]-<accepted>-----/
```

命令：

```sh
  ngctl mkpeer em0: macfilter lower ether
  ngctl name em0:lower macfilter
  # 将两个流都汇回 ether:upper
  ngctl mkpeer em0: one2many upper one
  ngctl name em0:upper recombiner
  # 将 macfilter:default 连接到 recombiner:many0
  ngctl connect macfilter: recombiner: default many0
  # 将 macfilter:accepted 连接到 tagger:in
  ngctl mkpeer macfilter: tag accepted in
  ngctl name macfilter:accepted tagger
  # 将 tagger:out 连接到 recombiner:many1
  ngctl connect tagger: recombiner: out many1
  # 将 tagger in -> out 流量的所有流量标记为 ipfw 标记 42
  ngctl msg tagger: sethookin '{ thisHook="in" ifNotMatch="out" }'
  ngctl msg tagger: sethookout '{ thisHook="out" tag_cookie=1148380143 tag_id=42 }'
  # 将流量从 ether:upper / combiner:one 经 combiner:many0 传递到
  # macfilter:default，再到 ether:lower
  ngctl msg recombiner: setconfig '{ xmitAlg=3 failAlg=1 enabledLinks=[ 1 1 ] }'
```

*注意：* tag_cookie 1148380143 是从 **`/usr/include/netinet/ip_var.h`** 中的 `MTAG_IPFW` 检索的。

以下命令可用于添加通过 `macfilter:accepted` 输出的 MAC 地址：

```sh
  ngctl msg macfilter: direct '{ hookname="known" ether=08:00:27:92:eb:aa }'
```

以下命令可用于检索数据包和字节计数器：

```sh
  ngctl msg macfilter: getmacs
```

它将返回 MAC 表的内容：

```sh
  Rec'd response "getmacs" (4) from "[54]:":
  Args:	{ n=1 macs=[ { ether=08:00:27:92:eb:aa hookid=1 packets_in=3571 bytes_in=592631 packets_out=3437 bytes_out=777142 } ] }
```

## 参见

[divert(4)](divert.4.md), ipfw(4), [netgraph(4)](netgraph.4.md), [ng_ether(4)](ng_ether.4.md), [ng_one2many(4)](ng_one2many.4.md), [ng_tag(4)](ng_tag.4.md), ngctl(8)

## 作者

此代码的原始版本由 Pekka Nikander 编写，随后由 Nick Hibma <n_hibma@FreeBSD.org> 进行了大量修改。

## 缺陷

未知。
