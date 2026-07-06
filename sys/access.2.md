# access(2)

`access` — 检查文件的可访问性

## 名称

`access`, `eaccess`, `faccessat`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
access(const char *path, int mode);

int
eaccess(const char *path, int mode);

int
faccessat(int fd, const char *path, int mode, int flag);
```

## 描述

`access()`、`eaccess()` 和 `faccessat()` 系统调用报告以 `mode` 参数所描述的方式访问 `path` 指定文件是否可能成功。`mode` 的值可以是所需权限的按位或（`R_OK` 表示读权限，`W_OK` 表示写权限，`X_OK` 表示执行/搜索权限），也可以是 `F_OK`（仅检查文件是否存在）。

由于多种原因，这些系统调用无法给出正确且确定的答案。它们至多能提供对预期结果的早期指示，需要通过实际尝试操作来确认。对于存在性检查，应改用 [stat(2)](stat.2.md) 或 lstat(2)。另请参见下文的 Sx 安全注意事项。

`eaccess()` 系统调用使用有效用户 ID 和组访问列表来授权请求；`access()` 系统调用使用实际用户 ID 代替有效用户 ID、实际组 ID 代替有效组 ID 以及组访问列表的其余部分。

有关文件访问权限以及实际用户与组 ID 和有效用户与组 ID 的更多信息，请参见 [intro(2)](intro.2.md) 的 DEFINITIONS 章节。

`faccessat()` 系统调用与 `access()` 等价，除非 `path` 指定了相对路径。此时，要确定可访问性的文件是相对于文件描述符 `fd` 关联的目录来定位的，而非相对于当前工作目录。如果 `faccessat()` 的 `fd` 参数传入特殊值 `AT_FDCWD`，则使用当前工作目录，行为与调用 `access()` 完全相同。`flag` 的值由以下列表中定义的标志按位或构成：

`#include <fcntl.h>`

**`AT_EACCESS`** 使用有效用户和组 ID 执行检查（类似 `eaccess()`），而非使用实际用户和组 ID（类似 `access()`）。

**`AT_RESOLVE_BENEATH`** 仅遍历 `fd` 描述符所指定目录之下的路径。参见 [open(2)](open.2.md) 手册页中对 `O_RESOLVE_BENEATH` 标志的描述。

**`AT_EMPTY_PATH`** 如果 `path` 参数为空字符串，则对描述符 `fd` 所引用的文件或目录进行操作。如果 `fd` 等于 `AT_FDCWD`，则对当前工作目录进行操作。

**`AT_SYMLINK_NOFOLLOW`** 如果 `path` 命名了一个符号链接，则评估该符号链接本身的访问权限。

即使进程的实际或有效用户具有适当权限且对 `X_OK` 指示成功，该文件也可能实际上未设置执行权限位。`R_OK` 和 `W_OK` 同理。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

`access()`、`eaccess()` 和 `faccessat()` 系统调用在以下情况下可能失败：

**[EINVAL]** `mode` 参数的值无效。

**[ENOTDIR]** 路径前缀中的某个组件不是目录。

**[ENAMETOOLONG]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[ENOENT]** 指定的文件不存在。

**[ELOOP]** 在转换路径名时遇到过多的符号链接。

**[EROFS]** 对只读文件系统上的文件请求写访问权限。

**[ETXTBSY]** 对正在执行的纯过程（共享文本）文件请求写访问权限。

**[EACCES]** 文件模式的权限位不允许所请求的访问，或路径前缀的某个组件拒绝搜索权限。

**[EFAULT]** `path` 参数指向进程分配地址空间之外。

**[EIO]** 在对文件系统进行读写操作时发生 I/O 错误。

**[EINTEGRITY]** 在从文件系统读取数据时检测到损坏的数据。

此外，`faccessat()` 系统调用在以下情况下也可能失败：

**[EBADF]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD` 也不是有效的文件描述符。

**[EINVAL]** `flag` 参数的值无效。

**[ENOTDIR]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

**[ENOTCAPABLE]** `path` 是绝对路径，或包含导致超出 `fd` 所指定目录层级的“..”组件，且进程处于 capability 模式。

## 参见

[chmod(2)](chmod.2.md), [intro(2)](intro.2.md), [stat(2)](stat.2.md)

## 标准

`access()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。`faccessat()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`access()` 函数首次出现于 Version 7 AT&T UNIX。`faccessat()` 系统调用首次出现于 FreeBSD 8.0。

## 安全注意事项

`access()`、`eaccess()` 和 `faccessat()` 系统调用存在检查时间到使用时间（time-of-check-to-time-of-use）的竞态条件，不应依赖其进行文件权限强制检查。应用应改为使用请求用户的凭证来执行所需操作。
