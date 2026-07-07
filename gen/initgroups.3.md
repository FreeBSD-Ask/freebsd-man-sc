# initgroups(3)

`initgroups` — 根据组数据库初始化补充组

## 名称

`initgroups`

## 库

Lb libc

## 概要

```c
#include <unistd.h>

int
initgroups(const char *name, gid_t basegid);
```

## 描述

`initgroups()` 函数根据其参数和系统的组数据库，初始化当前进程的补充组。

它首先使用 `getgrouplist()` 函数计算一个组列表，其中包含传入的 `basegid`（通常是密码数据库中用户的初始数字组 ID）以及组数据库中名为 `name` 的用户的补充组。然后使用 `setgroups()` 将此列表安装为当前进程的补充组。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`initgroups()` 函数可能失败，并将 `errno` 设置为 [setgroups(2)](../sys/setgroups.2.md) 系统调用所指定的任何错误，或设置为：

**`[ENOMEM]`** `initgroups()` 函数无法分配临时存储空间。

## 参见

[setgroups(2)](../sys/setgroups.2.md), [getgrouplist(3)](getgrouplist.3.md)

## 历史

`initgroups()` 函数出现于 4.2BSD。

`initgroups()` 函数在 FreeBSD 15 中改变了语义，与同一版本中 [setgroups(2)](../sys/setgroups.2.md) 的语义保持一致。在此之前，它还会将有效组 ID 设置为 `basegid`，并且在 FreeBSD 8 之前不会将后者包含在补充组中。就这些方面而言，已知其当前行为与截至本文撰写时当前的以下系统的指定版本兼容：

- Linux（最高至 6.6），使用 GNU libc（最高至 2.42）
- NetBSD 1.1 及更高版本（最高至 10）
- OpenBSD（最高至 7.7）
- 基于 illumos 的系统（最高至 2025 年 8 月的源码）

## 安全考虑

由于 `basegid` 通常是用户的初始数字组 ID，而当前进程的有效组 ID 一般会初始化为该值，因此使用函数更改其有效组 ID（通过 setgid(2) 或类似方式）或从设置了 set-group-ID 模式位的可执行文件派生的进程，将无法放弃因属于 `basegid` 而获得的访问权限，因为这些函数不会更改补充组。

这种行为通常是可取的，以便掩盖在这种情况下对有效组和补充组处理方式的差异，因为它们最终都在传统的 UNIX 自主访问检查中被不加区分地使用。它与为每个用户分配其私有组的做法很好地契合，因为从 set-group-ID 可执行文件启动的进程保留相同的用户，并且一致地也保留在同一用户的组中。最后，选择该行为也是为了与其他系统兼容（参见“历史”章节）。

然而，将 `basegid` 包含在补充组中的这一约定仅由 `initgroups()` 函数强制执行，而 [setgroups(2)](../sys/setgroups.2.md) 系统调用并不强制执行，因此明确希望补充组中仅包含组数据库所指定的组的应用程序，可以自行调用 `getgrouplist()`，然后对结果跳过第一个元素再调用 `setgroups()`（参见 [getgrouplist(3)](getgrouplist.3.md)）。
