# sysctl_ctx_init(9)

`sysctl_ctx_init` — 用于管理动态创建 sysctl OID 的 sysctl 上下文

## 名称

`sysctl_ctx_init`, `sysctl_ctx_free`, `sysctl_ctx_entry_add`, `sysctl_ctx_entry_find`, `sysctl_ctx_entry_del`

## 概要

```c
#include <sys/types.h>
#include <sys/sysctl.h>

int
sysctl_ctx_init(struct sysctl_ctx_list *clist)

int
sysctl_ctx_free(struct sysctl_ctx_list *clist)

struct sysctl_ctx_entry *
sysctl_ctx_entry_add(struct sysctl_ctx_list *clist, struct sysctl_oid *oidp)

struct sysctl_ctx_entry *
sysctl_ctx_entry_find(struct sysctl_ctx_list *clist, struct sysctl_oid *oidp)

int
sysctl_ctx_entry_del(struct sysctl_ctx_list *clist, struct sysctl_oid *oidp)
```

## 描述

这些函数提供了管理动态创建 OID 的接口。sysctl 上下文负责跟踪已创建的 OID，以及在需要时正确移除它们。它为 OID 移除操作添加了简单的事务性方面；即，如果移除操作在中途失败，可以将 sysctl 树回滚到之前的状态。

`sysctl_ctx_init` 函数初始化 sysctl 上下文。`clist` 参数必须指向已分配的变量。上下文在使用前*必须*初始化。一旦初始化，指向上下文的指针可以作为参数传递给所有 `SYSCTL_ADD_*` 宏（参见 [sysctl_add_oid(9)](sysctl_add_oid.9.md)），它将用指向新创建 OID 的条目更新。

在内部，上下文表示为 [queue(3)](../man3/queue.3.md) TAILQ 链表。该列表由 `struct sysctl_ctx_entry` 条目组成：

```c
struct sysctl_ctx_entry {
	struct sysctl_oid *entry;
	TAILQ_ENTRY(sysctl_ctx_entry) link;
};
TAILQ_HEAD(sysctl_ctx_list, sysctl_ctx_entry);
```

每个上下文条目指向它管理的一个动态 OID。新创建的 OID 始终插入列表的前面。

`sysctl_ctx_free` 函数移除上下文及其管理的关联 OID。如果函数成功完成，所有管理的 OID 已被注销（从树中移除）并释放，连同其所有分配的内存，上下文的条目也已被释放。

移除操作分两步执行。首先，对于每个上下文条目，执行 sysctl_remove_oid(9) 函数，参数 `del` 设置为 0，这会抑制资源释放。如果此步骤中没有错误，`sysctl_ctx_free` 继续下一步。如果第一步失败，与上下文关联的所有已注销 OID 将重新注册。

*注意：* 在大多数情况下，程序员在创建 OID 时将 `OID_AUTO` 指定为 OID 编号。但是，在树中注册 OID 期间，此编号更改为大于或等于 `CTL_AUTO_START` 的第一个可用编号。如果上下文删除的第一步失败，OID 的重新注册不会更改已分配的 OID 编号（与 OID_AUTO 不同）。这确保重新注册的条目维护其在树中的原始位置。

第二步实际执行动态 OID 的删除。sysctl_remove_oid(9) 从开头遍历上下文列表（即最新的条目）。*重要：* 这次，函数不仅从树中删除 OID，还释放其内存（前提是 oid_refcnt == 0），以及所有上下文条目的内存。

`sysctl_ctx_entry_add` 函数允许将现有动态 OID 添加到上下文。

`sysctl_ctx_entry_del` 函数从上下文中移除条目。*重要：* 在这种情况下，仅释放相应的 `struct sysctl_ctx_entry`，但 `oidp` 指针保持不变。此后，程序员负责管理分配给此 OID 的资源。

`sysctl_ctx_entry_find` 函数在上下文列表中搜索给定的 `oidp`，返回指向找到的 `struct sysctl_ctx_entry` 的指针，或 `NULL`。

## 实例

以下是如何创建新的顶级类别以及如何将另一个子树连接到现有静态节点的示例。此示例使用上下文来跟踪 OID。

```sh
#include <sys/sysctl.h>
 ...
static struct sysctl_ctx_list clist;
static struct sysctl_oid *oidp;
static int a_int;
static const char *string = "dynamic sysctl";
 ...
sysctl_ctx_init(&clist);
oidp = SYSCTL_ADD_ROOT_NODE(&clist,
	OID_AUTO, "newtree", CTLFLAG_RW, 0, "new top level tree");
oidp = SYSCTL_ADD_INT(&clist, SYSCTL_CHILDREN(oidp),
	OID_AUTO, "newint", CTLFLAG_RW, &a_int, 0, "new int leaf");
 ...
oidp = SYSCTL_ADD_NODE(&clist, SYSCTL_STATIC_CHILDREN(_debug),
	OID_AUTO, "newtree", CTLFLAG_RW, 0, "new tree under debug");
oidp = SYSCTL_ADD_STRING(&clist, SYSCTL_CHILDREN(oidp),
	OID_AUTO, "newstring", CTLFLAG_RD, string, 0, "new string leaf");
 ...
/* 现在我们可以释放 OID */
if (sysctl_ctx_free(&clist)) {
	printf("can't free this context - other OIDs depend on it");
	return (ENOTEMPTY);
} else {
	printf("Success!n");
	return (0);
}
```

此示例创建以下子树：

```sh
debug.newtree.newstring
newtree.newint
```

注意，两个树都通过一次 `sysctl_ctx_free` 调用被移除并释放资源，该调用从释放最新条目（叶子）开始，然后继续释放较旧的条目（在此示例中为节点）。

## 参见

[queue(3)](../man3/queue.3.md), [sysctl(8)](../man8/sysctl.8.md), [sysctl(9)](sysctl.9.md), [sysctl_add_oid(9)](sysctl_add_oid.9.md), sysctl_remove_oid(9)

## 历史

这些函数首次出现在 FreeBSD 4.2 中。

## 作者

Andrzej Bialecki <abial@FreeBSD.org>

## 缺陷

当前的移除算法有些繁重。在最坏的情况下，所有 OID 需要被注销、重新注册，然后再注销和删除。但是，该算法确实保证移除操作的事务属性。

上下文上的所有操作都涉及链表遍历。因此，条目的创建和移除相对昂贵。
