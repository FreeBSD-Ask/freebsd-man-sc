# mac_portacl.4

`mac_portacl` — 网络端口访问控制策略

## 名称

`mac_portacl`

## 概要

要将端口访问控制策略编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_PORTACL

或者，要在引导时加载端口访问控制策略模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_portacl_load= YES
```

## 描述

`mac_portacl` 策略允许管理员通过 [sysctl(8)](../man8/sysctl.8.md) 接口在管理层面限制对本地 UDP 和 TCP 端口的绑定。

要启用 `mac_portacl` 策略，必须在套接字上强制执行 MAC 策略（参见 [mac(4)](mac.4.md)），并且受 `mac_portacl` 保护的端口不得包含在 `net.inet.ip.portrange.reservedlow` 和 `net.inet.ip.portrange.reservedhigh` [sysctl(8)](../man8/sysctl.8.md) MIB 指定的范围内。

`mac_portacl` 策略仅影响由用户进程显式绑定的端口（用于监听/出站 TCP 套接字，或发送/接收 UDP 套接字）。此策略不会限制为进程未显式选择端口的出站连接隐式绑定的端口：这些端口由 IP 协议栈自动选择。

当启用 `mac_portacl` 时，它将控制对端口的绑定访问，端口号最高至 `security.mac.portacl.port_high` [sysctl(8)](../man8/sysctl.8.md) 变量中设置的端口号。默认情况下，如果端口访问控制列表未明确允许，则绑定到 `mac_portacl` 受控端口的所有尝试都会失败；但如果 [sysctl(8)](../man8/sysctl.8.md) 变量 `security.mac.portacl.suser_exempt` 设置为非零值，则超级用户绑定将被允许。

### 运行时配置

以下 [sysctl(8)](../man8/sysctl.8.md) MIB 可用于微调此 MAC 策略的强制执行。除 `security.mac.portacl.rules` 外，所有 [sysctl(8)](../man8/sysctl.8.md) 变量也可在 loader.conf(5) 中设置为 [loader(8)](../man8/loader.8.md) 可调参数。

> `idtype : id : protocol : port` [, `idtype : id : protocol : port , ...`]

**`idtype`** 描述要执行的主体匹配类型。可以是 `uid`（按用户 ID 匹配）或 `gid`（按组 ID 匹配）。

**`id`** 允许绑定到指定端口的用户或组 ID（取决于 `idtype`）。注意：用户和组名无效；只能使用实际的 ID 数字。

**`protocol`** 描述此条目适用的协议。支持 `tcp` 或 `udp`。

**`port`** 描述此条目适用的端口。注意：MAC 安全策略不能通过允许其他安全系统策略可能拒绝的访问来覆盖这些策略，例如 `net.inet.ip.portrange.reservedlow` / `net.inet.ip.portrange.reservedhigh`。如果指定的端口落在该范围内，`mac_portacl` 条目将不起作用（即，即使是指定的用户/组也可能无法绑定到指定端口）。

**`security.mac.portacl.enabled`** 强制执行 `mac_portacl` 策略。（默认值：1。）

**`security.mac.portacl.port_high`** `mac_portacl` 将强制执行规则的最高端口号。（默认值：1023。）

**`security.mac.portacl.rules`** 端口访问控制列表按以下格式指定：

**`security.mac.portacl.suser_exempt`** 允许超级用户（即 root）绑定到所有 `mac_portacl` 保护的端口，即使端口访问控制列表未明确允许也是如此。（默认值：1。）

**`security.mac.portacl.autoport_exempt`** 允许应用程序使用自动绑定到端口 0。应用程序在将 IP 地址绑定到套接字时使用端口 0 作为自动端口分配的请求。此可调参数将端口 0 分配豁免于规则检查。（默认值：1。）

## 参见

mac(3), [ip(4)](ip.4.md), [mac_biba(4)](mac_biba.4.md), [mac_bsdextended(4)](mac_bsdextended.4.md), [mac_ddb(4)](mac_ddb.4.md), [mac_ifoff(4)](mac_ifoff.4.md), [mac_mls(4)](mac_mls.4.md), [mac_none(4)](mac_none.4.md), [mac_partition(4)](mac_partition.4.md), [mac_seeotheruids(4)](mac_seeotheruids.4.md), [mac_test(4)](mac_test.4.md), [mac(9)](../man9/mac.9.md)

## 历史

MAC 首次出现于 FreeBSD 5.0，`mac_portacl` 首次出现于 FreeBSD 5.1。

## 作者

本软件由 NAI Labs（Network Associates Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下，作为 DARPA CHATS 研究计划的一部分，贡献给 FreeBSD 项目。
