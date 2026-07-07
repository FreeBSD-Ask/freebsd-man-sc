# bluetooth.protocols(5)

`bluetooth.protocols` — 蓝牙协议服务多路复用器数据库

## 名称

`bluetooth.protocols`

## 描述

**/etc/bluetooth/protocols** 文件包含有关已知蓝牙协议服务多路复用器（Protocol Service Multiplexor）值的信息。对于每个蓝牙协议服务多路复用器，应存在一行包含以下信息：

```sh
正式协议服务多路复用器名称
正式协议服务多路复用器值
别名
```

各字段之间由任意数量的空格和/或制表符分隔。`#` 表示注释的开始；从该字符到行末的内容不会被搜索该文件的例程解释。

蓝牙协议服务多路复用器名称可包含除字段分隔符、换行符或注释字符以外的任何可打印字符。

## 文件

**/etc/bluetooth/protocols**

## 参见

bluetooth(3)

## 作者

Maksim Yevmenkin <m_evmenkin@yahoo.com>
