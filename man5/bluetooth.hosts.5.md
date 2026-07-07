# bluetooth.hosts(5)

`bluetooth.hosts` — 蓝牙主机名数据库

## 名称

`bluetooth.hosts`

## 描述

**/etc/bluetooth/hosts** 文件包含有关已知蓝牙主机的信息。对于每个蓝牙主机，应存在一行包含以下信息：

```sh
蓝牙地址
正式主机名
别名
```

各字段之间由任意数量的空格和/或制表符分隔。`#` 表示注释的开始；从该字符到行末的内容不会被搜索该文件的例程解释。

蓝牙地址以六个由冒号分隔的十六进制字节指定（BD_ADDR）。主机名可包含除字段分隔符、换行符或注释字符以外的任何可打印字符。

## 文件

**/etc/bluetooth/hosts**

## 参见

bluetooth(3)

## 作者

Maksim Yevmenkin <m_evmenkin@yahoo.com>
