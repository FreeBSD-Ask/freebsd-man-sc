# kldunload(8)

`kldunload` — 从内核中卸载文件

## 名称

`kldunload`

## 概要

`kldunload [-fv] -i id ...`

`kldunload [-fv] [-n] name ...`

## 描述

`kldunload` 工具用于卸载先前由 [kldload(8)](kldload.8.md) 加载的文件。

可用选项如下：

**`-f`** 强制卸载。此选项会忽略模块对 `MOD_QUIESCE` 返回的错误，意味着即使模块当前正在使用中也应被卸载。用户只能自行应对由此带来的后果。

**`-v`** 显示更详细的信息。

**`-i`** `id` 卸载具有此 ID 的文件。

**`-n`** `name` 卸载具有此名称的文件。

**`name`** 卸载具有此名称的文件。

## 退出状态

`kldunload` 工具成功时退出值为 0，发生错误时大于 0。

## 参见

kldunload(2), [kldload(8)](kldload.8.md), [kldstat(8)](kldstat.8.md)

## 历史

`kldunload` 工具首次出现于 FreeBSD 3.0，替代了 `lkm` 接口。

## 作者

Doug Rabson <dfr@FreeBSD.org>
