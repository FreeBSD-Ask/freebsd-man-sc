# acl_get_entry(3)

`acl_get_entry` — 从 ACL 中检索 ACL 条目

## 名称

`acl_get_entry`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_get_entry(acl_t acl, int entry_id, acl_entry_t *entry_p);
```

## 描述

`acl_get_entry` 函数是一个 POSIX.1e 调用，用于从参数 `acl` 所指示的 ACL 中检索由参数 `entry_id` 指定的 ACL 条目的描述符。

如果 `entry_id` 的值为 `ACL_FIRST_ENTRY`，则该函数将在 `entry_p` 中返回 `acl` 中第一个 ACL 条目的描述符。如果在尚未成功调用过 `acl_get_entry`，或尚未成功调用过 `acl_create_entry`、`acl_delete_entry`、`acl_dup`、`acl_from_text`、`acl_get_fd`、`acl_get_file`、`acl_set_fd`、`acl_set_file` 或 `acl_valid` 的情况下，以 `entry_id` 设为 `ACL_NEXT_ENTRY` 调用 `acl_get_entry`，则结果未定义。

## 返回值

如果 `acl_get_entry` 函数成功获取 ACL 条目，返回值 1。如果 ACL 中没有 ACL 条目，`acl_get_entry` 返回值 0。如果 `entry_id` 的值为 `ACL_NEXT_ENTRY`，且 ACL 中的最后一个 ACL 条目已由前一次对 `acl_get_entry` 的调用返回，则返回值 0，直到以 `entry_id` 为 `ACL_FIRST_ENTRY` 成功调用为止。否则，返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_get_entry` 函数在以下情况失败：

`[EINVAL]` 参数 `acl` 未指向有效的 ACL。参数 `entry_id` 既不是 `ACL_FIRST_ENTRY` 也不是 `ACL_NEXT_ENTRY`。

## 参见

[acl(3)](acl.3.md), [acl_calc_mask(3)](acl_calc_mask.3.md), [acl_create_entry(3)](acl_create_entry.3.md), [acl_delete_entry(3)](acl_delete_entry.3.md), [acl_dup(3)](acl_dup.3.md), [acl_from_text(3)](acl_from_text.3.md), acl_get_fd(3), acl_get_file(3), [acl_init(3)](acl_init.3.md), acl_set_fd(3), acl_set_file(3), [acl_valid(3)](acl_valid.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_get_entry` 函数添加于 FreeBSD 5.0。

## 作者

`acl_get_entry` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
