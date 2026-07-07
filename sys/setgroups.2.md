# setgroups(2)

`setgroups` — 设置调用进程的补充组

## 名称

`setgroups`

## 库

Lb libc

## 概要

```c
#include <sys/param.h>
#include <unistd.h>

int
setgroups(int ngroups, const gid_t *gidset);
```

## 描述

`setgroups()` 系统调用根据 `gidset` 数组设置调用进程的补充组。`ngroups` 参数指示数组中的条目数，且不得超过 `{NGROUPS_MAX}`。

`ngroups` 参数可以设置为零以清除所有补充组，在这种情况下 `gidset` 将被忽略。

只有超级用户可以安装新的补充组集合。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`setgroups()` 系统调用将在以下情况下失败：

**[`EPERM`]** 调用者不是超级用户。

**[`EINVAL`]** `ngroups` 参数中指定的数量大于 `{NGROUPS_MAX}` 限制。

**[`EFAULT`]** 从 `gidset` 开始的组数组部分位于进程地址空间之外。

## 参见

[getgroups(2)](getgroups.2.md), [setcred(2)](setcred.2.md), [initgroups(3)](../gen/initgroups.3.md)

## 历史

`setgroups()` 系统调用出现于 4.2BSD。

在 FreeBSD 15.0 之前，`setgroups()` 系统调用会将进程的有效组 ID 设置为 `gidset` 的第一个元素，而仅将其他元素作为补充组。尽管将第一个元素作为要设置的有效组 ID 来处理，它仍接受空的 `gidset`（`ngroups` 为零）作为要求丢弃所有补充组的情形，此时保持有效组 ID 不变。

## 安全注意事项

`setgroups()` 系统调用将进程的补充组设置为 `gidset` 数组中包含的那些组。特别地，如[历史](#历史)中所述，它不再单独处理 `gidset` 的第一个元素。以前，它会将其设置为有效组 ID，而仅将其他元素用作补充组。

仅依赖 `setgroups()` 来更改有效组 ID 的程序必须进行修改，例如同时调用 [setegid(2)](setregid.2.md) 或改用 [setcred(2)](setcred.2.md)，否则它们会在无意中保留原有的有效组 ID。

使用 `setgroups()` 时将有效组 ID 作为数组 `gidset` 的第一个元素且未在数组其余部分重复该 ID 的程序（包括那些使用 `initgroups()` 的程序），现在会将此组 ID 插入补充组集合中。这通常是期望的行为，正如 [initgroups(3)](../gen/initgroups.3.md) 手册页中所解释的，其结果是后续进程有效组 ID 的更改不会移除对原始有效组 ID 的成员资格，因为这些更改不影响补充组。明确不希望如此的应用程序必须进行修改，停止将有效组 ID 作为第一个元素传递给 `setgroups()`。

要清除调用进程的所有补充组，应始终使用以下语句

```c
setgroups(0, NULL);
```

该语句在较旧的 FreeBSD 版本上也能工作（参见[历史](#历史)小节）。
