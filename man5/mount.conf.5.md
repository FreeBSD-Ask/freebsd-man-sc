# mount.conf(5)

`mount.conf` — 根文件系统挂载配置文件

## 名称

`mount.conf`

## 概要

**/.mount.conf**

## 描述

在引导过程中，FreeBSD 内核会使用 `src/sys/kern/vfs_mountroot.c` 中 `vfs_mountroot` 函数的逻辑来挂载根文件系统。根挂载逻辑可描述如下：

- 内核会在内存中合成一个配置文件，其中包含挂载根文件系统的默认指令。相关逻辑位于 `vfs_mountroot_conf0` 中。
- 内核首先将 [devfs(4)](../man4/devfs.4.md) 挂载为根文件系统。
- 接着，内核解析第 1 步中创建的内存中配置文件，并尝试挂载实际的根文件系统。配置文件的格式参见“文件格式”一节。
- 当实际的根文件系统挂载完成后，[devfs(4)](../man4/devfs.4.md) 将被重新挂载到 **/dev** 目录。
- 如果刚刚挂载的根文件系统中不存在 `/.mount.conf` 文件，则根挂载逻辑到此停止。
- 如果刚刚挂载的根文件系统中存在 `/.mount.conf` 文件，则解析该文件，内核使用这个新的配置文件尝试重新挂载根文件系统。配置文件的格式参见“文件格式”一节。
- 如果新的根文件系统中有 **/.mount** 目录，旧的根文件系统将被重新挂载到 **/.mount**。
- 根挂载逻辑返回第 4 步。

根挂载逻辑是递归的，只要每个新挂载的根文件系统都存在 `/.mount.conf` 文件，第 8 步就会重复执行。

## 文件格式

内核解析 `.mount.conf` 中的每一行，并在解析后立即尝试执行该行指定的操作。

```sh
mount -t {FS} -o {OPTIONS} {MOUNTPOINT} /
```

**`#`** 以 `#` 开头的行是注释，将被忽略。

**`{FS}:{MOUNTPOINT} {OPTIONS}`** 内核会尝试以相当于以下操作的方式挂载：如果挂载成功，`.mount.conf` 中的后续行将被忽略。如果 `.mount.conf` 中的所有行都已处理完毕但未成功挂载任何根文件系统，则执行 `.onfail` 指定的操作。

**`.ask`** 当内核处理到这一行时，会显示 `mountroot>` 命令行提示。在此提示下，操作员可以输入根挂载。

**`.md`** `file` 使用 `file` 作为后端存储，创建一个以内存为后端的 [md(4)](../man4/md.4.md) 虚拟盘。

**`.onfail`** `[panic|reboot|retry|continue]` 如果在解析 `.mount.conf` 中所有行之后内核仍无法挂载根文件系统，`.onfail` 指令告知内核执行何种操作。

**`.timeout`** `N` 在尝试挂载根文件系统之前，如果根挂载设备不存在，最多等待 `N` 秒让设备出现，然后再尝试挂载。如果未指定 `.timeout`，默认超时为 3 秒。

## 实例

以下 `.mount.conf` 示例会指示内核首先尝试将根文件系统挂载为 **/dev/cd0** 上的 ISO CD9660 文件系统，如果失败，则挂载为 **/dev/cd1** 上的 ISO CD9660 文件系统，再失败则挂载为 **/dev/ada0s1a** 上的 UFS 文件系统。如果都失败，将显示 `mountroot>` 命令行提示，操作员可在其中手动输入要挂载的根文件系统。最后如果仍然失败，内核将 panic。

```sh
.onfail panic
.timeout 3
cd9660:/dev/cd0 ro
.timeout 0
cd9660:/dev/cd1 ro
.timeout 3
ufs:/dev/ada0s1a
.ask
```

以下 `.mount.conf` 示例会指示内核创建一个 [md(4)](../man4/md.4.md) 内存盘，关联到文件 **/data/OS-1.0.iso**，然后在新创建的 md 设备上挂载 ISO CD9660 文件系统。最后一行是注释，将被忽略。

```sh
.timeout 3
.md /data/OS-1.0.iso
cd9600:/dev/md# ro
# 也可以使用 cd9660:/dev/md0 ro
```

以下 `.mount.conf` 示例会指示内核创建一个 [md(4)](../man4/md.4.md) 内存盘，关联到文件 **/data/base.ufs.uzip**，然后在新创建的 md uzip 设备上挂载 UFS 文件系统，该设备由 [geom_uzip(4)](../man4/geom_uzip.4.md) 驱动创建。

```sh
.md /data/base.ufs.uzip
ufs:/dev/md#.uzip ro
# 也可以使用 ufs:/dev/md0.uzip ro
```

以下 `.mount.conf` 示例会指示内核在一个含有 chroot(2) 环境的目录 **/jail/freebsd-8-stable** 上执行 unionfs 挂载。

```sh
.timeout 3
unionfs:/jail/freebsd-8-stable
```

## 注意事项

对于每个被挂载的根文件系统，*必须* 存在一个 **/dev** 目录，以便根挂载逻辑能够正确地重新挂载 [devfs(4)](../man4/devfs.4.md)。如果该目录不存在，系统可能在引导过程中挂起。

## 参见

nmount(2), [md(4)](../man4/md.4.md), [boot.config(5)](boot.config.5.md), [fstab(5)](fstab.5.md), [boot(8)](../man8/boot.8.md), [loader(8)](../man8/loader.8.md), [mount(8)](../man8/mount.8.md)

## 历史

`mount.conf` 文件首次出现于 FreeBSD 9.0。

## 作者

FreeBSD 内核中解析 **/.mount.conf** 的根挂载逻辑由 Marcel Moolenaar <marcel@FreeBSD.org> 编写。本手册页由 Craig Rodrigues <rodrigc@FreeBSD.org> 编写。
