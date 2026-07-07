# sysctl_add_oid(9)

`sysctl_add_oid` — 运行时 sysctl 树操作

## 名称

`sysctl_add_oid`, `sysctl_move_oid`, `sysctl_remove_oid`, `sysctl_remove_name`

## 概要

```c
#include <sys/types.h>
#include <sys/sysctl.h>

struct sysctl_oid *
sysctl_add_oid(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int kind, void *arg1, intmax_t arg2,
    int (*handler)(SYSCTL_HANDLER_ARGS), const char *format,
    const char *descr, const char *label)

int
sysctl_move_oid(struct sysctl_oid *oidp, struct sysctl_oid_list *parent)

int
sysctl_remove_oid(struct sysctl_oid *oidp, int del, int recurse)

int
sysctl_remove_name(struct sysctl_oid *oidp, const char *name, int del,
    int recurse)
```

## 描述

这些函数提供了在运行时（例如在模块生命周期内）创建和删除 sysctl OID 的接口。创建新 OID 时建议使用 [sysctl(9)](sysctl.9.md) 定义的包装宏。不应直接从代码中调用 `sysctl_add_oid`。

`CTLTYPE_NODE` 类型的动态 OID 是可重用的，因此多个代码段可以创建和删除它们，但实际上它们是基于引用计数分配和释放的。因此，两个或更多代码段可以创建它们都可以使用的部分重叠树。不能创建重叠的叶子，也不能创建具有相同名称和父节点的不同子类型。

`sysctl_add_oid` 函数创建任意类型的原始 OID 并将其连接到其父节点（如果有）。如果 OID 成功创建，函数返回指向它的指针，否则返回 `NULL`。`sysctl_add_oid` 的许多参数与 [sysctl(9)](sysctl.9.md) 定义的包装宏相同。

`sysctl_move_oid` 函数为现有 OID 重新设置父节点。OID 被分配一个新编号，就像创建时将 `number` 设置为 `OID_AUTO` 一样。

`sysctl_remove_oid` 函数从树中移除动态创建的 OID，并可选地释放其资源。它接受以下参数：

**`oidp`** 指向要移除的动态 OID 的指针。如果 OID 不是动态的，或指针为 `NULL`，函数返回 `EINVAL`。

**`del`** 如果非零，当 OID 的引用计数变为零时，`sysctl_remove_oid` 将尝试释放 OID 的资源。但是，如果 `del` 设置为 0，例程将仅从树中注销 OID，而不释放其资源。当调用者期望稍后回滚（可能部分失败的）多个 OID 的删除时，此行为很有用。

**`recurse`** 如果非零，尝试移除节点及其所有子节点。如果 `recurse` 设置为 0，任何尝试移除包含任何子节点的节点将导致 `ENOTEMPTY` 错误。*警告：谨慎使用递归删除！* 如果使用上下文，通常不需要它。上下文负责跟踪树的用户之间的相互依赖关系。但是，在某些极端情况下，可能需要移除子树的一部分，无论它是如何创建的，以释放其他资源。但请注意，如果其他代码段继续使用已移除的子树，这可能导致系统 [panic(9)](panic.9.md)。

`sysctl_remove_name` 函数查找匹配 `name` 参数的子节点，然后在该节点上调用 `sysctl_remove_oid` 函数，传递 `del` 和 `recurse` 参数。如果具有指定名称的节点不存在，返回 `ENOENT` 错误代码。否则返回 `sysctl_remove_oid` 的错误代码。

在大多数情况下，程序员应使用上下文（如 [sysctl_ctx_init(9)](sysctl_ctx_init.9.md) 中所述）来跟踪已创建的 OID，并稍后以有序方式删除它们。

## 参见

[sysctl(8)](../man8/sysctl.8.md), [sysctl(9)](sysctl.9.md), sysctl_ctx_free(9), [sysctl_ctx_init(9)](sysctl_ctx_init.9.md)

## 历史

这些函数首次出现在 FreeBSD 4.2 中。

## 作者

Andrzej Bialecki <abial@FreeBSD.org>

## 缺陷

在多个代码段之间共享节点会导致有时可能锁定资源的相互依赖关系。例如，如果模块 A 将子树连接到模块 B 创建的 OID，模块 B 将无法删除该 OID。这些问题由 sysctl 上下文正确处理。

树上的许多操作涉及遍历链表。因此，OID 的创建和移除相对昂贵。
