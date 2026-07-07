# acl_get_flag_np(3)

`acl_get_flag_np` — 检查标志集中是否设置了某个标志

## 名称

`acl_get_flag_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_get_flag_np(acl_flagset_t flagset_d, acl_flag_t flag);
```

## 描述

`acl_get_flag_np` 函数是一个非可移植函数，用于检查标志集中是否设置了 NFSv4 ACL 标志。

## 返回值

如果 `flag` 中的标志在标志集 `flagset_d` 中已设置，返回值 1，否则返回值 0。

## 错误

如果出现以下任何条件，`acl_get_flag_np` 函数将返回值 -1 并设置全局变量 `errno` 为相应值：

`[EINVAL]` 参数 `flag` 不包含有效的 ACL 标志，或参数 `flagset_d` 不是有效的 ACL 标志集。

## 参见

[acl(3)](acl.3.md), [acl_add_flag_np(3)](acl_add_flag_np.3.md), [acl_clear_flags_np(3)](acl_clear_flags_np.3.md), [acl_delete_flag_np(3)](acl_delete_flag_np.3.md), [acl_get_flagset_np(3)](acl_get_flagset_np.3.md), [acl_set_flagset_np(3)](acl_set_flagset_np.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_get_flag_np` 函数添加于 FreeBSD 8.0。

## 作者

`acl_get_flag_np` 函数由 Edward Tomasz Napierala <trasz@FreeBSD.org> 编写。
