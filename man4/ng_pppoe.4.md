# ng_pppoe(4)

`ng_pppoe` — RFC 2516 PPPoE 协议 netgraph 节点类型

## 名称

`ng_pppoe`

## 概要

`#include <sys/types.h>`

`#include <net/ethernet.h>`

`#include <netgraph.h>`

`#include <netgraph/ng_pppoe.h>`

## 描述

`pppoe` 节点类型执行 PPPoE 协议。它与以太网框架的 [netgraph(4)](netgraph.4.md) 扩展结合使用，将 Ethernet 数据包从 PPP 代理（未指定）分流和注入到 PPP 代理。

`NGM_PPPOE_GET_STATUS` 控制消息可在任何时候用于查询 PPPoE 模块的当前状态。当前可用的统计信息仅有输入和输出的总数据包计数。此节点尚不支持 `NGM_TEXT_STATUS` 控制消息。

## 钩子

此节点类型支持以下钩子：

**`ethernet`** 通常应连接到 [ng_ether(4)](ng_ether.4.md) 节点的钩子。一旦连接，`pppoe` 会通过此钩子向下发送消息以确定底层节点的以太网地址。获得的地址将被存储并用于出站数据报。

**`debug`** 目前无用途。

**`[unspecified]`** 任何其他名称都被假定为将连接到 PPP 客户端代理或 PPP 服务器代理的会话钩子。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

```sh
struct ngpppoestat {
    u_int   packets_in;     /* 从以太网进入的数据包 */
    u_int   packets_out;    /* 发往以太网的数据包 */
};
```

```sh
"remote-acmy-host|my-isp"
```

**`NGM_PPPOE_GET_STATUS`** 此命令以 `struct ngpppoestat` 形式返回状态信息：

**`NGM_TEXT_STATUS`** 此通用消息返回节点状态的可读版本。（尚未实现）

**`NGM_PPPOE_CONNECT`**（`pppoe_connect`）告知指定的新建钩子其会话应作为客户端进入状态机。该钩子必须是新建的，且可给定服务名作为参数。可以指定零长度服务名，这在某些 DSL 设置中很常见。可以使用 "" `[AC-Name\][Host-Uniq|]Service-Name` 语法请求连接到特定的访问集中器，和/或设置某些互联网提供商要求的特定 Host-Uniq 标签。要设置二进制 Host-Uniq，必须将其编码为十六进制小写字符串并以 "" `0x` 为前缀，例如 "" `0x6d792d746167` 等价于 "" `my-tag`。会话请求包将以广播方式发送到以太网上。此命令使用下面所示的 `ngpppoe_init_data` 结构。例如，此 init data 参数可用于连接到 "" `my-isp` 服务并使用 "" `my-host` uniq 标签，仅接受 "" `remote-ac` 作为访问集中器：

**`NGM_PPPOE_LISTEN`**（`pppoe_listen`）告知指定的新建钩子其会话应作为服务器监听者进入状态机。所给参数是要监听的服务名。零长度服务名将匹配所有服务请求。匹配的服务请求包将被原样传递回负责启动该服务的进程。然后该进程可以检查它并将其传递给为响应请求而启动的会话。此命令使用下面所示的 `ngpppoe_init_data` 结构。

**`NGM_PPPOE_OFFER`**（`pppoe_offer`）告知指定的新建钩子其会话应作为服务器进入状态机。所给参数是要提供的服务名。零长度服务名是合法的。状态机将进入一个状态，在该状态下它将等待请求包从启动服务器转发给它，而启动服务器很可能从 LISTEN 模式钩子（见上文）收到该请求包。这是为了使嵌入在原始会话请求包中的会话所需信息对最终响应请求的状态机可用。当收到会话请求包时，会话协商将继续进行。此命令使用下面所示的 `ngpppoe_init_data` 结构。

以上三个命令使用共同的数据结构：

```sh
struct ngpppoe_init_data {
    char       hook[NG_HOOKSIZ];       /* 要监听的钩子 */
    uint16_t   data_len;               /* 服务名长度 */
    char       data[0];                /* init data 放置于此 */
};
```

**`NGM_PPPOE_SUCCESS`**（`pppoe_success`）此命令发送给以上述消息之一启动此会话的节点，并报告状态变化。此消息报告会话协商成功。它使用下面所示的结构，并回报与成功会话对应的钩子名。

**`NGM_PPPOE_FAIL`**（`pppoe_fail`）此命令发送给以上述消息之一启动此会话的节点，并报告状态变化。此消息报告会话协商失败。它使用下面所示的结构，并回报与失败会话对应的钩子名。该钩子很可能在发送此消息后立即被移除。

**`NGM_PPPOE_CLOSE`**（`pppoe_close`）此命令发送给以上述消息之一启动此会话的节点，并报告状态变化。此消息报告关闭会话的请求。它使用下面所示的结构，并回报与已关闭会话对应的钩子名。该钩子很可能在发送此消息后立即被移除。目前此消息尚未使用，关闭时将收到 `NGM_PPPOE_FAIL` 消息。

**`NGM_PPPOE_ACNAME`** 此命令发送给以上述消息之一启动此会话的节点，并报告访问集中器名称。

以上四个命令使用共同的数据结构：

```sh
struct ngpppoe_sts {
    char    hook[NG_HOOKSIZ];
};
```

**"standard"** 节点按 RFC 2516 操作。

**"3Com"** 当 `pppoe` 作为 PPPoE 客户端时，它发起会话时将数据包封装到不正确的 3Com ethertype 中。此兼容性选项不影响服务器模式。在服务器模式下，`pppoe` 同时支持两种模式，具体取决于客户端连接时使用的 ethertype。

**"D-Link"** 当 `pppoe` 作为仅服务特定 Service-Name 的 PPPoE 服务器时，它将响应带空 Service-Name 标签的 PADI 请求，返回节点上所有可用的 Service-Name。当仅服务特定 Service-Name 时，此选项对于与作为客户端的 D-Link DI-614+ 和 DI-624+ SOHO 路由器兼容是必要的。此兼容性选项不影响客户端模式。

```sh
ngctl msg fxp0:orphans pppoe_setmode '"3Com"'
```

```sh
struct ngpppoe_maxp {
    char     hook[NG_HOOKSIZ];
    uint16_t data;
};
```

```sh
ngctl msg fxp0:orphans send_hurl '{ hook="myHook" data="http://example.net/cpe" }'
```

```sh
ngctl msg fxp0:orphans send_motm '{ hook="myHook" data="Welcome aboard" }'
```

**`NGM_PPPOE_GETMODE`**（`pppoe_getmode`）此命令以字符串形式返回节点的当前兼容性模式。此消息的 ASCII 形式为 "" `pppoe_getmode`。可以返回以下关键字：

**`NGM_PPPOE_SETMODE`**（`pppoe_setmode`）将节点配置为指定模式。需要字符串参数。此命令理解 `NGM_PPPOE_GETMODE` 命令返回的相同关键字。此消息的 ASCII 形式为 "" `pppoe_setmode`。例如，以下命令将配置节点以下一次以专有 3Com 模式发起会话：

**`NGM_PPPOE_SETENADDR`**（`setenaddr`）设置出站数据报的节点以太网地址。当节点未能从其对端在 `ethernet` 钩子上获得以太网地址，或用户希望用另一个地址覆盖此地址时，此消息很重要。此消息的 ASCII 形式为 "" `setenaddr`。

**`NGM_PPPOE_SETMAXP`**（`setmaxp`）按 RFC 4638 描述设置节点的 PPP-Max-Payload 值。此消息仅适用于客户端配置。此消息的 ASCII 形式为 "" `setmaxp`。返回给客户端的数据结构为：

**`NGM_PPPOE_SEND_HURL`**（`send_hurl`）告知具有活动会话的指定钩子发送带 HURL 标签的 PADM 消息。参数为要传递给客户端的 URL：

**`NGM_PPPOE_SEND_MOTM`**（`send_motm`）告知具有活动会话的指定钩子发送带 MOTM 标签的 PADM 消息。参数为要传递给客户端的消息：

以上两个命令使用上文所述的相同 ngpppoe_init_data 结构。

**`NGM_PPPOE_HURL`** 此命令在收到带 HURL 标签的 PADM 消息时发送给启动此会话的节点，包含一个 URL，主机可将其传递给 Web 浏览器以呈现给用户。

**`NGM_PPPOE_MOTM`** 此命令在收到带 MOTM 标签的 PADM 消息时发送给启动此会话的节点，包含一条"分钟消息"（Message Of The Minute），主机可将其显示给用户。

以上两个命令使用共同的数据结构：

```sh
struct ngpppoe_padm {
    char    msg[PPPOE_PADM_VALUE_SIZE];
};
```

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息、所有会话均已断开或 `ethernet` 钩子被断开时关闭。

## SYSCTL 变量

节点可以使用以下 [sysctl(8)](../man8/sysctl.8.md) 变量将传输的 LCP 以太网数据包（协议 0xc021）以 3 位优先级代码点（PCP）标记，对应 IEEE 802.1p 服务类别。

**`net.graph.pppoe.lcp_pcp: 0..7 (默认: 0)`** 将其设置为非零值以供父网络接口驱动（如 [vlan(4)](vlan.4.md)）使用。

## 实例

以下代码使用 `libnetgraph` 设置一个 `pppoe` 节点，并将其同时连接到套接字节点和以太网节点。它能处理 `pppoe` 节点已附加到以太网的情况。然后启动客户端会话。

```sh
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <sysexits.h>
#include <errno.h>
#include <err.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/select.h>
#include <net/ethernet.h>
#include <netgraph.h>
#include <netgraph/ng_ether.h>
#include <netgraph/ng_pppoe.h>
#include <netgraph/ng_socket.h>
static int setup(char *ethername, char *service, char *sessname,
				int *dfd, int *cfd);
int
main()
{
	int  fd1, fd2;
	setup("xl0", NULL, "fred", &fd1, &fd2);
	sleep (30);
}
static int
setup(char *ethername, char *service, char *sessname,
			int *dfd, int *cfd)
{
	struct ngm_connect ngc;	/* connect */
	struct ngm_mkpeer mkp;	/* mkpeer */
	/******** nodeinfo 相关 **********/
	u_char          rbuf[2 * 1024];
	struct ng_mesg *const resp = (struct ng_mesg *) rbuf;
	struct hooklist *const hlist
			= (struct hooklist *) resp->data;
	struct nodeinfo *const ninfo = &hlist->nodeinfo;
	int             ch, no_hooks = 0;
	struct linkinfo *link;
	struct nodeinfo *peer;
	/****连接 PPPoE 会话的消息*****/
	struct {
		struct ngpppoe_init_data idata;
		char            service[100];
	}               message;
	/********跟踪我们的小图 ********/
	char            path[100];
	char            source_ID[NG_NODESIZ];
	char            pppoe_node_name[100];
	int             k;
	/*
	 * 创建数据和控制套接字
	 */
	if (NgMkSockNode(NULL, cfd, dfd) < 0) {
		return (errno);
	}
	/*
	 * 通过请求其查询信息来查找所请求名称的 ether 节点
	 */
	if (strlen(ethername) > 16)
		return (EINVAL);
	sprintf(path, "%s:", ethername);
	if (NgSendMsg(*cfd, path, NGM_GENERIC_COOKIE,
		      NGM_LISTHOOKS, NULL, 0) < 0) {
		return (errno);
	}
	/*
	 * 命令已被接受，因此它存在。等待回复（几乎肯定已经在等待）。
	 */
	if (NgRecvMsg(*cfd, resp, sizeof(rbuf), NULL) < 0) {
		return (errno);
	}
	/**
	 * 以下关于该节点的信息可用：
	 * ninfo->name		(字符串)
	 * ninfo->type		(字符串)
	 * ninfo->id		(uint32_t)
	 * ninfo->hooks		(uint32_t) (钩子计数)
	 * 检查它是否是正确的类型。并获取其 ID 供稍后 mkpeer 使用。
	 */
	if (strncmp(ninfo->type, NG_ETHER_NODE_TYPE,
		    strlen(NG_ETHER_NODE_TYPE)) != 0) {
		return (EPROTOTYPE);
	}
	sprintf(source_ID, "[%08x]:", ninfo->id);
	/*
	 * 查找已附加的钩子。
	 */
	for (k = 0; k < ninfo->hooks; k++) {
		/**
		 * 以下关于每个钩子的信息可用。
		 * link->ourhook	(字符串)
		 * link->peerhook	(字符串)
		 * peer->name		(字符串)
		 * peer->type		(字符串)
		 * peer->id		(uint32_t)
		 * peer->hooks		(uint32_t)
		 */
		link = &hlist->link[k];
		peer = &hlist->link[k].nodeinfo;
		/* 忽略 debug 钩子 */
		if (strcmp("debug", link->ourhook) == 0)
			continue;
		/* 如果 orphans 钩子已附加，使用它 */
		if (strcmp(NG_ETHER_HOOK_ORPHAN,
		    link->ourhook) == 0) {
			break;
		}
		/* 另一个选项是 'divert' 钩子 */
		if (strcmp("NG_ETHER_HOOK_DIVERT",
		    link->ourhook) == 0) {
			break;
		}
	}
	/*
	 * 查看是否在那里找到了钩子。
	 */
	if (k < ninfo->hooks) {
		if (strcmp(peer->type, NG_PPPOE_NODE_TYPE) == 0) {
			/*
			 * 如果它是 PPPoE 类型，我们跳过自建，
			 * 而是继续使用现有的。
			 */
			sprintf(pppoe_node_name, "[%08x]:", peer->id);
		} else {
			/*
			 * 已经有人占用了数据，返回错误。
			 * 总有一天我们会尝试菊花链式连接..
			 */
			return (EBUSY);
		}
	} else {
		/*
		 * 尝试对节点 "ID" 在钩子 NG_ETHER_HOOK_ORPHAN 上
		 * 创建 PPPoE 类型节点。
		 */
		snprintf(mkp.type, sizeof(mkp.type),
			 "%s", NG_PPPOE_NODE_TYPE);
		snprintf(mkp.ourhook, sizeof(mkp.ourhook),
			 "%s", NG_ETHER_HOOK_ORPHAN);
		snprintf(mkp.peerhook, sizeof(mkp.peerhook),
			 "%s", NG_PPPOE_HOOK_ETHERNET);
		/* 发送消息 */
		if (NgSendMsg(*cfd, source_ID, NGM_GENERIC_COOKIE,
			      NGM_MKPEER, &mkp, sizeof(mkp)) < 0) {
			return (errno);
		}
		/*
		 * 为新节点取一个名字。
		 */
		sprintf(pppoe_node_name, "%s:%s",
			source_ID, NG_ETHER_HOOK_ORPHAN);
	}
	/*
	 * 现在我们有了一个附加到以太网卡的 PPPoE 节点。
	 * 以太网地址为 ethername: PPPoE 节点地址为
	 * pppoe_node_name: 附加到它。
	 * 将套接字节点连接到指定节点，在链路两端使用相同的钩子名。
	 */
	snprintf(ngc.path, sizeof(ngc.path), "%s", pppoe_node_name);
	snprintf(ngc.ourhook, sizeof(ngc.ourhook), "%s", sessname);
	snprintf(ngc.peerhook, sizeof(ngc.peerhook), "%s", sessname);
	if (NgSendMsg(*cfd, ".:", NGM_GENERIC_COOKIE,
		      NGM_CONNECT, &ngc, sizeof(ngc)) < 0) {
		return (errno);
	}
#ifdef	NONSTANDARD
	/*
	 * 在某些情况下我们与 3Com 硬件通信，因此
	 * 将节点配置为非标准模式。
	 */
	if (NgSendMsg(*cfd, ngc.path, NGM_PPPOE_COOKIE,
			NGM_PPPOE_SETMODE, NG_PPPOE_NONSTANDARD,
			strlen(NG_PPPOE_NONSTANDARD) + 1) == -1) {
		return (errno);
	}
#endif
	/*
	 * 向其发送消息告知其启动。
	 */
	bzero(&message, sizeof(message));
	snprintf(message.idata.hook, sizeof(message.idata.hook),
				"%s", sessname);
	if (service == NULL) {
		message.idata.data_len = 0;
	} else {
		snprintf(message.idata.data,
			 sizeof(message.idata.data), "%s", service);
		message.idata.data_len = strlen(service);
	}
	/* 告知会话/钩子作为客户端启动 */
	if (NgSendMsg(*cfd, ngc.path,
		      NGM_PPPOE_COOKIE, NGM_PPPOE_CONNECT, &message.idata,
		      sizeof(message.idata) + message.idata.data_len) < 0) {
		return (errno);
	}
	return (0);
}
```

## 参见

netgraph(3), [netgraph(4)](netgraph.4.md), [ng_ether(4)](ng_ether.4.md), [ng_ppp(4)](ng_ppp.4.md), [ng_socket(4)](ng_socket.4.md), [vlan(4)](vlan.4.md), ngctl(8), ppp(8)

> L. Mamakos, K. Lidl, J. Evarts, D. Carrel, D. Simone, R. Wheeler, "A Method for transmitting PPP over Ethernet (PPPoE)", RFC 2516.

## 历史

`pppoe` 节点类型实现于 FreeBSD 4.0。

## 作者

Julian Elischer <julian@FreeBSD.org>
