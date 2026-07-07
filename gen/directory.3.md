# directory(3)

`opendir` — 目录操作

## 名称

`opendir`, `fdopendir`, `readdir`, `readdir_r`, `telldir`, `seekdir`, `rewinddir`, `closedir`, `fdclosedir`, `dirfd`

## 库

libc

## 概要

`#include <dirent.h>`

```c
DIR *
opendir(const char *filename);

DIR *
fdopendir(int fd);

struct dirent *
readdir(DIR *dirp);

int
readdir_r(DIR *dirp, struct dirent *entry, struct dirent **result);

long
telldir(DIR *dirp);

void
seekdir(DIR *dirp, long loc);

void
rewinddir(DIR *dirp);

int
closedir(DIR *dirp);

int
fdclosedir(DIR *dirp);

int
dirfd(DIR *dirp);
```

## 描述

> **注意**：`readdir_r` 接口已弃用，因为除非 `NAME_MAX` 是固定值，否则无法正确使用它。

`opendir` 函数打开由 `filename` 命名的目录，将其与一个*目录流*关联，并返回一个指针，用于在后续操作中标识该*目录流*。

`fdopendir` 函数等同于 `opendir` 函数，区别在于目录由文件描述符 `fd` 而非名称指定。调用时与文件描述符关联的文件偏移量决定了将返回哪些条目。

从 `fdopendir` 成功返回后，该文件描述符由系统控制，如果试图关闭该文件描述符，或通过 `closedir` 、 `readdir` 、 `readdir_r` 或 `rewinddir` 以外的方式修改关联描述的状态，行为是未定义的。调用 `closedir` 时，该文件描述符会被关闭。成功调用 `fdopendir` 后，该文件描述符上会设置 `FD_CLOEXEC` 标志。

`readdir` 函数返回指向下一个目录条目的指针。该目录条目在下次对同一*目录流*调用 `readdir` 或 `closedir` 之前保持有效。

`readdir_r` 函数提供与 `readdir` 相同的功能，但调用者必须提供一个目录 `entry` 缓冲区来存储结果。该缓冲区必须足够大，以容纳一个 `struct dirent` ，且其 `d_name` 数组具有 `NAME_MAX` + 1 个元素。如果读取成功， `result` 指向 `entry` ；到达目录末尾时， `result` 被设置为 `NULL` 。

`telldir` 函数返回一个表示与指定*目录流*关联的当前位置的令牌。`telldir` 返回的值仅在其派生自的*目录流* 的生命周期内有效。如果目录被关闭后重新打开， `telldir` 先前返回的值将不再有效。调用 `rewinddir` 也会使 `telldir` 返回的值失效。

`seekdir` 函数设置*目录流* 上下一次 `readdir` 操作的位置。新位置回退到执行 `telldir` 操作时与*目录流* 关联的位置。

`rewinddir` 函数将指定*目录流* 的位置重置到目录起始处。

`closedir` 函数关闭指定的*目录流* 并释放与 `dirp` 关联的结构。

`fdclosedir` 函数等同于 `closedir` 函数，区别在于它返回与 `dirp` 关联的文件描述符，而非关闭它。

`dirfd` 函数返回与 `dirp` 关联的文件描述符。

## 实例

在目录中搜索条目 `name` 的示例代码如下：

```c
dirp = opendir(".");
if (dirp == NULL)
	return (ERROR);
len = strlen(name);
while ((dp = readdir(dirp)) != NULL) {
	if (dp->d_namlen == len && strcmp(dp->d_name, name) == 0) {
		(void)closedir(dirp);
		return (FOUND);
	}
}
(void)closedir(dirp);
return (NOT_FOUND);
```

## 返回值

`opendir` 和 `fdopendir` 函数成功时返回指向新*目录流* 的指针，失败时返回 `NULL` 。

`readdir` 函数成功时返回指向目录条目的指针，失败时返回 `NULL` 。`readdir_r` 函数成功时返回 0，失败时返回一个错误号。

`telldir` 函数成功时返回非负值，失败时返回 -1。

`closedir` 函数成功时返回 0，失败时返回 -1。`fdclosedir` 和 `dirfd` 函数成功时返回一个打开的文件描述符，失败时返回 -1。

## 错误

`opendir` 函数在以下情况下会失败：

**`[EACCES]`** 对 `filename` 路径前缀中的某个组件拒绝搜索权限，或对 `filename` 拒绝读取权限。

**`[ELOOP]`** 在解析 `filename` 参数时遇到符号链接循环。

**`[ENAMETOOLONG]`** `filename` 参数的长度超过 `PATH_MAX` ，或某个路径名组件长度超过 `NAME_MAX` 。

**`[ENOENT]`** `filename` 的某个组件未命名一个现有目录，或 `filename` 为空字符串。

**`[ENOTDIR]`** `filename` 的某个组件不是目录。

`fdopendir` 函数在以下情况下会失败：

**`[EBADF]`** `fd` 参数不是一个为读取而打开的有效文件描述符。

**`[ENOTDIR]`** 描述符 `fd` 未与目录关联。

`readdir` 和 `readdir_r` 函数还可能失败并设置 `errno` 为 getdents(2) 例程所指定的任何错误。

`telldir` 函数还可能失败并设置 `errno` 为 realloc(3) 例程所指定的任何错误。

`closedir` 函数还可能失败并设置 `errno` 为 [close(2)](../sys/close.2.md) 例程所指定的任何错误。

`dirfd` 函数在以下情况下会失败：

**`[EINVAL]`** `dirp` 参数未引用一个有效的目录流。

## 参见

[close(2)](../sys/close.2.md), [lseek(2)](../sys/lseek.2.md), [open(2)](../sys/open.2.md), [read(2)](../sys/read.2.md), [dir(5)](../man5/dir.5.md)

## 标准

`closedir` 、 `dirfd` 、 `fdopendir` 、 `opendir` 、 `readdir` 、 `readdir_r` 、 `rewinddir` 、 `seekdir` 和 `telldir` 函数预期遵循 IEEE Std 1003.1-2008 ("POSIX.1") 标准。`fdclosedir` 函数以及 `struct dirent` 的 `d_off` 、 `d_reclen` 和 `d_type` 字段是非标准的，不应在可移植程序中使用。

## 历史

`opendir` 、 `readdir` 、 `telldir` 、 `seekdir` 、 `rewinddir` 、 `closedir` 和 `dirfd` 函数出现于 4.2BSD。`fdopendir` 函数出现于 FreeBSD 8.0。`fdclosedir` 函数出现于 FreeBSD 10.0。

## 缺陷

如果同时发生并行的 unlink 操作且目录大于一页，`telldir` 和 `seekdir` 的行为可能不正确。现有代码确保在最后一次 `readdir` 之前立即通过 `telldir` 给出的位置进行 `seekdir` 时，始终能设置正确的位置以返回与最后一次 `readdir` 相同的值。这对于某些需要"退回最后读取的条目"的应用程序（如 Samba）来说已足够。回退到除目录起始处以外的任何其他位置，如果存在删除操作，可能导致意外行为。希望通过对 `getdirentries` 和 VFS 的更改来解决此情况。
