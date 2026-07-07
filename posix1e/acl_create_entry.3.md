# acl_create_entry(3)

`acl_create_entry` — 创建新的 ACL 条目

## 名称

`acl_create_entry`, `acl_create_entry_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_create_entry(acl_t *acl_p, acl_entry_t *entry_p);

int
acl_create_entry_np(acl_t *acl_p, acl_entry_t *entry_p, int index);
```

## 描述

`acl_create_entry` 函数是一个 POSIX.1e 调用，用于在 `acl_p` 所指向的 ACL 中创建新的 ACL 条目。`acl_create_entry_np` 函数是一个不可移植的版本，在位置 `index` 处创建 ACL 条目。位置编号从零开始，即以 `index` 参数等于零调用 `acl_create_entry_np` 会将该条目添加到 ACL 的开头。

## 返回值

成功完成时，`acl_create_entry` 函数返回 0。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_create_entry` 函数在以下情况失败：

`[EINVAL]` 参数 `acl_p` 未指向指向有效 ACL 的指针。参数 `index` 超出范围。

`[ENOMEM]` ACL 工作存储所需的内存超过了硬件或系统施加的内存管理约束所允许的数量。

## 参见

[acl(3)](acl.3.md), [acl_delete_entry(3)](acl_delete_entry.3.md), [acl_get_entry(3)](acl_get_entry.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_create_entry` 函数添加于 FreeBSD 5.0。

## 作者

`acl_create_entry` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
