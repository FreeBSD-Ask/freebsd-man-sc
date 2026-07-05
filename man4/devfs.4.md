# devfs.4

`devfs` — 设备文件系统

## 名称

`devfs`

## 概要

```sh
devfs	/dev	devfs rw 0 0
```

## 描述

设备文件系统，即 `devfs`，在全局文件系统命名空间中提供对内核设备命名空间的访问。常规挂载点为 **/dev**。

该文件系统包含若干目录、链接、符号链接和设备，其中一些也可写入。在 chroot 环境中，可使用 devfs(8) 创建新的 **/dev** 挂载点。

可使用 mknod(8) 工具恢复 `devfs` 下被删除的设备条目。

[fdescfs(4)](fdescfs.4.md) 文件系统是填充 **/dev/fd** 的另一种方式。`devfs` 和 [fdescfs(4)](fdescfs.4.md) 在 **/dev/fd** 中呈现的字符设备对应于访问该目录的进程的已打开文件描述符。`devfs` 仅为标准文件描述符 `0`、`1` 和 `2` 创建文件。[fdescfs(4)](fdescfs.4.md) 为所有已打开的描述符创建文件。

选项如下：

**`ruleset`** =`ruleset` 将规则集编号 `ruleset` 设为此挂载点的当前规则集，并应用其所有规则。如果规则集编号 `ruleset` 不存在，则创建一个编号为 `ruleset` 的空规则集。有关使用 devfs 规则集的更多信息，请参见 devfs(8)。

**`-o`** `options` 使用指定的挂载 `options`，如 [mount(8)](../man8/mount.8.md) 中所述。以下 devfs 文件系统特定选项可用：

## 文件

**`/dev`** 常规的 `devfs` 挂载点。

## 实例

挂载位于 **/mychroot/dev** 的 `devfs` 卷：

```sh
mount -t devfs devfs /mychroot/dev
```

## 参见

[fdescfs(4)](fdescfs.4.md), devfs(8), [mount(8)](../man8/mount.8.md), [make_dev(9)](../man9/make_dev.9.md)

## 历史

`devfs` 文件系统首次出现于 FreeBSD 2.0。它在 FreeBSD 5.0 中成为访问设备的首选方法，并在 FreeBSD 6.0 中成为唯一方法。`devfs` 手册页首次出现于 FreeBSD 2.2。

## 作者

`devfs` 手册页由 Mike Pritchard <mpp@FreeBSD.org> 编写。
