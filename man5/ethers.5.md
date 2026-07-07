# ethers(5)

`ethers` — 以太网地址数据库

## 名称

`ethers`

## 描述

`ethers` 数据库包含有关互联网络上已知主机的 48 位以太网地址的信息。数据存储在名为 **/etc/ethers** 的文件中，格式如下：

> `ethernet-address fully-qualified-host-name`

各项之间由任意数量的空格和/或制表符分隔。行首的 `#` 表示注释开始，注释延续到行尾。行首的 `+` 会使 ethers(3) 库函数除使用 **/etc/ethers** 文件中的数据外，还使用存储在 NIS `ethers.byname` 和 `ethers.byaddr` 映射中的数据。

以太网地址以 ASCII 形式表示为 "x:x:x:x:x:x"，其中 `x` 是 0x00 到 0xFF 之间的十六进制值。地址值应为网络字节序。**/etc/ethers** 数据库中指定的主机名应对应 [hosts(5)](hosts.5.md) 文件中的条目。

标准 C 库中的 Fn ether_line 函数可用于将 **/etc/ethers** 数据库中的各行拆分为各自的组成部分：以 `ether_addr` 结构存储的二进制以太网地址，以及以字符串存储的主机名。

## 文件

**`/etc/ethers`** `ethers` 文件位于 **/etc**。

## 参见

ethers(3), [yp(8)](../man8/yp.8.md)

## 历史

`ethers` 格式基于 SunOS 4.1.x 中使用的格式。
