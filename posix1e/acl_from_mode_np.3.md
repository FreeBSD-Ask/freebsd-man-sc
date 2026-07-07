# acl_from_mode_np(3)

`acl_from_mode_np` — 从状态信息创建 ACL

## 名称

`acl_from_mode_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
acl_t
acl_from_mode_np(const mode_t mode);
```

## 描述

`acl_from_mode_np` 函数是一个不可移植的调用，用于将 `mode` 所引用的权限集转换为相应的最小 ACL 结构，适合应用于文件或进行操作。

此函数会分配内存。当不再需要新 ACL 时，调用者应通过以 `(void *)acl_t` 为参数调用 [acl_free(3)](acl_free.3.md) 来释放任何可释放的内存。

## 返回值

成功完成时，该函数返回指向工作存储中 ACL 内部表示的指针。否则，返回 `(acl_t)NULL`，并设置 `errno` 以指示错误。

## 错误

如果发生以下任何情况，`acl_from_mode_np` 函数返回 `(acl_t)NULL`，并将 `errno` 设置为相应值：

`[ENOMEM]` ACL 工作存储所需的内存超过了硬件或系统施加的内存管理约束所允许的数量。

## 参见

[acl(3)](acl.3.md), [acl_free(3)](acl_free.3.md), [acl_from_text(3)](acl_from_text.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参见 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在进行。

## 作者

Gleb Popov
