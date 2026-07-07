# acl_set_permset(3)

`acl_set_permset` — 设置 ACL 条目的权限

## 名称

`acl_set_permset`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_set_permset(acl_entry_t entry_d, acl_permset_t permset_d);
```

## 描述

`acl_set_permset` 函数是一个 POSIX.1e 调用，用于使用 `permset_d` 中包含的权限设置 ACL 条目 `entry_d` 的权限。

## 返回值

`acl_set_permset` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_set_permset` 函数在以下情况失败：

`[EINVAL]` 参数 `entry_d` 不是 ACL 条目的有效描述符。

## 参见

[acl(3)](acl.3.md), [acl_add_perm(3)](acl_add_perm.3.md), [acl_clear_perms(3)](acl_clear_perms.3.md), [acl_delete_perm(3)](acl_delete_perm.3.md), [acl_get_permset(3)](acl_get_permset.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_set_permset` 函数添加于 FreeBSD 5.0。

## 作者

`acl_set_permset` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
