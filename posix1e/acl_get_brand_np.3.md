# acl_get_brand_np(3)

`acl_get_brand_np` — 从 ACL 中检索 ACL 品牌

## 名称

`acl_get_brand_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_get_brand_np(acl_t acl, int *brand_p);
```

## 描述

`acl_get_brand_np` 函数是一个非可移植调用，用于返回 ACL `acl` 的 ACL 品牌。成功完成后，参数 `brand_p` 所引用的位置将设置为 ACL `acl` 的 ACL 品牌。

品牌是一种内部机制，旨在防止错误地混合 POSIX.1e 和 NFSv4 条目。libc 还使用它来确定如何输出 ACL。第一次调用特定于某一品牌（POSIX.1e 或 NFSv4）的函数会为 ACL “打上品牌”。此后，调用特定于另一品牌的函数将导致错误。

## 返回值

`acl_get_brand_np` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_get_brand_np` 函数在以下情况失败：

`[EINVAL]` 参数 `acl` 未指向有效的 ACL。

## 参见

[acl(3)](acl.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_get_brand_np` 函数添加于 FreeBSD 8.0。

## 作者

`acl_get_brand_np` 函数由 Edward Tomasz Napierala <trasz@FreeBSD.org> 编写。
