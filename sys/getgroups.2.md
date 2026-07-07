# getgroups(2)

`getgroups` — 获取调用进程的补充组

## 名称

`getgroups`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
getgroups(int gidsetlen, gid_t *gidset);
```

## 描述

`getgroups()` 系统调用获取调用进程的补充组，并按严格升序将其存储在 `gidset` 数组中。`gidsetlen` 的值指示可放入 `gidset` 的最大条目数。

如果 `gidsetlen` 为零，`getgroups()` 返回调用进程补充组集合的基数，并忽略 `gidset` 参数。

返回的值不会超过 `{NGROUPS_MAX}` 个。`{NGROUPS_MAX}` 的值应使用 [sysconf(3)](../man3/sysconf.3.md) 获取，以避免将其硬编码到可执行文件中。

## 返回值

成功时，`getgroups()` 系统调用返回补充组集合的基数。如果 `gidsetlen` 参数为零，则总是成功。

返回值 -1 表示发生错误，错误码存储在全局变量 `errno` 中。

## 错误

`getgroups()` 可能产生的错误有：

**[`EINVAL`]** `gidsetlen` 参数小于补充组的数量（但不为零）。

**[`EFAULT`]** 在从 `gidset` 数组读取时遇到无效地址。

## 参见

[setgroups(2)](setgroups.2.md), [initgroups(3)](../man3/initgroups.3.md), [sysconf(3)](../man3/sysconf.3.md)

## 标准

`getgroups()` 系统调用遵循 IEEE Std 1003.1-2008 ("POSIX.1")，不报告有效组 ID。

## 历史

`getgroups()` 系统调用首次出现于 4.2BSD。

自 FreeBSD 14.3 起，`getgroups()` 系统调用按严格升序报告补充组。

在 FreeBSD 15.0 之前，`getgroups()` 系统调用会额外将有效组 ID 作为数组的第一个元素返回，位于补充组之前。

## 安全注意事项

`getgroups()` 系统调用在 `gidset` 数组中获取补充组集合。特别是，如前文历史部分所述，它不再在 `gidset` 的第一个槽位获取有效组 ID。以特定方式处理该槽位的程序必须修改为通过其他方式获取有效组 ID，例如调用 [getegid(2)](getegid.2.md)。

当且仅当有效组 ID 被显式设置为补充组时，它才存在于补充组集合中。`initgroups()` 函数强制执行此要求，而 `setgroups()` 系统调用则不然。请参阅 [initgroups(3)](../man3/initgroups.3.md) 手册页了解其设计理由。
