# protocols(5)

`protocols` — 协议名称数据库

## 名称

`protocols`

## 描述

`protocols` 文件包含有关 IPv4 和 IPv6 用于标识下一层协议所分配的协议号的信息。每个协议应在文件中占一行，包含以下信息：

```sh
official protocol name
protocol number
aliases
```

各字段之间由任意数量的空格和/或制表符分隔。`#` 表示注释的开始；从 `#` 到行尾的字符不会被搜索该文件的例程解释。

协议名可以包含除字段分隔符、换行符或注释字符以外的任何可打印字符。

## 文件

**/etc/protocols** — `protocols` 文件位于 **/etc** 中。

## 参见

getprotoent(3)

"Internet Protocol and Related Headers"

"IANA Allocation Guidelines For Values In the Protocol Field", March 2000.

"IANA Allocation Guidelines for the Protocol Field", February 2008.

## 历史

`protocols` 文件格式出现于 4.2BSD，描述了“DARPA 互联网中使用的已知协议”。

## 缺陷

应该使用名称服务器而不是静态文件。
