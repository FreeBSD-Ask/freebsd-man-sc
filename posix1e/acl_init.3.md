# acl_init(3)

`acl_init` — 初始化 ACL 工作存储

## 名称

`acl_init`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
acl_t
acl_init(int count);
```

## 描述

`acl_init` 函数为至少包含 `count` 个 ACL 条目的 ACL 分配并初始化工作存储。返回指向该工作存储的指针。分配用于容纳 ACL 的工作存储通过调用 [acl_free(3)](acl_free.3.md) 释放。该区域首次分配时，应包含一个不含任何 ACL 条目的 ACL。

该函数可能导致内存分配。当不再需要新 ACL 时，调用者应通过以 `(void*)acl_t` 为参数调用 [acl_free(3)](acl_free.3.md) 来释放可释放的内存。

## 实现说明

FreeBSD 对 POSIX.1e 接口和特性的支持目前仍在开发中。

## 返回值

成功完成时，该函数将返回指向工作存储的指针。否则，返回 `(acl_t)NULL`，并设置 `errno` 以指示错误。

## 错误

若发生以下任一情况，`acl_init` 函数将返回 `(acl_t)NULL`，并将 `errno` 设置为相应值：

`[EINVAL]` `count` 的值小于零。

`[ENOMEM]` 要返回的 `acl_t` 所需内存超过了硬件或系统施加的内存管理约束所允许的范围。

## 参见

[acl(3)](acl.3.md), [acl_free(3)](acl_free.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参见 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在继续。

## 作者

Robert N M Watson
