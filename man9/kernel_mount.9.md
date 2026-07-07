# kernel_mount(9)

`free_mntarg` — 作为内核挂载接口的一部分提供的函数

## 名称

`free_mntarg`, `kernel_mount`, `mount_arg`, `mount_argb`, `mount_argf`, `mount_argsu`

## 概要

```c
void
free_mntarg(struct mntarg *ma)

int
kernel_mount(struct mntarg *ma, int flags)

struct mntarg *
mount_arg(struct mntarg *ma, const char *name,
    const void *val, int len)

struct mntarg *
mount_argb(struct mntarg *ma, int flag, const char *name)

struct mntarg *
mount_argf(struct mntarg *ma, const char *name,
    const char *fmt, ...)

struct mntarg *
mount_argsu(struct mntarg *ma, const char *name,
    const void *val, int len)
```

## 描述

`kernel_mount` 系列函数作为 API 提供，用于构建将从内核内部挂载文件系统时使用的挂载参数列表。通过累积参数列表，API 成形并提供内核控制 [mount(8)](../man8/mount.8.md) 实用程序所需的信息。发生错误时，过程将停止。这不会导致 [panic(9)](panic.9.md)。

结构头存储在 `src/sys/kern/vfs_mount.c` 中，允许自动创建结构以简化挂载过程。整个过程完成时必须始终释放已分配的内存，否则就是错误。

`free_mntarg` 函数用于释放或清除 `mntarg` 结构。

`kernel_mount` 函数从结构中提取信息以在给定文件系统上执行挂载请求。此外，`kernel_mount` 函数总是调用 `free_mntarg` 函数。如果 `ma` 包含在构造期间生成的任何错误代码，将调用该代码并且不会尝试挂载文件系统。

`mount_arg` 函数接受一个普通参数，并根据各种挂载选项构造结构的一部分。如果长度值小于 0，则使用 strlen(3)。此参数将被引用，直到调用 `free_mntarg` 或 `kernel_mount`。

`mount_argb` 函数用于向结构添加布尔参数。`flag` 是布尔值，`name` 必须以 "no" 开头，否则将发生 panic。

`mount_argf` 函数将 [printf(9)](printf.9.md) 风格的参数添加到当前结构中。

`mount_argsu` 函数将来自用户态字符串的参数添加到结构中。

## 实例

`*_cmount` 函数的示例：

```c
static int
msdosfs_cmount(struct mntarg *ma, void *data, int flags, struct thread *td)
{
	struct msdosfs_args args;
	int error;
	if (data == NULL)
		return (EINVAL);
	error = copyin(data, &args, sizeof(args));
	if (error)
		return (error);
	ma = mount_argsu(ma, "from", args.fspec, MAXPATHLEN);
	ma = mount_arg(ma, "export", &args.export, sizeof(args.export));
	ma = mount_argf(ma, "uid", "%d", args.uid);
	ma = mount_argf(ma, "gid", "%d", args.gid);
	ma = mount_argf(ma, "mask", "%d", args.mask);
	ma = mount_argf(ma, "dirmask", "%d", args.dirmask);
	ma = mount_argb(ma, args.flags & MSDOSFSMNT_SHORTNAME, "noshortname");
	ma = mount_argb(ma, args.flags & MSDOSFSMNT_LONGNAME, "nolongname");
	ma = mount_argb(ma, !(args.flags & MSDOSFSMNT_NOWIN95), "nowin95");
	ma = mount_argb(ma, args.flags & MSDOSFSMNT_KICONV, "nokiconv");
	ma = mount_argsu(ma, "cs_win", args.cs_win, MAXCSLEN);
	ma = mount_argsu(ma, "cs_dos", args.cs_dos, MAXCSLEN);
	ma = mount_argsu(ma, "cs_local", args.cs_local, MAXCSLEN);
	error = kernel_mount(ma, flags);
	return (error);
}
```

## 参见

[VFS(9)](vfs.9.md), [VFS_MOUNT(9)](vfs_mount.9.md)

## 历史

`kernel_mount` 系列函数和本手册页首次出现在 FreeBSD 6.0 中。

## 作者

`kernel_mount` 系列函数和 API 由 Poul-Henning Kamp <phk@FreeBSD.org> 开发。本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 编写。
