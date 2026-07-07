# acl_from_text(3)

`acl_from_text` — 从文本创建 ACL

## 名称

`acl_from_text`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
acl_t
acl_from_text(const char *buf_p);
```

## 描述

`acl_from_text` 函数将 `buf_p` 所引用的 ACL 文本形式转换为 ACL 的内部工作结构，适合应用于文件或进行操作。

此函数可能会分配内存。当不再需要新 ACL 时，调用者应通过以 `(void *)acl_t` 为参数调用 [acl_free(3)](acl_free.3.md) 来释放任何可释放的内存。

## 实现说明

FreeBSD 对 POSIX.1e 接口和特性的支持目前仍在开发中。

## 返回值

成功完成时，该函数应返回指向工作存储中 ACL 内部表示的指针。否则，应返回 `(acl_t)NULL`，并应设置 `errno` 以指示错误。

## 错误

如果发生以下任何情况，`acl_from_text` 函数应返回 `(acl_t)NULL`，并将 `errno` 设置为相应值：

`[EINVAL]` 参数 `buf_p` 无法转换为 ACL。

`[ENOMEM]` ACL 工作存储所需的内存超过了硬件或系统施加的内存管理约束所允许的数量。

## 参见

[acl(3)](acl.3.md), [acl_free(3)](acl_free.3.md), [acl_get(3)](acl_get.3.md), [acl_to_text(3)](acl_to_text.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参见 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在进行。

## 作者

Robert N M Watson

## 缺陷

`acl_from_text` 和 `acl_to_text` 函数依赖 getpwent(3) 库调用来管理用户名与 uid 的映射，以及 getgrent(3) 库调用来管理组名与 gid 的映射。这些调用不是线程安全的，因此 `acl_from_text` 和 `acl_to_text` 也不是线程安全的。这些函数还可能干扰与 `getpwent` 和 `getgrent` 调用相关的有状态调用。
