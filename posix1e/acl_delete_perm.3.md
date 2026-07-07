# acl_delete_perm(3)

`acl_delete_perm` — 从权限集中删除权限

## 名称

`acl_delete_perm`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_delete_perm(acl_permset_t permset_d, acl_perm_t perm);
```

## 描述

`acl_delete_perm` 函数是一个 POSIX.1e 调用，用于从权限集 `permset_d` 中删除特定的权限。

## 返回值

`acl_delete_perm` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_delete_perm` 函数在以下情况失败：

`[EINVAL]` 参数 `permset_d` 不是权限集的有效描述符。参数 `perm` 不包含有效的 `acl_perm_t` 值。

## 参见

[acl(3)](acl.3.md), [acl_add_perm(3)](acl_add_perm.3.md), [acl_clear_perms(3)](acl_clear_perms.3.md), [acl_get_permset(3)](acl_get_permset.3.md), [acl_set_permset(3)](acl_set_permset.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_delete_perm` 函数添加于 FreeBSD 5.0。

## 作者

`acl_delete_perm` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
