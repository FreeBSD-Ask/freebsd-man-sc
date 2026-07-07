# jls(8)

`jls` — 列出 jail

## 名称

`jls`

## 概要

`jls [--libxo] [-dhNnqsv] [-j jail] [parameter ...]`

`jls -c [-d] -j jail`

## 描述

`jls` 工具列出所有活动的 jail，或指定的 jail。每个 jail 由所列 `parameters` 的空格分隔值表示，每个 jail 一行（除非参数本身包含换行符）。伪参数 `all` 将显示所有可用的 jail 参数。可通过 `sysctl -d security.jail.param` 获取可用参数列表。有关一些核心参数的描述，请参见 [jail(8)](jail.8.md)。

如果未给出 `parameters` 或未给出 `-chns` 中的任何选项，将打印以下四列：jail 标识符（jid）、IP 地址（ip4.addr）、主机名（host.hostname）和路径（path）。

使用 `-c` 选项时，`jls` 不会产生任何输出（使用错误除外）。此模式仅用于检查单个 jail 是否存在，不接受任何 `parameter` 或打印选项标志。

可用选项如下：

**`--libxo`** 通过 libxo(3) 以多种人类和机器可读格式生成输出。有关命令行参数的详细信息，请参见 xo_options(7)。

**`-c`** 仅检查 jail 是否存在。

**`-d`** 列出 `dying` 以及活动的 jail。

**`-h`** 打印包含所列参数的标题行。如果命令行上未给出参数，则假定为 `all`。

**`-N`** 在标准显示模式下，打印每个 jail 的名称而不是其数字 ID。如果 jail 没有名称，则打印数字 ID。

**`-n`** 以 "name=value" 格式打印参数，每个参数前有其名称。如果命令行上未给出参数，则假定为 `all`。

**`-q`** 如果参数包含空格或引号，或为空字符串，则在参数两侧加引号。

**`-s`** 打印适合传递给 [jail(8)](jail.8.md) 的参数，跳过只读和未使用的参数。隐含 `-nq`。

**`-v`** 用每个 jail 的多行摘要扩展标准显示，包含以下参数：jail 标识符（jid）、主机名（host.hostname）、路径（path）、jail 名称（name）、jail 状态（dying）、cpuset ID（cpuset）、IP 地址（ip4.addr 和 ip6.addr）。

**`-j`** `jail` 要列出的 `jail` 的 jid 或名称。未指定此选项时，将列出所有活动的 jail。

## 参见

jail_get(2), libxo(3), xo_options(7), [jail(8)](jail.8.md), [jexec(8)](jexec.8.md)

## 历史

`jls` 工具在 FreeBSD 5.1 中加入。可扩展的 jail 参数在 FreeBSD 8.0 中引入。libxo 支持在 FreeBSD 11.0 中加入。
