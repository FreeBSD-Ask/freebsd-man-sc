# genetlink(4)

`genetlink` — 通用 Netlink

## 名称

`genetlink`

## 概要

`#include <netlink/netlink.h>`

`#include <netlink/netlink_generic.h>`

`Ft int Fn socket AF_NETLINK SOCK_DGRAM NETLINK_GENERIC`

## 描述

`NETLINK_GENERIC` 是一个“容器”族，用于动态注册属于各子系统的其他族。这些子系统在注册时提供一个字符串族名，并接收一个动态分配的族 ID。然后，应用程序使用分配的族标识符通过 netlink 访问该子系统提供的功能。有将字符串族名解析为族标识符的标准方法。这些族提供的通知组也有类似的机制。

所有通用 netlink 族共享一个公共头：

```sh
struct genlmsghdr {
	uint8_t		cmd;		/* 族内的命令 */
	uint8_t		version;	/* cmd 的 ABI 版本 */
	uint16_t	reserved;	/* 保留：设置为 0 */
};
```

族 ID 编码在基础 netlink 头的 `nlmsg_type` 中。`cmd` 字段是族内的命令标识符。`version` 字段是命令版本。

## 方法

通用 Netlink 框架提供基础族 `GENL_ID_CTRL`（"nlctrl"），具有固定的族 ID。此族用于列出所有已注册族的详细信息。

框架支持以下消息：

### CTRL_CMD_GETFAMILY

根据 `NLM_F_DUMP` 标志获取单个族或所有已注册的族。每个族以 `CTRL_CMD_NEWFAMILY` 消息的形式报告。内核识别以下过滤器：

CTRL_ATTR_FAMILY_ID	(uint16_t) 内核分配的当前族 ID
CTRL_ATTR_FAMILY_NAME	(string) 族名

### TLV

GENL_ADMIN_PERM		需要提升的权限
GENL_CMD_CAP_DO		操作是修改请求
GENL_CMD_CAP_DUMP	操作是获取/转储请求

**`CTRL_ATTR_OP_ID`** 操作（消息）编号。

**`CTRL_ATTR_OP_FLAGS`** 操作标志。支持以下标志：

**`CTRL_ATTR_MCAST_GRP_ID`** 可在 `NETLINK_ADD_MEMBERSHIP` setsockopt(2) 中使用的组 ID。

**`CTRL_ATTR_MCAST_GRP_NAME`** (string) 人类可读的组名。

**`CTRL_ATTR_FAMILY_ID`** (uint16_t) 动态分配的族标识符。

**`CTRL_ATTR_FAMILY_NAME`** (string) 族名。

**`CTRL_ATTR_HDRSIZE`** (uint32_t) 族强制头大小（通常为 0）。

**`CTRL_ATTR_MAXATTR`** (uint32_t) 该族有效的最大属性编号。

**`CTRL_ATTR_OPS`** (nested) 该族支持的操作列表。该属性由嵌套 TLV 列表组成，属性值从 0 开始单调递增。每个 TLV 中存在以下属性：

**`CTRL_ATTR_MCAST_GROUPS`** (nested) 该族支持的通知组列表。该属性由嵌套 TLV 列表组成，属性值从 0 开始单调递增。每个 TLV 中存在以下属性：

### 组

定义了以下组：

"notify"	在族注册/移除时通知。

## 参见

[snl(3)](../man3/snl.3.md), [netlink(4)](netlink.4.md)

## 历史

`NETLINK_GENERIC` 协议族出现于 FreeBSD 13.2。

## 作者

netlink 由 Alexander Chernikov <melifaro@FreeBSD.org> 实现。它源自 Ng Peng Nam Sean 在 2021 年 Google Summer of Code 中的项目。
