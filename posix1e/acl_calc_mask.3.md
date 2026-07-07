# acl_calc_mask(3)

`acl_calc_mask` — 计算并设置 ACL 掩码权限

## 名称

`acl_calc_mask`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_calc_mask(acl_t *acl_p);
```

## 描述

`acl_calc_mask` 函数是一个 POSIX.1e 调用，用于计算并设置 `acl_p` 所引用 ACL 中 `ACL_MASK` ACL 条目关联的权限。

新权限的值是 `acl_p` 所引用 ACL 中包含的、与文件组类中的进程匹配的 `ACL_GROUP`、`ACL_GROUP_OBJ`、`ACL_USER` 标签类型所授予权限的并集。

如果 `acl_p` 所引用的 ACL 已包含 `ACL_MASK` 条目，其权限将被覆盖；如果不包含 `ACL_MASK` 条目，将添加一个。

## 返回值

`acl_calc_mask` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`acl_calc_mask` 函数在以下情况失败：

`[EINVAL]` 参数 `acl_p` 未指向有效 ACL 的指针。

## 参见

[acl(3)](acl.3.md), [acl_get_entry(3)](acl_get_entry.3.md), [acl_valid(3)](acl_valid.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_calc_mask` 函数添加于 FreeBSD 5.0。

## 作者

`acl_calc_mask` 函数由 Chris D. Faulhaber <jedgar@fxp.org> 编写。
