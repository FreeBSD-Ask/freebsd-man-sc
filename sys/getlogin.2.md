# getlogin(2)

`getlogin` — 获取/设置登录名

## 名称

`getlogin`, `getlogin_r`, `setlogin`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
char *
getlogin(void);
```

`#include <sys/param.h>`

```c
int
getlogin_r(char *name, size_t len);

int
setlogin(const char *name);
```

## 描述

`getlogin()` 例程返回与当前会话关联的用户的登录名，该名称此前由 `setlogin()` 设置。该名称通常在创建会话时与登录 shell 关联，并由从该登录 shell 派生的所有进程继承。（即使其中某些进程假定另一个用户 ID，例如使用 [su(1)](../man1/su.1.md) 时，也是如此。）

`getlogin_r()` 函数提供与 `getlogin()` 相同的服务，但调用者必须提供长度为 `len` 字节的缓冲区 `name` 来存放结果。该缓冲区的长度应至少为 `MAXLOGNAME` 字节。

`setlogin()` 系统调用将与当前会话关联的用户登录名设置为 `name`。此系统调用仅限超级用户使用，通常仅在代表命名用户创建新会话时使用（例如，在登录时，或调用远程 shell 时）。

*注意：* 每个会话只有一个登录名。

确保 `setlogin()` 仅在进程采取了充分步骤以确保已与其父进程的会话分离之后才被调用，这一点*至关重要*。调用 `setsid()` 系统调用是做到这一点的*唯一*方法。[daemon(3)](../man3/daemon.3.md) 函数会调用 `setsid()`，这是脱离控制终端并转入后台运行的理想方式。

特别地，执行 `ioctl(ttyfd, TIOCNOTTY, ...)` 或 `setpgrp(...)` 是*不够的*。

一旦父进程调用了 `setsid()` 系统调用，该进程的某个子进程即使不是会话领导者，也可以随后调用 `setlogin()`，但要注意会话中的所有进程将同时更改其登录名，包括父进程。

这与传统的 UNIX 继承特权的行为不同。

由于 `setlogin()` 系统调用仅限超级用户，因此假定（与所有其他特权程序一样）程序员已采取充分的预防措施以防止安全违规。

## 返回值

如果对 `getlogin()` 的调用成功，它返回一个指向静态缓冲区中以 null 终止的字符串的指针；如果名称尚未设置，则返回 `NULL`。`getlogin_r()` 函数在成功时返回零，失败时返回错误号。

`setlogin()` 系统调用在成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

这些调用可能返回以下错误：

**[`EFAULT`]** `name` 参数给出了无效地址。

**[`EINVAL`]** `name` 参数指向的字符串过长。登录名称限制为 `MAXLOGNAME`（来自 `<sys/param.h>`）个字符，目前包括 null 终止符在内为 33 个。

**[`EPERM`]** 调用者试图设置登录名，但不是超级用户。

**[`ERANGE`]** 缓冲区大小小于要返回的结果。

## 参见

[setsid(2)](setsid.2.md), [daemon(3)](../man3/daemon.3.md)

## 标准

`getlogin()` 系统调用和 `getlogin_r()` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1")。

## 历史

`getlogin()` 系统调用首次出现于 4.4BSD。`getlogin_r()` 的返回值从早期版本的 FreeBSD 更改为符合 ISO/IEC 9945-1:1996 ("POSIX.1")。

## 缺陷

在系统的早期版本中，除非进程与登录终端关联，否则 `getlogin()` 会失败。当前实现（使用 `setlogin()`）允许 `getlogin()` 在进程没有控制终端时也能成功。在系统的早期版本中，如果不检查用户 ID，`getlogin()` 返回的值不可信。可移植程序可能仍应进行此检查。
