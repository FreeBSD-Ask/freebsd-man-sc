# ng_btsocket(4)

`ng_btsocket` — Bluetooth socket 层

## 名称

`ng_btsocket`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <sys/bitstring.h>`

`#include <netgraph/bluetooth/include/ng_hci.h>`

`#include <netgraph/bluetooth/include/ng_l2cap.h>`

`#include <netgraph/bluetooth/include/ng_btsocket.h>`

## 描述

`ng_btsocket` 模块实现了三种 Netgraph 节点类型。每种类型又实现了 `PF_BLUETOOTH` 域中的一种协议。

## Dv BLUETOOTH_PROTO_HCI 协议

### Dv SOCK_RAW HCI socket

由 `btsock_hci_raw` Netgraph 类型实现。原始 HCI socket 仅允许向 send(2) 调用中指定的通信方发送原始 HCI 命令数据报。原始 HCI 数据报（HCI 命令、事件和数据）通常通过 recvfrom(2) 接收，该调用返回下一个数据报及其返回地址。原始 HCI socket 还可用于控制 HCI 节点。

Bluetooth 原始 HCI socket 地址定义如下：

```sh
/* 原始 HCI socket 的 sockaddr 的 Bluetooth 版本 */
struct sockaddr_hci {
        u_char	hci_len;      /* 总长度 */
        u_char	hci_family;   /* 地址族 */
	char	hci_node[32]; /* 地址（大小 == NG_NODESIZ） */
};
```

原始 HCI socket 支持多个 ioctl(2) 请求，例如：

**`SIOC_HCI_RAW_NODE_GET_STATE`** 返回 HCI 节点的当前状态。

**`SIOC_HCI_RAW_NODE_INIT`** 打开 HCI 节点的“inited”位。

**`SIOC_HCI_RAW_NODE_GET_DEBUG`** 返回 HCI 节点的当前调试级别。

**`SIOC_HCI_RAW_NODE_SET_DEBUG`** 设置 HCI 节点的当前调试级别。

**`SIOC_HCI_RAW_NODE_GET_BUFFER`** 返回 HCI 节点数据缓冲区的当前状态。

**`SIOC_HCI_RAW_NODE_GET_BDADDR`** 返回 HCI 节点的 BD_ADDR。

**`SIOC_HCI_RAW_NODE_GET_FEATURES`** 返回 HCI 节点硬件支持的功能列表。

**`SIOC_HCI_RAW_NODE_GET_STAT`** 返回 HCI 节点的各种统计计数器。

**`SIOC_HCI_RAW_NODE_RESET_STAT`** 将 HCI 节点的所有统计计数器重置为零。

**`SIOC_HCI_RAW_NODE_FLUSH_NEIGHBOR_CACHE`** 移除 HCI 节点的所有邻居缓存条目。

**`SIOC_HCI_RAW_NODE_GET_NEIGHBOR_CACHE`** 返回 HCI 节点的邻居缓存内容。

**`SIOC_HCI_RAW_NODE_GET_CON_LIST`** 返回 HCI 节点的活动基带连接（即 ACL 和 SCO 链路）列表。

**SIOC_HCI_RAW_NODE_GET_LINK_POLICY_MASK** 返回 HCI 节点的当前链路策略设置掩码。

**SIOC_HCI_RAW_NODE_SET_LINK_POLICY_MASK** 设置 HCI 节点的当前链路策略设置掩码。

**SIOC_HCI_RAW_NODE_GET_PACKET_MASK** 返回 HCI 节点的当前数据包掩码。

**SIOC_HCI_RAW_NODE_SET_PACKET_MASK** 设置 HCI 节点的当前数据包掩码。

**SIOC_HCI_RAW_NODE_GET_ROLE_SWITCH** 返回 HCI 节点的角色切换参数的当前值。

**SIOC_HCI_RAW_NODE_SET_ROLE_SWITCH** 设置 HCI 节点的角色切换参数的新值。

可通过 [sysctl(8)](../man8/sysctl.8.md) 检查和设置的 `net.bluetooth.hci.sockets.raw.ioctl_timeout` 变量控制原始 HCI socket 的控制请求超时（以秒为单位）。

原始 HCI socket 支持过滤器。应用程序可过滤某些 HCI 数据报类型。对于 HCI 事件数据报，应用程序可设置额外过滤器。原始 HCI socket 过滤器定义如下：

```sh
/*
 * 原始 HCI socket 过滤器。
 *
 * 对于数据包掩码，使用 (1 << (HCI 数据包指示符 - 1))
 * 对于事件掩码，使用 (1 << (事件号 - 1))
 */
struct ng_btsocket_hci_raw_filter {
        bitstr_t bit_decl(packet_mask, 32);
        bitstr_t bit_decl(event_mask, (NG_HCI_EVENT_MASK_SIZE * 8));
};
```

可使用 `SOL_HCI_RAW` 级别定义的 `SO_HCI_RAW_FILTER` 选项，通过 getsockopt(2) 获取或通过 setsockopt(2) 更改原始 HCI socket 的过滤器。

## Dv BLUETOOTH_PROTO_L2CAP 协议

Bluetooth L2CAP socket 地址定义如下：

```sh
/* L2CAP socket 的 sockaddr 的 Bluetooth 版本 */
struct sockaddr_l2cap {
        u_char    l2cap_len;    /* 总长度 */
        u_char    l2cap_family; /* 地址族 */
        uint16_t  l2cap_psm;    /* 协议/服务多路复用器 */
        bdaddr_t  l2cap_bdaddr; /* 地址 */
};
```

### Dv SOCK_RAW L2CAP socket

由 `btsock_l2c_raw` Netgraph 类型实现。原始 L2CAP socket 不提供对原始 L2CAP 数据报的访问。这些 socket 用于控制 L2CAP 节点和发出特殊的 L2CAP 请求，如 `ECHO_REQUEST` 和 `GET_INFO` 请求。

原始 L2CAP socket 支持多个 ioctl(2) 请求，例如：

**`SIOC_L2CAP_NODE_GET_FLAGS`** 返回 L2CAP 节点的当前状态。

**`SIOC_L2CAP_NODE_GET_DEBUG`** 返回 L2CAP 节点的当前调试级别。

**`SIOC_L2CAP_NODE_SET_DEBUG`** 设置 L2CAP 节点的当前调试级别。

**`SIOC_L2CAP_NODE_GET_CON_LIST`** 返回 L2CAP 节点的活动基带连接（即 ACL 链路）列表。

**`SIOC_L2CAP_NODE_GET_CHAN_LIST`** 返回 L2CAP 节点的活动通道列表。

**`SIOC_L2CAP_NODE_GET_AUTO_DISCON_TIMO`** 返回 L2CAP 节点的自动断开超时的当前值。

**`SIOC_L2CAP_NODE_SET_AUTO_DISCON_TIMO`** 设置 L2CAP 节点的自动断开超时的当前值。

**`SIOC_L2CAP_L2CA_PING`** 发出 L2CAP `ECHO_REQUEST`。

**`SIOC_L2CAP_L2CA_GET_INFO`** 发出 L2CAP `GET_INFO` 请求。

可通过 [sysctl(8)](../man8/sysctl.8.md) 检查和设置的 `net.bluetooth.l2cap.sockets.raw.ioctl_timeout` 变量控制原始 L2CAP socket 的控制请求超时（以秒为单位）。

### Dv SOCK_SEQPACKET L2CAP socket

由 `btsock_l2c` Netgraph 类型实现。L2CAP socket 要么是“主动”的，要么是“被动”的。主动 socket 发起到被动 socket 的连接。默认情况下，L2CAP socket 创建为主动；要创建被动 socket，必须在使用 bind(2) 系统调用将 socket 绑定后使用 listen(2) 系统调用。只有被动 socket 可使用 accept(2) 调用接受传入连接。只有主动 socket 可使用 connect(2) 调用发起连接。

L2CAP socket 支持“通配寻址”。在这种情况下，socket 必须绑定到 `NG_HCI_BDADDR_ANY` 地址。注意，PSM（协议/服务多路复用器）字段始终是必需的。一旦建立连接，socket 的地址由对等实体位置固定。分配给 socket 的地址是与发送和接收数据包的 Bluetooth 设备关联的地址，以及 PSM（协议/服务多路复用器）。

L2CAP socket 支持在 `SOL_L2CAP` 级别定义的多个选项，可使用 setsockopt(2) 设置并使用 getsockopt(2) 测试：

**`SO_L2CAP_IMTU`** 获取（设置）本地 socket 能够接受的最大有效载荷大小。

**`SO_L2CAP_OMTU`** 获取远程 socket 能够接受的最大有效载荷大小。

**`SO_L2CAP_IFLOW`** 获取 socket 的传入流规范。Bf -emphasis 未实现。Ef

**`SO_L2CAP_OFLOW`** 获取（设置）socket 的传出流规范。Bf -emphasis 未实现。Ef

**`SO_L2CAP_FLUSH`** 获取（设置）刷新超时的值。Bf -emphasis 未实现。Ef

## Dv BLUETOOTH_PROTO_RFCOMM 协议

Bluetooth RFCOMM socket 地址定义如下：

```sh
/* RFCOMM socket 的 sockaddr 的 Bluetooth 版本 */
struct sockaddr_rfcomm {
        u_char   rfcomm_len;     /* 总长度 */
        u_char   rfcomm_family;  /* 地址族 */
        bdaddr_t rfcomm_bdaddr;  /* 地址 */
        uint8_t  rfcomm_channel; /* 通道 */
};
```

### Dv SOCK_STREAM RFCOMM socket

注意，RFCOMM socket 没有关联的 Netgraph 节点类型。RFCOMM socket 实现为 L2CAP socket 之上的附加层。RFCOMM socket 要么是“主动”的，要么是“被动”的。主动 socket 发起到被动 socket 的连接。默认情况下，RFCOMM socket 创建为主动；要创建被动 socket，必须在使用 bind(2) 系统调用将 socket 绑定后使用 listen(2) 系统调用。只有被动 socket 可使用 accept(2) 调用接受传入连接。只有主动 socket 可使用 connect(2) 调用发起连接。

RFCOMM socket 支持“通配寻址”。在这种情况下，socket 必须绑定到 `NG_HCI_BDADDR_ANY` 地址。注意，RFCOMM 通道字段始终是必需的。一旦建立连接，socket 的地址由对等实体位置固定。分配给 socket 的地址是与发送和接收数据包的 Bluetooth 设备关联的地址，以及 RFCOMM 通道。

以下选项在 `SOL_RFCOMM` 级别为 RFCOMM socket 定义，可使用 getsockopt(2) 调用测试：

**`SO_RFCOMM_MTU`** 返回底层 RFCOMM 通道的最大传输单元大小（以字节为单位）。注意，应用程序仍可向 socket 写入/从 socket 读取更大的数据块。

**`SO_RFCOMM_FC_INFO`** 返回底层 RFCOMM 通道的流控制信息。

可通过 [sysctl(8)](../man8/sysctl.8.md) 检查和设置的 `net.bluetooth.rfcomm.sockets.stream.timeout` 变量控制 RFCOMM socket 的连接超时（以秒为单位）。

## 钩子

这些节点类型支持具有任意名称（只要唯一）的钩子，并始终接受钩子连接请求。

## NETGRAPH 控制消息

这些节点类型支持通用控制消息。

## 关闭

这些节点是持久的，无法关闭。

## 参见

[btsockstat(1)](../man1/btsockstat.1.md), socket(2), [netgraph(4)](netgraph.4.md), [ng_bluetooth(4)](ng_bluetooth.4.md), [ng_hci(4)](ng_hci.4.md), [ng_l2cap(4)](ng_l2cap.4.md), ngctl(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`btsock_l2c` 模块实现于 FreeBSD 5.0。

## 作者

Maksim Yevmenkin <m_evmenkin@yahoo.com>

## 缺陷

很可能有。如发现请报告。
