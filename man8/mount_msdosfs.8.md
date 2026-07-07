# mount_msdosfs(8)

`mount_msdosfs` — 挂载 MS-DOS（FAT）文件系统

## 名称

`mount_msdosfs`

## 概要

`mount_msdosfs [-9ls] [-D DOS_codepage] [-g gid] [-L locale] [-M mask] [-m mask] [-o options] [-u uid] [-W table] special node`

## 描述

`mount_msdosfs` 工具将驻留在设备 `special` 上的 MS-DOS 文件系统挂接到全局文件系统命名空间的 `node` 位置。此命令通常在启动时由 [mount(8)](mount.8.md) 执行，但任何用户都可以使用它将 MS-DOS 文件系统挂载到自己拥有的任何目录上（当然，前提是该用户对包含该文件系统的设备具有适当的访问权限）。

选项如下：

**`-o`** `options` 使用指定的挂载 `options`，如 [mount(8)](mount.8.md) 中所述。以下为 MSDOS 文件系统专用选项：

**`longnames`** 强制显示 Windows 95 长文件名。

**`shortnames`** 强制只显示旧的 MS-DOS 8.3 风格文件名。

**`nowin95`** 完全忽略 Windows 95 扩展文件信息。

**`-u`** `uid` 将文件系统中文件的所有者设为 `uid`。默认所有者是文件系统挂载目录的所有者。

**`-g`** `gid` 将文件系统中文件所属组设为 `gid`。默认组是文件系统挂载目录的组。

**`-m`** `mask` 指定文件系统中文件的最大权限。（例如，`mask` 为 `755` 表示默认情况下，文件所有者应具有读、写和执行权限，而其他人应只有读和执行权限。有关八进制文件模式的更多信息，请参见 [chmod(1)](../man1/chmod.1.md)。仅使用 `mask` 的低九位。如果提供了 `-M` 且省略了 `-m`，则使用 `-M` 的值。默认 `mask` 取自文件系统挂载目录。

**`-M`** `mask` 指定文件系统中目录的最大权限。如果提供了 `-m` 且省略了 `-M`，则使用 `-m` 的值。详情见上一选项的说明。

**`-s`** 强制忽略并不生成 Win'95 长文件名。

**`-l`** 强制列出并生成 Win'95 长文件名，并分离创建/修改/访问日期。如果未给出 `-s` 或 `-l`，则默认使用 `-l`。

**`-9`** 即使删除或重命名文件，也忽略特殊的 Win'95 目录项。这会强制启用 `-s`。

**`-L`** `locale` 指定用于 DOS 和 Win'95 文件名转换的区域设置名称。默认以 ISO 8859-1 作为本地字符集。

**`-D`** `DOS_codepage` 指定用于 DOS 文件名转换的 MS-DOS 代码页（即 IBM/OEM 代码页）名称。

**`-W`** `table`

> **此选项仅为向后兼容而保留，未来将被移除。请避免使用此选项。**

指定包含转换表的文本文件名：`iso22dos`、`iso72dos`、`koi2dos`、`koi8u2dos`。

## 实例

挂载位于 **/dev/ada1s1** 的俄语 MS-DOS 文件系统：

```sh
mount_msdosfs -L ru_RU.KOI8-R -D CP866 /dev/ada1s1 /mnt
```

挂载位于 **/dev/ada1s1** 的日语 MS-DOS 文件系统：

```sh
mount_msdosfs -L ja_JP.eucJP -D CP932 /dev/ada1s1 /mnt
```

## 参见

mount(2), unmount(2), [msdosfs(4)](../man4/msdosfs.4.md), [fstab(5)](../man5/fstab.5.md), [mount(8)](mount.8.md)

本地化 MS 操作系统列表：`http://www.microsoft.com/globaldev/reference/oslocversion.mspx`。

## 历史

`mount_msdosfs` 的前身名为 `mount_pcfs`，出现于 NetBSD 0.8。它在 NetBSD 1.0 中被重写，并首次出现于 FreeBSD 2.0。`mount_msdos` 在 FreeBSD 5.0 中被重命名为更贴切的 `mount_msdosfs`。字符代码转换例程于 2003 年添加。

## 作者

作为 `mount_pcfs` 的初始实现由 Paul Popelka <paulp@uts.amdahl.com> 编写。由 Christopher G. Demetriou <cgd@NetBSD.org> 重写。字符代码转换例程由 Ryuichiro Imura <imura@ryu16.org> 添加。

## 注意事项

使用 `-9` 标志可能导致文件系统损坏，尽管部分损坏由类似 Win'95 所用的程序加以处理。
