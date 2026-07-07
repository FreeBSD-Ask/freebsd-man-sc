# acl_get_entry_type_np(3)

`acl_get_entry_type_np` — 从 NFSv4 ACL 条目中检索 ACL 类型

## 名称

`acl_get_entry_type_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_get_entry_type_np(acl_entry_t entry_d, acl_entry_type_t *entry_type_p);
```

## 描述

`acl_get_entry_type_np` 函数是一个非可移植调用，用于返回 NFSv4 ACL 条目 `entry_d` 的 ACL 类型。成功完成后，参数 `entry_type_p` 所引用的位置将设置为 ACL 条目 `entry_d` 的 ACL 类型。

## 返回值

`acl_get_entry_type_np` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_get_entry_type_np` 函数在以下情况失败：

`[EINVAL]` 参数 `entry_d` 不是 NFSv4 ACL 条目的有效描述符。

## 参见

[acl(3)](acl.3.md), [acl_set_entry_type_np(3)](acl_set_entry_type_np.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_get_entry_type_np` 函数添加于 FreeBSD 8.0。

## 作者

`acl_get_entry_type_np` 函数由 Edward Tomasz Napierala <trasz@FreeBSD.org> 编写。
