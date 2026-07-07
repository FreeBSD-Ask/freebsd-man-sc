# chmod(2)

`chmod` — 更改文件模式

## 名称

`chmod`, `fchmod`, `lchmod`, `fchmodat`

## 库

Lb libc

## 概要

`#include <sys/stat.h>`

```c
int
chmod(const char *path, mode_t mode);

int
fchmod(int fd, mode_t mode);

int
lchmod(const char *path, mode_t mode);

int
fchmodat(int fd, const char *path, mode_t mode, int flag);
```

## 描述

由 `path` 指定名称或由文件描述符 `fd` 引用的文件的文件权限位将被更改为 `mode`。`chmod()` 系统调用会验证进程所有者（用户）拥有 `path`（或 `fd`）所指定的文件，或者是超级用户。`chmod()` 系统调用会跟随符号链接，以操作链接所指向的目标而非链接本身。

`lchmod()` 系统调用类似于 `chmod()`，但不跟随符号链接。

`fchmodat()` 等效于 `chmod()` 或 `lchmod()`，具体取决于 `flag`，但当 `path` 指定相对路径时除外。在此情况下，要更改的文件是相对于与文件描述符 `fd` 关联的目录来确定，而不是相对于当前工作目录。`flag` 的值由以下列表中定义的标志按位或运算构成，定义于

`#include <fcntl.h>`

**`AT_SYMLINK_NOFOLLOW`** 如果 `path` 命名一个符号链接，则更改该符号链接的模式。

**`AT_RESOLVE_BENEATH`** 仅遍历由 `fd` 描述符指定目录之下的路径。参见 [open(2)](open.2.md) 手册页中对 `O_RESOLVE_BENEATH` 标志的描述。

**`AT_EMPTY_PATH`** 如果 `path` 参数为空字符串，则对描述符 `fd` 所引用的文件或目录进行操作。如果 `fd` 等于 `AT_FDCWD`，则对当前工作目录进行操作。

如果 `fchmodat()` 在 `fd` 参数中传入特殊值 `AT_FDCWD`，则使用当前工作目录。如果同时 `flag` 为零，则其行为与调用 `chmod()` 相同。

mode 由以下定义的权限位掩码按位或运算构成，定义于

`#include <sys/stat.h>`

```c
#define S_IRWXU 0000700    /* 所有者的 RWX 掩码 */
#define S_IRUSR 0000400    /* 所有者的 R */
#define S_IWUSR 0000200    /* 所有者的 W */
#define S_IXUSR 0000100    /* 所有者的 X */
#define S_IRWXG 0000070    /* 组的 RWX 掩码 */
#define S_IRGRP 0000040    /* 组的 R */
#define S_IWGRP 0000020    /* 组的 W */
#define S_IXGRP 0000010    /* 组的 X */
#define S_IRWXO 0000007    /* 其他的 RWX 掩码 */
#define S_IROTH 0000004    /* 其他的 R */
#define S_IWOTH 0000002    /* 其他的 W */
#define S_IXOTH 0000001    /* 其他的 X */
#define S_ISUID 0004000    /* 执行时设置用户 ID */
#define S_ISGID 0002000    /* 执行时设置组 ID */
#define S_ISVTX 0001000    /* 粘滞位 */
```

非标准的 `S_ISTXT` 是 `S_ISVTX` 的同义词。

FreeBSD VM 系统完全忽略可执行文件的粘滞位（`S_ISVTX`）。在基于 UFS 的文件系统（FFS、LFS）上，粘滞位只能在目录上设置。

如果在目录上设置模式 `S_ISVTX`（“粘滞位”），无特权用户不能删除或重命名该目录中其他用户的文件。任何用户都可以在其拥有或具有适当权限的目录上设置粘滞位。有关粘滞位属性的更多详细信息，请参见 [sticky(7)](../man7/sticky.7.md)。

如果在目录上设置模式 `S_ISUID`（set UID），并且在挂载文件系统时使用了 `MNT_SUIDDIR` 选项，则在该目录中创建的任何新文件和子目录的所有者将被设置为与该目录的所有者相同。如果启用了此功能，新目录将继承其父目录的该位。执行位会从文件中移除，且不会授予 root。此行为不改变允许用户写入文件的要求，而仅改变文件创建后的最终所有者。组继承不受影响。

此功能设计用于通过 ftp、SAMBA 或 netatalk 为 PC 用户服务的文件服务器。它为 shell 用户带来了安全漏洞，因此不应在 shell 机器上使用，尤其是在主目录上。此选项需要内核中的 `SUIDDIR` 选项才能工作。只有 UFS 文件系统支持此选项。有关 `suiddir` 挂载选项的更多详细信息，请参见 [mount(8)](../man8/mount.8.md)。

写入文件或更改文件所有者会关闭 set-user-id 和 set-group-id 位，除非用户是超级用户。这通过保护 set-user-id（set-group-id）文件在被修改后不再保持 set-user-id（set-group-id）状态，使系统更加安全，但牺牲了一定程度的兼容性。

虽然在套接字上调用 `fchmod()` 通常是错误的，但对于 `AF_LOCAL` 套接字，在其绑定到文件名之前是可以这样做的；参见 [unix(4)](../man4/unix.4.md)。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

如果以下条件成立，`chmod()` 系统调用将失败，且文件模式保持不变：

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 指定的文件不存在。

**[`EACCES`]** 路径前缀的某个组件的搜索权限被拒绝。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EPERM`]** 有效用户 ID 与文件所有者不匹配，且有效用户 ID 不是超级用户。

**[`EPERM`]** 有效用户 ID 不是超级用户，有效用户 ID 与文件所有者匹配，但文件的组 ID 与有效组 ID 或补充组 ID 均不匹配。

**[`EPERM`]** 指定文件设置了不可变或仅追加标志，更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`EROFS`]** 指定文件位于只读文件系统上。

**[`EFAULT`]** `path` 参数指向进程所分配地址空间之外。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EFTYPE`]** 有效用户 ID 不是超级用户，模式包含粘滞位（`S_ISVTX`），且 path 未引用目录。

`fchmod()` 系统调用在以下情况下会失败：

**[`EBADF`]** 描述符无效。

**[`EINVAL`]** `fd` 参数引用的是套接字，而非文件。

**[`EROFS`]** 文件位于只读文件系统上。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

除 `chmod()` 的错误外，`fchmodat()` 还会在以下情况下失败：

**[`EBADF`]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD` 也不是一个有效的可用于搜索的文件描述符。

**[`EINVAL`]** `flag` 参数的值无效。

**[`ENOTDIR`]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

**[`ENOTCAPABLE`]** `path` 是绝对路径，或包含导致超出 `fd` 所指定目录层级的“..”组件，且进程处于 capability mode 或指定了 `AT_RESOLVE_BENEATH` 标志。

## 参见

[chmod(1)](../man1/chmod.1.md), [chflags(2)](chflags.2.md), [chown(2)](chown.2.md), [open(2)](open.2.md), [stat(2)](stat.2.md), [sticky(7)](../man7/sticky.7.md)

## 标准

`chmod()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")，但返回 `EFTYPE` 除外。目录上的 `S_ISVTX` 位预期符合 -susv3。`fchmodat()` 系统调用预期符合 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`chmod()` 函数出现于 Version 1 AT&T UNIX。`fchmod()` 系统调用出现于 4.2BSD。`lchmod()` 系统调用出现于 FreeBSD 3.0。`fchmodat()` 系统调用出现于 FreeBSD 8.0。
