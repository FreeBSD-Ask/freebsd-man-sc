# setregid(2)

`setregid` — 设置实际和有效组 ID

## 名称

`setregid`

## 库

Lb libc

## 概要

```c
#include <unistd.h>

int
setregid(gid_t rgid, gid_t egid);
```

## 描述

当前进程的实际和有效组 ID 被设置为参数指定的值。如果实际组 ID 被更改，保存的组 ID 将被更改为新的有效组 ID 值。

非特权用户可以将实际组 ID 更改为有效组 ID，反之亦然；只有超级用户才能进行其他更改。

为实际或有效组 ID 提供值 -1 会强制系统用当前 ID 替换该 -1 参数。

`setregid()` 系统调用旨在允许 set-group-ID 程序交换实际和有效组 ID，以临时放弃 set-group-ID 值。此系统调用无法正确工作，其目的现在由 setegid(2) 系统调用更好地实现。

当将实际和有效组 ID 设置为相同值时，推荐使用标准的 setgid(2) 系统调用。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

**[`EPERM`]** 当前进程不是超级用户，且指定的更改不是将有效组 ID 更改为实际组 ID。

## 参见

[getgid(2)](getgid.2.md), [issetugid(2)](issetugid.2.md), setegid(2), setgid(2), [setuid(2)](setuid.2.md)

## 历史

`setregid()` 系统调用出现于 4.2BSD。
