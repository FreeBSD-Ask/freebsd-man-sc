# growfs(7)

`growfs` — 启动时扩展根文件系统并添加交换分区的脚本

## 名称

`growfs`, `growfs_fstab`

## 描述

`growfs_fstab` 脚本通常在系统安装后的首次引导时运行。如果引导磁盘大于根文件系统和引导分区，并且根文件系统位于最后一个分区，则 `growfs_fstab` 可以扩展根文件系统。它还可以添加一个交换分区，默认大小为引导磁盘的 10%。交换分区限制为内存大小的两倍，最大 4 GB；内存不超过 8 GB 时为 8 GB；内存超过 8 GB 时等于内存大小。它还受 [sysctl(8)](../man8/sysctl.8.md) 值 `vm.swap_maxpages` 除以 2 的限制。默认情况下，如果发现现有交换分区或在 **/etc/fstab** 中列出了交换分区，或者磁盘小于 15 GB，则不会创建交换分区。`growfs_fstab` 脚本会在根文件系统变为可写之后将任何新的交换分区添加到 **/etc/fstab**，并在 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `dumpdev` 变量设置为 `AUTO` 时，将其启用为转储分区。

**/etc/rc.conf** 中的以下选项控制 `growfs_fstab` 的行为：

**`growfs_enable`**（“`NO`”）如果设置为“`YES`”，在机器首次引导时，根文件系统将自动扩展（如果可能），以填充其后的所有可用空间，并可选择在末尾添加一个交换设备。

**`growfs_swap_size`**（“``”）如果设置为“`0`”，则禁用交换分区的添加。空值（“``”）允许创建默认大小的交换分区。如果设置为其他值，则交换分区将按指定的字节数创建，即使检测到另一个交换分区也是如此。

`growfs_swap_size` 的设置可在内核环境中设置，在这种情况下它会覆盖 **/etc/rc.conf** 中的值。

要在不重启的情况下扩展根文件系统，请运行以下命令：

```sh
% /etc/rc.d/growfs onestart
```

此外，如果添加了交换分区，请运行以下命令：

```sh
% /etc/rc.d/growfs_fstab onestart
```

注意，如果磁盘再次扩展，并且根文件系统之前已经被扩展并添加了交换分区，则需要在此过程之前删除交换分区，以便将根文件系统扩展到新的大小。扩展过程中可以创建新的交换分区。

## 实现说明

`growfs_fstab` 脚本仅尝试扩展根文件系统，并且根分区之后必须有可用空间。它通常用于具有单个文件系统的镜像。该脚本要求 [awk(1)](../man1/awk.1.md) 存在并且在路径中。这通常意味着在运行脚本之前必须可用 **/usr**。

## 文件

**`/etc/fstab`**
**`/etc/rc.conf`**

## 退出状态

`growfs_fstab` 实用程序成功时退出值为 0，发生错误时退出值大于 0。

## 参见

[fstab(5)](../man5/fstab.5.md), [rc.conf(5)](../man5/rc.conf.5.md), [growfs(8)](../man8/growfs.8.md), zpool(8)

## 历史

`growfs_fstab` 手册页首次出现于 FreeBSD 10.1。添加交换分区的能力是在 FreeBSD 13.2 中添加的。

## 作者

该手册页和脚本由 John-Mark Gurney <jmg@FreeBSD.org> 编写。创建交换分区的能力由 Michael Karels <karels@FreeBSD.org> 添加。
