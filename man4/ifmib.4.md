# ifmib(4)

`ifmib` — 网络接口的管理信息库

## 名称

`ifmib`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <sys/sysctl.h>`

`#include <sys/time.h>`

`#include <net/if.h>`

`#include <net/if_mib.h>`

## 描述

`ifmib` 设施是 sysctl(3) 接口的一个应用，用于向客户端应用程序（如 [netstat(1)](../man1/netstat.1.md)、slstat(8) 和 SNMP 管理代理）提供有关网络接口的管理信息。此信息以表的形式组织，表中每一行代表一个逻辑网络接口（硬件设备或诸如 [lo(4)](lo.4.md) 之类的软件伪设备）。表中有两列，每列包含单个结构：一列包含与所有接口相关的通用信息，另一列包含特定于该接口类的信息。（通常，如果存在并且可在内核中实现，后者会实现为该特定接口类定义的 SNMP MIB。）

通过 sysctl(3) MIB 的“`net.link.generic`”分支访问 `ifmib` 设施。sysctl(3) `name` 中每一级的清单常量定义于

`#include <net/if_mib.h>`

表中最后一行的索引由“`net.link.generic.system.ifcount`”给出（或使用清单常量 `CTL_NET`、`PF_LINK`、`NETLINK_GENERIC`、`IFMIB_SYSTEM`、`IFMIB_IFCOUNT`）。管理应用程序搜索特定接口时，应从第 1 行开始逐行遍历表，直到找到所需接口或达到接口计数为止。注意，表可能是稀疏的，即给定的行可能不存在，由 `errno` 为 Er ENOENT 指示。应忽略此类错误并检查下一行。

可通过以下过程访问所有接口通用的通用接口信息：

```sh
int
get_ifmib_general(int row, struct ifmibdata *ifmd)
{
	int name[6];
	size_t len;
	name[0] = CTL_NET;
	name[1] = PF_LINK;
	name[2] = NETLINK_GENERIC;
	name[3] = IFMIB_IFDATA;
	name[4] = row;
	name[5] = IFDATA_GENERAL;
	len = sizeof(*ifmd);
	return sysctl(name, 6, ifmd, &len, (void *)0, 0);
}
```

`struct ifmibdata` 中的字段如下：

`#include <net/if.h>`

`#include <net/if.h>`

**`ifmd_name`** (`char []`) 接口名称，包括单元号

**`ifmd_pcount`** (`int`) 混杂监听器数量

**`ifmd_flags`** (`int`) 接口的标志（定义于

**`ifmd_snd_len`** (`int`) 发送队列的当前瞬时长度

**`ifmd_snd_drops`** (`int`) 因发送队列已满而在该接口上丢弃的数据包数

**`ifmd_data`** (`struct if_data`) 来自中所定义结构的更多信息（参见 if_data(9)）

可通过检查 `IFDATA_LINKSPECIFIC` 列来检索特定于类的信息。注意，结构的形式和长度取决于接口类。对于 `IFT_ETHER`、`IFT_ISO88023` 和 `IFT_STARLAN` 接口，该结构称为“`struct ifmib_iso_8802_3`”（定义于

`#include <net/if_mib.h>`

并实现了 RFC 1650 中针对类以太网络 MIB 的超集。

## 参见

sysctl(3), [dtrace_mib(4)](dtrace_mib.4.md), [intro(4)](intro.4.md), [ifnet(9)](../man9/ifnet.9.md)

> F. Kastenholz, "Definitions of Managed Objects for the Ethernet-like Interface Types Using SMIv2", August 1994, RFC 1650.

## 历史

`ifmib` 接口最早出现于 FreeBSD 2.2。

## 缺陷

许多类以太网接口尚不支持以太网 MIB。无论如何，所有接口都自动支持通用 MIB。
