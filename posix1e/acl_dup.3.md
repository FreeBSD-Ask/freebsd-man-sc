# acl_dup(3)

`acl_dup` — 复制 ACL

## 名称

`acl_dup`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
acl_t
acl_dup(acl_t acl);
```

## 描述

`acl_dup` 函数返回一个指针，指向参数 `acl` 所指向 ACL 的副本。

此函数可能会导致分配内存。当不再需要新的 ACL 时，调用者应通过以 `(void*)acl_t` 为参数调用 [acl_free(3)](acl_free.3.md) 来释放任何可释放的内存。

任何指向 `acl` 所引用 ACL 的现有 ACL 指针将继续指向该 ACL。

## 实现说明

FreeBSD 对 POSIX.1e 接口和特性的支持目前仍在开发中。

## 返回值

成功完成时，此函数返回指向所复制 ACL 的指针。否则，返回 `(acl_t)NULL`，并设置 `errno` 以指示错误。

## 错误

如果发生以下任何情况，`acl_dup` 函数将返回 `(acl_t)NULL`，并将 `errno` 设置为相应值：

`[EINVAL]` 参数 `acl` 未指向有效的 ACL。

`[ENOMEM]` 要返回的 `acl_t` 所需的内存超过了硬件或系统施加的内存管理约束所允许的数量。

## 参见

[acl(3)](acl.3.md), [acl_free(3)](acl_free.3.md), [acl_get(3)](acl_get.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参见 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在进行。

## 作者

Robert N M Watson
