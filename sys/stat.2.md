# stat(2)

`stat` — 获取文件状态

## 名称

`stat`, `lstat`, `fstat`, `fstatat`

## 库

Lb libc

## 概要

`#include <sys/stat.h>`

```c
int
stat(const char * restrict path, struct stat * restrict sb);

int
lstat(const char * restrict path, struct stat * restrict sb);

int
fstat(int fd, struct stat *sb);

int
fstatat(int fd, const char *path, struct stat *sb, int flag);
```

## 描述

`stat()` 系统调用获取由 `path` 所指向文件的信息。不要求对指定文件的读、写或执行权限，但通向该文件的路径名中列出的所有目录都必须可搜索。

`lstat()` 系统调用类似于 `stat()`，但当指定文件是符号链接时，`lstat()` 返回关于该链接的信息，而 `stat()` 返回该链接所引用文件的信息。

`fstat()` 系统调用获取由文件描述符 `fd` 所标识的已打开文件的相同信息。

`fstatat()` 系统调用等效于 `stat()` 和 `lstat()`，但当 `path` 指定相对路径时除外。对于 `fstatat()` 和相对 `path`，状态从相对于与文件描述符 `fd` 关联的目录的文件中获取，而不是相对于当前工作目录。

`flag` 的值由以下列表中定义的标志按位或运算构成，定义于

`#include <fcntl.h>`

**`AT_SYMLINK_NOFOLLOW`** 如果 `path` 命名一个符号链接，则返回该符号链接的状态。

**`AT_RESOLVE_BENEATH`** 仅遍历起始目录之下的路径。参见 [open(2)](open.2.md) 手册页中对 `O_RESOLVE_BENEATH` 标志的描述。

**`AT_EMPTY_PATH`** 如果 `path` 参数为空字符串，则对描述符 `fd` 所引用的文件或目录进行操作。如果 `fd` 等于 `AT_FDCWD`，则对当前工作目录进行操作。

如果 `fstatat()` 在 `fd` 参数中传入特殊值 `AT_FDCWD`，则使用当前工作目录，其行为分别与调用 `stat()` 或 `lstat()` 相同，具体取决于 `flag` 参数中是否设置了 `AT_SYMLINK_NOFOLLOW` 位。

当 `fstatat()` 以绝对 `path` 调用时，它忽略 `fd` 参数。

`sb` 参数是一个指向 `stat` 结构的指针，该结构由

`#include <sys/stat.h>`

定义，有关文件的信息将填入其中。

`struct stat` 中与文件系统相关的字段有：

**`st_dev`** 包含该文件的设备的数字 ID。

**`st_ino`** 文件的 inode 编号。

**`st_nlink`** 指向该文件的硬链接数。

**`st_flags`** 为该文件启用的标志。标志列表及其描述请参见 [chflags(2)](chflags.2.md)。

**`st_rdev`** 如果文件是字符或块特殊文件，则为该文件所引用设备的数字 ID；否则未指定。

`st_dev` 和 `st_ino` 字段一起在系统内唯一标识该文件。

`struct stat` 中与时间相关的字段有：

**`st_atim`** 文件数据最后一次被访问的时间。由 [read(2)](read.2.md) 和 [readv(2)](readv.2.md) 等系统调用隐式更改，由 [utimes(2)](utimes.2.md) 显式更改。

**`st_mtim`** 文件数据最后一次被修改的时间。由 [truncate(2)](truncate.2.md)、[write(2)](write.2.md) 和 [writev(2)](writev.2.md) 等系统调用隐式更改，由 [utimes(2)](utimes.2.md) 显式更改。此外，任何修改目录内容的系统调用都会更改受影响目录的 `st_mtim`。例如，[creat(2)](creat.2.md)、[mkdir(2)](mkdir.2.md)、[rename(2)](rename.2.md)、[link(2)](link.2.md) 和 [unlink(2)](unlink.2.md)。

**`st_ctim`** 文件状态最后一次被更改（inode 数据修改）的时间。由任何影响文件元数据（包括 `st_mtim`）的系统调用隐式更改，例如 [chflags(2)](chflags.2.md)、[chmod(2)](chmod.2.md)、[chown(2)](chown.2.md)、[truncate(2)](truncate.2.md)、[utimes(2)](utimes.2.md) 和 [write(2)](write.2.md)。此外，任何修改目录内容的系统调用都会更改受影响目录的 `st_ctim`。例如，[creat(2)](creat.2.md)、[mkdir(2)](mkdir.2.md)、[rename(2)](rename.2.md)、[link(2)](link.2.md) 和 [unlink(2)](unlink.2.md)。

**`st_birthtim`** inode 创建时间。

为兼容性定义了以下与时间相关的宏：

```c
#define	st_atime		st_atim.tv_sec
#define	st_mtime		st_mtim.tv_sec
#define	st_ctime		st_ctim.tv_sec
#ifndef _POSIX_SOURCE
#define	st_birthtime		st_birthtim.tv_sec
#endif
#ifndef _POSIX_SOURCE
#define	st_atimespec		st_atim
#define	st_mtimespec		st_mtim
#define	st_ctimespec		st_ctim
#define	st_birthtimespec	st_birthtim
#endif
```

`struct stat` 中与大小相关的字段有：

**`st_size`** 文件大小（以字节为单位）。

**`st_blksize`** 该文件的最佳 I/O 块大小。

**`st_blocks`** 为该文件分配的实际块数（以 512 字节为单位）。由于短符号链接存储在 inode 中，此数字可能为零。

`struct stat` 中与访问相关的字段有：

**`st_uid`** 文件所有者的用户 ID。

**`st_gid`** 文件的组 ID。

**`st_mode`** 文件的状态（见下文）。

状态信息字 `st_mode` 具有以下位：

```c
#define S_IFMT   0170000  /* 文件类型掩码 */
#define S_IFIFO  0010000  /* 命名管道 (fifo) */
#define S_IFCHR  0020000  /* 字符特殊文件 */
#define S_IFDIR  0040000  /* 目录 */
#define S_IFBLK  0060000  /* 块特殊文件 */
#define S_IFREG  0100000  /* 普通文件 */
#define S_IFLNK  0120000  /* 符号链接 */
#define S_IFSOCK 0140000  /* 套接字 */
#define S_IFWHT  0160000  /* whiteout */
#define S_ISUID  0004000  /* 执行时设置用户 ID */
#define S_ISGID  0002000  /* 执行时设置组 ID */
#define S_ISVTX  0001000  /* 设置了 sticky(7) 位 */
#define S_IRWXU  0000700  /* 所有者的 RWX 掩码 */
#define S_IRUSR  0000400  /* 读权限，所有者 */
#define S_IWUSR  0000200  /* 写权限，所有者 */
#define S_IXUSR  0000100  /* 执行/搜索权限，所有者 */
#define S_IRWXG  0000070  /* 组的 RWX 掩码 */
#define S_IRGRP  0000040  /* 读权限，组 */
#define S_IWGRP  0000020  /* 写权限，组 */
#define S_IXGRP  0000010  /* 执行/搜索权限，组 */
#define S_IRWXO  0000007  /* 其他的 RWX 掩码 */
#define S_IROTH  0000004  /* 读权限，其他 */
#define S_IWOTH  0000002  /* 写权限，其他 */
#define S_IXOTH  0000001  /* 执行/搜索权限，其他 */
```

访问模式列表，请参见

`#include <sys/stat.h>`

[access(2)](access.2.md) 和 [chmod(2)](chmod.2.md)。以下宏可用于测试 `m` 参数中传入的 `st_mode` 值是否对应于指定类型的文件：

**`S_ISBLK(m)`** 测试是否为块特殊文件。

**`S_ISCHR(m)`** 测试是否为字符特殊文件。

**`S_ISDIR(m)`** 测试是否为目录。

**`S_ISFIFO(m)`** 测试是否为管道或 FIFO 特殊文件。

**`S_ISLNK(m)`** 测试是否为符号链接。

**`S_ISREG(m)`** 测试是否为普通文件。

**`S_ISSOCK(m)`** 测试是否为套接字。

**`S_ISWHT(m)`** 测试是否为 whiteout。

如果测试为真，这些宏求值为非零值；如果测试为假，则求值为 0。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 兼容性

系统的早期版本对 `st_dev`、`st_uid`、`st_gid`、`st_rdev`、`st_size`、`st_blksize` 和 `st_blocks` 字段使用不同的类型。

## 错误

`stat()` 和 `lstat()` 系统调用在以下情况下会失败：

**[`EACCES`]** 路径前缀的某个组件的搜索权限被拒绝。

**[`EFAULT`]** `sb` 或 `path` 参数指向无效地址。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 指定的文件不存在。

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`EOVERFLOW`]** 以字节为单位的文件大小无法在 `sb` 所指向的结构中正确表示。

`fstat()` 系统调用在以下情况下会失败：

**[`EBADF`]** `fd` 参数不是有效的打开文件描述符。

**[`EFAULT`]** `sb` 参数指向无效地址。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EOVERFLOW`]** 以字节为单位的文件大小无法在 `sb` 所指向的结构中正确表示。

除 `lstat()` 返回的错误外，`fstatat()` 还可能在以下情况下失败：

**[`EBADF`]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD` 也不是一个有效的可用于搜索的文件描述符。

**[`EINVAL`]** `flag` 参数的值无效。

**[`ENOTDIR`]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

**[`ENOTCAPABLE`]** `path` 是绝对路径，或包含导致超出 `fd` 所指定目录层级的“..”组件，且进程处于 capability mode 或指定了 `AT_RESOLVE_BENEATH` 标志。

## 参见

[access(2)](access.2.md), [chmod(2)](chmod.2.md), [chown(2)](chown.2.md), [fhstat(2)](fhstat.2.md), [statfs(2)](statfs.2.md), [utimes(2)](utimes.2.md), [sticky(7)](../man7/sticky.7.md), [symlink(7)](../man7/symlink.7.md)

## 标准

`stat()` 和 `fstat()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。`fstatat()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`stat()` 和 `fstat()` 系统调用出现于 Version 1 AT&T UNIX。`lstat()` 系统调用出现于 4.2BSD。`fstatat()` 系统调用出现于 FreeBSD 8.0。

## 缺陷

对套接字应用 `fstat()` 返回一个清零的缓冲区，但 blocksize 字段以及唯一的设备和 inode 编号除外。