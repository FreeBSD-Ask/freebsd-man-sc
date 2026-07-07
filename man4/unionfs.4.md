# unionfs(4)

`unionfs` — 联合挂载文件系统

## 名称

`unionfs`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> option UNIONFS

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
unionfs_load="YES"
```

## 描述

UNIONFS 驱动是可堆叠联合文件系统的一种实现。

## 参见

mount_unionfs(8)

## 标准

> J. S. Pendry, M. K. McKusick, "Union mounts in 4.4BSD-Lite", 1995 年 12 月。

> P. H. Kamp, R. N. M. Watson, "Jails: Confining the omnipotent root", 2000 年 5 月。

## 历史

`unionfs` 设备驱动首次出现于 FreeBSD 5.0。

## 作者

`unionfs` 设备驱动由 Jan-Simon Pendry 为 4.4BSD 编写，Masanori OZAWA <ozawa@ongs.co.jp> 为 FreeBSD 7.0 重新实现了锁的处理。本手册页由 Gordon Bergling <gbe@FreeBSD.org> 编写。

## 缺陷

有关 `unionfs` 文件系统的缺陷列表，请参见 mount_unionfs(8) 手册页。
