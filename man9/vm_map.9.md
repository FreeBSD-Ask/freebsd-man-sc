# vm_map(9)

`vm_map` — 虚拟内存子系统的虚拟地址空间部分

## 名称

`vm_map`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/vm_map.h>`

## 描述

`vm_map` 子系统用于管理虚拟地址空间。本节描述代码中使用的主要数据结构。

`struct vm_map` 是地址空间的通用表示。此地址空间可能属于用户进程或内核。内核实际上使用多个映射，这些映射作为从属映射维护，使用 [vm_map_submap(9)](vm_map_submap.9.md) 函数创建。

```c
struct vm_map {
	struct vm_map_entry header;
	union {
	        struct sx lock;
		struct mtx system_mtx;
	};
        int nentries;
        vm_size_t size;
        u_int timestamp;
        u_int flags;
        vm_map_entry_t root;
        pmap_t pmap;
        int busy;
};
```

`struct vm_map` 的字段如下：

**`header`** `struct vm_map_entry` 对象的循环双向链表的头部节点。每个对象定义此映射地址空间内的特定区域。

**`lock`** 用于串行化对结构的访问。

**`system_mtx`** 如果映射是系统映射则使用的互斥锁。

**`nentries`** 循环映射条目列表中正在使用的成员计数。

**`size`** 指定虚拟地址空间的大小。

**`timestamp`** 用于确定映射自上次访问以来是否已更改。

**`flags`** 映射标志，如下所述。

**`root`** 用于快速查找映射条目的二叉搜索树的根节点。

**`pmap`** 指向与此虚拟映射关联的底层物理映射的指针。

**`busy`** 映射忙碌计数器，防止 fork。

可能的映射标志：

**`MAP_WIREFUTURE`** 固定此映射中的所有未来页面。

**`MAP_BUSY_WAKEUP`** 有等待映射忙碌状态的等待者。

**`MAP_NEEDS_WAKEUP`** 指示有线程正在等待映射内的分配。仅由系统映射使用。

**`MAP_SYSTEM_MAP`** 如果设置，表示该映射是系统映射；否则属于用户进程。

以下标志可以传递给 [vm_map_find(9)](vm_map_find.9.md) 和 [vm_map_insert(9)](vm_map_insert.9.md) 以指定映射内区域的写时复制属性：

**`MAP_COPY_ON_WRITE`** 映射是写时复制。

**`MAP_NOFAULT`** 映射不应产生页面错误。

**`MAP_PREFAULT`** 映射应预错误到物理内存中。

**`MAP_PREFAULT_PARTIAL`** 映射应部分预错误到物理内存中。

**`MAP_DISABLE_SYNCER`** 不定期刷新脏页；仅在绝对必要时刷新。

**`MAP_DISABLE_COREDUMP`** 不在核心转储中包含此映射。

**`MAP_PREFAULT_MADVISE`** 指定请求来自调用 madvise(2) 的用户进程。

**`MAP_ACC_CHARGED`** 区域已通过某种方式向请求者计费。

**`MAP_ACC_NO_CHARGE`** 不对分配的区域计费。

`struct vm_map_entry` 是区域的通用表示。每个条目管理的区域与 `union vm_map_object` 关联，如下所述。

```c
struct vm_map_entry {
        struct vm_map_entry *prev;
        struct vm_map_entry *next;
        struct vm_map_entry *left;
        struct vm_map_entry *right;
        vm_offset_t start;
        vm_offset_t end;
        vm_offset_t avail_ssize;
        vm_size_t adj_free;
        vm_size_t max_free;
        union vm_map_object object;
        vm_ooffset_t offset;
        vm_eflags_t eflags;
        /* 仅在任务映射中： */
        vm_prot_t protection;
        vm_prot_t max_protection;
        vm_inherit_t inheritance;
        int wired_count;
        vm_pindex_t lastr;
};
```

`struct vm_map_entry` 的字段如下：

**`prev`** 指向双向循环列表中前一个节点的指针。

**`next`** 指向双向循环列表中下一个节点的指针。

**`left`** 指向二叉搜索树中左节点的指针。

**`right`** 指向二叉搜索树中右节点的指针。

**`start`** 此条目区域的下地址边界。

**`end`** 此条目区域的上地址边界。

**`avail_ssize`** 如果条目用于进程栈，指定条目可以增长多少。

**`adj_free`** 紧邻此映射条目之后（更高地址）的空闲、未映射地址空间量。

**`max_free`** 此映射条目子树中最大连续空闲空间量。

**`object`** 指向与此条目关联的 `struct vm_map_object` 的指针。

**`offset`** 从 `start` 开始映射的 `object` 内的偏移量。

**`eflags`** 应用于此条目的标志，如下所述。

以下五个成员仅对构成用户进程地址空间一部分的条目有效：

**`protection`** 应用于此区域的内存保护位。

**`max_protection`** 可以实际应用于此区域的内存保护位掩码。

**`inheritance`** 包含指定在 fork 处理期间应如何处理此条目的标志。

**`wired_count`** 此条目已固定到物理内存的次数计数。

**`lastr`** 包含导致页面错误的最后一次读取的地址。

以下标志可以通过在 `eflags` 成员中作为掩码指定来应用于每个条目：

**`MAP_ENTRY_NOSYNC`** 系统不应定期刷新与此映射关联的数据，仅在需要时刷新。

**`MAP_ENTRY_IS_SUB_MAP`** 如果设置，则 `object` 成员指定一个从属映射。

**`MAP_ENTRY_COW`** 指示这是写时复制区域。

**`MAP_ENTRY_NEEDS_COPY`** 指示写时复制区域需要复制。

**`MAP_ENTRY_NOFAULT`** 指定在此区域内的访问不应导致页面错误。如果在此区域内发生页面错误，系统将 panic。

**`MAP_ENTRY_USER_WIRED`** 指示此区域是代表用户进程固定的。

**`MAP_ENTRY_BEHAV_NORMAL`** 系统应为此区域使用默认分页行为。

**`MAP_ENTRY_BEHAV_SEQUENTIAL`** 系统应降低此区域内每个页面之前页面在错误调入时的优先级。

**`MAP_ENTRY_BEHAV_RANDOM`** 提示此区域内的页面将被随机访问，预取可能不利。

**`MAP_ENTRY_IN_TRANSITION`** 指示条目的固定或解除固定正在进行，其他内核线程不应尝试修改结构中的字段。

**`MAP_ENTRY_NEEDS_WAKEUP`** 指示有内核线程正在等待此区域变为可用。

**`MAP_ENTRY_NOCOREDUMP`** 该区域不应包含在核心转储中。

`inheritance` 成员的类型为 `vm_inherit_t`。它管理 fork 处理期间映射条目的继承行为。以下是为 `vm_inherit_t` 定义的值：

**`VM_INHERIT_SHARE`** 与条目关联的对象应被克隆并与新映射共享。如有必要，将创建新的 `struct vm_object`。

**`VM_INHERIT_COPY`** 与条目关联的对象应复制到新映射。

**`VM_INHERIT_NONE`** 条目不应复制到新映射。

**`VM_INHERIT_DEFAULT`** 指定默认行为 `VM_INHERIT_COPY`。

`union vm_map_object` 用于指定 `struct vm_map_entry` 关联的结构。

`union vm_map_object` 的字段如下：

```c
union vm_map_object {
        struct vm_object *vm_object;
        struct vm_map *sub_map;
};
```

通常，`sub_map` 成员仅由系统映射使用，以指示内存范围由从属系统映射管理。在用户进程映射中，每个 `struct vm_map_entry` 由 `struct vm_object` 支持。

## 参见

[pmap(9)](pmap.9.md), [vm_map_check_protection(9)](vm_map_check_protection.9.md), [vm_map_delete(9)](vm_map_delete.9.md), [vm_map_entry_resize_free(9)](vm_map_entry_resize_free.9.md), [vm_map_find(9)](vm_map_find.9.md), [vm_map_findspace(9)](vm_map_findspace.9.md), [vm_map_inherit(9)](vm_map_inherit.9.md), [vm_map_init(9)](vm_map_init.9.md), [vm_map_insert(9)](vm_map_insert.9.md), [vm_map_lock(9)](vm_map_lock.9.md), [vm_map_lookup(9)](vm_map_lookup.9.md), [vm_map_madvise(9)](vm_map_madvise.9.md), [vm_map_max(9)](vm_map_max.9.md), vm_map_min(9), vm_map_pmap(9), [vm_map_protect(9)](vm_map_protect.9.md), [vm_map_remove(9)](vm_map_remove.9.md), [vm_map_stack(9)](vm_map_stack.9.md), [vm_map_submap(9)](vm_map_submap.9.md), [vm_map_sync(9)](vm_map_sync.9.md), [vm_map_wire(9)](vm_map_wire.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
