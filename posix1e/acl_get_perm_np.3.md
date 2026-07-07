# acl_get_perm_np(3)

`acl_get_perm_np` — 检查权限集中是否设置了某个权限

## 名称

`acl_get_perm_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_get_perm_np(acl_permset_t permset_d, acl_perm_t perm);
```

## 描述

`acl_get_perm_np` 函数是一个非可移植函数，用于检查权限集中是否设置了某个权限。

## 返回值

如果 `perm` 所表示的权限在权限集 `permset_d` 中设置了，返回值为 1，否则返回值为 0。

## 错误

如果发生以下任一情况，`acl_get_perm_np` 函数将返回值 -1，并将全局变量 `errno` 设置为相应值：

`[EINVAL]` 参数 `perm` 不包含有效的 ACL 权限，或参数 `permset_d` 不是有效的 ACL 权限集。

## 参见

[acl(3)](acl.3.md), [acl_add_perm(3)](acl_add_perm.3.md), [acl_clear_perms(3)](acl_clear_perms.3.md), [acl_delete_perm(3)](acl_delete_perm.3.md), [acl_get_permset(3)](acl_get_permset.3.md), [acl_set_permset(3)](acl_set_permset.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_get_perm_np` 函数添加于 FreeBSD 5.0。

## 作者

`acl_get_perm_np` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
