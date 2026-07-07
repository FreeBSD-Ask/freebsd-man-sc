# lastlogin(8)

`lastlogin` — 显示用户的最近登录时间

## 名称

`lastlogin`

## 概要

`lastlogin [--libxo] [-f file] [-rt] [user ...]`

## 描述

`lastlogin` 工具将列出每个指定 `user` 的最近一次登录会话，默认情况下列出所有用户的。每行输出包含用户名、会话所使用的 tty、主机名（若有）以及会话的开始时间。

如果给出了多个 `user`，则按命令行中给出的顺序打印每个用户的会话信息。否则，将打印所有用户的信息。默认情况下，条目按用户名排序。

`lastlogin` 工具与 [last(1)](../man1/last.1.md) 的不同之处在于它仅打印关于最近一次登录会话的信息。在标准使用方式下，最近登录数据库从不会被轮转或删除。

可用选项如下：

**`--libxo`** 通过 libxo(3) 以多种人类和机器可读的格式生成输出。有关命令行参数的详细信息，请参见 xo_options(7)。

**`-f`** `file` 打开指定的最近登录数据库 `file`，而非系统范围的数据库。

**`-r`** 以逆序打印条目。

**`-t`** 按最近登录时间排序，而非按用户名排序。

## 文件

**/var/log/utx.lastlogin** 最近登录数据库

## 参见

[last(1)](../man1/last.1.md), getutxent(3), libxo(3), xo_options(7), ac(8)

## 作者

John M. Vinopal 于 1996 年 1 月编写了此程序并将其贡献给 NetBSD 项目。Philip Paeps 于 2018 年 8 月添加了 libxo(3) 支持。
