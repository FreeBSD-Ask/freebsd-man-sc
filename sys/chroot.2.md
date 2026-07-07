# chroot(2)

`chroot` — 更改根目录

## 名称

`chroot`, `fchroot`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
chroot(const char *dirname);

int
fchroot(int fd);
```

## 描述

`dirname` 参数是某个目录路径名的地址，以 ASCII NUL 结尾。`chroot()` 系统调用使 `dirname` 成为根目录，即以 **`/`** 开头的路径名进行路径查找时的起始点。

要将某个目录成为根目录，进程必须对该目录具有执行（搜索）权限。

需要注意的是，`chroot()` 对进程的当前目录没有影响。

此调用仅限超级用户使用，除非 `security.bsd.unprivileged_chroot` sysctl 变量设置为 1，且进程已启用 `PROC_NO_NEW_PRIVS_CTL` [procctl(2)](procctl.2.md)。

根据 `kern.chroot_allow_open_directories` sysctl 变量的设置，引用目录的已打开文件描述符会使 `chroot()` 按如下方式失败：

如果 `kern.chroot_allow_open_directories` 设置为零，则只要存在任何已打开的目录，`chroot()` 就会以 `EPERM` 失败。

如果 `kern.chroot_allow_open_directories` 设置为一（默认值），则当存在任何已打开的目录且进程已受到 `chroot()` 系统调用约束时，`chroot()` 会以 `EPERM` 失败。

`kern.chroot_allow_open_directories` 的任何其他值将跳过对已打开目录的检查，模拟其他系统上仍然存在的 `chroot()` 历史不安全行为。

`fchroot()` 系统调用与 `chroot()` 相同，区别在于它接受文件描述符而非路径。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

如果以下条件成立，`chroot()` 和 `fchroot()` 系统调用将失败，且根目录保持不变：

**[`EPERM`]** 有效用户 ID 不是超级用户，且 `security.bsd.unprivileged_chroot` sysctl 为 0。

**[`EPERM`]** 有效用户 ID 不是超级用户，且进程未启用 `PROC_NO_NEW_PRIVS_CTL` [procctl(2)](procctl.2.md)。

**[`EPERM`]** 一个或多个文件描述符是已打开的目录，且 `kern.chroot_allow_open_directories` sysctl 未设置为允许此情况。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

如果以下条件成立，`chroot()` 系统调用将失败，且根目录保持不变：

**[`ENOTDIR`]** 路径名的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 指定的目录不存在。

**[`EACCES`]** 路径名中任何组件的搜索权限被拒绝。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EFAULT`]** `dirname` 参数指向进程所分配地址空间之外。

如果以下条件成立，`fchroot()` 系统调用将失败，且根目录保持不变：

**[`EACCES`]** 文件描述符所引用目录的搜索权限被拒绝。

**[`EBADF`]** `fd` 参数不是有效的文件描述符。

**[`ENOTDIR`]** 文件描述符未引用目录。

## 参见

[chdir(2)](chdir.2.md), [jail(2)](jail.2.md)

## 历史

`chroot()` 系统调用出现于 Version 7 AT&T UNIX。它在 -susv2 中被标记为“legacy”，并在后续标准中被移除。`fchroot()` 系统调用首次出现于 FreeBSD 15.0。

## 缺陷

如果进程能够将其工作目录更改为目标目录，但另一个访问控制检查失败（例如对已打开目录的检查，或 MAC 检查），则此系统调用可能返回错误，而进程的工作目录已更改。

## 安全注意事项

系统中存在许多硬编码的文件路径，系统可能会在进程启动后加载这些文件。通常建议在成功的 `fchroot()` 调用之后立即放弃特权，并将写访问限制在 `fchroot()` 根目录的一个有限子树内。例如，设置沙盒使被沙盒化的用户对任何已知系统目录都没有写权限。

要与系统的其余部分完全隔离，请改用 [jail(2)](jail.2.md)。
