# nullfs(4)

`nullfs` — 空文件系统

## 名称

`nullfs`

## 概要

`要启用对此驱动的支持，请在内核配置文件中加入以下行：`

> options NULLFS

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
nullfs_load="YES"
```

## 描述

`nullfs` 驱动允许 FreeBSD 内核挂载环回文件系统子树。

## 实例

挂载 `nullfs` 文件系统：

```sh
mount_nullfs /usr/ports /home/devel/ports
```

也可以在 [fstab(5)](../man5/fstab.5.md) 中定义类似以下的条目：

```sh
/usr/ports	/home/devel/ports	nullfs		rw	0	0
```

## 参见

[fstab(5)](../man5/fstab.5.md), mount_nullfs(8)

## 历史

`nullfs` 层首次出现于 4.4BSD。

## 作者

`nullfs` 内核实现由 John Heideman 编写。

本手册页由 Daniel Gerzo <danger@FreeBSD.org> 编写。
