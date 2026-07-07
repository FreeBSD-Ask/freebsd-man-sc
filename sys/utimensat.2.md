# utimensat(2)

`futimens`, `utimensat` — 设置文件访问和修改时间

## 名称

`futimens`, `utimensat`

## 库

Lb libc

## 概要

```c
#include <sys/stat.h>

int
futimens(int fd, const struct timespec times[2]);

int
utimensat(int fd, const char *path, const struct timespec times[2],
    int flag);
```

## 描述

由 `path` 命名或由 `fd` 引用的文件的访问和修改时间将按参数 `times` 所指定的方式更改。文件的 inode 更改时间设置为当前时间。

如果 `path` 指定的是相对路径，则当 `fd` 为 `AT_FDCWD` 时，它相对于当前工作目录；否则相对于与文件描述符 `fd` 关联的目录。

`timespec` 结构的 `tv_nsec` 字段可以设置为特殊值 `UTIME_NOW` 以设置为当前时间，或设置为 `UTIME_OMIT` 以保持时间不变。在这两种情况下，`tv_sec` 字段都被忽略。

如果 `times` 为非 `NULL`，则假定它指向一个包含两个 timespec 结构的数组。访问时间设置为第一个元素的值，修改时间设置为第二个元素的值。对于支持文件创建（诞生）时间的文件系统（如 `UFS2`），如果第二个元素早于当前设置的诞生时间，诞生时间将设置为第二个元素的值。要同时设置诞生时间和修改时间，需要两次调用：第一次设置诞生时间，第二次设置（可能较新的）修改时间。理想情况下，应添加一个新的系统调用以允许一次设置全部三个时间。如果 `times` 为 `NULL`，则等同于传递一个指向两个 timespec 结构数组的指针，且两个 `tv_nsec` 字段都设置为 `UTIME_NOW`。

如果两个 `tv_nsec` 字段都为 `UTIME_OMIT`，则时间戳保持不变，且文件本身不需要任何权限，尽管路径前缀可能需要搜索权限。如果指定的文件不存在，调用可能成功也可能失败。

如果两个 `tv_nsec` 字段都为 `UTIME_NOW`，调用者必须是文件的所有者、有写文件的权限，或者是超级用户。

对于时间戳的所有其他值，调用者必须是文件的所有者或超级用户。

`utimensat()` 系统调用的 `flag` 参数的值由以下列表中定义的标志按位或构成，定义在：

```c
#include <fcntl.h>
```

**`AT_SYMLINK_NOFOLLOW`** 如果 `path` 命名的是一个符号链接，则更改该符号链接的时间。默认情况下，`utimensat()` 更改符号链接所引用的文件的时间。

**`AT_RESOLVE_BENEATH`** 仅遍历由 `fd` 描述符指定的目录下方的路径。参见 [open(2)](open.2.md) 手册页中对 `O_RESOLVE_BENEATH` 标志的描述。

**`AT_EMPTY_PATH`** 如果 `path` 参数为空字符串，则对由描述符 `fd` 引用的文件或目录进行操作。如果 `fd` 等于 `AT_FDCWD`，则对当前工作目录进行操作。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

这些系统调用将失败，如果：

**[`EACCES`]** `times` 参数为 `NULL`，或两个 `tv_nsec` 值都为 `UTIME_NOW`，且进程的有效用户 ID 与文件所有者不匹配，也不是超级用户，且写访问被拒绝。

**[`EFAULT`]** `times` 参数指向进程分配地址空间之外。

**[`EINVAL`]** `times` 参数指定的至少一个值的 `tv_nsec` 分量值小于 0 或大于 999999999，且不等于 `UTIME_NOW` 或 `UTIME_OMIT`。

**[`EIO`]** 在读取或写入受影响的 inode 时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取数据时检测到损坏的数据。

**[`EPERM`]** `times` 参数不为 `NULL`，两个 `tv_nsec` 值也不都为 `UTIME_NOW`，两个 `tv_nsec` 值也不都为 `UTIME_OMIT`，且调用进程的有效用户 ID 与文件所有者不匹配，也不是超级用户。

**[`EPERM`]** 指定文件设置了不可变或仅追加标志，更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`EROFS`]** 包含该文件的文件系统以只读方式挂载。

`futimens()` 系统调用将失败，如果：

**[`EBADF`]** `fd` 参数未引用有效的描述符。

`utimensat()` 系统调用将失败，如果：

**[`EACCES`]** 路径前缀的某个组件的搜索权限被拒绝。

**[`EBADF`]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD` 也不是有效的文件描述符。

**[`EFAULT`]** `path` 参数指向进程分配地址空间之外。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 `NAME_MAX` 个字符，或整个路径名超过 `PATH_MAX` 个字符。

**[`ENOENT`]** 指定的文件不存在。

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENOTDIR`]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

**[`ENOTCAPABLE`]** `path` 是绝对路径，或包含导致目录逃逸出由 `fd` 指定的目录层级的 ".." 组件，且进程处于 capability 模式或指定了 `AT_RESOLVE_BENEATH` 标志。

## 参见

[chflags(2)](chflags.2.md), [stat(2)](stat.2.md), [symlink(2)](symlink.2.md), [utimes(2)](utimes.2.md), [utime(3)](../gen/utime.3.md), symlink(7)

## 标准

`futimens()` 和 `utimensat()` 系统调用预期符合 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`futimens()` 和 `utimensat()` 系统调用出现于 FreeBSD 10.3。
