# acl_set_tag_type(3)

`acl_set_tag_type` — 设置 ACL 条目的标签类型

## 名称

`acl_set_tag_type`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_set_tag_type(acl_entry_t entry_d, acl_tag_t tag_type);
```

## 描述

`acl_set_tag_type` 函数是一个 POSIX.1e 调用，用于将 ACL 条目 `entry_d` 的 ACL 标签类型设置为 `tag_type` 的值。

有效值为：

| ACL_USER_OBJ | 权限适用于文件所有者 |
| --- | --- |
| ACL_USER | 权限适用于由限定符指定的附加用户 |
| ACL_GROUP_OBJ | 权限适用于文件属组 |
| ACL_GROUP | 权限适用于由限定符指定的附加组 |
| ACL_MASK | 权限指定掩码 |
| ACL_OTHER | 权限适用于其他 |
| ACL_OTHER_OBJ | 同 ACL_OTHER |
| ACL_EVERYONE | 权限适用于 everyone@ |

以 `tag_type` 等于 ACL_MASK、ACL_OTHER 或 ACL_OTHER_OBJ 调用 `acl_set_tag_type` 会将 ACL 标记为 POSIX.1e 品牌。以 ACL_EVERYONE 调用则会将 ACL 标记为 NFSv4 品牌。

## 返回值

`acl_set_tag_type` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_set_tag_type` 函数在以下情况失败：

`[EINVAL]` 参数 `entry_d` 不是 ACL 条目的有效描述符。参数 `tag_type` 不是有效的 ACL 标签类型。ACL 已标记为其他品牌。

## 参见

[acl(3)](acl.3.md), [acl_get_brand_np(3)](acl_get_brand_np.3.md), [acl_get_tag_type(3)](acl_get_tag_type.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_set_tag_type` 函数添加于 FreeBSD 5.0。

## 作者

`acl_set_tag_type` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
