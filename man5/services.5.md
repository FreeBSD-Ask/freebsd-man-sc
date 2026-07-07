# services(5)

`services` — Internet 服务名和端口号数据库

## 名称

`services`

## 描述

`services` 文件包含有关 Internet 中已知服务的信息。对于每种服务应单独占一行，包含以下信息：

```sh
official service name
port number
protocol name
aliases
```

各项之间由任意数量的空格和/或制表符分隔。端口号和协议名被视为单个*项*；使用“/”分隔端口和协议（例如“512/tcp”）。`#` 表示注释开始；从 `#` 到行尾的字符不会被搜索该文件的例程解释。

服务名可以包含除字段分隔符、换行符或注释字符以外的任何可打印字符。

如果在 [nsswitch.conf(5)](nsswitch.conf.5.md) 中将 “db” 指定为数据源，则会搜索 **/var/db/services.db**。在修改了 services 文件后，需要使用 services_mkdb(8) 更新 **/var/db/services.db** 中的数据库。

## NIS 交互

可以通过在 **/etc/services** 文件中单独一行添加一个 “+” 来启用对 NIS `services.byname` 映射的访问。这会使 NIS 服务映射的内容插入到 “+” 出现的位置。

## 文件

**`/etc/services`** `services` 文件位于 **/etc**。

## 参见

getservent(3), [nsswitch.conf(5)](nsswitch.conf.5.md), services_mkdb(8)

## 历史

`services` 文件格式出现于 4.2BSD。

## 缺陷

应使用名称服务器而不是静态文件。
