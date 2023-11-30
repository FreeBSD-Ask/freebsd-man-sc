  TZSETUP(8)  

TZSETUP(8)

FreeBSD System Manager's Manual

TZSETUP(8)

[名称](#__u540D___u79F0_)
=======================

`tzsetup` —

设置本地时区

[概要](#__u6982___u8981_)
=======================

`tzsetup` \[`-nrs`\] \[`-C` chroot\_directory\] \[zoneinfo\_file | zoneinfo\_name\]

[描述](#__u63CF___u8FF0_)
=======================

`tzsetup` 实用程序读取时区信息数据库并提供一个菜单，允许用户在不知道数据库布局细节的情况下选择特定区域。 所选区域安装为系统默认区域。 `tzsetup` 实用程序还确定对于硬件时钟不保持 UTC 的系统是否需要进行任何调整。

可以使用以下选项：

[`-C`](#C) chroot\_directory

打开与 chroot\_directory 相关的所有文件和目录。

[`-n`](#n)

不要创建或复制文件。

[`-r`](#r)

重新安装上次安装的 zoneinfo 文件。 该名称是从 /var/db/zoneinfo 获得的。

[`-s`](#s)

如果未设置为 UTC ，请跳过有关调整时钟的初始问题。

可以通过在命令行上指定 zoneinfo\_file 的位置或 zoneinfo\_name-
的名称来短路菜单系统；这主要用于预配置的安装脚本或知道要安装哪个 zoneinfo 的人。

[时区数据库](#__u65F6___u533A___u6570___u636E___u5E93_)
==================================================

时区数据库的内容由 /usr/share/zoneinfo/zone.tab 索引。 该文件为每个时区数据文件列出了 ISO 区域代码、近似地理坐标（采用 ISO 格式）和区域内的位置。

数据库的维护者维护以下策略：

1.  每个国家或有人居住的地理区域至少有一个区域。
2.  自 UNIX 纪元（1970 年 1 月 1 日， GMT ）开始以来，每个不同的、记录在案的时区历史都有一个区域。
3.  每个区域都以其中人口最多的城市命名。 （在可能的情况下，该数据库包括其城市 1970 年之前的历史。）

数据库的源代码 ( (/usr/src/share/zoneinfo/\[a-z\]\*) ) 包含许多附加注释和文档参考，供有历史头脑的人参考。

[文件](#__u6587___u4EF6_)
=======================

/etc/localtime

当前时区文件

/etc/wall\_cmos\_clock

见 adjkerntz(8)

/usr/share/misc/iso3166

ISO 地区代码到名称的映射

/usr/share/zoneinfo

zoneinfo 文件的目录

/usr/share/zoneinfo/zone.tab

时区文件到国家和位置的映射

/var/db/zoneinfo

最后安装的时区文件的保存名称

[实例](#__u5B9E___u4F8B_)
=======================

正常使用，通过基于对话框的用户界面选择正确的 zoneinfo 文件：

`tzsetup`

安装文件 /usr/share/zoneinfo/Australia/Sydney:

`tzsetup /usr/share/zoneinfo/Australia/Sydney`

安装澳大利亚/悉尼的 zoneinfo 文件，假定位于 /usr/share/zoneinfo:

`tzsetup Australia/Sydney`

重新安装 zoneinfo 文件后，您可以重新安装最新安装的 zoneinfo 文件（在 /var/db/zoneinfo 中指定）：

`tzsetup -r`

[参见](#__u53C2___u89C1_)
=======================

date(1), adjtime(2), ctime(3), timezone(3), tzfile(5), adjkerntz(8), zdump(8), zic(8)

[免责声明](#__u514D___u8D23___u58F0___u660E_)
=========================================

将某些地方表示为与某些国家和/或领土相关联的目的只是为了识别，并不意味着 FreeBSD 项目对任何实体的领土主张有任何认可或拒绝。

[缺陷](#__u7F3A___u9677_)
=======================

当 `tzsetup` 创建或更新 /etc/localtime 时已经运行的程序不会反映更新的时区。 当系统首次配置为非 UTC 硬件时钟时，有必要运行 adjkerntz(8) （这通常作为系统启动的一部分发生）以更新内核对正确时区偏移的想法。

October 21, 2009

FreeBSD 13.1-RELEASE