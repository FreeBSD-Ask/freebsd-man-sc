# tcpdrop(8)

`tcpdrop` — 丢弃 TCP 连接

## 名称

`tcpdrop`

## 概要

`tcpdrop local-address local-port foreign-address foreign-port`
`tcpdrop [-l] -a`
`tcpdrop [-l] -C cc-algo [-S stack] [-s state]`
`tcpdrop [-l] [-C cc-algo] -S stack [-s state]`
`tcpdrop [-l] [-C cc-algo] [-S stack] -s state`

## 描述

`tcpdrop` 命令可用于从命令行丢弃 TCP 连接。

如果指定 `-a`，则 `tcpdrop` 将尝试丢弃所有 TCP 连接。

如果指定 `-C` `cc-algo`，则 `tcpdrop` 将尝试丢弃所有使用 TCP 拥塞控制算法 `cc-algo` 的连接。

如果指定 `-S` `stack`，则 `tcpdrop` 将尝试丢弃所有使用 TCP 协议栈 `stack` 的连接。

如果指定 `-s` `state`，则 `tcpdrop` 将尝试丢弃所有处于 `state` 状态的 TCP 连接。`state` 为 `SYN_SENT`、`SYN_RCVD`、`ESTABLISHED`、`CLOSE_WAIT`、`FIN_WAIT_1`、`CLOSING`、`LAST_ACK`、`FIN_WAIT_2` 或 `TIME_WAIT` 之一。

如果同时指定了 `-C` `cc-algo`、`-S` `stack` 和 `-s` `state` 中的多个，`tcpdrop` 将尝试丢弃所有使用拥塞控制算法 `cc-algo`、处于 `state` 状态且（如果指定）使用 TCP 协议栈 `stack` 的 TCP 连接。由于处于 `TIME_WAIT` 状态的 TCP 连接不与任何 TCP 协议栈关联，将 `-s` `TIME_WAIT` 选项与 `-S` `stack` 选项组合使用会导致 `tcpdrop` 不丢弃任何 TCP 连接。

`-l` 标志可与 `-a`、`-C`、`-S` 或 `-s` 选项一起使用，用于列出逐个丢弃所有相应 TCP 连接的 tcpdrop 调用。

如果未指定 `-a`、`-C`、`-S` 或 `-s` 中的任何一个选项，则仅丢弃给定本地地址 `local-address`、端口 `local-port` 与外部地址 `foreign-address`、端口 `foreign-port` 之间的连接。

地址和端口可通过名称或数值指定。同时支持 IPv4 和 IPv6 地址格式。

地址和端口可用句点或冒号分隔，而非用空格分隔。

## 退出状态

`tcpdrop` 工具成功时退出状态为 0，出错时大于 0。

## 实例

如果到 httpd(8) 的连接导致网络链路拥塞，可以丢弃负责的 TCP 会话：

```sh
# sockstat -c | grep httpd
www      httpd      16525 3  tcp4 \
	192.168.5.41:80      192.168.5.1:26747
```

以下命令将丢弃该连接：

```sh
# tcpdrop 192.168.5.41 80 192.168.5.1 26747
```

以下命令将丢弃除到/来自端口 22（sshd(8) 使用的端口）外的所有连接：

```sh
# tcpdrop -l -a | grep -vw 22 | sh
```

丢弃所有使用 new-reno 拥塞控制算法的 TCP 连接：

```sh
# tcpdrop -C new-reno
```

以下命令将丢弃所有使用 TCP 协议栈 rack 的连接：

```sh
# tcpdrop -S rack
```

丢弃所有处于 LAST_ACK 状态的 TCP 连接：

```sh
# tcpdrop -s LAST_ACK
```

丢弃所有使用 new-reno 拥塞控制算法、TCP 协议栈 rack 且处于 LAST_ACK 状态的 TCP 连接：

```sh
# tcpdrop -C new-reno -S rack -s LAST_ACK
```

## 参见

[netstat(1)](../man1/netstat.1.md), [sockstat(1)](../man1/sockstat.1.md), [tcp(4)](../man4/tcp.4.md), [tcp_functions(9)](../man9/tcp_functions.9.md)

## 作者

Markus Friedl <markus@openbsd.org>
Juli Mallett <jmallett@FreeBSD.org>
