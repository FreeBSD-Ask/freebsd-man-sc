# acl_equiv_mode_np(3)

`acl_equiv_mode_np` — 检查 ACL 是否可以表示为 UNIX 权限

## 名称

`acl_equiv_mode_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_equiv_mode_np(acl_t acl, mode_t* mode_p);
```

## 描述

`acl_equiv_mode_np` 函数是一个非可移植调用，用于检查 `acl` 参数所包含的条目是否仅使用 ACL_USER_OBJ、ACL_GROUP_OBJ 和 ACL_OTHER 标签类型，并且这些条目中包含的权限是否仅由 ACL_READ、ACL_WRITE 和 ACL_EXECUTE 组成。如果检查通过，该 ACL 可以表示为传统的 UNIX 文件权限位集合。

如果 `mode_p` 不为 NULL 且检查通过，该函数将使用与 ACL 中包含的权限相对应的模式值填充该参数。

## 返回值

成功完成时，如果 ACL 可以表示为 UNIX 权限，函数返回 0；如果无法表示，返回 1。否则，返回值为 -1，并设置 `errno` 以指示错误。

## 错误

如果发生以下任一情况，`acl_equiv_mode_np` 函数返回值 -1，并将 `errno` 设置为相应值：

`[EINVAL]` 参数 `acl` 未指向有效的 ACL。

## 参见

[acl(3)](acl.3.md), [acl_from_mode_np(3)](acl_from_mode_np.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参阅 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在继续。

## 作者

Gleb Popov
