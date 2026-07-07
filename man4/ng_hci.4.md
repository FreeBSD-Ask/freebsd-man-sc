# ng_hci(4)

`ng_hci` — 同时作为蓝牙主机控制器接口的 Netgraph 节点类型

## 名称

`ng_hci` (HCI) 层

## 概要

`#include <sys/types.h>`

`#include <netgraph/bluetooth/include/ng_hci.h>`

## 描述

`hci` 节点类型是一种 Netgraph 节点类型，按照蓝牙规范 v1.1 第 H1 章实现蓝牙主机控制器接口（HCI）层。

## 蓝牙简介

蓝牙是一种短距离无线链路，旨在取代连接便携式和/或固定电子设备的线缆。蓝牙工作在 2.4 GHz 的免许可 ISM 频段。蓝牙协议结合了电路交换和分组交换。蓝牙可以支持异步数据通道、最多三个同时同步语音通道，或同时支持异步数据和同步语音的通道。每个语音通道在每个方向上支持 64 kb/s 的同步（语音）通道。异步通道最大可支持 723.2 kb/s 非对称（在返回方向上仍可达 57.6 kb/s），或 433.9 kb/s 对称。

蓝牙系统提供点对点连接（仅涉及两个蓝牙单元）或点对多点连接。在点对多点连接中，通道由多个蓝牙单元共享。共享同一通道的两个或多个单元形成一个“piconet”。一个蓝牙单元作为 piconet 的主设备，其他单元作为从设备。piconet 中最多可以有七个活动从设备。此外，更多的从设备可以保持锁定到主设备的所谓驻留状态。这些驻留从设备不能在通道上活动，但保持与主设备同步。对于活动和驻留从设备，通道访问都由主设备控制。

多个覆盖区域重叠的 piconet 形成一个“scatternet”。每个 piconet 只能有一个主设备。但从设备可以基于时分多路复用参与不同的 piconet。此外，一个 piconet 中的主设备可以是另一个 piconet 中的从设备。各 piconet 之间不需要频率同步。每个 piconet 有自己的跳频通道。

### 时隙

通道被划分为时隙，每个时隙长度为 625 微秒。时隙根据 piconet 主设备的蓝牙时钟编号。时隙编号范围从 0 到 2^27-1，循环周期为 2^27。在时隙中，主设备和从设备可以发送数据包。

### SCO 链路

SCO 链路是主设备与特定从设备之间的对称点对点链路。SCO 链路保留时隙，因此可以视为主设备与从设备之间的电路交换连接。SCO 链路通常支持语音等时间受限的信息。主设备可以支持最多到同一从设备或不同从设备的三个 SCO 链路。从设备可以支持来自同一主设备的最多三个 SCO 链路，如果链路来自不同主设备则最多两个。SCO 数据包从不重传。

### ACL 链路

在未保留给 SCO 链路的时隙中，主设备可以基于每个时隙与任何从设备交换数据包。ACL 链路在主设备和参与 piconet 的所有活动从设备之间提供分组交换连接。同时支持异步和等时服务。主设备和一个从设备之间只能存在一个 ACL 链路。对于大多数 ACL 数据包，应用数据包重传以确保数据完整性。

## 主机控制器接口（HCI）

HCI 为基带控制器和链路管理器提供命令接口，并访问硬件状态和控制寄存器。此接口提供访问蓝牙基带能力的统一方法。

主机上的 HCI 层与蓝牙硬件上的 HCI 固件交换数据和命令。主机控制器传输层（即物理总线）驱动程序为两个 HCI 层提供相互交换信息的能力。

主机将收到与所使用的主机控制器传输层无关的 HCI 事件异步通知。HCI 事件用于在发生某些情况时通知主机。当主机发现事件发生时，将解析收到的事件数据包以确定发生了哪个事件。以下各节定义 HCI 数据包格式。

### HCI 命令数据包

```sh
#define NG_HCI_CMD_PKT 0x01
typedef struct {
        uint8_t  type;   /* 必须为 0x1 */
        uint16_t opcode; /* 操作码 */
        uint8_t  length; /* 参数长度（字节） */
} __attribute__ ((packed)) ng_hci_cmd_pkt_t;
```

HCI 命令数据包用于从主机向主机控制器发送命令。当主机控制器完成大多数命令时，会向主机发送命令完成事件。某些命令在完成时不会收到命令完成事件。相反，当主机控制器收到这些命令之一时，会在开始执行命令时向主机发回命令状态事件。随后，当与该命令相关的操作完成时，主机控制器会将与所发送命令相关联的事件发送给主机。

### HCI 事件数据包

```sh
#define NG_HCI_EVENT_PKT 0x04
typedef struct {
        uint8_t type;   /* 必须为 0x4 */
        uint8_t event;  /* 事件 */
        uint8_t length; /* 参数长度（字节） */
} __attribute__ ((packed)) ng_hci_event_pkt_t;
```

HCI 事件数据包由主机控制器在事件发生时用于通知主机。

### HCI ACL 数据数据包

```sh
#define NG_HCI_ACL_DATA_PKT 0x02
typedef struct {
        uint8_t  type;       /* 必须为 0x2 */
        uint16_t con_handle; /* 连接句柄 + PB + BC 标志 */
        uint16_t length;     /* 负载长度（字节） */
} __attribute__ ((packed)) ng_hci_acldata_pkt_t;
```

HCI ACL 数据数据包用于在主机和主机控制器之间交换 ACL 数据。

### HCI SCO 数据数据包

```sh
#define NG_HCI_SCO_DATA_PKT 0x03
typedef struct {
        uint8_t  type;       /* 必须为 0x3 */
        uint16_t con_handle; /* 连接句柄 + 保留位 */
        uint8_t  length;     /* 负载长度（字节） */
} __attribute__ ((packed)) ng_hci_scodata_pkt_t;
```

HCI SCO 数据数据包用于在主机和主机控制器之间交换 SCO 数据。

## HCI 初始化

初始化时，HCI 控制应用程序必须发出以下 HCI 命令（顺序不限）。

**`Read_BD_ADDR`** 获取蓝牙单元的 BD_ADDR。

**`Read_Local_Supported_Features`** 获取蓝牙单元支持的功能列表。

**`Read_Buffer_Size`** 确定可从主机发送到主机控制器的 HCI ACL 和 SCO HCI 数据包（不含头部）的最大尺寸。还有两个额外的返回参数，指定主机控制器可以在其缓冲区中等待发送的 HCI ACL 和 SCO 数据包总数。

HCI 初始化成功执行后，HCI 控制应用程序必须为节点打开“inited”位。一旦 HCI 节点初始化完成，所有上游钩子将收到如下定义的 `NGM_HCI_NODE_UP` Netgraph 消息。

```sh
#define NGM_HCI_NODE_UP 112 /* HCI -> 上层 */
typedef struct {
        uint16_t  pkt_size; /* 最大 ACL/SCO 数据包大小（不含头部） */
        uint16_t  num_pkts; /* ACL/SCO 数据包队列大小 */
        uint16_t  reserved; /* 占位符 */
        bdaddr_t  bdaddr;   /* bdaddr */
} ng_hci_node_up_ep;
```

## HCI 流控

HCI 层基于基带连接（即 ACL 和 SCO 链路）执行流控。每个基带连接都有“连接句柄”和发出数据包队列。上层协议一次最多可发送 `( num_pkts` - `pending`) 个数据包。HCI 层将发送 `NGM_HCI_SYNC_CON_QUEUE` Netgraph 消息通知上层每个连接句柄的当前队列状态。`NGM_HCI_SYNC_CON_QUEUE` Netgraph 消息定义如下。

```sh
#define NGM_HCI_SYNC_CON_QUEUE 113 /* HCI -> 上层 */
typedef struct {
        uint16_t con_handle; /* 连接句柄 */
        uint16_t completed;  /* 已完成的数据包数 */
} ng_hci_sync_con_queue_ep;
```

## 钩子

本节点类型支持以下钩子：

**`drv`** 蓝牙主机控制器传输层钩子。单个 HCI 数据包包含在单个 `mbuf` 结构中。

**`acl`** 上层协议/节点连接到此钩子。单个 HCI ACL 数据数据包包含在单个 `mbuf` 结构中。

**`sco`** 上层协议/节点连接到此钩子。单个 HCI SCO 数据数据包包含在单个 `mbuf` 结构中。

**`raw`** 原始钩子。每个进出的 HCI 帧（包括 HCI 命令帧）都会被传递到此钩子。通常蓝牙原始 HCI 套接字层连接到此钩子。单个 HCI 帧包含在单个 `mbuf` 结构中。

## 蓝牙上层协议接口（LP 控制消息）

**`NGM_HCI_LP_CON_REQ`** 请求下层协议创建连接。如果到远程设备的物理链路不存在，必须将此消息发送给下层协议（基带）以建立物理连接。

**`NGM_HCI_LP_DISCON_REQ`** 请求下层协议（基带）终止连接。

**`NGM_HCI_LP_CON_CFM`** 确认 `NGM_HCI_LP_CON_REQ` 请求建立下层（基带）连接的成功或失败。包括在建立物理链路需要身份验证时传递身份验证质询。

**`NGM_HCI_LP_CON_IND`** 指示下层协议（基带）已成功建立传入连接。

**`NGM_HCI_LP_CON_RSP`** 接受或拒绝先前连接指示请求的响应。

**`NGM_HCI_LP_DISCON_IND`** 指示下层协议（基带）已终止连接。这可能是对 `NGM_HCI_LP_DISCON_REQ` 的响应，也可能是超时事件。

**`NGM_HCI_LP_QOS_REQ`** 请求下层协议（基带）适配特定的 QoS 参数集。

**`NGM_HCI_LP_QOS_CFM`** 确认给定服务质量的请求成功或失败。

**`NGM_HCI_LP_QOS_IND`** 指示下层协议（基带）检测到 QoS 协议被违反。

## NETGRAPH 控制消息

本节点类型支持通用控制消息，以及以下消息：

**`NGM_HCI_NODE_GET_STATE`** 返回节点的当前状态。

**`NGM_HCI_NODE_INIT`** 为节点打开“inited”位。

**`NGM_HCI_NODE_GET_DEBUG`** 返回包含节点当前调试级别的整数。

**`NGM_HCI_NODE_SET_DEBUG`** 此命令接受一个整数参数，设置节点的当前调试级别。

**`NGM_HCI_NODE_GET_BUFFER`** 返回数据缓冲区的当前状态。

**`NGM_HCI_NODE_GET_BDADDR`** 返回节点中缓存的 BD_ADDR。

**`NGM_HCI_NODE_GET_FEATURES`** 返回硬件支持的功能列表（由节点缓存）。

**`NGM_HCI_NODE_GET_NEIGHBOR_CACHE`** 返回邻居缓存的内容。

**`NGM_HCI_NODE_FLUSH_NEIGHBOR_CACHE`** 移除所有邻居缓存条目。

**`NGM_HCI_NODE_GET_CON_LIST`** 返回活动基带连接列表（即 ACL 和 SCO 链路）。

**`NGM_HCI_NODE_GET_STAT`** 返回各种统计计数器。

**`NGM_HCI_NODE_RESET_STAT`** 将所有统计计数器重置为零。

**NGM_HCI_NODE_SET_LINK_POLICY_SETTINGS_MASK** 设置当前链路策略设置掩码。创建新的 ACL 连接后，HCI 节点会尝试为 ACL 连接设置链路策略。默认情况下，会启用每个支持的链路管理器（LM）模式。用户可以通过设置链路策略设置掩码来覆盖此设置，掩码指定要启用的 LM 模式。

**NGM_HCI_NODE_GET_LINK_POLICY_SETTINGS_MASK** 返回当前链路策略设置掩码。

**NGM_HCI_NODE_SET_PACKET_MASK** 设置当前数据包掩码。创建新的基带（ACL 或 SCO）连接时，HCI 节点会指定设备支持的每种数据包类型。用户可以通过设置数据包掩码来覆盖此设置，掩码指定用于新基带连接的数据包类型。

**NGM_HCI_NODE_GET_PACKET_MASK** 返回当前数据包掩码。

**NGM_HCI_NODE_SET_ROLE_SWITCH** 设置角色切换的值。当此值不为零时启用角色切换。这是默认状态。注意，蓝牙链路层的实际角色切换只有在硬件支持角色切换且已启用时才会执行。

**NGM_HCI_NODE_GET_ROLE_SWITCH** 返回节点的角色切换值。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在所有钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), hccontrol(8), ngctl(8)

## 历史

`hci` 节点类型实现于 FreeBSD 5.0。

## 作者

Maksim Yevmenkin <m_evmenkin@yahoo.com>

## 缺陷

很可能存在缺陷。如发现请报告。
