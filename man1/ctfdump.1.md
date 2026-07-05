# ctfdump.1

`ctfdump` — 转储 ELF 文件中的 SUNW_ctf 节

## 名称

`ctfdump`

## 概要

`ctfdump [-dfhlsSt] -u ufile file`

## 描述

`ctfdump` 实用程序转储 ELF 二进制文件中存在的 CTF（Compact C Type Format，紧凑 C 类型格式）数据节（SUNW_ctf）的内容。该节此前由 ctfconvert(1) 或 ctfmerge(1) 创建。

以下选项可用：

**`-d`** 显示数据对象节。

**`-f`** 显示函数节。

**`-h`** 显示头部。

**`-l`** 显示标签节。

**`-s`** 显示字符串表。

**`-S`** 显示统计信息。

**`-t`** 显示类型节。

**`-u`** `ufile` 将未压缩的 CTF 数据写入名为 `ufile` 的原始 CTF 文件。

## 退出状态

`ctfdump` 实用程序成功时退出值为 0，发生错误时大于 0。

## 参见

ctfconvert(1), ctfmerge(1), ctf(5)

## 历史

`ctfdump` 实用程序首次出现于 FreeBSD 7.0。

## 作者

CTF 工具集源自 OpenSolaris。
