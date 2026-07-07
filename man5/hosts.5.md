# hosts(5)

`hosts` — 主机名数据库

## 名称

`hosts`

## 描述

`hosts` 文件包含有关网络上已知主机的信息。它可以与 DNS 以及 NIS 映射 `hosts.byaddr` 和 `hosts.byname` 配合使用，由 [nsswitch.conf(5)](nsswitch.conf.5.md) 控制。对于每个主机，应存在单独一行，包含以下信息：

```sh
Internet address
official host name
aliases
```

各项之间由任意数量的空格和/或制表符分隔。`#` 表示注释开始；从 `#` 到行尾的字符不会被搜索该文件的例程解释。

此文件提供了名称服务器未运行时使用的备份。对于名称服务器，建议此文件中仅包含少量地址。这些地址包括 [ifconfig(8)](../man8/ifconfig.8.md) 在引导时所需的本地接口地址以及本地网络上的少量机器。

网络地址以 IPv4 的常规 "."（点）表示法或 IPv6 的冒号十六进制表示法指定，由 Internet 地址操作库 inet(3) 中的 inet_pton(3) 例程解析。主机名可以包含除字段分隔符、换行符或注释字符以外的任何可打印字符。

## 文件

**`/etc/hosts`** `hosts` 文件位于 **/etc**。

## 参见

gethostbyname(3), inet(3), [nsswitch.conf(5)](nsswitch.conf.5.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`hosts` 文件格式出现于 4.1cBSD。
