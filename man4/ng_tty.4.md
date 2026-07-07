# ng_tty(4)

`ng_tty` — 同时也是 TTY 钩子的 netgraph 节点类型

## 名称

`ng_tty`

## 概要

`#include <sys/types.h>`

`#include <sys/ttycom.h>`

`#include <netgraph/ng_tty.h>`

## 描述

`tty` 节点类型既是 netgraph 节点类型又是 TTY 钩子。

该节点有一个名为 `hook` 的钩子。在 tty 设备上接收的入站字节会从此钩子发出，而在 `hook` 上接收的帧会通过 tty 设备传输出去。两个方向都不对数据进行修改。当钩子安装在 tty 上时，正常的 read 和 write 操作不可用，返回 Er EIO。

入站数据作为缓冲区指针和长度通过 tty 旁路钩子直接传递给 ng_tty，然后被转换为 mbuf 并传递给对端。

该节点支持可选的“热字符”。如果驱动程序无法将数据直接传递给 tty 旁路钩子，则每个字符会逐个输入。如果设置为非零且旁路模式不可用，则来自 tty 设备的入站数据将排队直到看到此字符。这避免了发送大量包含少量字节的 mbuf，但引入了潜在的无限延迟。默认热字符为 0x7e，与 `hook` 连接到 [ng_async(4)](ng_async.4.md) 类型节点时一致。热字符对数据传输没有影响。

## 钩子

此节点类型支持以下钩子：

**`hook`** [tty(4)](tty.4.md) 串行数据包含在 `mbuf` 结构中，帧间边界任意。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

**`NGM_TTY_SET_HOTCHAR`** 此命令接受一个整数参数，从低 8 位设置热字符。热字符为零会禁用排队，因此所有接收到的数据都会立即转发。

**`NGM_TTY_GET_HOTCHAR`** 返回一个整数，低八位包含当前热字符。

**`NGM_TTY_SET_TTY`** 此命令接受整数进程 ID 和打开 tty 的文件描述符，并注册 tty 钩子。

## 关闭

此节点在相应设备关闭时关闭。

## 参见

ioctl(2), [netgraph(4)](netgraph.4.md), [ng_async(4)](ng_async.4.md), [tty(4)](tty.4.md), ngctl(8)

## 历史

`tty` 节点类型实现于 FreeBSD 4.0。

## 作者

Archie Cobbs <archie@FreeBSD.org> Andrew Thompson <thompsa@FreeBSD.org>

## 缺陷

串行驱动程序代码也有“热字符”的概念。不幸的是，此值以线路规程为依据静态定义，无法更改。因此，如果为 `tty` 节点设置了 0x7e（默认值）以外的热字符，节点无法将此信息传达给串行驱动程序，可能导致次优性能。
