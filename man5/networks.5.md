# networks.5

`networks` — 网络名数据库

## 名称

`networks`

## 描述

`networks` 文件包含有关组成 DARPA Internet 的已知网络的信息。对于每个网络，应有如下信息占据一行：

```sh
official network name
network number
aliases
```

各项之间以任意数量的空格和/或制表符分隔。“`#`” 表示注释的开始；从该字符到行尾的内容不会被搜索该文件的例程所解释。此文件通常根据网络信息控制中心（NIC）维护的官方网络数据库创建，但可能需要进行本地修改以更新有关非官方别名和/或未知网络的信息。

网络号可以使用 Internet 地址操作库 inet(3) 中的 inet_network(3) 例程，以传统的 “`.`”（点）表示法指定。网络名可以包含除字段分隔符、换行符或注释字符以外的任何可打印字符。

## 文件

**/etc/networks** `networks` 文件位于 **/etc**。

## 参见

getnetent(3)

## 历史

`networks` 文件格式出现于 4.2BSD。

## 缺陷

应当使用域名服务器代替静态文件。
