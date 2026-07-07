# getfh(2)

`getfh` — 获取文件句柄

## 名称

`getfh`, `lgetfh`, `getfhat`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

```c
int
getfh(const char *path, fhandle_t *fhp);

int
lgetfh(const char *path, fhandle_t *fhp);

int
getfhat(int fd, const char *path, fhandle_t *fhp, int flag);
```

## 描述

`getfh()` 系统调用在 `fhp` 所指向的文件句柄中返回指定文件或目录的文件句柄。

`lgetfh()` 系统调用类似于 `getfh()`，但当指定文件是符号链接时，`lgetfh()` 返回关于该链接的信息，而 `getfh()` 返回该链接所引用文件的信息。

`getfhat()` 系统调用等效于 `getfh()` 和 `lgetfh()`，但当 `path` 指定相对路径时除外。对于 `getfhat()` 和相对 `path`，状态从相对于与文件描述符 `fd` 关联的目录的文件中获取，而不是相对于当前工作目录。

`flag` 的值由以下列表中定义的标志按位或运算构成，定义于

`#include <fcntl.h>`

**`AT_SYMLINK_NOFOLLOW`** 如果 `path` 命名一个符号链接，则返回该符号链接的状态。

**`AT_RESOLVE_BENEATH`** 仅遍历由 `fd` 描述符指定目录之下的路径。参见 [open(2)](open.2.md) 手册页中对 `O_RESOLVE_BENEATH` 标志的描述。

如果 `getfhat()` 在 `fd` 参数中传入特殊值 `AT_FDCWD`，则使用当前工作目录，其行为分别与调用 `getfh()` 或 `lgetfh()` 相同，具体取决于 `flag` 参数中是否设置了 `AT_SYMLINK_NOFOLLOW` 位。

当 `getfhat()` 以绝对 `path` 调用时，它忽略 `fd` 参数。

这些系统调用仅限超级用户使用。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getfh()` 和 `lgetfh()` 系统调用在以下一个或多个条件成立时失败：

**[`EPERM`]** 调用者没有执行该操作的适当特权。

**[`ENOTDIR`]** `path` 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** `path` 某个组件的长度超过 255 个字符，或 `path` 的长度超过 1023 个字符。

**[`ENOENT`]** `path` 所引用的文件不存在。

**[`EACCES`]** `path` 路径前缀的某个组件的搜索权限被拒绝。

**[`ELOOP`]** 在转换 `path` 时遇到过多的符号链接。

**[`EFAULT`]** `fhp` 参数指向无效地址。

**[`EFAULT`]** `path` 参数指向无效地址。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`ESTALE`]** 文件句柄 `fhp` 不再有效。

除 `getfh()` 和 `lgetfh()` 返回的错误外，`getfhat()` 系统调用还可能在以下情况下失败：

**[`EBADF`]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD` 也不是一个有效的可用于搜索的文件描述符。

**[`EINVAL`]** `flag` 参数的值无效。

**[`ENOTDIR`]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

## 参见

[fhopen(2)](fhopen.2.md), [open(2)](open.2.md), [stat(2)](stat.2.md)

## 历史

`getfh()` 系统调用首次出现于 4.4BSD。`lgetfh()` 系统调用首次出现于 FreeBSD 5.3。`getfhat()` 系统调用首次出现于 FreeBSD 12.1。