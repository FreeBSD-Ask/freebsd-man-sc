# ng_source(4)

`ng_source` — 用于流量生成的 netgraph 节点

## 名称

`ng_source`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_source.h>`

## 描述

`source` 节点根据使用控制消息和输入数据包设置的参数作为数据包源。`source` 节点类型主要用于测试和基准测试。

## 钩子

`source` 节点有两个钩子：`input` 和 `output`。`output` 钩子必须保持连接，断开它将导致节点关闭。

## 操作

节点的操作如下。在 `input` 钩子上接收的数据包在内部排队。当 `output` 钩子已连接时，`source` 节点假定其邻居节点为 [ng_ether(4)](ng_ether.4.md) 节点类型。它会查询邻居的接口名。然后 `source` 节点将其邻居 [ng_ether(4)](ng_ether.4.md) 节点上的 `autosrc` 选项禁用，并出于其邪恶目的使用该接口的队列。如果无法自动获取接口名，则应通过 `NGM_SOURCE_SETIFACE` 控制消息显式配置，并手动关闭 [ng_ether(4)](ng_ether.4.md) 节点上的 `autosrc`。

如果节点连接到的 netgraph 网络未终止于真实 [ng_ether(4)](ng_ether.4.md) 接口，则需使用 `NGM_SOURCE_SETPPS` 控制消息显式限制数据包注入速率。

收到 `NGM_SOURCE_START` 控制消息后，节点在每个时钟滴答上开始将先前排队的数据包尽可能快地从 `output` 钩子发送出去，速度取决于所连接接口的承受能力。活动期间，节点在每个时钟滴答上检查接口队列中的可用空间，并从 `output` 钩子发送相应数量的数据包。一旦已发送 start 消息中指示的数据包数，或收到 `NGM_SOURCE_STOP` 消息，节点将停止发送数据。

## 控制消息

此节点类型支持通用控制消息以及以下消息，这些消息必须附加 `NGM_SOURCE_COOKIE` 发送。

**`outOctets`** 从 `output` 钩子发送出的八位字节数/字节数。

**`outFrames`** 从 `output` 钩子发送出的帧数/数据包数。

**`queueOctets`** 从 `input` 钩子排队的八位字节数。

**`queueFrames`** 从 `input` 钩子排队的帧数。

**`startTime`** 上次收到 start 消息的时间。

**`endTime`** 上次收到 end 消息或达到输出数据包计数的时间。

**`elapsedTime`** `endTime` `-` `startTime` 或当前时间 - `startTime`。

**`offset`** 自数据包开头起插入时间戳的偏移量。

**`flags`** 设为 1 以启用时间戳。

**`offset`** 自数据包开头起插入计数器的偏移量。

**`flags`** 设为 1 以启用计数器。

**`width`** 计数器的字节宽度。可为 1、2 或 4。

**`next_val`** 下次插入计数器的值。

**`min_val`** 计数器使用的最小值。

**`max_val`** 计数器使用的最大值。

**`increment`** 每次插入后加到计数器上的值。可为负数。

**`index`** 要配置的计数器，从 0 到 3。

**`NGM_SOURCE_GET_STATS`**（`getstats`）返回包含以下字段的结构：

**`NGM_SOURCE_CLR_STATS`**（`clrstats`）清零并重置 `getstats` 返回的统计信息（`queueOctets` 和 `queueFrames` 除外）。

**`NGM_SOURCE_GETCLR_STATS`**（`getclrstats`）与 `getstats` 相同，但同时清零统计信息。

**`NGM_SOURCE_START`**（`start`）此消息需要单个 `uint64_t` 参数，即停止前要发送的数据包数。节点开始将排队的数据包从 `output` 钩子发送出去。`output` 钩子必须已连接，且节点必须已配置接口。

**`NGM_SOURCE_STOP`**（`stop`）如果节点处于活动状态则停止。

**`NGM_SOURCE_CLR_DATA`**（`clrdata`）清空从 `input` 钩子排队的数据包。

**`NGM_SOURCE_SETIFACE`**（`setiface`）此消息需要作为参数的待配置接口名。

**`NGM_SOURCE_SETPPS`**（`setpps`）此消息需要单个 `uint32_t` 参数，用于设置每秒发送数据包数的上限。

**`NGM_SOURCE_SET_TIMESTAMP`**（`settimestamp`）此消息指定应在传输的数据包中插入时间戳（采用 `struct timeval` 格式）。此消息需要包含以下字段的结构：

**`NGM_SOURCE_GET_TIMESTAMP`**（`gettimestamp`）以上文所述结构形式返回当前时间戳设置。

**`NGM_SOURCE_SET_COUNTER`**（`setcounter`）此消息指定应在传输的数据包中嵌入计数器。最多可独立配置四个计数器。此消息需要包含以下字段的结构：

**`NGM_SOURCE_GET_COUNTER`**（`getcounter`）此消息需要单个 `uint8_t` 参数，指定要查询的计数器。以上文所述结构形式返回当前计数器设置。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息、所有钩子均已断开或 `output` 钩子被断开时关闭。

## 实例

将节点附加到接口的 [ng_ether(4)](ng_ether.4.md) 节点。如果 `ng_ether` 尚未加载，你需要先加载。例如，以下命令加载 `ng_ether` 模块，并将新 `source` 节点的 `output` 钩子附加到 `bge0:` `ng_ether` 节点的 `orphans` 钩子。

```sh
kldload ng_ether
ngctl mkpeer bge0: source orphans output
```

此时新节点可以被称为“`bge0:orphans`”。可以像这样为节点命名：

```sh
ngctl name bge0:orphans src0
```

之后可将其称为“`src0:`”。

创建后，可以将数据包作为原始二进制数据发送到节点。每个数据包必须在单独的 netgraph 消息中传递。

以下示例使用简短的 Perl 脚本将 ICMP 数据包的十六进制表示转换为二进制，并通过 nghook(8) 传递到 `source` 节点的 `input` 钩子：

```sh
perl -pe 's/(..)[ eten]*/chr(hex($1))/ge' <<EOF | nghook src0: input
ff ff ff ff ff ff 00 00 00 00 00 00 08 00 45 00
00 54 cb 13 00 00 40 01 b9 87 c0 a8 2b 65 0a 00
00 01 08 00 f8 d0 c9 76 00 00 45 37 01 73 00 01
04 0a 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15
16 17 18 19 1a 1b 1c 1d 1e 1f 20 21 22 23 24 25
26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35
36 37
EOF
```

要检查节点是否已排队这些数据包，可以获取节点统计信息：

```sh
ngctl msg bge0:orphans getstats
Args:   { queueOctets=64 queueFrames=1 }
```

按需从 `output` 钩子发送所需数量的数据包：

```sh
ngctl msg bge0:orphans start 16
```

可以等待它们发送完成（如果需要可定期获取统计信息），或发送停止消息：

```sh
ngctl msg bge0:orphans stop
```

检查统计信息（此处我们使用 `getclrstats` 同时清零统计信息）：

```sh
ngctl msg bge0:orphans getclrstats
Args:   { outOctets=1024 outFrames=16 queueOctets=64 queueFrames=1
startTime={ tv_sec=1035305880 tv_usec=758036 } endTime={ tv_sec=1035305880
tv_usec=759041 } elapsedTime={ tv_usec=1005 } }
```

时间来自 `struct timeval`，`tv_sec` 字段是自纪元以来的秒数，可通过 TCL 的 [clock format] 或通过 [date(1)](../man1/date.1.md) 命令转换为日期字符串：

```sh
date -r 1035305880
Tue Oct 22 12:58:00 EDT 2002
```

## 参见

[netgraph(4)](netgraph.4.md), [ng_echo(4)](ng_echo.4.md), [ng_hole(4)](ng_hole.4.md), [ng_tee(4)](ng_tee.4.md), ngctl(8), nghook(8)

## 历史

`source` 节点类型实现于 FreeBSD 4.8。

## 作者

Dave Chapeskie
