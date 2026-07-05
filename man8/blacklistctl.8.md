# blacklistctl.8

`blacklistctl` — 显示和修改 blacklistd 数据库的状态

## 名称

`blacklistctl`

## 概要

`blacklistctl dump [-abdnrw] [-D dbname]`

## 描述

`blacklistctl` 是一个用于显示和修改 blacklistd(8) 数据库状态的程序。支持以下子命令：

### dump

`dump` 子命令支持以下选项：

**`-a`** 显示所有数据库条目，默认仅显示活动条目。非活动条目的最后访问时间（或使用 `-r` 时的剩余时间）会显示为 `never`。

**`-b`** 仅显示已阻止的条目。

**`-D`** `dbname` 指定要使用的 `blacklistd` 数据库文件的位置。默认为 **/var/db/blocklistd.db**。

**`-d`** 提高调试级别。

**`-n`** 不显示标题行。

**`-r`** 显示剩余阻止时间，而不是最后活动时间。

**`-w`** 通常地址列宽适用于 IPv4，使用 `-w` 标志可使显示宽度足以容纳 IPv6 地址。

`dump` 子命令的输出由标题行（除非指定了 `-n`）和数据库中每条记录对应的一行组成，每行包含以下列：

**`address/ma:port`** 与该数据库条目关联的客户端连接的远程地址、掩码和本地端口号。

**`id`** 该列显示与数据库条目关联的包过滤规则标识符。对于不为每条规则创建唯一标识符的包过滤器，该列可能仅显示单词 `OK`。

**`nfail`** 报告的该客户端在所注明端口上的失败次数，以及在阻止前允许的失败次数（使用 `-a` 时显示为星号 <*>）。

**`last access` | `remaining time`** 最后一次报告该客户端尝试访问的时间，或使用 `-r` 时显示阻止该客户端的规则被移除前的剩余时间。

## 参见

blacklistd(8)

## 注释

`blacklistctl` 程序已更名为 blocklistctl(8)。

有时报告的失败尝试次数可能超过 blacklistd(8) 配置的阻止阈值。这可能是因为规则已被手动移除，或者在规则阻止被添加时还有更多尝试正在进行中。这种情况属于正常现象；此时 blacklistd(8) 会先尝试移除现有规则，然后重新添加，以确保仅有一条规则处于活动状态。

## 历史

`blacklistctl` 首次出现在 NetBSD 7 中。FreeBSD 对 `blacklistctl` 的支持实现于 FreeBSD 11。

## 作者

Christos Zoulas
