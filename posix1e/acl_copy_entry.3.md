# acl_copy_entry(3)

`acl_copy_entry` — 将一个 ACL 条目复制到另一个 ACL 条目

## 名称

`acl_copy_entry`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_copy_entry(acl_entry_t dest_d, acl_entry_t src_d);
```

## 描述

`acl_copy_entry` 函数是一个 POSIX.1e 调用，用于将 ACL 条目 `src_d` 的内容复制到 ACL 条目 `dest_d`。

## 返回值

成功完成时，`acl_copy_entry` 函数返回 0。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_copy_entry` 函数在以下情况失败：

`[EINVAL]` 参数 `src_d` 或 `dest_d` 不是 ACL 条目的有效描述符，或参数 `src_d` 和 `dest_d` 引用同一个 ACL 条目。

## 参见

[acl(3)](acl.3.md), [acl_get_entry(3)](acl_get_entry.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_copy_entry` 函数添加于 FreeBSD 5.0。

## 作者

`acl_copy_entry` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
