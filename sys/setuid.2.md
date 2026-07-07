# setuid(2)

`setuid` — 设置用户和组 ID

## 名称

`setuid`, `seteuid`, `setgid`, `setegid`

## 库

Lb libc

## 概要

```c
#include <unistd.h>

int
setuid(uid_t uid);

int
seteuid(uid_t euid);

int
setgid(gid_t gid);

int
setegid(gid_t egid);
```

## 描述

`setuid()` 系统调用将当前进程的实际和有效用户 ID 以及保存的 set-user-ID 设置为指定值。如果指定的 ID 等于进程的实际用户 ID 或有效用户 ID，或者有效用户 ID 为超级用户，则允许调用 `setuid()` 系统调用。

`setgid()` 系统调用将当前进程的实际和有效组 ID 以及保存的 set-group-ID 设置为指定值。如果指定的 ID 等于进程的实际组 ID 或有效组 ID，或者有效用户 ID 为超级用户，则允许调用 `setgid()` 系统调用。

`seteuid()` 系统调用（`setegid()`）设置当前进程的有效用户 ID（组 ID）。有效用户 ID 可以设置为实际用户 ID 或保存的 set-user-ID 的值（参见 [intro(2)](intro.2.md) 和 [execve(2)](execve.2.md)）；通过这种方式，set-user-ID 可执行文件的有效用户 ID 可以通过切换到实际用户 ID 来切换，然后再通过恢复 set-user-ID 值来重新启用。类似地，有效组 ID 可以设置为实际组 ID 或保存的 set-group-ID 的值。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

系统调用将在以下情况下失败：

**[`EPERM`]** 用户不是超级用户，且指定的 ID 不是实际、有效 ID 或保存 ID。

## 参见

[getgid(2)](getgid.2.md), [getuid(2)](getuid.2.md), [issetugid(2)](issetugid.2.md), [setregid(2)](setregid.2.md), [setreuid(2)](setreuid.2.md)

## 标准

`setuid()` 和 `setgid()` 系统调用符合 IEEE Std 1003.1-1990 ("POSIX.1") 规范，其中 `_POSIX_SAVED_IDS` 未定义，并采用了附录 B.4.2.2 中允许的扩展。`seteuid()` 和 `setegid()` 系统调用是基于 POSIX 的 `_POSIX_SAVED_IDS` 概念的扩展，已被提议作为该标准的未来修订内容。

## 历史

`setuid()` 函数出现于 Version 1 AT&T UNIX。`setgid()` 函数出现于 Version 4 AT&T UNIX。

## 安全注意事项

对文件的读写权限在调用 [open(2)](open.2.md) 时确定。一旦文件描述符打开，放弃权限不会影响进程的读写权限，即使指定的用户 ID 对该文件没有读写权限。这些文件通常在任何新执行的进程中保持打开状态，导致用户能够读取或修改潜在的敏感数据。

为防止这些文件在 [exec(3)](../gen/exec.3.md) 调用后保持打开状态，务必设置 close-on-exec 标志：

```c
void
pseudocode(void)
{
	int fd;
	/* ... */

	fd = open("/path/to/sensitive/data", O_RDWR | O_CLOEXEC);
	if (fd == -1)
		err(1, "open");

	/* ... */
	execve(path, argv, environ);
}
```
