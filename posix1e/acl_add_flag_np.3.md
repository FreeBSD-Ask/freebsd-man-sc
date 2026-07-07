# acl_add_flag_np(3)

`acl_add_flag_np` — 向标志集中添加标志

## 名称

`acl_add_flag_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_add_flag_np(acl_flagset_t flagset_d, acl_flag_t flag);
```

## 描述

`acl_add_flag_np` 函数是一个非可移植调用，用于将 `flags` 中包含的 NFSv4 ACL 标志添加到标志集 `flagset_d` 中。

注意：尝试添加标志集中存在的标志不视为错误。

有效值为：

| ACL_ENTRY_FILE_INHERIT | 将被文件继承。 |
| --- | --- |
| ACL_ENTRY_DIRECTORY_INHERIT | 将被目录继承。 |
| ACL_ENTRY_NO_PROPAGATE_INHERIT | 将不传播。 |
| ACL_ENTRY_INHERIT_ONLY | 仅继承。 |
| ACL_ENTRY_INHERITED | 从父级继承 |

## 返回值

`acl_add_flag_np` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_add_flag_np` 函数在以下情况失败：

`[EINVAL]` 参数 `flagset_d` 不是 ACL 条目内标志集的有效描述符。参数 `flag` 不包含有效的 `acl_flag_t` 值。

## 参见

[acl(3)](acl.3.md), [acl_clear_flags_np(3)](acl_clear_flags_np.3.md), [acl_delete_flag_np(3)](acl_delete_flag_np.3.md), [acl_get_flagset_np(3)](acl_get_flagset_np.3.md), [acl_set_flagset_np(3)](acl_set_flagset_np.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_add_flag_np` 函数添加于 FreeBSD 8.0。

## 作者

`acl_add_flag_np` 函数由 Edward Tomasz Napierala <trasz@FreeBSD.org> 编写。
