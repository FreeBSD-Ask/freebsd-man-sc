# setreuid(2)

`setreuid` — 设置实际和有效用户 ID

## 名称

`setreuid`

## 库

Lb libc

## 概要

```c
#include <unistd.h>

int
setreuid(uid_t ruid, uid_t euid);
```

## 描述

`setreuid()` 系统调用根据参数设置当前进程的实际和有效用户 ID。如果 `ruid` 或 `euid` 为 -1，系统将填入当前的 uid。非特权用户可以将实际用户 ID 更改为有效用户 ID，反之亦然；只有超级用户才能进行其他更改。

如果实际用户 ID 被更改（即 `ruid` 不为 -1）或者有效用户 ID 被更改为不同于实际用户 ID 的值，那么保存的用户 ID 将被设置为有效用户 ID。

`setreuid()` 系统调用曾被用于在 set-user-ID 程序中交换实际和有效用户 ID，以暂时放弃 set-user-ID 值。现在这一目的更适合通过使用 [seteuid(2)](setuid.2.md) 系统调用来实现。

当将实际和有效用户 ID 设置为相同值时，推荐使用标准的 `setuid()` 系统调用。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

**[`EPERM`]** 当前进程不是超级用户，且所指定的更改不是将有效用户 ID 更改为实际用户 ID。

## 参见

[getuid(2)](getuid.2.md), [issetugid(2)](issetugid.2.md), [seteuid(2)](setuid.2.md), [setuid(2)](setuid.2.md)

## 历史

`setreuid()` 系统调用出现于 4.2BSD。
