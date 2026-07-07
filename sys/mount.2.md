# mount(2)

`mount` — 挂载或卸载文件系统

## 名称

`mount`, `nmount`, `unmount`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

```c
int
mount(const char *type, const char *dir, int flags, void *data);

int
unmount(const char *dir, int flags);
```

`#include <sys/uio.h>`

```c
int
nmount(struct iovec *iov, u_int niov, int flags);
```

## 描述

`mount()` 系统调用将一个文件系统对象嫁接到系统文件树的 `dir` 位置。参数 `data` 描述要挂载的文件系统对象。参数 `type` 告诉内核如何解释 `data`（参见下文的 `type`）。文件系统的内容通过新的挂载点 `dir` 变得可用。在成功挂载时，`dir` 中的任何文件可以说是被扫到地毯下面了，在文件系统卸载之前不可用。

`nmount()` 系统调用的行为与 `mount()` 类似，不同之处在于挂载选项（文件系统类型名称、要挂载的设备、挂载点名称等）以名称-值对数组的形式传入 `iov` 数组，包含 `niov` 个元素。所有文件系统都需要以下选项：

| 选项 | 说明 |
| --- | --- |
| `fstype` | 文件系统类型名称（如 "procfs"） |
| `fspath` | 挂载点路径名（如 **/proc**） |

根据文件系统类型的不同，可能会识别或需要其他选项；例如，大多数基于磁盘的文件系统除了上面列出的选项外，还需要一个“from”选项，包含特殊设备的路径名。

默认情况下，只有超级用户可以调用 `mount()` 系统调用。可以通过将 `vfs.usermount` [sysctl(8)](../man8/sysctl.8.md) 变量设置为非零值来移除此限制；参见 BUGS 部分获取更多信息。

可以指定以下 `flags` 来抑制影响文件系统访问的默认语义。

**`MNT_RDONLY`** 文件系统应被视为只读；即使是超级用户也不能写入。指定 MNT_UPDATE 而不带此选项会将只读文件系统升级为读/写。

**`MNT_NOEXEC`** 不允许从文件系统执行文件。

**`MNT_NOSUID`** 执行文件时不遵守 setuid 或 setgid 位。当调用者不是超级用户时，此标志会自动设置。

**`MNT_NOATIME`** 禁用文件访问时间的更新。

**`MNT_SNAPSHOT`** 创建文件系统的快照。目前仅在 UFS2 文件系统上支持，参见 [mksnap_ffs(8)](../man8/mksnap_ffs.8.md) 获取更多信息。

**`MNT_SUIDDIR`** 设置了 SUID 位的目录会将新文件的所有者更改为目录自身的所有者。此标志需要在内核中编译 SUIDDIR 选项才能生效。参见 [mount(8)](../man8/mount.8.md) 和 [chmod(2)](chmod.2.md) 联机手册获取更多信息。

**`MNT_SYNCHRONOUS`** 对文件系统的所有 I/O 都应同步进行。

**`MNT_ASYNC`** 对文件系统的所有 I/O 都应异步进行。

**`MNT_FORCE`** 即使文件系统看起来不干净，也强制以读写方式挂载。危险。与 `MNT_UPDATE` 和 `MNT_RDONLY` 一起使用时，指定即使某些文件已打开进行写入，也要将文件系统强制降级为只读挂载。

**`MNT_NOCLUSTERR`** 禁用读聚类。

**`MNT_NOCLUSTERW`** 禁用写聚类。

**`MNT_NOCOVER`** 不要挂载到另一个挂载点的根之上。

**`MNT_EMPTYDIR`** 挂载点目录必须为空目录。

`MNT_UPDATE` 标志表示 mount 命令正应用于已挂载的文件系统。这允许更改挂载标志，而无需卸载并重新挂载文件系统。某些文件系统可能不允许更改所有标志。例如，许多文件系统不允许从读/写更改为只读。

`MNT_RELOAD` 标志使 vfs 子系统更新与指定已挂载文件系统相关的数据结构。

`type` 参数命名文件系统。系统已知的文件系统类型可以通过 [lsvfs(1)](../man1/lsvfs.1.md) 获取。

`data` 参数是指向一个结构的指针，该结构包含挂载的类型特定参数。这些参数结构的格式在每个文件系统的联机手册中描述。按照约定，文件系统联机手册通过在 [lsvfs(1)](../man1/lsvfs.1.md) 返回的文件系统名称前加上“mount_”前缀来命名。因此，NFS 文件系统由 [mount_nfs(8)](../man8/mount_nfs.8.md) 联机手册描述。应注意，默认文件系统（称为 UFS 和 UFS2）没有联机手册。

`unmount()` 系统调用将文件系统与指定的挂载点 `dir` 分离。

`flags` 参数可以包含 `MNT_FORCE`，以指定即使文件仍处于活动状态也应强制卸载文件系统。活动的特殊设备继续工作，但即使文件系统稍后重新挂载，对任何其他活动文件的进一步访问都会导致错误。

如果指定了 `MNT_BYFSID` 标志，`dir` 应改为编码为“`FSID`:`val0`:`val1`”形式的文件系统 ID，其中 `val0` 和 `val1` 是 `fsid_t` `val[]` 数组内容的十进制表示。具有指定文件系统 ID 的文件系统将被卸载。

## 返回值

若成功，`mount()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mount()` 和 `nmount()` 系统调用在发生以下情况之一时失败：

**[`EPERM`]** 调用者既不是超级用户也不是 `dir` 的所有者。

**[`ENAMETOOLONG`]** 路径名的某个分量超过 255 个字符，或整个路径名长度超过 1023 个字符。

**[`ELOOP`]** 在转换路径名时遇到太多符号链接。

**[`ENOENT`]** `dir` 的某个分量不存在。

**[`ENOTDIR`]** `name` 的某个分量不是目录，或 `special` 的路径前缀不是目录。

**[`EBUSY`]** 另一个进程当前持有对 `dir` 的引用。

**[`EBUSY`]** 给定了 `MNT_NOCOVER` 选项，且请求的挂载点已经是另一个挂载点的根。

**[`EFAULT`]** `dir` 参数指向进程分配的地址空间之外。

**[`EIO`]** 从 `special` 读取数据时发生 I/O 错误。

**[`EINTEGRITY`]** `special` 的后备存储在读取时检测到损坏的数据。

以下错误可能发生在 *ufs* 文件系统挂载时：

**[`ENODEV`]** ufs_args `fspec` 的某个分量不存在。

**[`ENOTBLK`]** `fspec` 参数不是块设备。

**[`ENOTEMPTY`]** 指定了 `MNT_EMPTYDIR` 选项，且请求的挂载点不是空目录。

**[`ENXIO`]** `fspec` 的主设备号超出范围（这表示关联硬件没有设备驱动程序）。

**[`EBUSY`]** `fspec` 已经挂载。

**[`EMFILE`]** 挂载表中没有剩余空间。

**[`EINVAL`]** 文件系统的超级块具有错误的魔数或超出范围的块大小。

**[`EINTEGRITY`]** 文件系统的超级块具有错误的校验哈希。通常可以通过运行 [fsck(8)](../man8/fsck.8.md) 来更正校验哈希。

**[`ENOMEM`]** 没有足够的内存来读取文件系统的柱面组信息。

**[`EIO`]** 读取超级块或柱面组信息时发生 I/O 错误。

**[`EFAULT`]** `fspec` 参数指向进程分配的地址空间之外。

以下错误可能发生在 *nfs* 文件系统挂载时：

**[`ETIMEDOUT`]** *Nfs* 尝试联系服务器超时。

**[`EFAULT`]** nfs_args 描述的信息的某些部分指向进程分配的地址空间之外。

`unmount()` 系统调用可能因以下错误之一而失败：

**[`EPERM`]** 调用者既不是超级用户也不是发起相应 `mount()` 调用的用户。

**[`ENAMETOOLONG`]** 路径名长度超过 1023 个字符。

**[`EINVAL`]** 请求的目录不在挂载表中。

**[`ENOENT`]** 使用 `MNT_BYFSID` 指定的文件系统 ID 在挂载表中未找到。

**[`EINVAL`]** 使用 `MNT_BYFSID` 指定的文件系统 ID 无法解码。

**[`EINVAL`]** 指定的文件系统是根文件系统。

**[`EBUSY`]** 某个进程正持有该文件系统上文件的引用。

**[`EIO`]** 写入缓存的文件系统信息时发生 I/O 错误。

**[`EFAULT`]** `dir` 参数指向进程分配的地址空间之外。

## 参见

[lsvfs(1)](../man1/lsvfs.1.md), [mksnap_ffs(8)](../man8/mksnap_ffs.8.md), [mount(8)](../man8/mount.8.md), [umount(8)](../man8/umount.8.md)

## 历史

`mount()` 和 `unmount()` 函数出现于 Version 1 AT&T UNIX。`nmount()` 系统调用首次出现于 FreeBSD 5.0。

## 缺陷

某些错误代码需要翻译为更明确的消息。

允许不受信任的用户挂载任意介质（例如通过启用 `vfs.usermount`）不应被视为安全。FreeBSD 中的大多数文件系统在构建时并未考虑防范恶意设备。
