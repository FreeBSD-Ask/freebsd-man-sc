# mount_cd9660(8)

`mount_cd9660` — 挂载 ISO-9660 文件系统

## 名称

`mount_cd9660`

## 概要

`mount_cd9660 [-begjrv] [-C charset] [-G gid] [-m mask] [-M mask] [-o options] [-s startsector] [-U uid] special node`

## 描述

`mount_cd9660` 工具将驻留在设备 `special` 上的 ISO-9660 文件系统挂接到全局文件系统命名空间的 `node` 位置。此命令通常在启动时由 [mount(8)](mount.8.md) 执行。

选项如下：

**`-b`** 放宽对补充卷描述符标志字段的检查，某些 Joliet 格式磁盘上该字段被设为错误值。

**`-e`** 启用扩展属性的使用。

**`-g`** 不去除文件的版本号。（默认情况下，如果磁盘上存在具有不同版本号的文件，则只列出最后一个。）无论是否去除版本号，文件都可以在不明确指定版本号的情况下打开。

**`-G`** `group` 将文件系统中文件所属组设为 `group`。在没有扩展属性或 Rockridge 扩展的卷上，默认 gid 为零。

**`-U`** `user` 将文件系统中文件的所有者设为 `user`。在没有扩展属性或 Rockridge 扩展的卷上，默认 uid 为零。

**`-m`** `mask` 指定文件系统中文件的最大权限。例如，`mask` 为 `544` 时，文件所有者只有读和执行权限，其他人只有读权限。有关八进制文件模式的更多信息，请参见 [chmod(1)](../man1/chmod.1.md)。默认 `mask` 为 7777。在没有扩展属性或 Rockridge 扩展的卷上，默认权限为 555。

**`-M`** `mask` 指定文件系统中目录的最大权限。详情见上一选项的说明。

**`-j`** 不使用文件系统中包含的任何 Joliet 扩展。

**`-o`** 选项通过 `-o` 标志后跟以逗号分隔的选项字符串来指定。可能选项及其含义请参见 [mount(8)](mount.8.md) 手册页。以下为 cd9660 专用选项：

**`extatt`** 等同于 `-e`。

**`gens`** 等同于 `-g`。

**`nojoliet`** 等同于 `-j`。

**`norrip`** 等同于 `-r`。

**`brokenjoliet`** 等同于 `-b`。

**`-r`** 不使用文件系统中包含的任何 Rockridge 扩展。

**`-s`** `startsector` 从 `startsector` 处启动文件系统。通常，如果底层设备是 CD-ROM 驱动器，`mount_cd9660` 会尝试从包含数据的 CD-ROM 中找到最后一道轨道，并从那里启动文件系统。如果设备不是 CD-ROM，或无法检查目录表，文件系统将从扇区 0 启动。此选项可用于覆盖该行为。注意，`startsector` 以 CD-ROM 块为单位，每块 2048 字节。这与 cdcontrol(1) 的 `info` 命令所打印的值相同。通过在此处指定正确的 `startsector`，可以挂载多会话 CD 中的任意会话。

**`-C`** `charset` 指定使用 Joliet 扩展时用于转换 Unicode 文件名的本地 `charset`。

**`-v`** 详细显示关于起始扇区决策的信息。

## 实例

以下命令可用于挂载 Kodak Photo-CD：

```sh
mount_cd9660 -o rw -v -s 0 /dev/cd0 /cdrom
```

## 参见

cdcontrol(1), mount(2), unmount(2), [cd9660(4)](../man4/cd9660.4.md), [fstab(5)](../man5/fstab.5.md), mdconfig(8), [mount(8)](mount.8.md)

## 历史

`mount_cd9660` 工具首次出现于 4.4BSD。

Unicode 转换例程由 Ryuichiro Imura <imura@ryu16.org> 于 2003 年添加。

## 缺陷

目前不支持 POSIX 设备节点映射。

如果使用 Rockridge 扩展，则不去除版本号。在这种情况下，访问没有 Rockridge 名称且不带版本号的文件时，会得到版本号最低的文件，而非版本号最高的文件。

不支持 ECMA。
