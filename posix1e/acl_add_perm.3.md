# acl_add_perm(3)

`acl_add_perm` — 向权限集中添加权限

## 名称

`acl_add_perm`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_add_perm(acl_permset_t permset_d, acl_perm_t perm);
```

## 描述

`acl_add_perm` 函数是一个 POSIX.1e 调用，用于将 `perm` 中包含的权限添加到权限集 `permset_d` 中。

注意：尝试添加权限集中存在的权限不视为错误。

对于 POSIX.1e ACL，有效值为：

| ACL_EXECUTE | 执行权限 |
| --- | --- |
| ACL_WRITE | 写入权限 |
| ACL_READ | 读取权限 |

对于 NFSv4 ACL，有效值为：

| ACL_READ_DATA | 读取权限 |
| --- | --- |
| ACL_LIST_DIRECTORY | 同 ACL_READ_DATA |
| ACL_WRITE_DATA | 写入权限，或创建文件的权限 |
| ACL_ADD_FILE | 同 ACL_READ_DATA |
| ACL_APPEND_DATA | 创建目录的权限。对文件忽略 |
| ACL_ADD_SUBDIRECTORY | 同 ACL_APPEND_DATA |
| ACL_READ_NAMED_ATTRS | 忽略 |
| ACL_WRITE_NAMED_ATTRS | 忽略 |
| ACL_EXECUTE | 执行权限 |
| ACL_DELETE_CHILD | 删除文件和子目录的权限 |
| ACL_READ_ATTRIBUTES | 读取基本属性的权限 |
| ACL_WRITE_ATTRIBUTES | 修改基本属性的权限 |
| ACL_DELETE | 删除该 ACL 所附加对象的权限 |
| ACL_READ_ACL | 读取 ACL 的权限 |
| ACL_WRITE_ACL | 修改 ACL 和文件模式的权限 |
| ACL_SYNCHRONIZE | 忽略 |

使用 `perm` 等于 ACL_WRITE 或 ACL_READ 调用 `acl_add_perm` 会将 ACL 标记为 POSIX。使用 ACL_READ_DATA、ACL_LIST_DIRECTORY、ACL_WRITE_DATA、ACL_ADD_FILE、ACL_APPEND_DATA、ACL_ADD_SUBDIRECTORY、ACL_READ_NAMED_ATTRS、ACL_WRITE_NAMED_ATTRS、ACL_DELETE_CHILD、ACL_READ_ATTRIBUTES、ACL_WRITE_ATTRIBUTES、ACL_DELETE、ACL_READ_ACL、ACL_WRITE_ACL 或 ACL_SYNCHRONIZE 调用该函数会将 ACL 标记为 NFSv4。

## 返回值

`acl_add_perm` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_add_perm` 函数在以下情况失败：

`[EINVAL]` 参数 `permset_d` 不是 ACL 条目内权限集的有效描述符。参数 `perm` 不包含有效的 `acl_perm_t` 值。ACL 已标记为其他类型。

## 参见

[acl(3)](acl.3.md), [acl_clear_perms(3)](acl_clear_perms.3.md), [acl_delete_perm(3)](acl_delete_perm.3.md), [acl_get_brand_np(3)](acl_get_brand_np.3.md), [acl_get_permset(3)](acl_get_permset.3.md), [acl_set_permset(3)](acl_set_permset.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_add_perm` 函数添加于 FreeBSD 5.0。

## 作者

`acl_add_perm` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
