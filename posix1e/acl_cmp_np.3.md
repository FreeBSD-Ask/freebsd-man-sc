# acl_cmp_np(3)

`acl_cmp_np` — 比较两个 ACL

## 名称

`acl_cmp_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_cmp_np(acl_t acl1, acl_t acl2);
```

## 描述

`acl_cmp_np` 函数是一个非可移植调用，用于检查 `acl1` 和 `acl2` 所指向的 ACL 是否等价。当两个 ACL 包含相同的条目，且标签类型、限定符和权限均匹配时，认为两者相等。

## 返回值

成功完成时，若给定的 ACL 等价则该函数返回 0，若不同则返回 1。否则返回 -1，并由 `errno` 指示错误。

## 错误

若发生以下任一情况，`acl_cmp_np` 函数将返回 -1，并将 `errno` 设置为相应值：

`[EINVAL]` 第一个或第二个参数未指向有效的 ACL。

## 参见

[acl(3)](acl.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。如需加入该列表，请参阅 FreeBSD POSIX.1e 实现页面获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在继续。

## 作者

Gleb Popov
