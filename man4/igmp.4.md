# igmp.4

`igmp` — Internet 组管理协议

## 名称

`igmp`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`#include <netinet/in_systm.h>`

`#include <netinet/ip.h>`

`#include <netinet/igmp.h>`

`Ft int Fn socket AF_INET SOCK_RAW IPPROTO_IGMP`

## 描述

IGMP 是 IPv4 主机和路由器用于传播多播组成员身份信息的控制平面协议。通常此协议不会被直接使用，仅由内核本身响应用户应用程序的多播成员请求而使用。路由协议可以打开 raw 套接字以直接与 `igmp` 交互。

自 FreeBSD 8.0 起，实现了 IGMP 版本 3。这增加了对源特定多播（SSM）的支持，应用程序可借此告知上游多播路由器它们仅对从特定源接收多播流感兴趣。

## SYSCTL 变量

**net.inet.igmp.stats** 此不透明的只读变量向 [netstat(1)](../man1/netstat.1.md) 暴露协议栈范围的 IGMPv3 协议统计信息。

**net.inet.igmp.ifinfo** 此不透明的只读变量向 ifmcstat(8) 暴露每条链路的 IGMPv3 状态。

**net.inet.igmp.gsrdelay** 此变量指定处理组与源特定查询（GSR）的时间阈值（秒）。由于 GSR 查询处理需要在主机上维护状态，可能需要分配内存，因此是拒绝服务（DoS）的潜在攻击点。如果在此阈值内收到多个 GSR 查询，将丢弃它们，以缓解 DoS 的潜在威胁。

**net.inet.igmp.default_version** 此变量控制所有链路上使用的默认 IGMP 版本。此 sysctl 默认通常设置为 3。

**net.inet.igmp.legacysupp** 如果此变量非零，则在链路上接收到的 IGMP v1 和 v2 成员报告将被允许抑制本主机原本会发出的 IGMP v3 状态变更报告。此 sysctl 默认通常启用。

**net.inet.igmp.v2enable** 如果此变量非零，则本主机将处理 IGMP v2 成员查询，并启用向后兼容，直到 v2“Old Querier Present”定时器到期。此 sysctl 默认通常启用。

**net.inet.igmp.v1enable** 如果此变量非零，则本主机将处理 IGMP v1 成员查询，并启用向后兼容，直到 v1“Old Querier Present”定时器到期。此 sysctl 默认通常启用。

**net.inet.igmp.sendlocal** 如果此变量非零，则会针对 224.0.0.0/24 链路范围前缀中的组发出 IGMP 状态变更。如果在具有嗅探 IGMP 流量以缓解整个网络中多播传播的第 2 层设备的网络环境中部署 FreeBSD，建议启用此行为。此 sysctl 默认通常启用。

**net.inet.igmp.sendra** 如果此变量非零，则 IGMP v2 和 v3 报告将包含 IP Router Alert 选项。此 sysctl 默认通常启用。

**net.inet.igmp.recvifkludge** 如果此变量非零，则将接收到的以 0.0.0.0 为源的 IGMP 报告重写为包含子网地址。当链路上存在尚未配置主 IPv4 地址的主机时，此功能很有用。此 sysctl 默认通常启用。

## 参见

[netstat(1)](../man1/netstat.1.md), sourcefilter(3), [inet(4)](inet.4.md), [multicast(4)](multicast.4.md), ifmcstat(8)

## 历史

`igmp` 手册页重新出现于 FreeBSD 8.0。
