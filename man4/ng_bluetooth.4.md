# ng_bluetooth.4

`ng_bluetooth` — 全局 Bluetooth 变量的占位符

## 名称

`ng_bluetooth`

## 概要

`#include <sys/types.h>`

`#include <netgraph/bluetooth/include/ng_bluetooth.h>`

## 描述

`ng_bluetooth` 模块是全局 Bluetooth 变量的占位符。所有 Bluetooth 变量都可以通过 [sysctl(8)](../man8/sysctl.8.md) 检查和更改。

### Bluetooth 变量

下面是默认变量的描述。每个 Bluetooth 模块可能会向树中添加自己的变量。

**`net.bluetooth.version`** 一个只读整数变量，显示 Bluetooth 栈的当前版本。

**`net.bluetooth.hci.command_timeout`** 一个读写整数变量，控制主机控制器接口（HCI）命令超时（以秒为单位），即 HCI 层将等待 Bluetooth 设备发出 `Command_Complete` 或 `Command_Status` 事件的时间。

**`net.bluetooth.hci.connection_timeout`** 一个读写整数变量，控制 HCI 连接超时，即 HCI 层将等待 `Connection_Complete` 事件的时间。通常不需要此超时，因为 Bluetooth 设备有自己的连接超时并会发回事件。此超时用于确保在 HCI 传输层损坏时不会有连接停滞。更改此变量时需谨慎。确保你理解自己在做什么。

**`net.bluetooth.hci.max_neighbor_age`** 一个读写整数变量，控制 HCI 邻居缓存中条目的生存时间（以秒为单位）。每次 Bluetooth 设备执行 `Inquiry` 操作时，结果将放入缓存。之后当 Bluetooth 设备建立基带连接时，它将尝试在缓存中找到匹配条目并使用它。这可能加速基带连接的建立。

**`net.bluetooth.l2cap.rtx_timeout`** 一个读写整数变量，控制链路层控制和适配协议（L2CAP）重传超时（RTX，以秒为单位）。每次 L2CAP 层提交控制命令时，都会设置 RTX 超时。RTX 超时的值应大于或等于 HCI 连接超时的值。更改此变量时需谨慎。确保你理解自己在做什么。

**`net.bluetooth.l2cap.ertx_timeout`** 一个读写整数变量，控制 L2CAP 扩展重传超时（ERTX，以秒为单位）。在某些情况下，远程对等方可能以 `PENDING` 状态响应 L2CAP 控制命令。在这种情况下，L2CAP 命令超时重置为 ERTX 超时值。ERTX 超时的值应大于或等于 RTX 超时的值。更改此变量时需谨慎。确保你理解自己在做什么。

## 参见

[ng_btsocket(4)](ng_btsocket.4.md), [ng_hci(4)](ng_hci.4.md), [ng_l2cap(4)](ng_l2cap.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`ng_bluetooth` 模块实现于 FreeBSD 5.0。

## 作者

Maksim Yevmenkin <m_evmenkin@yahoo.com>
