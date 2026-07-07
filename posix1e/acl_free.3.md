# acl_free(3)

`acl_free` — 释放 ACL 工作状态

## 名称

`acl_free`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_free(void *obj_p);
```

## 描述

`acl_free` 调用允许释放 ACL 工作空间，例如由 [acl_dup(3)](acl_dup.3.md) 或 [acl_from_text(3)](acl_from_text.3.md) 所分配的空间。

## 实现说明

FreeBSD 对 POSIX.1e 接口和特性的支持目前仍在开发中。

## 返回值

`acl_free` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

如果发生以下任何情况，`acl_free` 函数将返回 -1，并将 `errno` 设置为相应值：

`[EINVAL]` 参数 `obj_p` 的值无效。

## 参见

[acl(3)](acl.3.md), [acl_dup(3)](acl_dup.3.md), [acl_from_text(3)](acl_from_text.3.md), [acl_get(3)](acl_get.3.md), [acl_init(3)](acl_init.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参见 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在进行。

## 作者

Robert N M Watson
