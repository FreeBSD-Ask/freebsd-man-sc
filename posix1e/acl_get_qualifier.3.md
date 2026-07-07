# acl_get_qualifier(3)

`acl_get_qualifier` — 从 ACL 条目中检索限定符

## 名称

`acl_get_qualifier`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
void *
acl_get_qualifier(acl_entry_t entry_d);
```

## 描述

`acl_get_qualifier` 函数是一个 POSIX.1e 调用，用于将参数 `entry_d` 所指示 ACL 条目的标签限定符检索到工作存储中，并返回指向该存储的指针。

如果 `entry_d` 所引用 ACL 条目的标签类型值为 `ACL_USER`，则 `acl_get_qualifier` 返回的值将是指向 `uid_t` 类型的指针。

如果 `entry_d` 所引用 ACL 条目的标签类型值为 `ACL_GROUP`，则 `acl_get_qualifier` 返回的值将是指向 `gid_t` 类型的指针。

如果 `entry_d` 所引用 ACL 条目的标签类型值为 `ACL_UNDEFINED_TAG`、`ACL_USER_OBJ`、`ACL_GROUP_OBJ`、`ACL_OTHER`、`ACL_MASK`，或不支持限定符的实现定义值，则 `acl_get_qualifier` 将返回 `(void *)NULL`，且函数将失败。

此函数可能会导致分配内存。当不再需要新的限定符时，调用者应通过以 `void *` 为参数调用 `acl_free` 来释放任何可释放的内存。

## 返回值

`acl_get_qualifier` 函数成功时返回指向所分配存储的指针；否则返回 `NULL` 指针，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_get_qualifier` 函数在以下情况失败：

`[EINVAL]` 参数 `entry_d` 未指向 ACL 条目的有效描述符。参数 `entry_d` 所引用 ACL 条目的标签类型值不是 `ACL_USER` 或 `ACL_GROUP`。

`[ENOMEM]` 要返回的值所需的内存超过了硬件或系统施加的内存管理约束所允许的数量。

## 参见

[acl(3)](acl.3.md), [acl_create_entry(3)](acl_create_entry.3.md), [acl_free(3)](acl_free.3.md), [acl_get_entry(3)](acl_get_entry.3.md), [acl_get_tag_type(3)](acl_get_tag_type.3.md), [acl_set_qualifier(3)](acl_set_qualifier.3.md), [acl_set_tag_type(3)](acl_set_tag_type.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_get_qualifier` 函数添加于 FreeBSD 5.0。

## 作者

`acl_get_qualifier` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
