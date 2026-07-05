# tzsetup.8

`tzsetup` — 设置本地时区

## 名称

`tzsetup`

## 概要

`tzsetup [-nrs] [-C chroot_directory] [zoneinfo_file | zoneinfo_name]`

## 描述

`tzsetup` 工具读取时区信息数据库并呈现一个菜单，允许用户在不知道数据库布局细节的情况下选择特定时区。选定的时区安装为系统默认时区。`tzsetup` 工具还会确定对于硬件时钟不保持 UTC 的系统是否需要进行任何调整。

可用选项如下：

**`-C`** `chroot_directory` 相对于 `chroot_directory` 打开所有文件和目录。

**`-n`** 不创建或符号链接文件。

**`-r`** 重新安装上次安装的 zoneinfo 文件。名称从 **/var/db/zoneinfo** 获取。

**`-s`** 如果未设置为 UTC，则跳过有关调整时钟的初始问题。`tzsetup` 既不会创建也不会删除 **/etc/wall_cmos_clock**。在新安装的系统上，硬件时钟将保持 UTC。

通过在命令行上指定 `zoneinfo_file` 的位置或 `zoneinfo_name` 的名称，可以绕过菜单系统；这主要用于预配置的安装脚本或知道要安装哪个 zoneinfo 的人。

## 时区数据库

时区数据库的内容由 **/usr/share/zoneinfo/zone1970.tab** 索引。此文件为每个时区数据文件列出 ISO 3166 领土代码、近似地理坐标（ISO 6709 格式）以及领土内的位置。

数据库的维护者遵循以下策略：

- 每个国家或有人居住的地理领土至少有一个时区。
- 自 UNIX 纪元（1970 年 1 月 1 日，GMT）开始以来，每个不同的、有记录的时区历史都有一个时区。
- 每个时区以其中人口最多的城市命名。（在可能的情况下，数据库包含该城市 1970 年以前的历史。）

数据库的源代码（**/usr/src/contrib/tzdata/[a-z]***）包含许多额外的注释和文档参考，供对历史感兴趣的人参考。

## 文件

**/etc/localtime** 当前时区文件

**/etc/wall_cmos_clock** 参见 adjkerntz(8)

**/usr/share/misc/iso3166** ISO 3166 领土代码到名称的映射

**/usr/share/zoneinfo** zoneinfo 文件目录

**/usr/share/zoneinfo/zone1970.tab** 时区文件到国家和位置的映射

**/var/db/zoneinfo** 上次安装的时区文件保存的名称

## 实例

正常使用，通过基于对话框的用户界面选择正确的 zoneinfo 文件：

```sh
# tzsetup
```

安装文件 **/usr/share/zoneinfo/Australia/Sydney**：

```sh
# tzsetup /usr/share/zoneinfo/Australia/Sydney
```

安装 Australia/Sydney 的 zoneinfo 文件，假定位于 **/usr/share/zoneinfo**：

```sh
# tzsetup Australia/Sydney
```

重新安装 zoneinfo 文件后，你可以重新安装最近安装的 zoneinfo 文件（如 **/var/db/zoneinfo** 中所指定）：

```sh
# tzsetup -r
```

## 参见

[date(1)](../man1/date.1.md), adjtime(2), ctime(3), timezone(3), tzfile(5), adjkerntz(8), zdump(8), zic(8)

## 免责声明

将某些地区与某些国家和/或领土关联起来仅用于识别目的，不意味着 FreeBSD 项目对任何实体的领土主张表示认可或拒绝。

## 缺陷

当 `tzsetup` 创建或更新 **/etc/localtime** 时已经在运行的程序不会反映更新后的时区。当系统首次配置为非 UTC 硬件时钟时，需要运行 adjkerntz(8)（通常作为系统启动的一部分发生）以更新内核对正确时区偏移的概念。
