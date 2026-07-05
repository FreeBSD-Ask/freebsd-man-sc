# fstab.5

`fstab` — 文件系统的静态信息

## 名称

`fstab`

## 概要

`#include <fstab.h>`

## 描述

`fstab` 文件包含有关各种文件系统的描述性信息。`fstab` 只能被程序读取，不能被写入；正确创建和维护此文件是系统管理员的职责。每个文件系统在单独一行中描述；每行上的字段由制表符或空格分隔。`fstab` 中记录的顺序很重要，因为 fsck(8)、[mount(8)](../man8/mount.8.md) 和 [umount(8)](../man8/umount.8.md) 会按顺序遍历 `fstab` 执行各自的操作。

第一个字段（`fs_spec`）描述要挂载的特殊设备或远程文件系统。其内容由 strunvis(3) 函数解码。这样允许在设备名中使用空格或制表符，否则它们会被解释为字段分隔符。

第二个字段（`fs_file`）描述文件系统的挂载点。对于交换分区，此字段应指定为 "none"。其内容由 strunvis(3) 函数解码，同上。

第三个字段（`fs_vfstype`）描述文件系统的类型。系统可以支持多种文件系统类型。只有 root、/usr 和 /tmp 文件系统需要静态编译到内核中；其他所有文件系统将在挂载时自动加载。（例外：FFS 目前无法按需加载。）有些人仍然倾向于将其他文件系统也静态编译进去。

第四个字段（`fs_mntops`）描述与文件系统相关联的挂载选项。其格式为以逗号分隔的选项列表。它至少包含挂载类型（见下文的 `fs_type`）加上适用于该文件系统类型的任何附加选项。有关可指定的附加选项，请参阅 [mount(8)](../man8/mount.8.md) 手册页中的选项标志（`-o`）以及文件系统特定的手册页，例如 mount_nfs(8)。所有可以传递给文件系统特定挂载命令的选项也可以在 `fstab` 中使用，只是格式需要略有不同。`-o` 选项的参数可以不带前导 `-o` 标志直接使用。其他选项则需要同时指定文件系统特定的标志及其参数，二者之间用等号分隔。例如，挂载 [msdosfs(4)](../man4/msdosfs.4.md) 文件系统时，选项

```sh
-o sync -o noatime -m 644 -M 755 -u foo -g bar
```

在 `fstab` 的选项字段中应写为

```sh
sync,noatime,-m=644,-M=755,-u=foo,-g=bar
```

如果指定了选项 "userquota" 和/或 "groupquota"，文件系统将由 quotacheck(8) 命令自动处理，并使用 quotaon(8) 启用用户和/或组磁盘配额。默认情况下，文件系统配额保存在名为 `quota.user` 和 `quota.group` 的文件中，这些文件位于相关文件系统的根目录下。可以在配额选项后加上等号和替代的绝对路径名来覆盖这些默认值。因此，如果 `/tmp` 的用户配额文件存储在 **/var/quotas/tmp.user**，此位置可以指定为：

```sh
userquota=/var/quotas/tmp.user
```

如果指定了选项 "failok"，系统将忽略挂载该文件系统期间发生的任何错误，否则这些错误会导致系统进入单用户模式。此选项由 [mount(8)](../man8/mount.8.md) 命令实现，不会传递给内核。

如果指定了选项 "noauto"，文件系统将不会在系统启动时自动挂载。注意，对于第三方类型的网络文件系统（即由基本系统之外的其他软件支持的类型），要在系统启动时自动挂载，必须使用 [rc.conf(5)](rc.conf.5.md) 变量 `extra_netfs_types` 来扩展 [rc(8)](../man8/rc.8.md) 启动脚本的网络文件系统类型列表。

如果指定了选项 "late"，文件系统将在系统启动过程中远程挂载点挂载完成之后的阶段自动挂载。有关此选项的更多细节，请参阅 [mount(8)](../man8/mount.8.md) 手册页。

如果指定了选项 "update"，表示应相应地更改已挂载文件系统的状态。例如，这允许将只读挂载的文件系统升级为读写挂载，反之亦然。默认情况下，在处理 `fstab` 时，与已挂载文件系统对应的条目将被跳过，除非是根文件系统，此时会自动应用类似于 "update" 的逻辑。

"update" 选项通常与两个 `fstab` 文件配合使用。第一个 `fstab` 文件用于建立初始的文件系统集合。然后运行第二个 `fstab` 文件来更新初始文件系统集合并添加额外的文件系统。

挂载类型从 `fs_mntops` 字段中提取并单独存储在 `fs_type` 字段中（不会从 `fs_mntops` 字段中删除）。如果 `fs_type` 为 "rw" 或 "ro"，则 `fs_file` 字段中指定名称的文件系统通常以读写或只读方式挂载到指定的特殊文件上。

如果 `fs_type` 为 "sw"，则在系统重启过程结束时，由 swapon(8) 命令将该特殊文件作为一块交换空间启用。对于交换设备，关键字 "trimonce" 会触发向设备发送 `BIO_DELETE` 命令。此命令将设备的块标记为未使用，但可能存储磁盘标签的块除外。这种标记可能会擦除崩溃转储。若要将设备的 `swapon` 延迟到 `savecore` 将崩溃转储复制到其他位置之后，请使用 "late" 选项。对于由 vnode 支持的交换空间，`fs_mntops` 字段支持 "file"。当 `fs_spec` 是 [md(4)](../man4/md.4.md) 设备文件（"md""md[0-9]* "）且 `fs_mntopts` 中指定了 "file" 时，将创建一个 [md(4)](../man4/md.4.md) 设备，使用指定的文件作为后备存储，然后新设备用作交换空间。`.eli` 设备上的交换条目将导致自动创建加密设备。可以传递 "ealgo"、"aalgo"、"keylen"、"notrim" 和 "sectorsize" 选项来控制 geli(8) 的相应参数。除 `fs_spec` 和 `fs_type` 之外的字段均不使用。如果 `fs_type` 指定为 "xx"，则该条目被忽略。这对于显示当前未使用的磁盘分区很有用。

第五个字段（`fs_freq`）由 dump(8) 命令用于这些文件系统，以确定哪些文件系统需要转储。如果第五个字段不存在，则返回值零，`dump` 将假定该文件系统不需要转储。如果第五个字段大于 0，则它指定此文件系统两次转储之间的天数。

第六个字段（`fs_passno`）由 fsck(8) 和 quotacheck(8) 程序用于确定在重启时进行文件系统和配额检查的顺序。`fs_passno` 字段可以是 0 到 `INT_MAX Ns -1` 之间的任何值。

根文件系统应指定 `fs_passno` 为 1，其他文件系统的 `fs_passno` 应为 2 或更大。`fs_passno` 值为 1 的文件系统始终按顺序检查，并在处理另一个文件系统之前完成，而且会在所有 `fs_passno` 值更大的文件系统之前处理。

对于任何给定的 `fs_passno` 值，同一驱动器内的文件系统将按顺序检查，但不同驱动器上的文件系统将同时检查，以利用硬件的并行能力。一旦当前 `fs_passno` 的所有文件系统检查完成，将对下一个 `fs_passno` 开始相同的过程。

如果第六个字段不存在或为零，则返回值零，fsck(8) 和 quotacheck(8) 将假定该文件系统不需要检查。

当系统实用程序可能会误判文件系统位于不同的物理设备上（而实际上并非如此，例如 [ccd(4)](../man4/ccd.4.md) 设备）时，`fs_passno` 字段可用于实现更精细的控制。所有 `fs_passno` 值较低的文件系统将在开始处理 `fs_passno` 值较高的文件系统之前完成。例如，所有 `fs_passno` 为 2 的文件系统将在任何 `fs_passno` 为 3 或更大的文件系统开始之前完成。不同的 `fs_passno` 值之间允许存在间隔。例如，**/etc/fstab** 中列出的文件系统可以具有诸如 0、1、2、15、100、200、300 的 `fs_passno` 值，并且在 **/etc/fstab** 中可以以任何顺序出现。

```sh
#define	FSTAB_RW	"rw"	/* 读写设备 */
#define	FSTAB_RQ	"rq"	/* 带配额的读写 */
#define	FSTAB_RO	"ro"	/* 只读设备 */
#define	FSTAB_SW	"sw"	/* 交换设备 */
#define	FSTAB_XX	"xx"	/* 完全忽略 */
struct fstab {
	char	*fs_spec;	/* 块特殊设备名 */
	char	*fs_file;	/* 文件系统路径前缀 */
	char	*fs_vfstype;	/* 文件系统类型，ufs、nfs */
	char	*fs_mntops;	/* 挂载选项，类似 -o */
	char	*fs_type;	/* 从 fs_mntops 中提取的 FSTAB_* */
	int	fs_freq;	/* 转储频率，以天为单位 */
	int	fs_passno;	/* 并行 fsck 的遍数 */
};
```

从 `fstab` 中读取记录的正确方法是使用 getfsent(3)、getfsspec(3)、getfstype(3) 和 getfsfile(3) 例程。

## 文件

**`/etc/fstab`** `dump` 文件位于 **/etc**。

## 实例

```sh
# Device	Mountpoint	FStype	Options		Dump	Pass#
#
# UFS 文件系统。
/dev/da0p2	/		ufs	rw		1	1
#
# 块设备上的交换空间。
/dev/da0p1	none		swap	sw		0	0
#
# 使用带 GELI 加密的块设备的交换空间。
# aalgo、ealgo、keylen、sectorsize 选项可用于
# .eli 设备。
/dev/da1p2.eli	none		swap	sw		0	0
#
# tmpfs。
tmpfs		/tmp		tmpfs	rw,size=1g,mode=1777	0 0
#
# 由交换空间支持的 md(4) 上的 UFS 文件系统。/dev/md10 会
# 自动创建。如果是 "md"，将自动选择
# 单元号。
md10		/scratch	mfs	rw,-s1g		0	0
#
# 由 vnode 支持的 md(4) 上的交换空间。
md11		none		swap	sw,file=/swapfile	0 0
#
# CDROM。通常使用 "noauto" 选项，因为
# 介质是可移动的。
/dev/cd0	/cdrom		cd9660	ro,noauto	0	0
#
# NFS 导出的文件系统。"serv" 是 NFS 服务器名
# 或 IP 地址。
serv:/export	/nfs		nfs	rw,noinet6	0	0
```

## 参见

getfsent(3), getvfsbyname(3), strunvis(3), [ccd(4)](../man4/ccd.4.md), dump(8), fsck(8), geli(8), [mount(8)](../man8/mount.8.md), quotacheck(8), quotaon(8), swapon(8), [umount(8)](../man8/umount.8.md)

## 历史

`dump` 文件格式出现于 4.0BSD。
