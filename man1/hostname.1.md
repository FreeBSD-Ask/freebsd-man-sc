  HOSTNAME(1)  

HOSTNAME(1)

FreeBSD General Commands Manual

HOSTNAME(1)

[名称](#__u540D___u79F0_)
=======================

`hostname` —

设置或打印当前主机系统的名称

[概要](#__u6982___u8981_)
=======================

`hostname` \[`-f`\] \[`-s` | `-d`\] \[name-of-host\]

[描述](#__u63CF___u8FF0_)
=======================

`hostname` 实用程序打印当前主机的名称。 超级用户可以通过提供参数来设置主机名；这通常在初始化脚本 /etc/rc.d/hostname 中完成，通常在启动时运行。 该脚本使用 /etc/rc.conf 中的 hostname 变量。

选项：

[`-f`](#f)

在打印的名称中包含域信息。这是默认行为。

[`-s`](#s)

从打印的名称中删除任何域信息。

[`-d`](#d)

只打印域信息。

[实例](#__u5B9E___u4F8B_)
=======================

设置机器的主机名并查看结果：

$ hostname beastie.localdomain.org $ hostname beastie.localdomain.org 

不显示域信息：

$ hostname -s beastie 

仅显示域信息：

$ hostname -d localdomain.org 

[参见](#__u53C2___u89C1_)
=======================

gethostname(3), rc.conf(5)

[历史](#__u5386___u53F2_)
=======================

`hostname` 命令出现在 4.2BSD 中。

October 5, 2020

FreeBSD 13.1-RELEASE