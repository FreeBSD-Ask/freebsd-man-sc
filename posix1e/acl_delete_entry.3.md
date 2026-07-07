# acl_delete_entry(3)

`acl_delete_entry` — 从 ACL 中删除 ACL 条目

## 名称

`acl_delete_entry`, `acl_delete_entry_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_delete_entry(acl_t acl, acl_entry_t entry_d);

int
acl_delete_entry_np(acl_t acl, int index);
```

## 描述

`acl_delete_entry` 函数是一个 POSIX.1e 调用，用于从 ACL `acl` 中删除 ACL 条目 `entry_d`。`acl_delete_entry_np` 函数是一个不可移植的版本，用于从 ACL `acl` 中删除位置 `index` 处的 ACL 条目。位置编号从零开始，即以 `index` 参数等于零调用 `acl_delete_entry_np` 会删除第一个 ACL 条目。

## 返回值

成功完成时，`acl_delete_entry` 函数返回 0。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_delete_entry` 函数在以下情况失败：

`[EINVAL]` 参数 `acl` 未指向有效的 ACL。参数 `entry_d` 不是 `acl` 中 ACL 条目的有效描述符。参数 `index` 超出范围。

## 参见

[acl(3)](acl.3.md), [acl_copy_entry(3)](acl_copy_entry.3.md), [acl_get_entry(3)](acl_get_entry.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_delete_entry` 函数添加于 FreeBSD 5.0。

## 作者

`acl_delete_entry` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
