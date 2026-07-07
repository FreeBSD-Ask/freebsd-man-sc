# ftp-proxy(8)

`ftp-proxy` — Internet 文件传输协议代理守护进程

## 名称

`ftp-proxy`

## 概要

`ftp-proxy [-6Adrv] [-a address] [-b address] [-D level] [-m maxsessions] [-P port] [-p port] [-q queue] [-R address] [-T tag] [-t timeout]`

## 描述

`ftp-proxy` 是 Internet 文件传输协议的代理。FTP 控制连接应使用 [pf(4)](../man4/pf.4.md) 的 `rdr` 命令重定向到该代理，之后代理将代表客户端连接到服务器。

该代理允许数据连接通过，对其进行重写和重定向，以使用正确的地址。所有从客户端到服务器的连接都会被重写源地址，使其看起来来自代理。相应地，所有从服务器到代理的连接都会被重写目的地址，使其重定向到客户端。代理使用 [pf(4)](../man4/pf.4.md) 的 `anchor` 功能来实现此操作。

假设 FTP 控制连接从 $client 到 $server，代理使用 $proxy 源地址连接到服务器，并且协商端口为 $port，则 `ftp-proxy` 会将以下规则添加到各个 anchor 中。（这些示例规则使用 inet，但代理也支持 inet6。）

主动模式（PORT 或 EPRT）的情况：

```sh
rdr from $server to $proxy port $port -> $client
pass quick inet proto tcp \
    from $server to $client port $port
```

被动模式（PASV 或 EPSV）的情况：

```sh
nat from $client to $server port $port -> $proxy
pass in quick inet proto tcp \
    from $client to $server port $port
pass out quick inet proto tcp \
    from $proxy to $server port $port
```

可用选项如下：

**`-6`** IPv6 模式。代理将为所有通信预期并使用 IPv6 地址。IPv6 下仅允许扩展 FTP 模式 EPSV 和 EPRT。默认为 IPv4 模式。

**`-A`** 仅允许匿名 FTP 连接。允许用户“ftp”或用户“anonymous”。

**`-a`** `address` 代理将使用此地址作为到服务器的控制连接的源地址。

**`-b`** `address` 代理监听重定向控制连接的地址。默认为 **127.0.0.1**，在 IPv6 模式下为 **::1**。

**`-D`** `level` 调试级别，范围为 0 到 7。数值越高输出越详细。默认为 5。（这些级别对应 syslog(3) 级别。）

**`-d`** 不以守护进程方式运行。进程将留在前台，日志输出到标准错误。

**`-m`** `maxsessions` 并发 FTP 会话的最大数量。当代理达到此限制时，新连接将被拒绝。默认为 100 个会话。该限制最低可降至 1，最高可升至 500。

**`-P`** `port` 固定的服务器端口。仅与 `-R` 配合使用。默认为端口 21。

**`-p`** `port` 代理监听重定向连接的端口。默认为端口 8021。

**`-q`** `queue` 创建规则时附加队列 `queue`，以便数据连接可以排队。

**`-R`** `address` 固定的服务器地址，也称为反向模式。代理将始终连接到同一服务器，无论客户端原本想连接到哪里（在被重定向之前）。使用此选项可代理 NAT 后面的服务器，或将所有连接转发到另一个代理。

**`-r`** 在主动模式中将源端口重写为 20，以适应坚持要求此 RFC 特性的老旧客户端。

**`-T`** `tag` 过滤规则将为数据连接添加标签 `tag`，并且不使用 quick 匹配。这样可以在 `ftp-proxy` anchor 之后实现使用 `tagged` 关键字的替代规则。这些规则可以使用 `ftp-proxy` 本身未实现的特殊 [pf(4)](../man4/pf.4.md) 功能，如 route-to、reply-to、label、rtable、overload 等。

**`-t`** `timeout` 控制连接可以空闲的秒数，超过后代理将断开连接。最大值为 86400 秒，也是默认值。不要设置得过低，因为在进行大数据传输时控制连接通常处于空闲状态。

**`-v`** 在 `ftp-proxy` 提交的 pf 规则上设置“log”标志。使用两次可设置“log-all”标志。默认情况下 pf 规则不记录日志。

## 配置

要使用该代理，[pf.conf(5)](../man5/pf.conf.5.md) 需要以下规则。所有 anchor 都是必需的。请根据需要调整规则。

NAT 部分：

```sh
nat-anchor "ftp-proxy/*"
rdr-anchor "ftp-proxy/*"
rdr pass on $int_if proto tcp from $lan to any port 21 -> \
    127.0.0.1 port 8021
```

规则部分：

```sh
anchor "ftp-proxy/*"
pass out proto tcp from $proxy to any port 21
```

## 参见

[ftp(1)](../man1/ftp.1.md), [pf(4)](../man4/pf.4.md), [pf.conf(5)](../man5/pf.conf.5.md)

## 注意事项

如果系统运行在高于 1 的 securelevel(7) 下，[pf(4)](../man4/pf.4.md) 不允许修改规则集。在该级别下，`ftp-proxy` 无法向 anchor 添加规则，FTP 数据连接可能会被阻止。

协商的数据连接端口低于 1024 时不被允许。

出于安全原因，主动模式中协商的 IP 地址将被忽略。这使得第三方文件传输无法实现。

`ftp-proxy` 通过 chroot 到 **/var/empty** 并切换到用户“proxy”来放弃特权。
