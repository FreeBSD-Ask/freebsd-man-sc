# host(1)

`host` — DNS 查询工具

## 名称

`host`

## 概要

`host [-aCdilrsTvw46] [-c class] [-N ndots] [-R number] [-t type] [-W wait] name [server]`

## 描述

`host` 是一个用于执行 DNS 查询的简单工具。通常用于在域名和 IP 地址之间进行转换。

`name` 是要查询的域名。它也可以是点分十进制 IPv4 地址或冒号分隔的 IPv6 地址，此时 `host` 默认对该地址执行反向查询。

未提供 `name` 时，`host` 会打印简短的用法说明。

`server` 是可选参数，可以是 `host` 应查询的域名服务器（而非 **/etc/resolv.conf** 中列出的服务器）的域名或 IP 地址。当 `server` 为域名时，使用系统解析器获取其地址。

支持的选项：

**`-a`** 进行类型为 `ANY` 的详细查询。等同于 `-v` `-t` `ANY`。

**`-C`** 从区域 `name` 的所有权威域名服务器查询 `SOA` 记录。域名服务器列表通过对 `name` 进行 `NS` 查询获取。

**`-c`** `class` 执行类别为 `class` 的 DNS 查询。可识别的类别包括 `IN`（Internet）、`CH`（Chaosnet）、`HS`（Hesiod）、`NONE`、`ANY` 和 `CLASSN`（其中 `N` 为 1 到 255 的数字）。默认为 `IN`。

**`-d`** 产生详细输出。这是 `-v` 的同义词，提供它是为了向后兼容。

**`-i`** 对 IPv6 地址的反向查询使用 IP6.INT 域（定义于 RFC1886；注意 RFC4159 已废弃 IP6.INT）。默认使用 IP6.ARPA。

**`-l`** 通过执行区域传送（`AXFR`）列出区域 `name` 中的所有 `NS`、`PTR`、`A` 和 `AAAA` 记录。可将此选项与 `-a` 组合以打印所有记录，或与 `-t` 组合仅打印特定记录。

**`-N`** `ndots` 将至少包含这么多点号的名字视为绝对名称。即，在查阅 **/etc/resolv.conf** 中的 `domain` 或 `search` 选项之前，先尝试直接解析它们。

**`-r`** 通过清除查询的 RD（"期望递归"）位，向域名服务器执行非递归查询。

**`-R`** `number` 当查询未及时收到应答时，重试这么多次。默认重试 1 次。如果 `number` 为负数或零，则使用 1。

**`-s`** 如实报告 SERVFAIL 响应，不忽略它们。

**`-T`** 通过 TCP 查询域名服务器。默认使用 UDP，但 `AXFR` 和 `IXFR` 查询除外，它们需要 TCP。如果 UDP 响应被截断（即设置了 TC 位），`host` 还会在 TCP 模式下重试 UDP 查询。

**`-t`** `type` 执行类型为 `type` 的 DNS 查询，`type` 可以是任何标准查询类型名（`A`、`CNAME`、`MX`、`TXT` 等）、通配符查询（`ANY`）或 `TYPEN`（其中 `N` 为 1 到 65535 的数字）。对于 `IXFR`（增量区域传送）查询，可以通过在等号后附加数字来指定起始序列号（例如 `-t` `IXFR=12345678`）。默认查询 `A`、`AAAA` 和 `MX` 记录，除非指定了 `-C` 或 `-l` 选项（此时执行 `SOA` 或 `AXFR` 查询），或 `name` 是有效的 IP 地址（此时使用 `PTR` 查询执行反向查询）。

**`-v`** 产生详细输出。

**`-w`** 永远（或非常长时间地）等待域名服务器的响应。

**`-W`** `wait` 等待这么多少秒后超时，等待域名服务器的回复。如果 `wait` 为负数或零，则使用 1。默认 TCP 连接等待 10 秒，UDP 等待 5 秒（两者均可重试，参见选项 `-R`）。

**`-4`** 仅使用 IPv4 传输。

**`-6`** 仅使用 IPv6 传输。

## 文件

**/etc/resolv.conf**

## 参见

drill(1), resolv.conf(5)

## 兼容性

`host` 力求在支持的选项和产生的输出方面，与 BIND9 发行版中的 'host' 工具合理兼容。以下是已知的显著差异列表：

- 不支持调试选项（`-D` 和 `-m`）。
- 不支持查询类别 `CLASS0` 和类型 `TYPE0`。
- 域名中的反斜杠会被特殊处理。
- 最多支持 255 次重试（选项 `-R`）。
- 某些资源记录的格式不同。例如，`RRSIG` 和 `DNSKEY` 记录显示时不带空格。
- 解析 **/etc/resolv.conf** 时，会忽略 `sortlist` 和 `options` 命令。当存在多个 `search` 和/或 `domain` 命令时，`host` 首先使用最后一个 `domain` 命令，然后使用所有 `search` 命令，而 BIND9 的 'host' 使用最后指定的命令。
- 详细数据包输出中缺少 'Pseudosection TSIG'。

## 作者

Vitaly Magerya <magv@tx97.net>
