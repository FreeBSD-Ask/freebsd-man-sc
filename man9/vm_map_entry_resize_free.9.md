# vm_map_entry_resize_free(9)

`vm_map_entry_resize_free` — vm 映射空闲空间算法

## 名称

`vm_map_entry_resize_free`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/vm_map.h>`

`void vm_map_entry_resize_free(vm_map_t map, vm_map_entry_t entry)`

## 描述

本手册页描述 VM 映射空闲空间算法中使用的 `vm_map_entry` 字段、如何维护这些变量的一致性，以及 `vm_map_entry_resize_free()` 函数。

VM 映射条目既组织为双向链表（`prev` 和 `next` 指针），也组织为二叉搜索树（`left` 和 `right` 指针）。搜索树组织为 Sleator 和 Tarjan 伸展树，也称为"自调整树"。

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
        ...
};
```

空闲空间算法向 `struct vm_map_entry` 添加了两个字段：`adj_free` 和 `max_free`。`adj_free` 字段是紧邻映射条目之后（更高地址）的空闲地址空间量。此字段在映射头中不使用。注意，`adj_free` 依赖于链表而非伸展树，`adj_free` 可计算为：

```c
entry->adj_free = (entry->next == &map->header ?
    map->max_offset : entry->next->start) - entry->end;
```

`max_free` 字段是条目子树中最大连续空闲空间量。注意，`max_free` 依赖于伸展树而非链表，`max_free` 通过取其自身 `adj_free` 及其左右子树的 `max_free` 的最大值来计算。同样，`max_free` 在映射头中不使用。

这些字段允许 `vm_map_findspace()` 的 O(log n) 实现。使用 `max_free`，可以立即测试整个子树中是否有足够大的空闲区域。这使得可以在一次遍历树的过程中找到给定大小的首次适配空闲区域，因此使用伸展树的摊还 O(log n)。

当空闲区域改变大小时，必须更新前一映射条目中的 `adj_free` 和 `max_free` 并沿树向上传播 `max_free`。这在插入和删除条目时由 `vm_map_entry_link()` 和 `vm_map_entry_unlink()` 处理。注意，`vm_map_entry_link()` 同时更新新条目和前一条目，`vm_map_entry_unlink()` 更新前一条目。还应注意，`max_free` 实际上并不沿树向上传播。相反，该条目首先被伸展到根，然后在那里进行更改。这是伸展树中的常见技术，也是映射条目链接和取消链接到树中的方式。

`vm_map_entry_resize_free()` 函数更新给定 `entry` 中的空闲空间变量并将这些值沿树向上传播。每当就地调整映射条目大小（即通过修改其 `start` 或 `end` 值）时，应调用此函数。注意，如果更改 `end`，则应调整该条目；如果更改 `start`，则应调整前一条目。调用此函数前必须锁定映射，同样，传播 `max_free` 通过将该条目伸展到根来执行。

## 实例

考虑使用 `vm_map_insert()` 添加映射条目。

```c
ret = vm_map_insert(map, object, offset, start, end, prot,
    max_prot, cow);
```

在此情况下，无需进一步操作来维护空闲空间变量的一致性。`vm_map_insert()` 函数调用 `vm_map_entry_link()`，后者同时更新新条目和前一条件。对于 `vm_map_delete()` 以及直接调用 `vm_map_entry_link()` 或 `vm_map_entry_unlink()` 也是如此。

现在考虑在不调用 `vm_map_entry_link()` 或 `vm_map_entry_unlink()` 的情况下就地调整条目大小。

```c
entry->start = new_start;
if (entry->prev != &map->header)
        vm_map_entry_resize_free(map, entry->prev);
```

在此情况下，重置 `start` 会更改前一条目之后的空闲空间量，因此使用 `vm_map_entry_resize_free()` 更新前一条目。

最后，假设我们更改条目的 `end` 地址。

```c
entry->end = new_end;
vm_map_entry_resize_free(map, entry);
```

此处，我们在条目本身上调用 `vm_map_entry_resize_free()`。

## 参见

[vm_map(9)](vm_map.9.md), [vm_map_findspace(9)](vm_map_findspace.9.md)

> Daniel D. Sleator, Robert E. Tarjan, "Self-Adjusting Binary Search Trees", *JACM*, vol. 32(3), pp. pp. 652-686, July 1985.

## 历史

伸展树添加到 FreeBSD 5.0 的 VM 映射中，基于树的 O(log n) 空闲空间算法添加到 FreeBSD 5.3 中。

## 作者

基于树的空闲空间算法及本手册页由 Mark W. Krentel <krentel@dreamscape.com> 编写。
