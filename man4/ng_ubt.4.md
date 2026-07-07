# ng_ubt(4)

`ng_ubt` — 同时也是蓝牙 USB 设备驱动程序的 Netgraph 节点类型

## 名称

`ng_ubt`

## 概要

`#include <sys/types.h>`

`#include <netgraph/bluetooth/include/ng_ubt.h>`

## 描述

`ubt` 节点类型既是持久的 Netgraph 节点类型，又是蓝牙 USB 设备的驱动程序。它按蓝牙规范手册 v1.1 的 H2 章实现蓝牙 USB 传输层。当插入受支持的 USB 设备时会创建新节点。

该节点有一个名为 `hook` 的钩子。在设备上接收的入站字节会（按长度）重新组装成 HCI 帧。完整的 HCI 帧从该钩子发出。如果设备未发送 HCI 帧指示器，节点会添加一个。在 `hook` 上接收的 HCI 帧会被传输出去。除非设备要求存在 HCI 帧指示器，否则节点会将其丢弃。

## 硬件

`ubt` 驱动支持所有符合蓝牙规范 v1.1 的蓝牙 USB 设备，包括：

- 3Com 3CREB96
- AIPTEK BR0R02
- EPoX BT-DG02
- Mitsumi 蓝牙 USB 适配器
- MSI MS-6967
- TDK 蓝牙 USB 适配器
- Broadcom 蓝牙 USB 适配器

## 钩子

此节点类型支持以下钩子：

**`hook`** 单个 HCI 帧包含在单个 `mbuf` 结构中。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

**`NGM_UBT_NODE_GET_DEBUG`**（`get_debug`）返回一个整数，包含节点当前的调试级别。

**`NGM_UBT_NODE_SET_DEBUG`**（`set_debug`）此命令接受一个整数参数，设置节点当前的调试级别。

**`NGM_UBT_NODE_GET_QLEN`**（`get_qlen`）此命令接受一个指定队列编号的参数，返回节点该队列的当前最大长度。

**`NGM_UBT_NODE_SET_QLEN`**（`set_qlen`）此命令接受两个参数，分别指定队列编号和队列最大长度，设置节点该队列的最大长度。

**`NGM_UBT_NODE_GET_STAT`**（`get_stat`）返回节点的各种统计信息，例如：发送的字节（帧）数、接收的字节（帧）数以及输入（输出）错误数。

**`NGM_UBT_NODE_RESET_STAT`**（`reset_stat`）将所有统计计数器重置为零。

## 关闭

此节点在相应 USB 设备被拔出时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ugen(4)](ugen.4.md), [usb(4)](usb.4.md), ngctl(8)

## 历史

`ubt` 节点类型实现于 FreeBSD 5.0。

## 作者

Maksim Yevmenkin <m_evmenkin@yahoo.com>

## 缺陷

同步 USB 传输存在问题。这意味着 USB 设备将无法传输 SCO 数据（语音）。USB 中断传输以批量入站传输方式实现（并非真正的 bug）。
