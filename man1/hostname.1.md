# hostname.1

`hostname` — 设置或打印当前主机系统的名称

## 名称

`hostname`

## 概要

`hostname [-f] [-s | -d] [name-of-host]`

## 描述

`hostname` 实用程序打印当前主机的名称。超级用户可以通过提供参数来设置主机名；这通常在初始化脚本 **/etc/rc.d/hostname** 中完成，该脚本通常在启动时运行。此脚本使用 **/etc/rc.conf** 中的 `hostname` 变量。

选项：

**`-f`** 在打印的名称中包含域名信息。这是默认行为。

**`-s`** 从打印的名称中去掉任何域名信息。

**`-d`** 仅打印域名信息。

## 实例

设置机器的主机名并检查结果：

```sh
$ hostname beastie.localdomain.org
$ hostname
beastie.localdomain.org
```

不显示域名信息：

```sh
$ hostname -s
beastie
```

仅显示域名信息：

```sh
$ hostname -d
localdomain.org
```

## 参见

gethostname(3), [rc.conf(5)](../man5/rc.conf.5.md)

## 历史

`hostname` 命令首次出现于 4.2BSD。
