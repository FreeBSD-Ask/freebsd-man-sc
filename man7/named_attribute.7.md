# named_attribute(7)

`named_attribute` — 类 Solaris 的扩展属性系统接口

## 名称

`named_attribute`

## 描述

命名属性（NFS 第 4 版术语）的系统接口描述。

### 简介

本文档描述一种扩展属性的备用系统接口，与 [extattr(2)](../sys/extattr_get_file.2.md) 相比有所不同。该接口基于 Solaris 和 NFS 第 4 版所提供的接口。

该接口将一个目录（称为命名属性目录）关联到某个文件系统对象。读取该目录的方式与读取普通目录相同，通过 [getdents(2)](../sys/getdirentries.2.md) 或 [getdirentries(2)](../sys/getdirentries.2.md) 系统调用完成。其中 `.` 和 `..` 条目分别指向目录本身和所关联的文件对象。该目录中的其他条目是所关联文件对象的扩展属性名称，称为命名属性。这些命名属性是用于存储属性值的常规文件。

命名属性目录并不存在于文件系统的名字空间中。通过对文件执行 [open(2)](../sys/open.2.md) 或 [openat(2)](../sys/open.2.md) 系统调用并指定 `O_NAMEDATTR` 标志、`path` 参数为 `.`，即可访问该目录以查询文件的命名属性。此文件描述符可作为多种系统调用的 `fd` 参数使用，例如：[fchdir(2)](../sys/chdir.2.md)、[unlinkat(2)](../sys/unlink.2.md) 和 [renameat(2)](../sys/rename.2.md)。[renameat(2)](../sys/rename.2.md) 仅允许在同一命名属性目录内重命名命名属性。

当把文件系统名字空间中某个文件对象的文件描述符作为 [openat(2)](../sys/open.2.md) 的 `fd` 参数，同时指定 `flag` `O_NAMEDATTR` 且 `path` 参数为某命名属性的名称（非 `.` 或 `..`），将返回该命名属性的文件描述符。如果指定了 `flag` `O_CREAT`，则当命名属性不存在时会创建它。`path` 参数必须是单个分量名称，其中不得包含“/”。对这些命名属性文件描述符的 I/O 操作可由标准 I/O 系统调用完成，例如：[read(2)](../sys/read.2.md)、[write(2)](../sys/write.2.md)、[lseek(2)](../sys/lseek.2.md) 和 [ftruncate(2)](../sys/truncate.2.md)。

如果文件系统支持命名属性，[pathconf(2)](../sys/pathconf.2.md) 中 `_PC_NAMEDATTR_ENABLED` `name` 参数将返回 1。如果文件具有一个或多个命名属性，[pathconf(2)](../sys/pathconf.2.md) 中 `_PC_HAS_NAMEDATTR` `name` 参数将返回 1。如果应用程序在不存在命名属性目录时对“.”执行 [openat(2)](../sys/open.2.md) 来打开命名属性目录，将创建一个空的命名属性目录。可通过测试 `_PC_HAS_NAMEDATTR` 来避免不必要地创建这些命名属性目录。

与 [extattr(2)](../sys/extattr_get_file.2.md) 相比，命名属性接口是用于操纵扩展属性的另一种机制/系统调用接口。尽管命名属性机制可能要求文件系统内部以不同方式实现扩展属性，但 ZFS 和 NFSv4 都同时提供这两种机制，可交替用于操纵扩展属性，但存在若干限制。

- [extattr(2)](../sys/extattr_get_file.2.md) 接口要求扩展属性的值通过单次系统调用使用单一缓冲区来设置或获取。这限制了属性值的大小。
- 命名属性接口不支持系统名字空间扩展属性，因此系统名字空间扩展属性必须通过 [extattr(2)](../sys/extattr_get_file.2.md) 来操纵。
- 对于 ZFS，如果在 ZFS `xattr` 属性设置为“sa”时创建了字节数较小的扩展属性，则该扩展属性只能通过 [extattr(2)](../sys/extattr_get_file.2.md) 看到，而不能作为命名属性看到。在将 `xattr` 属性设置为“dir”后，通过 [tar(1)](../man1/bsdtar.1.md) 对文件进行归档/解档，会使这些属性同时作为命名属性和通过 [extattr(2)](../sys/extattr_get_file.2.md) 可见。
- 对于 ZFS，还存在这样的可能：先在 ZFS `xattr` 属性设置为“sa”时创建一个属性，然后将 ZFS `xattr` 属性改为“dir”后再创建另一个同名属性，从而得到两个同名属性。在 ZFS `xattr` 属性设置为“sa”时创建的那个属性可通过 [rmextattr(8)](../man8/rmextattr.8.md) 删除。
- 为避免 ZFS 上的这些问题，强烈建议在文件系统上使用命名属性时，在创建文件系统后即将 ZFS `xattr` 属性设置为“dir”。

与 [extattr(2)](../sys/extattr_get_file.2.md) 相比，命名属性机制/系统调用接口具有若干优势。由于属性值通过 [read(2)](../sys/read.2.md) 和 [write(2)](../sys/write.2.md) 系统调用更新，属性数据可像任何常规文件一样大，并且可部分更新。（注意，该接口不提供 [extattr(2)](../sys/extattr_get_file.2.md) 所提供的原子性保证。）访问命名属性目录的权限由所关联文件对象的访问控制信息决定。然而，可以像常规文件那样为每个单独的属性设置访问控制信息。这样即可通过 [fchown(2)](../sys/chown.2.md) 对属性权限实现“按属性”的细粒度控制。

目前，唯一支持该接口的本地文件系统是 ZFS，且仅当 `xattr` 属性设置为“dir”时才支持。（注意，即使“zfs get xattr <file-system>”显示“on”，也必须执行命令“zfs set xattr=dir <file-system>”，并重新挂载以使设置生效。）NFSv4 挂载也支持该接口，但前提是 NFSv4 服务器文件系统支持命名属性（openattr 操作）。FreeBSD NFSv4 服务器仅对导出文件系统的 ZFS 且该文件系统的“xattr”属性设置为“dir”时才支持命名属性。

## 实例

```sh
#include <stdio.h>
#include <dirent.h>
#include <fcntl.h>
#include <unistd.h>
...
/* 针对“Myfile”文件。为简洁起见，省略了失败检查。 */
int file_fd, nameddir_fd, namedattr_fd;
ssize_t siz;
char buf[DIRBLKSIZ], *cp;
struct dirent *dp;
long named_enabled, has_named_attrs;
...
/* 检查是否支持命名属性。 */
named_enabled = pathconf("myfile", _PC_NAMEDATTR_ENABLED);
if (named_enabled <= 0)
	err(1, "Named attributes not enabled");
/* 测试该文件是否存在命名属性。 */
has_named_attrs = pathconf("myfile", _PC_HAS_NAMEDATTR);
if (has_named_attrs == 1)
	printf("myfile has named attribute(s)n");
else
	printf("myfile does not have any named attributesn");
/* 打开命名属性目录。 */
file_fd = open("myfile", O_RDONLY, 0);
nameddir_fd = openat(file_fd, ".", O_NAMEDATTR, 0);
...
/* 读取该目录，为简便起见，假定其全部内容可放入 DIRBLKSIZ。 */
siz = getdents(fd, buf, sizeof(buf));
cp = buf;
while (cp < &buf[siz]) {
	dp = (struct dirent *)cp;
	printf("name=%sn", dp->d_name);
	cp += dp->d_reclen;
}
...
/* 打开/创建名为“foo”的命名属性。 */
namedattr_fd = openat(file_fd, "foo", O_CREAT | O_RDWR |
    O_TRUNC | O_NAMEDATTR, 0600);
...
/* 写入 foo 的属性值。 */
write(namedattr_fd, "xxxyyy", 6);
...
/* 读取 foo 的属性值。 */
lseek(namedattr_fd, 0, SEEK_SET);
siz = read(namedattr_fd, buf, sizeof(buf));
...
/* 关闭“foo”。 */
close(namedattr_fd);
...
/* 将“foo”重命名为“oldfoo”。 */
renameat(nameddir_fd, "foo", nameddir_fd, "oldfoo");
/* 删除“oldfoo”。 */
unlinkat(nameddir_fd, "oldfoo", AT_RESOLVE_BENEATH);
```

可使用 [runat(1)](../man1/runat.1.md) 命令对命名属性执行 shell 命令。例如：

```sh
$ runat myfile cp /etc/hosts attrhosts	# 创建 attrhosts
$ runat myfile cat attrhosts		# 显示 attrhosts 的内容
$ runat myfile ls -l			# 列出 myfile 的属性
```

如果使用 bash(1) shell，命令“cd -@ foo”会进入文件对象“foo”的命名属性目录。

## 参见

bash(1), [runat(1)](../man1/runat.1.md), [tar(1)](../man1/bsdtar.1.md), [chdir(2)](../sys/chdir.2.md), [extattr(2)](../sys/extattr_get_file.2.md), [lseek(2)](../sys/lseek.2.md), [open(2)](../sys/open.2.md), [pathconf(2)](../sys/pathconf.2.md), [read(2)](../sys/read.2.md), [rename(2)](../sys/rename.2.md), [truncate(2)](../sys/truncate.2.md), [unlinkat(2)](../sys/unlink.2.md), [write(2)](../sys/write.2.md), [zfsprops(7)](zfsprops.7.md), [rmextattr(8)](../man8/rmextattr.8.md)

## 历史

该接口首次出现于 FreeBSD 15.0。
