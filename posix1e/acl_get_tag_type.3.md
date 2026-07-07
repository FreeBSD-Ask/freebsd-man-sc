# acl_get_tag_type(3)

`acl_get_tag_type` — 从 ACL 条目中检索标签类型

## 名称

`acl_get_tag_type`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_get_tag_type(acl_entry_t entry_d, acl_tag_t *tag_type_p);
```

## 描述

`acl_get_tag_type` 函数是一个 POSIX.1e 调用，用于返回 ACL 条目 `entry_d` 的标签类型。成功完成后，参数 `tag_type_p` 所引用的位置将设置为 ACL 条目 `entry_d` 的标签类型。

## 返回值

`acl_get_tag_type` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_get_tag_type` 函数在以下情况失败：

`[EINVAL]` 参数 `entry_d` 不是 ACL 条目的有效描述符。

## 参见

[acl(3)](acl.3.md), [acl_create_entry(3)](acl_create_entry.3.md), [acl_get_entry(3)](acl_get_entry.3.md), [acl_get_qualifier(3)](acl_get_qualifier.3.md), [acl_init(3)](acl_init.3.md), [acl_set_qualifier(3)](acl_set_qualifier.3.md), [acl_set_tag_type(3)](acl_set_tag_type.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_get_tag_type` 函数添加于 FreeBSD 5.0。

## 作者

`acl_get_tag_type` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
