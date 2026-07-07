# acl_get_permset(3)

`acl_get_permset` — 从 ACL 条目中检索权限集

## 名称

`acl_get_permset`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_get_permset(acl_entry_t entry_d, acl_permset_t *permset_p);
```

## 描述

`acl_get_permset` 函数是一个 POSIX.1e 调用，用于通过 `permset_p` 返回 ACL 条目 `entry_d` 中权限集的描述符。使用返回的权限集进行的后续操作将作用于该 ACL 条目内的权限集。

## 返回值

`acl_get_permset` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_get_permset` 函数在以下情况失败：

`[EINVAL]` 参数 `entry_d` 不是 ACL 条目的有效描述符。

## 参见

[acl(3)](acl.3.md), [acl_add_perm(3)](acl_add_perm.3.md), [acl_clear_perms(3)](acl_clear_perms.3.md), [acl_delete_perm(3)](acl_delete_perm.3.md), [acl_get_perm_np(3)](acl_get_perm_np.3.md), [acl_set_permset(3)](acl_set_permset.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_get_permset` 函数添加于 FreeBSD 5.0。

## 作者

`acl_get_permset` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
