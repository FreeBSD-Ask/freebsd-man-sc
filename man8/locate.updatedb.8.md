# locate.updatedb(8)

`locate.updatedb` — 更新 locate 数据库

## 名称

`locate.updatedb`

## 概要

**/usr/libexec/locate.updatedb**

## 描述

**/usr/libexec/locate.updatedb** 工具用于更新 [locate(1)](../man1/locate.1.md) 所使用的数据库。它通常由 **/etc/periodic/weekly/310.locate** 脚本每周运行一次。

新构建数据库的内容可由 **/etc/locate.rc** 文件控制。

## 环境变量

**`LOCATE_CONFIG`** 配置文件的路径

## 文件

**/var/db/locate.database** 默认数据库

**/etc/locate.rc** 配置文件

## 参见

[locate(1)](../man1/locate.1.md), [periodic(8)](periodic.8.md)

> Woods, James A., "Finding Files Fast", *;login*, 8:1, pp. pp. 8-10, 1983.
