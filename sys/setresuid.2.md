# setresuid(2)

`getresgid` — 获取或设置实际、有效和保存的用户或组 ID

## 名称

`getresgid`, `getresuid`, `setresgid`, `setresuid`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <unistd.h>`

```c
int
getresgid(gid_t *rgid, gid_t *egid, gid_t *sgid);

int
getresuid(uid_t *ruid, uid_t *euid, uid_t *suid);

int
setresgid(gid_t rgid, gid_t egid, gid_t sgid);

int
setresuid(uid_t ruid, uid_t euid, uid_t suid);
```

## 描述

`setresuid()` 系统调用设置当前进程的实际、有效和保存用户 ID。类似的 `setresgid()` 设置实际、有效和保存组 ID。

特权进程可以将这些 ID 设置为任意值。非特权进程受限，每个新 ID 必须与当前某个 ID 匹配。

传递 -1 作为参数会使相应值保持不变。

`getresgid()` 和 `getresuid()` 调用分别获取当前进程的实际、有效和保存组 ID 和用户 ID。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

**[`EPERM`]** 调用进程非特权，且尝试将一个或多个 ID 更改为不是当前实际 ID、当前有效 ID 或当前保存 ID 的值。

**[`EFAULT`]** 传递给 `getresgid()` 或 `getresuid()` 的地址无效。

## 参见

[getegid(2)](getegid.2.md), [geteuid(2)](geteuid.2.md), [getgid(2)](getgid.2.md), [getuid(2)](getuid.2.md), [issetugid(2)](issetugid.2.md), [setgid(2)](setgid.2.md), [setregid(2)](setregid.2.md), [setreuid(2)](setreuid.2.md), [setuid(2)](setuid.2.md)

## 历史

这些函数首次出现于 HP-UX。
