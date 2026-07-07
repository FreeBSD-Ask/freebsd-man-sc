# wg(4)

`wg` — WireGuard 协议驱动

## 名称

`wg`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device wg

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_wg_load="YES"
```

## 描述

`wg` 驱动提供虚拟专用网络（VPN）接口，使用 WireGuard 协议与其他 WireGuard 对端安全交换三层流量。

`wg` 接口识别一个或多个对端，按需与每个对端建立安全隧道，并跟踪每个对端的 UDP 端点以便交换加密流量。

可在运行时使用 `ifconfig wgN create` 命令创建接口。接口本身可使用 wg(8) 进行配置。

以下术语表提供了 WireGuard 术语的简要概述：

**对端（Peer）** 对端通过安全隧道交换 IPv4 或 IPv6 流量。每个 `wg` 接口可配置为识别一个或多个对端。

**密钥（Key）** 每个对端使用其私钥和相应的公钥向其他人标识自己。对端使用自己的私钥和对端的公钥配置 `wg` 接口。

**预共享密钥（Pre-shared key）** 除了公钥外，每对对端还可配置唯一的预共享对称密钥。这用于其握手，以防止在对端的 Diffie-Hellman 交换攻击变得可行时，对端的加密隧道被攻破。这是可选的，但建议使用。

**允许的 IP 地址（Allowed IP addresses）** 单个 `wg` 接口可维护连接不同网络的并发隧道。因此，接口为其隧道流量实现基本的路由和反向路径过滤功能。这些功能引用针对每个对端配置的一组允许 IP 地址范围。接口将出站隧道流量路由到配置了最具体匹配允许 IP 地址范围的对端，如果不存在此类匹配则丢弃。接口仅接受来自为传入流量配置了最具体匹配允许 IP 地址范围的对端的隧道流量，如果不存在此类匹配则丢弃。也就是说，路由到给定对端的隧道流量无法通过同一 `wg` 接口的另一个对端返回。这确保了对端无法伪造彼此的流量。

**握手（Handshake）** 两个对端握手以相互认证并建立一系列共享的临时加密密钥。任一对端都可发起握手。握手仅在有待发送流量时发生，并在传输期间每两分钟重复一次。

**无连接（Connectionless）** 由于握手行为，不存在连接或断开状态。

### 密钥

WireGuard 的私钥可从任何足够安全的随机源生成。Curve25519 密钥和预共享密钥均长 32 字节，通常以 base64 编码以方便使用。

可使用 wg(8) 按如下方式生成密钥：

```sh
$ wg genkey
```

虽然有效的 Curve25519 密钥必须将 5 位设置为特定值，但这是由接口完成的，因此它接受任何随机的 32 字节 base64 字符串。

## NETMAP

[netmap(4)](netmap.4.md) 应用程序可以仿真模式打开 WireGuard 接口。netmap 应用程序将接收已解密、未封装的数据包，前面加有虚拟以太网头。Ethertype 字段将是 `ETHERTYPE_IP` 或 `ETHERTYPE_IPV6` 之一，具体取决于数据包的地址族。应用程序发送的数据包应类似地以虚拟以太网头开始；在数据包加密和隧道传输之前，该头将被剥离。

## 实例

创建 `wg` 接口并设置随机私钥。

```sh
# ifconfig wg0 create
# wg genkey | wg set wg0 listen-port 54321 private-key /dev/stdin
```

从 `wg` 接口检索关联的公钥。

```sh
$ wg show wg0 public-key
```

使用其公钥连接到特定端点并设置允许的 IP 地址：

```sh
# wg set wg0 peer '7lWtsDdqaGB3EY9WNxRN3hVaHMtu1zXw71+bOjNOVUw=' endpoint 10.0.1.100:54321 allowed-ips 192.168.2.100/32
```

移除对端：

```sh
# wg set wg0 peer '7lWtsDdqaGB3EY9WNxRN3hVaHMtu1zXw71+bOjNOVUw=' remove
```

## 诊断

`wg` 接口支持运行时调试，可使用以下命令启用：

> `ifconfig wgN debug`

一些常见的错误消息包括：

- 对端未将本地接口配置为对端。对端必须能够相互认证。
- 对端端点 IP 地址配置不正确。
- 存在阻止主机之间通信的防火墙规则。

- Handshake for peer X did not complete after 5 seconds, retrying 对端 X 未回复我们的发起数据包，例如因为：
- Invalid handshake initiation 传入的握手数据包无法处理。这可能是因为本地接口不包含该对端的正确公钥。
- Invalid initiation MAC 传入的握手发起数据包的 MAC 无效。这可能是因为发起发送方拥有错误的握手接收方公钥。
- Packet has unallowed src IP from peer X 解密后，传入数据包的源 IP 地址未分配给对端 X 的允许 IP。

## 参见

[inet(4)](inet.4.md), [ip(4)](ip.4.md), [ipsec(4)](ipsec.4.md), [netintro(4)](netintro.4.md), [netmap(4)](netmap.4.md), [ovpn(4)](ovpn.4.md), ipf(5), [pf.conf(5)](../man5/pf.conf.5.md), [ifconfig(8)](../man8/ifconfig.8.md), [ipfw(8)](../man8/ipfw.8.md), wg(8)

> "WireGuard whitepaper".

## 历史

`wg` 设备驱动最早出现在 FreeBSD 13.2 中。

## 作者

`wg` 设备驱动由 Jason A. Donenfeld <Jason@zx2c4.com>、Matt Dunwoodie <ncon@nconroy.net>、Kyle Evans <kevans@FreeBSD.org> 和 Matt Macy <mmacy@FreeBSD.org> 编写。

本手册页由 Gordon Bergling <gbe@FreeBSD.org> 编写，基于 David Gwynne <dlg@openbsd.org> 编写的 OpenBSD 手册页。
