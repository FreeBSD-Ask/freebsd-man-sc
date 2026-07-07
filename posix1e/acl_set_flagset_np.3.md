# acl_set_flagset_np(3)

`acl_set_flagset_np` — 设置 NFSv4 ACL 条目的标志

## 名称

`acl_set_flagset_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_set_flagset_np(acl_entry_t entry_d, acl_flagset_t flagset_d);
```

## 描述

`acl_set_flagset_np` 函数是一个非可移植调用，用于使用 `flagset_d` 中包含的标志设置 NFSv4 ACL 条目 `entry_d` 的标志。

此调用将 ACL 标记为 NFSv4 品牌。

## 返回值

`acl_set_flagset_np` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_set_flagset_np` 函数在以下情况失败：

`[EINVAL]` 参数 `entry_d` 不是 ACL 条目的有效描述符。ACL 已标记为 POSIX.1e 品牌。

## 参见

[acl(3)](acl.3.md), [acl_add_flag_np(3)](acl_add_flag_np.3.md), [acl_clear_flags_np(3)](acl_clear_flags_np.3.md), [acl_delete_flag_np(3)](acl_delete_flag_np.3.md), [acl_get_brand_np(3)](acl_get_brand_np.3.md), [acl_get_flagset_np(3)](acl_get_flagset_np.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_set_flagset_np` 函数添加于 FreeBSD 8.0。

## 作者

`acl_set_flagset_np` 函数由 Edward Tomasz Napierala <trasz@FreeBSD.org> 编写。
