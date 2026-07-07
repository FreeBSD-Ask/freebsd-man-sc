# pathconf(2)

`pathconf` — 获取可配置路径名变量

## 名称

`pathconf`, `lpathconf`, `fpathconf`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
long
pathconf(const char *path, int name);

long
lpathconf(const char *path, int name);

long
fpathconf(int fd, int name);
```

## 描述

`pathconf()`、`lpathconf()` 和 `fpathconf()` 系统调用为应用程序提供了一种方法，以确定与路径名或文件描述符关联的可配置系统限制或选项变量的当前值。

对于 `pathconf()` 和 `lpathconf()`，`path` 参数是文件或目录的名称。对于 `fpathconf()`，`fd` 参数是一个打开的文件描述符。`name` 参数指定要查询的系统变量。每个 name 值的符号常量可在头文件 `<unistd.h>` 中找到。

`lpathconf()` 系统调用类似于 `pathconf()`，但当指定文件是符号链接时，`lpathconf()` 返回关于该链接的信息，而 `pathconf()` 返回该链接所引用文件的信息。

可用值如下：

**`_PC_LINK_MAX`** 最大文件链接数。

**`_PC_MAX_CANON`** 终端规范输入行的最大字节数。

**`_PC_MAX_INPUT`** 终端输入队列中可用空间的最小最大字节数。

**`_PC_NAME_MAX`** 文件名中的最大字节数。

**`_PC_PATH_MAX`** 路径名中的最大字节数。

**`_PC_PIPE_BUF`** 将以原子方式写入管道的最大字节数。

**`_PC_CHOWN_RESTRICTED`** 如果 [chown(2)](chown.2.md) 系统调用需要适当特权，则返回 1，否则返回 0。IEEE Std 1003.1-2001 ("POSIX.1") 在所有情况下都要求适当特权，但此行为在标准的早期版本中是可选的。

**`_PC_NO_TRUNC`** 如果尝试使用长于 {`NAME_MAX`} 的路径名组件会导致 `ENAMETOOLONG` 错误，则返回大于零的值；否则，此类组件将被截断为 {`NAME_MAX`}。IEEE Std 1003.1-2001 ("POSIX.1") 在所有情况下都要求该错误，但此行为在标准的早期版本中是可选的，且某些不兼容 POSIX 的文件系统不支持此行为。

**`_PC_VDISABLE`** 返回终端字符禁用值。

**`_PC_ASYNC_IO`** 如果支持异步 I/O，则返回 1，否则返回 0。

**`_PC_PRIO_IO`** 如果此文件支持优先级 I/O，则返回 1，否则返回 0。

**`_PC_SYNC_IO`** 如果此文件支持同步 I/O，则返回 1，否则返回 0。

**`_PC_ALLOC_SIZE_MIN`** 为文件的任何部分分配的最小存储字节数。

**`_PC_FILESIZEBITS`** 表示最大文件大小所需的位数。

**`_PC_REC_INCR_XFER_SIZE`** 在 `_PC_REC_MIN_XFER_SIZE` 和 `_PC_REC_MAX_XFER_SIZE` 之间文件传输大小的推荐增量。

**`_PC_REC_MAX_XFER_SIZE`** 推荐的最大文件传输大小。

**`_PC_REC_MIN_XFER_SIZE`** 推荐的最小文件传输大小。

**`_PC_REC_XFER_ALIGN`** 推荐的文件传输缓冲区对齐方式。

**`_PC_SYMLINK_MAX`** 符号链接中的最大字节数。

**`_PC_ACL_EXTENDED`** 如果可在指定文件上设置访问控制列表（ACL），则返回 1，否则返回 0。

**`_PC_ACL_NFS4`** 如果可在指定文件上设置 NFSv4 ACL，则返回 1，否则返回 0。

**`_PC_ACL_PATH_MAX`** 每个文件的最大 ACL 条目数。

**`_PC_CAP_PRESENT`** 如果可在指定文件上设置能力状态，则返回 1，否则返回 0。

**`_PC_INF_PRESENT`** 如果可在指定文件上设置信息标签，则返回 1，否则返回 0。

**`_PC_MAC_PRESENT`** 如果可在指定文件上设置强制访问控制（MAC）标签，则返回 1，否则返回 0。

**`_PC_MIN_HOLE_SIZE`** 如果文件系统支持报告空洞（参见 [lseek(2)](lseek.2.md)），`pathconf()` 和 `fpathconf()` 返回一个正数，表示以字节为单位返回的最小空洞大小。返回的空洞偏移量将与此相同值对齐。如果文件系统未指定最小空洞大小但仍报告空洞，则返回特殊值 1。

**`_PC_DEALLOC_PRESENT`** 如果文件系统支持打孔操作（参见 [fspacectl(2)](fspacectl.2.md)），则返回 1，否则返回 0。

**`_PC_NAMEDATTR_ENABLED`** 如果文件系统启用了命名属性，则返回 1，否则返回 0。

**`_PC_HAS_NAMEDATTR`** 如果该文件存在一个或多个命名属性，则返回 1，否则返回 0。

**`_PC_HAS_HIDDENSYSTEM`** 如果所有 `UF_ARCHIVE`、`UF_HIDDEN` 和 `UF_SYSTEM` 标志都可以通过 [chflags(2)](chflags.2.md) 设置，则返回 1，否则返回 0。

**`_PC_CLONE_BLKSIZE`** 如果文件系统支持块克隆，则返回通过 [copy_file_range(2)](copy_file_range.2.md) 进行块克隆所需的块大小，否则返回 0。

**`_PC_CASE_INSENSITIVE`** 如果文件系统执行不区分大小写的查找，则返回 1，否则返回 0。

## 返回值

如果对 `pathconf()` 或 `fpathconf()` 的调用不成功，则返回 -1 并适当设置 `errno`。否则，如果该变量关联的功能在系统中没有限制，则返回 -1 且不修改 `errno`。否则，返回当前变量值。

## 错误

如果发生以下任一情况，`pathconf()` 和 `fpathconf()` 系统调用将返回 -1 并将 `errno` 设置为相应值。

**[`EINVAL`]** `name` 参数的值无效。

**[`EINVAL`]** 实现不支持该变量名与关联文件之间的关联。

`pathconf()` 系统调用在以下情况下会失败：

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 {`NAME_MAX`} 个字符（但参见上文的 `_PC_NO_TRUNC`），或整个路径名超过 {`PATH_MAX`} 个字符。

**[`ENOENT`]** 指定的文件不存在。

**[`EACCES`]** 路径前缀的某个组件的搜索权限被拒绝。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

`fpathconf()` 系统调用在以下情况下会失败：

**[`EBADF`]** `fd` 参数不是有效的打开文件描述符。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

## 参见

[chflags(2)](chflags.2.md), [copy_file_range(2)](copy_file_range.2.md), [lseek(2)](lseek.2.md), [sysctl(3)](../gen/sysctl.3.md)

## 历史

`pathconf()` 和 `fpathconf()` 系统调用首次出现于 4.4BSD。`lpathconf()` 系统调用首次出现于 FreeBSD 8.0。
