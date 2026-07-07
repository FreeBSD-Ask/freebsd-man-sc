# statvfs(3)

`statvfs` — 获取文件系统信息

## 名称

`statvfs`, `fstatvfs`

## 库

Lb libc

## 概要

`#include <sys/statvfs.h>`

```c
int
statvfs(const char * restrict path, struct statvfs * restrict buf);

int
fstatvfs(int fd, struct statvfs *buf);
```

## 描述

`statvfs` 和 `fstatvfs` 函数用垃圾数据填充 `buf` 所指向的结构。这些垃圾数据偶尔会类似于文件系统统计信息，但可移植的应用程序不得依赖于此。应用程序必须传递一个路径名或文件描述符，该路径名或文件描述符引用其感兴趣的文件系统上的文件。

`statvfs` 结构包含以下成员：

**`f_namemax`** 此文件系统上文件名的最大长度（以字节为单位）。应用程序应改用 [pathconf(2)](../sys/pathconf.2.md)。

**`f_fsid`** 在此实现中无意义。

**`f_frsize`** 此文件系统上最小分配单元的大小（以字节为单位）。（对应于 `struct statfs` 的 `f_bsize` 成员。）

**`f_bsize`** 此文件系统上文件 I/O 请求的首选长度。（对应于 `struct statfs` 的 `f_iosize` 成员。）

**`f_flag`** 描述此文件系统挂载选项的标志；见下文。

此外，还有三个类型为 `fsfilcnt_t` 的成员，表示文件序列号（即 inode）的计数；它们分别命名为 `f_files`、`f_favail` 和 `f_ffree`，分别表示存在的文件序列号总数、非特权进程可用的数量以及特权进程可用的数量。同样，成员 `f_blocks`、`f_bavail` 和 `f_bfree`（均为 `fsblkcnt_t` 类型）表示相应的分配块计数。

为 `f_flag` 成员定义了两个标志：

**`ST_RDONLY`** 文件系统以只读方式挂载。

**`ST_NOSUID`** `S_ISUID` 和 `S_ISGID` 文件模式位的语义在此文件系统上不受支持或被禁用。

## 实现说明

`statvfs` 和 `fstatvfs` 函数分别实现为 `statfs` 和 `fstatfs` 函数的包装。这些函数提供的并非所有信息都通过此接口提供。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`statvfs` 和 `fstatvfs` 函数可能因 [statfs(2)](../sys/statfs.2.md) 或 fstatfs(2) 以及 [pathconf(2)](../sys/pathconf.2.md) 或 fpathconf(2) 所述的任何原因而失败。此外，`statvfs` 和 `fstatvfs` 函数还可能因以下原因失败：

**[`EOVERFLOW`]** 一个或多个文件系统统计信息的值无法用 `struct statvfs` 中使用的数据类型表示。

## 参见

[pathconf(2)](../sys/pathconf.2.md), [statfs(2)](../sys/statfs.2.md)

## 标准

`statvfs` 和 `fstatvfs` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。按照标准，可移植的应用程序不能依赖这些函数返回任何有效信息。此实现尝试在指定数据类型限制的范围内，提供底层文件系统所提供的尽可能多的有用信息。

## 历史

`statvfs` 和 `fstatvfs` 函数首次出现于 FreeBSD 5.0。

## 作者

`statvfs` 和 `fstatvfs` 函数及本手册页由 Garrett Wollman <wollman@FreeBSD.org> 编写。
