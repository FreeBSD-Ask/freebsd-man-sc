# ng_bpf(4)

`ng_bpf` — Berkeley 数据包过滤器 netgraph 节点类型

## 名称

`ng_bpf`

## 概要

`#include <sys/types.h>`

`#include <net/bpf.h>`

`#include <netgraph.h>`

`#include <netgraph/ng_bpf.h>`

## 描述

`bpf` 节点类型允许将 Berkeley 数据包过滤器（参见 [bpf(4)](bpf.4.md)）应用于通过 Netgraph 网络传输的数据。每个节点允许任意数量的连接到任意命名的钩子。每个钩子关联一个 [bpf(4)](bpf.4.md) 过滤器程序（仅应用于传入数据）、一个匹配数据包的目标钩子、一个不匹配数据包的目标钩子以及各种统计计数器。

[bpf(4)](bpf.4.md) 程序返回一个无符号整数，通常解释为要返回的数据包前缀的长度。在此节点类型的上下文中，返回零被视为不匹配，在这种情况下，整个数据包从非匹配目标钩子传递出去。返回大于零的值会导致数据包被截断为该长度并从匹配目标钩子传递出去。一个或两个目标钩子都可以是空字符串或不存在，在这种情况下数据包被丢弃。

新钩子初始配置为丢弃所有数据包。可使用 `NGM_BPF_SET_PROGRAM` 控制消息安装新的过滤程序。

## 钩子

此节点类型支持任意数量具有任意名称的钩子。

## 控制消息

此节点类型支持通用控制消息，外加以下消息：

```sh
struct ng_bpf_hookprog {
  char            thisHook[NG_HOOKSIZ];     /* 钩子名 */
  char            ifMatch[NG_HOOKSIZ];      /* 匹配目标钩子 */
  char            ifNotMatch[NG_HOOKSIZ];   /* 不匹配目标钩子 */
  int32_t         bpf_prog_len;             /* 程序中的指令数 */
  struct bpf_insn bpf_prog[];               /* bpf 程序 */
};
```

**`NGM_BPF_SET_PROGRAM`** (`setprogram`) 此命令设置将应用于钩子上传入数据的过滤程序。必须提供以下结构作为参数：要更新的钩子在 `thisHook` 中指定。BPF 程序是 `bpf_prog` 数组中的指令序列；必须有 `bpf_prog_len` 条指令。匹配和不匹配的传入数据包分别从 `ifMatch` 和 `ifNotMatch` 命名的钩子传递出去。程序必须是有效的 [bpf(4)](bpf.4.md) 程序，否则返回 Er EINVAL。

**`NGM_BPF_GET_PROGRAM`** (`getprogram`) 此命令接受一个 ASCII 字符串参数（钩子名），并返回相应的 `struct ng_bpf_hookprog`（如上所示）。

**`NGM_BPF_GET_STATS`** (`getstats`) 此命令接受一个 ASCII 字符串参数（钩子名），并返回与该钩子关联的统计信息，作为 `struct ng_bpf_hookstat`。

**`NGM_BPF_CLR_STATS`** (`clrstats`) 此命令接受一个 ASCII 字符串参数（钩子名），并清除与该钩子关联的统计信息。

**`NGM_BPF_GETCLR_STATS`** (`getclrstats`) 此命令与 `NGM_BPF_GET_STATS` 相同，区别在于统计信息也会被原子性地清除。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或当所有钩子都已断开时关闭。

## 实例

可以使用命令行配置节点，使用 [tcpdump(1)](../man1/tcpdump.1.md) 生成原始 BPF 指令，然后将其转换为 `NGM_BPF_SET_PROGRAM` 控制消息的 ASCII 形式，如下所示：

```sh
#!/bin/sh
PATTERN="tcp dst port 80"
NODEPATH="my_node:"
INHOOK="hook1"
MATCHHOOK="hook2"
NOTMATCHHOOK="hook3"
BPFPROG=$( tcpdump -s 8192 -p -ddd ${PATTERN} | \
           ( read len ; \
             echo -n "bpf_prog_len=$len " ; \
             echo -n "bpf_prog=[" ; \
             while read code jt jf k ; do \
                 echo -n " { code=$code jt=$jt jf=$jf k=$k }" ; \
             done ; \
             echo " ]" ) )
ngctl msg ${NODEPATH} setprogram { thisHook=\"${INHOOK}\" \
  ifMatch=\"${MATCHHOOK}\" \
  ifNotMatch=\"${NOTMATCHHOOK}\" \
  ${BPFPROG} }
```

基于前面的示例，可以通过仅允许具有预期以太网和 IP 地址的流量，来防止 jail（或 VM）进行欺骗：

```sh
#!/bin/sh
NODEPATH="my_node:"
JAIL_MAC="0a:00:de:ad:be:ef"
JAIL_IP="128.66.1.42"
JAIL_HOOK="jail"
HOST_HOOK="host"
DEBUG_HOOK="nomatch"
bpf_prog() {
    local PATTERN=$1
    tcpdump -s 8192 -p -ddd ${PATTERN} | (
        read len
        echo -n "bpf_prog_len=$len "
        echo -n "bpf_prog=["
        while read code jt jf k ; do
            echo -n " { code=$code jt=$jt jf=$jf k=$k }"
        done
        echo " ]"
    )
}
# 防止 jail 进行欺骗（过滤来自 jail 的数据包）
ngctl msg ${NODEPATH} setprogram {                        \
    thisHook=\"${JAIL_HOOK}\"                             \
    ifMatch=\"${HOST_HOOK}\"                              \
    ifNotMatch=\"${DEBUG_HOOK}\"                          \
    $(bpf_prog "ether src ${JAIL_MAC} && src ${JAIL_IP}") \
}
# 防止 jail 接收欺骗数据包（过滤来自
# 主机的数据包）
ngctl msg ${NODEPATH} setprogram {                        \
    thisHook=\"${HOST_HOOK}\"                             \
    ifMatch=\"${JAIL_HOOK}\"                              \
    ifNotMatch=\"${DEBUG_HOOK}\"                          \
    $(bpf_prog "ether dst ${JAIL_MAC} && dst ${JAIL_IP}") \
}
```

## 参见

[bpf(4)](bpf.4.md), [netgraph(4)](netgraph.4.md), ngctl(8)

## 历史

`bpf` 节点类型实现于 FreeBSD 4.0。

## 作者

Archie Cobbs <archie@FreeBSD.org>

## 缺陷

当构建为可加载内核模块时，此模块包含文件 `net/bpf_filter.c`。虽然如果 `net/bpf_filter.c` 已存在于内核中，加载模块应该失败，但目前不会，且文件的重复副本不会相互干扰。然而，这在未来可能会改变。
