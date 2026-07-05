# hosts.lpd.5

`hosts.lpd` — 允许使用本地打印服务的受信任主机

## 名称

`hosts.lpd`

## 描述

`hosts.lpd` 文件包含允许使用本地打印服务的主机名或 IP 地址列表。每个主机名或 IP 地址单独占一行。

如果你想允许所有主机访问，通常可以使用 NIS netgroups 功能，方法是添加一行只包含单个 `+` 字符的条目。

## 文件

**`/etc/hosts.lpd`** `hosts.lpd` 文件位于 **/etc**。

## 参见

printcap(5), lpd(8)
