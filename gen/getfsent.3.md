# getfsent(3)

`getfsent` — 获取文件系统描述符文件条目

## 名称

`getfsent`, `getfsspec`, `getfsfile`, `setfsent`, `endfsent`

## 库

Lb libc

## 概要

```c
#include <fstab.h>

struct fstab *
getfsent(void);

struct fstab *
getfsspec(const char *spec);

struct fstab *
getfsfile(const char *file);

int
setfsent(void);

void
endfsent(void);

void
setfstab(const char *file);

const char *
getfstab(void);
```

## 描述

`getfsent`、`getfsspec` 和 `getfsfile` 函数各自返回一个指向具有以下结构的对象的指针，该结构包含文件系统描述文件中某一行的各分解字段：

```c
struct fstab {
	char	*fs_spec;	/* 块特殊设备名 */
	char	*fs_file;	/* 文件系统路径前缀 */
	char	*fs_vfstype;	/* 文件系统类型，ufs、nfs */
	char	*fs_mntops;	/* 挂载选项，类似 -o */
	char	*fs_type;	/* 来自 fs_mntops 的 FSTAB_* */
	int	fs_freq;	/* 转储频率，以天为单位 */
	int	fs_passno;	/* 并行 fsck 的遍次编号 */
};
```

各字段的含义见 [fstab(5)](../man5/fstab.5.md)。

`setfsent` 函数打开文件（关闭任何先前打开的文件），或如果文件已打开则将其倒回。

`endfsent` 函数关闭文件。

`setfstab` 函数设置后续操作所使用的文件。由 `setfstab` 设置的值不会在调用 `endfsent` 后保留。

`getfstab` 函数返回将要使用的文件名。

`getfsspec` 和 `getfsfile` 函数搜索整个文件（如有必要则打开它）以查找匹配的特殊文件名或文件系统文件名。

对于希望读取整个数据库的程序，`getfsent` 读取下一条目（如有必要则打开文件）。

文件中所有 type 字段等同于 `FSTAB_XX` 的条目都将被忽略。

## 返回值

`getfsent`、`getfsspec` 和 `getfsfile` 函数在 `EOF` 或出错时返回 `NULL` 指针。`setfsent` 函数失败时返回 0，成功时返回 1。`endfsent` 函数不返回任何值。

## 环境变量

**`PATH_FSTAB`** 如果设置了环境变量 `PATH_FSTAB`，所有操作都将针对指定文件执行。如果进程环境或内存地址空间被视为"受污染"，则 `PATH_FSTAB` 将不被采纳。（参见 [issetugid(2)](../sys/issetugid.2.md) 获取更多信息。）

## 文件

**/etc/fstab**

## 参见

[fstab(5)](../man5/fstab.5.md)

## 历史

`getfsent` 函数出现于 4.0BSD；`endfsent`、`getfsfile`、`getfsspec` 和 `setfsent` 函数出现于 4.3BSD；`setfstab` 和 `getfstab` 函数出现于 FreeBSD 5.1。

## 缺陷

这些函数使用静态数据存储；如果数据留待将来使用，应在任何后续调用覆盖它之前进行复制。
