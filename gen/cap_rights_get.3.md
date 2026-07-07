# cap_rights_get(3)

`cap_rights_get` — 获取能力权限

## 名称

`cap_rights_get`

## 库

Lb libc

## 概要

`#include <sys/capsicum.h>`

```c
int
cap_rights_get(int fd, cap_rights_t *rights);
```

## 描述

`cap_rights_get` 函数用于获取给定描述符的当前能力权限。如果能力权限未被限制，该函数会用所有能力权限填充 `rights` 参数，或填充上一次在给定描述符上成功调用 [cap_rights_limit(2)](../sys/cap_rights_limit.2.md) 时所配置的能力权限。

`rights` 参数可使用 [cap_rights_init(3)](../man3/cap_rights_init.3.md) 系列函数进行检视。

完整的能力权限列表可在 [rights(4)](../man4/rights.4.md) 手册页中找到。

## 返回值

`cap_rights_get` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 实例

以下示例演示了如何限制文件描述符的能力权限以及如何获取它们。

```c
cap_rights_t setrights, getrights;
int fd;

memset(&setrights, 0, sizeof(setrights));
memset(&getrights, 0, sizeof(getrights));

fd = open("/tmp/foo", O_RDONLY);
if (fd < 0)
	err(1, "open() failed");

cap_rights_init(&setrights, CAP_FSTAT, CAP_READ);
if (cap_rights_limit(fd, &setrights) < 0 && errno != ENOSYS)
	err(1, "cap_rights_limit() failed");

if (cap_rights_get(fd, &getrights) < 0 && errno != ENOSYS)
	err(1, "cap_rights_get() failed");

assert(memcmp(&setrights, &getrights, sizeof(setrights)) == 0);
```

## 错误

`cap_rights_get` 除非遇到以下情况，否则均会成功：

**[`EBADF`]** `fd` 参数不是有效的活动描述符。

**[`EFAULT`]** `rights` 参数指向了无效的地址。

## 参见

[cap_rights_limit(2)](../sys/cap_rights_limit.2.md), [errno(2)](../sys/errno.2.md), [open(2)](../sys/open.2.md), [assert(3)](assert.3.md), [cap_rights_init(3)](../man3/cap_rights_init.3.md), [err(3)](err.3.md), [memcmp(3)](../man3/memcmp.3.md), [memset(3)](../man3/memset.3.md), [capsicum(4)](../man4/capsicum.4.md), [rights(4)](../man4/rights.4.md)

## 历史

`cap_rights_get` 函数首次出现于 FreeBSD 9.2。对能力和能力模式的支持是作为 TrustedBSD 项目的一部分开发的。

## 作者

此函数由 Pawel Jakub Dawidek <pawel@dawidek.net> 在 FreeBSD Foundation 的赞助下创建。
