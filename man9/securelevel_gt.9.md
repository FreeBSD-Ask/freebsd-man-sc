# securelevel_gt(9)

`securelevel_gt` — 测试活动安全级别

## 名称

`securelevel_gt`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/proc.h>
```

```c
int
securelevel_gt(struct ucred *cr, int level)

int
securelevel_ge(struct ucred *cr, int level)
```

## 描述

这些函数将活动安全级别与给定的 `level` 进行测试。如果调用凭据 `cr` 被 jail(2) 系统调用监禁，并且设置了与主机环境不同的安全级别，则使用具有最高值的安全级别。

`securelevel_gt` 函数评估活动安全级别是否大于提供的 `level`。

`securelevel_ge` 函数评估活动安全级别是否大于或等于提供的 `level`。

## 返回值

如果条件评估为 true，这些函数返回 `EPERM`，否则返回 0。

## 参见

[securelevel(7)](../man7/security.7.md)
