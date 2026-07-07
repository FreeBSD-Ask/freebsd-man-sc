# utimes(2)

`utimes`, `lutimes`, `futimes`, `futimesat` — 设置文件访问和修改时间

## 名称

`utimes`, `lutimes`, `futimes`, `futimesat`

## 库

Lb libc

## 概要

```c
#include <sys/time.h>

int
utimes(const char *path, const struct timeval *times);

int
lutimes(const char *path, const struct timeval *times);

int
futimes(int fd, const struct timeval *times);

int
futimesat(int fd, const char *path, const struct timeval times[2]);
```

## 描述

*这些接口已被 futimens(2) 和 [utimensat(2)](utimensat.2.md) 取代，因为它们无法精确到纳秒。*

由 `path` 命名或由 `fd` 引用的文件的访问和修改时间将按参数 `times` 所指定的方式更改。

如果 `times` 为 `NULL`，访问和修改时间设置为当前时间。调用者必须是文件的所有者、有写文件的权限，或者是超级用户。

如果 `times` 为非 `NULL`，则假定它指向一个包含两个 timeval 结构的数组。访问时间设置为第一个元素的值，修改时间设置为第二个元素的值。对于支持文件创建（诞生）时间的文件系统（如 `UFS2`），如果第二个元素早于当前设置的诞生时间，诞生时间将设置为第二个元素的值。要同时设置诞生时间和修改时间，需要两次调用：第一次设置诞生时间，第二次设置（可能较新的）修改时间。理想情况下，应添加一个新的系统调用以允许一次设置全部三个时间。调用者必须是文件的所有者或超级用户。

无论哪种情况，文件的 inode 更改时间都设置为当前时间。

`lutimes()` 系统调用类似于 `utimes()`，区别在于当指定文件是符号链接时，`lutimes()` 更改该链接的访问和修改时间，而 `utimes()` 更改链接所引用的文件的时间。

`futimesat()` 系统调用等价于 `utimes()`，区别在于 `path` 指定相对路径的情况。此时，访问和修改时间设置为相对于与文件描述符 `fd` 关联的目录的文件，而非当前工作目录。如果 `futimesat()` 的 `fd` 参数传入特殊值 `AT_FDCWD`，则使用当前工作目录，行为与调用 `utimes()` 完全相同。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

所有系统调用将失败，如果：

**[`EACCES`]** 路径前缀的某个组件的搜索权限被拒绝。

**[`EACCES`]** `times` 参数为 `NULL`，且进程的有效用户 ID 与文件所有者不匹配，也不是超级用户，且写访问被拒绝。

**[`EFAULT`]** `path` 或 `times` 参数指向进程分配地址空间之外。

**[`EFAULT`]** `times` 参数指向进程分配地址空间之外。

**[`EINVAL`]** `times` 参数指定的至少一个值的 `tv_usec` 分量值小于 0 或大于 999999。

**[`EIO`]** 在读取或写入受影响的 inode 时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取数据时检测到损坏的数据。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 `NAME_MAX` 个字符，或整个路径名超过 `PATH_MAX` 个字符。

**[`ENOENT`]** 指定的文件不存在。

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`EPERM`]** `times` 参数不为 `NULL`，且调用进程的有效用户 ID 与文件所有者不匹配，也不是超级用户。

**[`EPERM`]** 指定文件设置了不可变或仅追加标志。更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`EROFS`]** 包含该文件的文件系统以只读方式挂载。

`futimes()` 系统调用将失败，如果：

**[`EBADF`]** `fd` 参数未引用有效的描述符。

除 `utimes()` 返回的错误外，`futimesat()` 可能失败，如果：

**[`EBADF`]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD` 也不是有效的可搜索文件描述符。

**[`ENOTDIR`]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

## 参见

[chflags(2)](chflags.2.md), [stat(2)](stat.2.md), [utimensat(2)](utimensat.2.md), [utime(3)](../gen/utime.3.md)

## 标准

`utimes()` 函数预期符合 -xpg4.2。`futimesat()` 系统调用遵循 The Open Group Extended API Set 2 规范，但在 IEEE Std 1003.1-2008 ("POSIX.1") 中被 `utimensat()` 取代。

## 历史

`utimes()` 系统调用出现于 4.2BSD。`futimes()` 和 `lutimes()` 系统调用首次出现于 FreeBSD 3.0。`futimesat()` 系统调用出现于 FreeBSD 8.0。
