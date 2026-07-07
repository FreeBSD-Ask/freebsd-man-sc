# ng_async(4)

`ng_async` — 异步成帧 netgraph 节点类型

## 名称

`ng_async`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_async.h>`

## 描述

`async` 节点类型执行同步帧与异步帧之间的转换，如 RFC 1662 中为 PPP 协议定义的那样。异步成帧使用标志字节和字节填充，在面向字节的异步串行线路上模拟面向帧的连接。

节点在 `async` 钩子上发送和接收异步数据。传入数据的 mbuf 边界被忽略。一旦收到完整的数据包，它将被解码并剥离所有成帧字节，作为单个帧从 `sync` 钩子传输出去。

同步帧在 `sync` 钩子上发送和接收。在此钩子上接收的数据包被编码为异步帧并从 `async` 发出。接收的数据包应以地址和控制字段开始，或在使用地址和控制字段压缩时以 PPP 协议字段开始，且不包含校验和字段。如果前四个字节是 `0xff 0x03 0xc0 0x21`（一个 LCP 协议帧），则对该帧启用完整的控制字符转义（在 PPP 中，LCP 数据包始终以不压缩地址和控制字段并转义所有控制字符的方式发送）。

此节点支持在 `async` 上传输的数据包的“标志共享”。这是一种优化，其中一帧的尾部标志字节与下一帧的开头标志字节共享。帧之间的标志共享在发送空闲一秒后被禁用。

## 钩子

此节点类型支持以下钩子：

**`async`** 异步连接。通常此钩子会连接到 [ng_tty(4)](ng_tty.4.md) 节点，后者处理通过 tty 设备传输串行数据。

**`sync`** 同步连接。此钩子发送和接收同步帧。对于 PPP，这些帧应包含地址、控制和协议字段，但不包含校验和字段。通常此钩子会连接到 [ng_ppp(4)](ng_ppp.4.md) 类型节点的某个单独链路钩子。

## 控制消息

此节点类型支持通用控制消息，外加以下消息：

```sh
struct ng_async_cfg {
	u_char    enabled;  /* 开启/关闭编码 */
	uint16_t  amru;     /* 最大异步接收帧长度 */
	uint16_t  smru;     /* 最大同步接收帧长度 */
	uint32_t  accm;     /* ACCM 编码 */
};
```

**`NGM_ASYNC_CMD_SET_CONFIG`** (`setconfig`) 设置节点配置，由 `struct ng_async_cfg` 描述：`enabled` 字段启用或禁用所有编码/解码功能（默认禁用）。禁用时，节点以简单的“直通”模式运行。`amru` 和 `smru` 字段分别是异步和同步 MRU（最大接收单元）值。两者默认为 1600；注意异步 MRU 适用于异步解码后的传入帧长度。`accm` 字段是异步字符控制映射，控制 0x00 到 0x1f 字符的转义（默认 0xffffffff）。

**`NGM_ASYNC_CMD_GET_CONFIG`** (`getconfig`) 此命令返回当前配置结构。

**`NGM_ASYNC_CMD_GET_STATS`** (`getstats`) 此命令返回包含数据包、八位组和错误计数节点统计信息的 `struct ng_async_stat`。

**`NGM_ASYNC_CMD_CLR_STATS`** (`clrstats`) 清除节点统计信息。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或当所有钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_ppp(4)](ng_ppp.4.md), [ng_tty(4)](ng_tty.4.md), ngctl(8)

> W. Simpson, "PPP in HDLC-link Framing", RFC 1662.

> W. Simpson, "The Point-to-Point Protocol (PPP)", RFC 1661.

## 历史

`async` 节点类型实现于 FreeBSD 4.0。

## 作者

Archie Cobbs <archie@FreeBSD.org>
