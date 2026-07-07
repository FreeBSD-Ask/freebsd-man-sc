# chflags(2)

`chflags`, `lchflags`, `fchflags`, `chflagsat` — 设置文件标志

## 名称

`chflags`, `lchflags`, `fchflags`, `chflagsat`

## 库

Lb libc

## 概要

```c
#include <sys/stat.h>
#include <unistd.h>

int
chflags(const char *path, unsigned long flags);

int
lchflags(const char *path, unsigned long flags);

int
fchflags(int fd, unsigned long flags);

int
chflagsat(int fd, const char *path, unsigned long flags, int atflag);
```

## 描述

由 `path` 命名或由描述符 `fd` 引用的文件的标志被更改为 `flags`。

`lchflags()` 系统调用类似于 `chflags()`，区别在于当指定文件是符号链接时，`lchflags()` 将更改链接本身的标志，而非其指向的文件的标志。

`chflagsat()` 等价于 `chflags()` 或 `lchflags()`（取决于 `atflag`），区别在于 `path` 指定相对路径的情况。此时，要更改的文件相对于与文件描述符 `fd` 关联的目录确定，而非当前工作目录。`atflag` 的值由以下列表中定义的标志按位或构成，定义在：

```c
#include <fcntl.h>
```

**`AT_SYMLINK_NOFOLLOW`** 如果 `path` 命名的是一个符号链接，则更改该符号链接的标志。

**`AT_RESOLVE_BENEATH`** 仅遍历由 `fd` 描述符指定的目录下方的路径。参见 [open(2)](open.2.md) 手册页中对 `O_RESOLVE_BENEATH` 标志的描述。

**`AT_EMPTY_PATH`** 如果 `path` 参数为空字符串，则对由描述符 `fd` 引用的文件或目录进行操作。如果 `fd` 等于 `AT_FDCWD`，则对当前工作目录进行操作。

如果 `chflagsat()` 的 `fd` 参数传入特殊值 `AT_FDCWD`，则使用当前工作目录。如果 `atflag` 也为零，则行为与调用 `chflags()` 完全相同。

指定的标志由以下值按位或构成：

**`SF_APPEND`** 文件只能被追加。

**`SF_ARCHIVED`** 文件已被归档。此标志的含义与 DOS、Windows 和 CIFS 的 FILE_ATTRIBUTE_ARCHIVE 属性相反。此标志已被弃用，可能会在未来版本中移除。

**`SF_IMMUTABLE`** 文件不可被更改。

**`SF_NOUNLINK`** 文件不可被重命名或删除。

**`SF_SNAPSHOT`** 文件是快照文件。

**`UF_APPEND`** 文件只能被追加。

**`UF_ARCHIVE`** 文件需要归档。此标志与 DOS、Windows 和 CIFS 的 FILE_ATTRIBUTE_ARCHIVE 属性含义相同。FreeBSD 中的文件系统可能对此标志有特殊处理，也可能没有。例如，ZFS 会跟踪文件的更改，并在文件更新时设置此位。UFS 仅存储该标志，依赖应用程序在需要时更改它。

**`UF_HIDDEN`** 文件可以根据应用程序的判断从目录列表中隐藏。该文件具有 DOS、Windows 和 CIFS 的 FILE_ATTRIBUTE_HIDDEN 属性。

**`UF_IMMUTABLE`** 文件不可被更改。

**`UF_NODUMP`** 不转储该文件。

**`UF_NOUNLINK`** 文件不可被重命名或删除。

**`UF_OFFLINE`** 文件处于离线状态，或具有 Windows 和 CIFS 的 FILE_ATTRIBUTE_OFFLINE 属性。FreeBSD 中的文件系统会存储和显示此标志，但在设置时不提供任何特殊处理。

**`UF_OPAQUE`** 通过 union 层级查看时，该目录是不透明的。

**`UF_READONLY`** 文件是只读的，不可被写入或追加。文件系统可以使用此标志来保持与 DOS、Windows 和 CIFS 的 FILE_ATTRIBUTE_READONLY 属性的兼容性。

**`UF_REPARSE`** 文件包含 Windows 重解析点，具有 Windows 和 CIFS 的 FILE_ATTRIBUTE_REPARSE_POINT 属性。

**`UF_SPARSE`** 文件具有 Windows 的 FILE_ATTRIBUTE_SPARSE_FILE 属性。文件系统也可以使用它来指示稀疏文件。

**`UF_SYSTEM`** 文件具有 DOS、Windows 和 CIFS 的 FILE_ATTRIBUTE_SYSTEM 属性。FreeBSD 中的文件系统可能存储和显示此标志，但在设置时不提供任何特殊处理。

如果设置了 `SF_IMMUTABLE`、`SF_APPEND` 或 `SF_NOUNLINK` 之一，非超级用户无法更改任何标志，即使是超级用户也只有在 securelevel 为 0 时才能更改标志。（详情参见 [init(8)](../man8/init.8.md)。）

`UF_IMMUTABLE`、`UF_APPEND`、`UF_NOUNLINK`、`UF_NODUMP` 和 `UF_OPAQUE` 标志可以由文件所有者或超级用户设置或取消设置。

`SF_IMMUTABLE`、`SF_APPEND`、`SF_NOUNLINK` 和 `SF_ARCHIVED` 标志只能由超级用户设置或取消设置。非超级用户试图切换这些标志将被拒绝。这些标志可以在任何时候设置，但通常只有在系统处于单用户模式时才能取消设置。（详情参见 [init(8)](../man8/init.8.md)。）

所有标志的实现都依赖于文件系统。关于行为差异的一个示例，参见上文对 `UF_ARCHIVE` 标志的描述。在编写应用程序时，应注意考虑各种文件系统对这些标志的支持或不支持情况。

`SF_SNAPSHOT` 标志由系统维护，无法被切换。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`chflags()` 系统调用将失败，如果：

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 指定的文件不存在。

**[`EACCES`]** 路径前缀的某个组件的搜索权限被拒绝。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EPERM`]** 有效用户 ID 与文件所有者不匹配，且有效用户 ID 不是超级用户。

**[`EPERM`]** 设置了 `SF_IMMUTABLE`、`SF_APPEND` 或 `SF_NOUNLINK` 之一，且用户不是超级用户或 securelevel 大于 0。

**[`EPERM`]** 非超级用户试图切换 `SF_ARCHIVED`、`SF_IMMUTABLE`、`SF_APPEND` 或 `SF_NOUNLINK` 之一。

**[`EPERM`]** 试图切换 `SF_SNAPSHOT` 标志。

**[`EROFS`]** 指定文件位于只读文件系统上。

**[`EFAULT`]** `path` 参数指向进程分配地址空间之外。

**[`EIO`]** 在读取或写入文件系统时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取数据时检测到损坏的数据。

**[`EOPNOTSUPP`]** 底层文件系统不支持文件标志，或不支持 `flags` 中设置的所有标志。

`fchflags()` 系统调用将失败，如果：

**[`EBADF`]** 描述符无效。

**[`EINVAL`]** `fd` 参数引用的是套接字，而非文件。

**[`EPERM`]** 有效用户 ID 与文件所有者不匹配，且有效用户 ID 不是超级用户。

**[`EPERM`]** 设置了 `SF_IMMUTABLE`、`SF_APPEND` 或 `SF_NOUNLINK` 之一，且用户不是超级用户或 securelevel 大于 0。

**[`EPERM`]** 非超级用户试图切换 `SF_ARCHIVED`、`SF_IMMUTABLE`、`SF_APPEND` 或 `SF_NOUNLINK` 之一。

**[`EPERM`]** 试图切换 `SF_SNAPSHOT` 标志。

**[`EROFS`]** 文件位于只读文件系统上。

**[`EIO`]** 在读取或写入文件系统时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取数据时检测到损坏的数据。

**[`EOPNOTSUPP`]** 底层文件系统不支持文件标志，或不支持 `flags` 中设置的所有标志。

**[`ENOTCAPABLE`]** `path` 是绝对路径，或包含导致目录逃逸出由 `fd` 指定的目录层级的 ".." 组件，且进程处于 capability 模式或指定了 `AT_RESOLVE_BENEATH` 标志。

## 参见

chflags(1), fflagstostr(3), [strtofflags(3)](../gen/strtofflags.3.md), [init(8)](../man8/init.8.md), mount_unionfs(8)

## 历史

`chflags()` 和 `fchflags()` 系统调用首次出现于 4.4BSD。`lchflags()` 系统调用首次出现于 FreeBSD 5.0。`chflagsat()` 系统调用首次出现于 FreeBSD 10.0。
