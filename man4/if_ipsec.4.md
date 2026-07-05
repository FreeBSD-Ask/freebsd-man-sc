# if_ipsec.4

`if_ipsec` — IPsec 虚拟隧道接口

## 名称

`if_ipsec`

## 概要

`if_ipsec` 网络接口是 FreeBSD IPsec 实现的一部分。要将其编译进内核，请将以下行放入内核配置文件中：

> options IPSEC

`如果内核编译时使用了以下选项，它也可作为 ipsec 内核模块的一部分加载：`

> options IPSEC_SUPPORT

## 描述

`if_ipsec` 网络接口用于创建基于路由的 VPN。它可在 IPv4 或 IPv6 上隧道传输 IPv4 和 IPv6 流量，并使用 ESP 对其进行保护。

`if_ipsec` 接口通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `create` 和 `destroy` 子命令动态创建和销毁。管理员必须配置 IPsec `tunnel` 端点地址。这些地址将用于 ESP 数据包的外层 IP 头。管理员还可以通过 [ifconfig(8)](../man8/ifconfig.8.md) 配置内层 IP 头的协议和地址，并修改路由表以将数据包路由通过 `if_ipsec` 接口。

`if_ipsec` 接口配置后会自动创建特殊的安全策略。这些策略可用于从 IKE 守护进程获取安全关联，而安全关联是建立 IPsec 隧道所必需的。也可以使用 setkey(8) 工具手动创建所需的安全关联。

每个 `if_ipsec` 接口都有一个额外的数字配置选项 `reqid` `id`。此 `id` 用于区分多个 `if_ipsec` 接口之间的流量和安全策略。`reqid` 可在接口创建时指定，也可稍后更改。如未指定，将自动分配。注意，更改 `reqid` 会导致生成新的安全策略，这可能需要创建新的安全关联。

## 实例

下面的示例展示了两台 FreeBSD 主机之间手动配置 IPsec 隧道的过程。主机 A 的 IP 地址为 192.168.0.3，主机 B 的 IP 地址为 192.168.0.5。

在主机 A 上：

```sh
ifconfig ipsec0 create reqid 100
ifconfig ipsec0 inet tunnel 192.168.0.3 192.168.0.5
ifconfig ipsec0 inet 172.16.0.3/16 172.16.0.5
setkey -c
add 192.168.0.3 192.168.0.5 esp 10000 -m tunnel -u 100 -E rijndael-cbc "VerySecureKey!!1";
add 192.168.0.5 192.168.0.3 esp 10001 -m tunnel -u 100 -E rijndael-cbc "VerySecureKey!!2";
^D
```

在主机 B 上：

```sh
ifconfig ipsec0 create reqid 200
ifconfig ipsec0 inet tunnel 192.168.0.5 192.168.0.3
ifconfig ipsec0 inet 172.16.0.5/16 172.16.0.3
setkey -c
add 192.168.0.3 192.168.0.5 esp 10000 -m tunnel -u 200 -E rijndael-cbc "VerySecureKey!!1";
add 192.168.0.5 192.168.0.3 esp 10001 -m tunnel -u 200 -E rijndael-cbc "VerySecureKey!!2";
^D
```

注意，主机 A 上的值 100 和主机 B 上的值 200 用作 reqid。在 setkey(8) 命令中必须使用相同的值作为策略条目的标识符。

## 参见

[gif(4)](gif.4.md), [gre(4)](gre.4.md), [ipsec(4)](ipsec.4.md), [ifconfig(8)](../man8/ifconfig.8.md), setkey(8)

## 作者

Andrey V. Elsukov <ae@FreeBSD.org>
