# vm_map_find(9)

`vm_map_find` — 在映射中查找空闲区域，并可选地映射一个 vm_object

## 名称

`vm_map_find`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_find(vm_map_t map, vm_object_t object, vm_ooffset_t offset,
    vm_offset_t *addr, vm_size_t length, vm_offset_t max_addr,
    int find_space, vm_prot_t prot, vm_prot_t max, int cow)
```

## 描述

`vm_map_find` 函数尝试在目标 `map` 中查找具有给定 `length` 的空闲区域。如果找到空闲区域，`vm_map_find` 通过调用 [vm_map_insert(9)](vm_map_insert.9.md) 创建 `object` 的映射。

参数 `offset`、`prot`、`max` 和 `cow` 在创建映射时（仅当找到空闲区域时）原封不动地传递给 [vm_map_insert(9)](vm_map_insert.9.md)。

如果 `object` 非 `NULL`，调用者在调用此函数之前必须增加该对象的引用计数，以计入新的条目。

如果 `max_addr` 非零，它指定映射的上界。仅当能找到完全位于 `max_addr` 之下的空闲区域时，映射才会成功。

`find_space` 参数指定在搜索所请求长度的空闲区域时要使用的策略。对于除 `VMFS_NO_SPACE` 外的所有值，将调用 [vm_map_findspace(9)](vm_map_findspace.9.md) 来定位起始地址大于或等于 `*addr` 的所请求长度的空闲区域。支持以下策略：

**`VMFS_NO_SPACE`** 仅当在给定地址 `*addr` 处存在所请求长度的空闲区域时，映射才会成功。

**`VMFS_ANY_SPACE`** 只要存在空闲区域，映射就会成功。

**`VMFS_SUPER_SPACE`** 只要存在起始地址位于超级页边界上的空闲区域，映射就会成功。如果 `object` 非 `NULL` 且已由超级页支持，则映射将需要相对于现有超级页对齐的空闲区域，而不是起始地址位于超级页边界上的空闲区域。

**`VMFS_OPTIMAL_SPACE`** 只要存在空闲区域，映射就会成功。但是，如果 `object` 非 `NULL` 且已由超级页支持，此策略将尝试查找到相对于现有超级页对齐的空闲区域。

**`VMFS_ALIGNED_SPACE`** (`n`) 只要存在在 2^`n` 边界上对齐的空闲区域，映射就会成功。

## 实现说明

此函数通过调用 [vm_map_lock(9)](vm_map_lock.9.md) 获取 `map` 上的锁，并持有该锁直到函数返回。

空闲区域的搜索定义为从地址 `addr` 起的首次适配（first-fit）。

## 返回值

`vm_map_find` 函数在映射成功创建时返回 `KERN_SUCCESS`。如果找不到空间，或 `find_space` 为 `VMFS_NO_SPACE` 且给定地址 `addr` 已被映射，则返回 `KERN_NO_SPACE`。如果发现的范围无效，则返回 `KERN_INVALID_ADDRESS`。

## 参见

[vm_map(9)](vm_map.9.md), [vm_map_findspace(9)](vm_map_findspace.9.md), [vm_map_insert(9)](vm_map_insert.9.md), [vm_map_lock(9)](vm_map_lock.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
