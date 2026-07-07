# acl_strip_np(3)

`acl_strip_np` — 从 ACL 中移除扩展条目

## 名称

`acl_strip_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
acl_t
acl_strip_np(const acl_t acl, int recalculate_mask);
```

## 描述

`acl_strip_np` 函数返回一个指针，指向根据参数 `acl` 所指向 ACL 计算得出的平凡 ACL。

此函数可能会导致分配内存。当不再需要新 ACL 时，调用者应通过以 `(void*)acl_t` 为参数调用 [acl_free(3)](acl_free.3.md) 来释放任何可释放的内存。

任何指向 `acl` 所引用 ACL 的现有 ACL 指针将继续指向该 ACL。

## 返回值

成功完成时，此函数返回指向新分配 ACL 的指针。否则，返回 `(acl_t)NULL`，并设置 `errno` 以指示错误。

## 错误

若发生以下任一情况，`acl_strip_np` 函数将返回 `(acl_t)NULL`，并将 `errno` 设置为相应值：

`[EINVAL]` 参数 `acl` 未指向有效的 ACL。

`[ENOMEM]` 要返回的 `acl_t` 所需的内存超过了硬件或系统施加的内存管理约束所允许的数量。

## 参见

[acl(3)](acl.3.md), [acl_is_trivial_np(3)](acl_is_trivial_np.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参见 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_strip_np` 函数添加于 FreeBSD 8.0。

## 作者

Edward Tomasz Napierala <trasz@FreeBSD.org>
