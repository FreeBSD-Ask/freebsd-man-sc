# dir(5)

`dir` — 目录文件格式

## 名称

`dir`, `dirent`

## 概要

`#include <dirent.h>`

## 描述

目录提供了一种方便的分层方法来分组文件，同时屏蔽了存储介质的底层细节。目录文件通过其 inode(5) 条目中的一个标志与普通文件区分开来。目录文件由若干记录（目录项）组成，每条记录包含关于某个文件的信息以及指向该文件本身的指针。目录项可以包含其他目录以及普通文件；这种嵌套的目录称为子目录。通过这种方式形成了目录和文件的层次结构，称为文件系统（或称为文件系统树）。

每个目录文件包含两个特殊的目录项：一个是指向目录自身的指针，称为 dot `.`；另一个是指向其父目录的指针，称为 dot-dot `..`。dot 和 dot-dot 是有效的路径名，但是系统根目录 `/` 没有父目录，dot-dot 像 dot 一样指向自身。

文件系统节点是普通的目录文件，在其上嫁接了文件系统对象，例如物理磁盘或该磁盘的某个分区。（参见 mount(2) 和 [mount(8)](../man8/mount.8.md)）

目录项格式定义在以下文件中：

`#include <sys/dirent.h>`

（应用程序不应直接包含此文件）：

```sh
#ifndef	_SYS_DIRENT_H_
#define	_SYS_DIRENT_H_
#include <machine/ansi.h>
/*
 * dirent 结构定义了 getdirentries(2) 系统调用返回的目录项格式。
 *
 * 目录项开头是一个 struct dirent，包含其
 * inode 号、该项长度以及该项中包含的
 * 名称长度。其后是以 null 字节填充至 8 字节
 * 边界的名称。所有名称保证以 null 结尾。
 * 目录中名称的最大长度为 MAXNAMLEN。
 * 在头部最后一个成员和
 * d_name 之间显式添加了填充，以避免在 LP64 架构上
 * dirent 末尾出现 ABI 填充。有代码依赖于 d_name
 * 位于末尾这一特性。此外，为 ILP32 架构
 * 保留此填充可简化 compat32 层。
 */
struct dirent {
	ino_t      d_fileno;		/* 该项的文件号 */
	off_t      d_off;		/* 下一个目录项的目录偏移量 */
	__uint16_t d_reclen;		/* 本记录的长度 */
	__uint8_t  d_type;		/* 文件类型，见下文 */
	__uint8_t  d_namlen;		/* d_name 中字符串的长度 */
	__uint32_t d_pad0;
#if __BSD_VISIBLE
#define	MAXNAMLEN	255
	char	d_name[MAXNAMLEN + 1];	/* 名称不得超过此长度 */
#else
	char	d_name[255 + 1];	/* 名称不得超过此长度 */
#endif
};
/*
 * 文件类型
 */
#define	DT_UNKNOWN	 0
#define	DT_FIFO		 1
#define	DT_CHR		 2
#define	DT_DIR		 4
#define	DT_BLK		 6
#define	DT_REG		 8
#define	DT_LNK		10
#define	DT_SOCK		12
#define	DT_WHT		14
/*
 * 在 stat 结构类型与目录类型之间转换。
 */
#define	IFTODT(mode)	(((mode) & 0170000) >> 12)
#define	DTTOIF(dirtype)	((dirtype) << 12)
/*
 * _GENERIC_DIRSIZ 宏给出能容纳
 * 该目录项的最小记录长度。它返回 struct direct 中
 * 不含 d_name 字段的空间量，加上容纳名称及
 * 终止 null 字节所需的空间 (dp->d_namlen+1)，
 * 并向上取整到 8 字节边界。
 *
 * XXX 虽然此宏位于实现命名空间中，但它需要
 * 一个不在该命名空间中的常量。
 */
#define	_GENERIC_DIRLEN(namlen)					\
	((__offsetof(struct dirent, d_name) + (namlen) + 1 + 7) & ~7)
#define	_GENERIC_DIRSIZ(dp)	_GENERIC_DIRLEN((dp)->d_namlen)
#endif /* __BSD_VISIBLE */
#ifdef _KERNEL
#define	GENERIC_DIRSIZ(dp)	_GENERIC_DIRSIZ(dp)
#endif
#endif /* !_SYS_DIRENT_H_ */
```

## 参见

[fs(5)](fs.5.md), inode(5)

## 历史

`dirent` 文件格式出现于 Version 7 AT&T UNIX。

## 缺陷

struct dirent 的 d_type 成员的使用不具备可移植性，因为它是 FreeBSD 特有的。在某些文件系统上也可能失效，例如 cd9660 文件系统。
