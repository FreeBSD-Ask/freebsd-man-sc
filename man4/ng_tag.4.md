# ng_tag.4

`ng_tag` — mbuf 标签操控 netgraph 节点类型

## 名称

`ng_tag`

## 概要

`#include <netgraph/ng_tag.h>`

## 描述

`tag` 节点类型允许检查、剥离或向穿过 Netgraph 网络的数据应用 mbuf 数据包标签（见 [mbuf_tags(9)](../man9/mbuf_tags.9.md)）。mbuf 标签在 FreeBSD 内核网络子系统的许多部分都有使用，包括 [vlan(4)](vlan.4.md) 中描述的 VLAN 标签存储、[mac(9)](../man9/mac.9.md) 中描述的强制访问控制（MAC）标签、[ipsec(4)](ipsec.4.md) 中描述的 IPsec 策略信息，以及 [pf(4)](pf.4.md) 使用的数据包过滤标签。还应考虑设置或检查 [ipfw(8)](../man8/ipfw.8.md) 标签，这些标签也以 mbuf 标签形式实现。

每个节点允许任意数量的连接到任意命名的钩子。每个钩子关联一个标签（将在此钩子上传入的数据包所附加的所有标签列表中搜索该标签）、用于匹配数据包的目标钩子、用于不匹配数据包的目标钩子、将附加到通过此钩子离开节点的数据上的标签，以及各种统计计数器。

遍历传入数据包的标签列表以查找具有指定 `type` 和 `cookie` 值的标签。匹配时，如果指定的 `tag_len` 非零，则检查标签的 `tag_data` 是否与钩子结构中指定的相同。具有匹配标签的数据包被转发到“match”目标钩子，否则转发到“non-match”钩子。一个或两个目标钩子可以是空字符串，或可能不存在，在这种情况下数据包会被丢弃。

离开节点的数据包的标签列表会扩展一个在出站钩子结构中指定的新标签（可以通过在相应出站钩子的结构中指定零 `type` 和 `cookie` 值来避免附加新标签，从而完全不变地传递数据包）。此外，如果设置了 `strip` 标志，匹配后可以从传入数据包中剥离标签。这可用于简单的标签移除或标签替换，如果与出站匹配钩子上的标签添加结合使用。注意，新标签是无条件附加的，不检查标签列表中是否已存在此类标签（这由用户自行判断是否需要关注）。

新钩子初始配置为丢弃所有传入数据包（因为所有钩子名为空字符串；可以指定零值以将所有数据包转发到 non-match 钩子），并将所有出站数据包不加任何标签地转发。

通过节点的数据包的数据负载完全不变，所有操作仅影响标签列表。

## 钩子

此节点类型支持任意数量的具有任意名称的钩子。为允许内部优化，用户不应尝试使用指向尚不存在的钩子的结构来配置钩子。安全做法是先创建所有钩子，然后开始配置它们。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

```sh
struct ng_tag_hookin {
  char		  thisHook[NG_HOOKSIZ];     /* 钩子名 */
  char		  ifMatch[NG_HOOKSIZ];	    /* 匹配目标钩子 */
  char		  ifNotMatch[NG_HOOKSIZ];   /* 不匹配目标钩子 */
  uint8_t	  strip;		    /* 找到则剥离标签 */
  uint32_t	  tag_cookie;		    /* ABI/模块 ID */
  uint16_t	  tag_id;		    /* 标签 ID */
  uint16_t	  tag_len;		    /* 数据长度 */
  uint8_t	  tag_data[0];		    /* 标签数据 */
};
```

```sh
struct ng_tag_hookout {
  char		  thisHook[NG_HOOKSIZ];     /* 钩子名 */
  uint32_t	  tag_cookie;		    /* ABI/模块 ID */
  uint16_t	  tag_id;		    /* 标签 ID */
  uint16_t	  tag_len;		    /* 数据长度 */
  uint8_t	  tag_data[0];		    /* 标签数据 */
};
```

**`NGM_TAG_SET_HOOKIN`**（`sethookin`）此命令设置将在钩子上传入数据包的标签列表中搜索的标签值。必须提供以下结构作为参数：要更新的钩子在 `thisHook` 中指定。与指定 `tag_id`（类型）和 `tag_cookie` 对应的标签数据字节放在 `tag_data` 数组中；必须有 `tag_len` 个字节。匹配和不匹配的传入数据包分别从 `ifMatch` 和 `ifNotMatch` 命名的钩子送出。如果 `strip` 标志非零，则找到的标签会从数据包标签列表中删除。

**`NGM_TAG_GET_HOOKIN`**（`gethookin`）此命令以 ASCII 字符串参数（钩子名）获取对应的 `struct ng_tag_hookin`，如上所示。

**`NGM_TAG_SET_HOOKOUT`**（`sethookout`）此命令设置将应用于出站数据包的标签值。必须提供以下结构作为参数：要更新的钩子在 `thisHook` 中指定。其他变量的含义与上面所示的 `struct ng_tag_hookin` 基本相同，只是用于设置新标签中的值。

**`NGM_TAG_GET_HOOKOUT`**（`gethookout`）此命令以 ASCII 字符串参数（钩子名）获取对应的 `struct ng_tag_hookout`，如上所示。

**`NGM_TAG_GET_STATS`**（`getstats`）此命令以 ASCII 字符串参数（钩子名）返回与该钩子关联的统计信息，作为 `struct ng_tag_hookstat`。

**`NGM_TAG_CLR_STATS`**（`clrstats`）此命令以 ASCII 字符串参数（钩子名）清零与该钩子关联的统计信息。

**`NGM_TAG_GETCLR_STATS`**（`getclrstats`）此命令与 `NGM_TAG_GET_STATS` 相同，但同时会原子地清零统计信息。

*注意：* 统计计数器以及上述三个统计消息只有在代码以 `NG_TAG_DEBUG` 选项编译时才有效。原因是统计在实践中很少使用，但仍会为每个数据包消耗 CPU 周期。此外，由于线程之间缺乏同步（这非常昂贵），在 SMP 系统上甚至不准确。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在所有钩子均已断开时关闭。

## 实例

可以将 [ipfw(8)](../man8/ipfw.8.md) 标签与 [ng_bpf(4)](ng_bpf.4.md) 流量分析器结合使用来实现简单的 L7 过滤。下面的示例说明如何过滤 DirectConnect P2P 网络数据流量，由于它使用随机端口，无法通过常规手段完成。已知此类数据连接始终包含一个带有 6 字节负载字符串 "$Send|" 的 TCP 数据包。因此，使用 ipfw 的 `netgraph` 动作将所有 TCP 数据包分流到一个 [ng_bpf(4)](ng_bpf.4.md) 节点，该节点将检查指定的字符串并将不匹配的数据包返回给 [ipfw(8)](../man8/ipfw.8.md)。匹配的数据包传递给 `tag` 节点，该节点将设置标签并将它们传回 [ng_bpf(4)](ng_bpf.4.md) 节点上一个钩子，该钩子被编程为接受所有数据包并将它们传回 [ipfw(8)](../man8/ipfw.8.md)。将使用 [ng_bpf(4)](ng_bpf.4.md) 手册页中提供的脚本对节点进行编程。注意，从 [ipfw(8)](../man8/ipfw.8.md) 分流到 Netgraph 的数据包没有链路层头部，因此 [tcpdump(1)](../man1/tcpdump.1.md) 表达式中的偏移量必须相应调整。因此，入站钩子上的表达式为“`ether[40:2]=0x244c && ether[42:4]=0x6f636b20`”，而从 `tag` 出来的钩子上为空表达式以匹配所有数据包。

以下是用于创建和命名节点以便更易访问的 ngctl(8) 脚本：

```sh
/usr/sbin/ngctl -f- <<-SEQ
	mkpeer ipfw: bpf 41 ipfw
	name ipfw:41 dcbpf
	mkpeer dcbpf: tag matched th1
	name dcbpf:matched ngdc
SEQ
```

现在“`ngdc`”节点（类型为 `tag`）必须被编程为将“`th1`”钩子上接收的所有数据包回显，并附加 [ipfw(8)](../man8/ipfw.8.md) 标签 412。`tag_cookie` 的 `MTAG_IPFW` 值取自以下文件：

`#include <netinet/ip_fw.h>`

`tag_id` 的值为标签编号（412），标签长度为零：

```sh
ngctl msg ngdc: sethookin { thisHook=e"th1e" ifNotMatch=e"th1e" }
ngctl msg ngdc: sethookout { thisHook=e"th1e" e
  tag_cookie=1148380143 e
  tag_id=412 }
```

不要忘记使用上述表达式编程 [ng_bpf(4)](ng_bpf.4.md) 的“`ipfw`”钩子（见 [ng_bpf(4)](ng_bpf.4.md) 中执行此操作的脚本），并使用空表达式编程“`matched`”钩子：

```sh
ngctl msg dcbpf: setprogram { thisHook=e"matchede" ifMatch=e"ipfwe" e
  bpf_prog_len=1 bpf_prog=[ { code=6 k=8192 } ] }
```

完成 [netgraph(4)](netgraph.4.md) 节点后，必须添加 [ipfw(8)](../man8/ipfw.8.md) 规则以启用数据包流：

```sh
ipfw add 100 netgraph 41 tcp from any to any iplen 46
ipfw add 110 reset tcp from any to any tagged 412
```

注意：应通过设置相应的 [sysctl(8)](../man8/sysctl.8.md) 变量，确保数据包在 [netgraph(4)](netgraph.4.md) 内部处理后能够返回到 ipfw：

```sh
sysctl net.inet.ip.fw.one_pass=0
```

## 参见

[netgraph(4)](netgraph.4.md), [ng_bpf(4)](ng_bpf.4.md), [ng_ipfw(4)](ng_ipfw.4.md), [ipfw(8)](../man8/ipfw.8.md), ngctl(8), [mbuf_tags(9)](../man9/mbuf_tags.9.md)

## 历史

`tag` 节点类型实现于 FreeBSD 6.2。

## 作者

Vadim Goncharov <vadimnuclight@tpu.ru>

## 缺陷

对于操控任何带有数据负载（即 `tag_len` 非零的所有标签）的标签，应注意低层字节流上标签的不可移植的机器相关表示。或许这应由另一个程序完成，而非手动操作。
