# ng_etf.4

`ng_etf` — Ethertype 过滤 netgraph 节点类型

## 名称

`ng_etf`

## 概要

`#include <netgraph.h>`

`#include <netgraph/ng_etf.h>`

## 描述

`etf` 节点类型根据以太网头部中的 ethertype（假定位于数据的前 14 字节）在钩子之间多路复用和过滤数据。传入以太网帧在*downstream*钩子上被接受，如果 ethertype 匹配节点已配置过滤的值，则数据包从配置该值时标识的钩子转发出去。如果不匹配任何已配置值，则传递给*nomatch*钩子。如果*nomatch*钩子未连接，则数据包被丢弃。

反方向（朝向*downstream*钩子）传输的数据包也会被检查和过滤。如果数据包的 ethertype 匹配节点配置的某个值，则它必须从为该值配置的钩子上到达，否则将被丢弃。控制消息配置之外的 ethertype 值必须通过*nomatch*钩子到达。

## 钩子

此节点类型支持以下钩子：

***downstream*** 通常此钩子会使用 *lower* 钩子连接到 [ng_ether(4)](ng_ether.4.md) 节点。

***nomatch*** 通常此钩子也会使用 *upper* 钩子连接到 [ng_ether(4)](ng_ether.4.md) 类型节点。

**<*任何**合法名称*> 任何其他钩子名都将被接受，并可用作 ethertype 的匹配目标。通常此钩子会附加到需要并生成具有特定 ethertype 集合的数据包的协议处理节点。

## 控制消息

此节点类型支持通用控制消息，外加以下消息：

```sh
struct ng_etffilter {
    char	matchhook[NG_HOOKSIZ];	/* 钩子名 */
    uint16_t	ethertype;		/* 此 ethertype 到此钩子 */
};
```

**`NGM_ETF_GET_STATUS`** (`getstatus`) 此命令返回包含数据包计数节点统计信息的 `struct ng_etfstat`。

**`NGM_ETF_SET_FILTER`** (`setfilter`) 将新的 ethertype 过滤器设置到节点中，并指定该类型数据包应使用的进出钩子。钩子和 ethertype 在 `struct ng_etffilter` 类型的结构中指定：

## 实例

使用 ngctl(8) 可按如下方式从命令行设置过滤器：

```sh
#!/bin/sh
ETHER_IF=fxp0
MATCH1=0x834
MATCH2=0x835
cat <<DONE >/tmp/xwert
# 创建新的 ethertype 过滤器并附加到以太网 lower 钩子。
# 首先移除上次的残留部分。
shutdown ${ETHER_IF}:lower
mkpeer ${ETHER_IF}: etf lower downstream
# 给它命名以便轻松引用。
name ${ETHER_IF}:lower etf
# 将 nomatch 钩子连接到同一接口的上部。
# 所有不匹配的数据包将像过滤器不存在一样处理。
connect ${ETHER_IF}: etf: upper nomatch
DONE
ngctl -f /tmp/xwert
# 设置钩子以捕获数据包并显示它们。
echo "Unrecognised packets:"
nghook -a etf: newproto &
# 将两个随机 ethertype 过滤到该钩子。
ngctl 'msg etf: setfilter { matchhook="newproto" ethertype=${MATCH1} }
ngctl 'msg etf: setfilter { matchhook="newproto" ethertype=${MATCH2} }
```

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或当所有钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_ether(4)](ng_ether.4.md), ngctl(8), nghook(8)

## 历史

`etf` 节点类型实现于 FreeBSD 5.0。

## 作者

Julian Elischer <julian@FreeBSD.org>
