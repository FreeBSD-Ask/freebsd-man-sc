# blackhole.4

`blackhole` — 静默丢弃被拒绝的 SCTP、TCP 或 UDP 数据包

## 名称

`blackhole`

## 概要

`sysctl net.inet.sctp.blackhole[={0 | 1 | 2}]`
`sysctl net.inet.tcp.blackhole[={0 | 1 | 2 | 3}]`
`sysctl net.inet.tcp.blackhole_local[={0 | 1}]`
`sysctl net.inet.udp.blackhole[={0 | 1}]`
`sysctl net.inet.udp.blackhole_local[={0 | 1}]`

## 描述

`blackhole` [sysctl(8)](../man8/sysctl.8.md) MIB 用于控制系统在收到针对没有监听套接字的 SCTP、TCP 或 UDP 端口的连接请求时，或在监听套接字上收到意外数据包时的行为。

黑洞行为有助于减缓正在对系统进行端口扫描以试图检测脆弱服务的攻击者，也可能减缓拒绝服务攻击的企图。

黑洞行为默认禁用。若启用，本地发起的数据包仍会获得响应，除非同时强制启用了 `net.inet.tcp.blackhole_local`（针对 TCP）和/或 `net.inet.udp.blackhole_local`（针对 UDP）。

### SCTP

将 SCTP 黑洞 MIB 设置为数值 1 会阻止在响应收到的 INIT 时发送 ABORT 数据包。设置为数值 2 的作用与之相同，但还会在收到意外数据包时阻止发送 ABORT 数据包。

### TCP

正常情况下，当 TCP SYN 段到达一个没有套接字接受连接的端口时，系统会返回一个 RST 段，并丢弃传入的 SYN 段。发起连接的系统会看到“Connection refused”。将 TCP 黑洞 MIB 设置为数值 1 时，传入的 SYN 段仅被丢弃，不发送 RST，使系统看起来像一个黑洞。将 MIB 设置为数值 2 时，到达关闭端口的任何段都会被丢弃且不返回 RST。将 MIB 设置为数值 3 时，到达关闭端口的任何段或在监听端口上收到的意外段都会被丢弃且不发送 RST 应答。这在一定程度上提供了针对隐蔽端口扫描的保护。

### UDP

启用黑洞行为会关闭对到达无监听套接字端口的 UDP 数据报的 ICMP 端口不可达消息发送。需要注意的是，此行为会阻止远程系统对该系统运行 traceroute(8)。

## 警告

SCTP、TCP 和 UDP 黑洞功能不应被视为防火墙方案的替代品。更好的安全性应由 `blackhole` [sysctl(8)](../man8/sysctl.8.md) MIB 与某个可用的防火墙软件包结合使用构成。

此机制不能替代系统安全加固，应与其他安全机制配合使用。

## 参见

[ip(4)](ip.4.md), [sctp(4)](sctp.4.md), [tcp(4)](tcp.4.md), [udp(4)](udp.4.md), ipf(8), [ipfw(8)](../man8/ipfw.8.md), pfctl(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

TCP 和 UDP `blackhole` MIB 首次出现于 FreeBSD 4.0。

SCTP `blackhole` MIB 首次出现于 FreeBSD 9.1。

## 作者

Geoffrey M. Rehmet
