# acl_set_qualifier(3)

`acl_set_qualifier` — 设置 ACL 标签限定符

## 名称

`acl_set_qualifier`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_set_qualifier(acl_entry_t entry_d, const void *tag_qualifier_p);
```

## 描述

`acl_set_qualifier` 函数是一个 POSIX.1e 调用，用于将 ACL 条目 `entry_d` 的标签限定符设置为 `tag_qualifier_p` 所引用的值。

## 返回值

`acl_set_qualifier` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_set_qualifier` 函数在以下情况失败：

`[EINVAL]` 参数 `entry_d` 不是 ACL 条目的有效描述符。ACL 条目 `entry_d` 的标签类型不是 `ACL_USER` 或 `ACL_GROUP`。`tag_qualifier_p` 所指向的值无效。

`[ENOMEM]` 要返回的值所需的内存超过了硬件或系统施加的内存管理约束所允许的数量。

## 参见

[acl(3)](acl.3.md), [acl_get_qualifier(3)](acl_get_qualifier.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_get_qualifier` 函数添加于 FreeBSD 5.0。

## 作者

`acl_get_qualifier` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
