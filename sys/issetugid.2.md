# issetugid(2)

`issetugid` — 判断当前进程是否因 uid 或 gid 变更而被 tainted

## 名称

`issetugid`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
issetugid(void);
```

## 描述

`issetugid()` 系统调用在进程环境或内存地址空间被视为 "tainted"（被污染）时返回 1，否则返回 0。

如果进程是通过 [execve(2)](execve.2.md) 系统调用创建的，且该调用设置了 setuid 或 setgid 位（并因此获得了额外权限），或者进程在开始执行后修改了其 real、effective 或 saved 的用户 ID 或组 ID 中的任何一个，则该进程被视为 tainted。

提供此系统调用是为了让库例程（例如 libc、libtermcap）能够可靠地判断是否可以安全地使用从用户处获得的信息，特别是当使用 [getenv(3)](../stdlib/getenv.3.md) 的结果来控制操作时，应持怀疑态度对待。

"tainted" 状态会通过 [fork(2)](fork.2.md) 系统调用（或调用 fork 的其他库代码，例如 [popen(3)](../gen/popen.3.md)）被子进程继承。

假定一个程序在准备执行另一个程序时清除所有特权的同时也会重置环境，因此 "tainted" 状态不会被传递下去。这对于 [su(1)](../man1/su.1.md) 等以 setuid 启动但需要能够创建 untainted 进程的程序非常重要。

## 错误

`issetugid()` 系统调用总是成功，没有保留用于指示错误的返回值。

## 参见

[execve(2)](execve.2.md), [fork(2)](fork.2.md), [setegid(2)](setuid.2.md), [seteuid(2)](setuid.2.md), [setgid(2)](setuid.2.md), [setregid(2)](setregid.2.md), [setreuid(2)](setreuid.2.md), [setuid(2)](setuid.2.md)

## 历史

`issetugid()` 系统调用首次出现于 OpenBSD 2.0，并在 FreeBSD 3.0 中实现。
