# nlsysevent.4

`nlsysevent` — 基于 Netlink 的内核事件通知模块

## 名称

`nlsysevent`

## 概要

`要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
nlsysevent_load="YES"
```

`或者，要在运行时加载模块：`

```sh
kldload nlsysevent
```

## 描述

`nlsysevent` 内核模块提供一个 [netlink(4)](netlink.4.md) 通用 Netlink 接口，用于接收内核设备事件。它挂钩到 [devctl(4)](devctl.4.md) 通知系统，并将所有内核事件作为通用 Netlink 多播消息在 `NETLINK_GENERIC` 协议族下重新发布。

这提供了从 **`/dev/devctl`** 读取事件（由 devd(8) 使用）的替代方案，其优势是多个消费者可以同时订阅事件，且消费者可以有选择地订阅特定事件组。

### 通用 Netlink 协议族

该模块注册一个名为“`nlsysevent`”的通用 Netlink 协议族。动态分配的族标识符可使用 [genetlink(4)](genetlink.4.md) 中描述的标准 `CTRL_CMD_GETFAMILY` 请求来解析。

### 命令

定义了以下命令：

**`NLSE_CMD_NEWEVENT`** 在内核事件发生时发送。此消息从不由用户态主动请求；它只投递给已订阅一个或多个多播组的套接字。

### 属性

每条 `NLSE_CMD_NEWEVENT` 消息包含以下 TLV 属性：

**`NLSE_ATTR_SYSTEM`**（字符串）产生事件的系统名称（例如“`ACPI`”、“`IFNET`”、“`USB`”）。

**`NLSE_ATTR_SUBSYSTEM`**（字符串）系统内的子系统名称。

**`NLSE_ATTR_TYPE`**（字符串）事件类型。

**`NLSE_ATTR_DATA`**（字符串）与事件关联的可选附加数据。如果没有提供附加数据，此属性可能不存在。

### 多播组

该模块为每个系统名称创建一个多播组。模块加载时预注册以下组：

| |
| --- |
| `ACPI` |
| `AEON` |
| `CAM` |
| `CARP` |
| `coretemp` |
| `DEVFS` |
| `device` |
| `ETHERNET` |
| `GEOM` |
| `HYPERV_NIC_VF` |
| `IFNET` |
| `INFINIBAND` |
| `KERNEL` |
| `nvme` |
| `PMU` |
| `RCTL` |
| `USB` |
| `VFS` |
| `VT` |
| `ZFS` |

当内核事件中出现新的系统名称时，会动态创建附加组，最多可达 64 个组。

给定系统名称的组标识符可通过 `CTRL_CMD_GETFAMILY` 解析，然后使用 `NETLINK_ADD_MEMBERSHIP` 套接字选项订阅。

## 实例

可以使用 genl(1) 工具监视事件：

```sh
genl monitor nlsysevent
```

## 参见

genl(1), [snl(3)](../man3/snl.3.md), [devctl(4)](devctl.4.md), [genetlink(4)](genetlink.4.md), [netlink(4)](netlink.4.md), devd(8)

## 历史

`nlsysevent` 模块首次出现于 FreeBSD 15.0。

## 作者

`nlsysevent` 内核模块及本手册页由 Baptiste Daroussin <bapt@FreeBSD.org> 编写。
