# vm_map_lookup(9)

`vm_map_lookup`, `vm_map_lookup_done` — 查找支持给定虚拟区域的 vm_object

## 名称

`vm_map_lookup`, `vm_map_lookup_done`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_lookup(vm_map_t *var_map, vm_offset_t vaddr, vm_prot_t fault_type,
    vm_map_entry_t *out_entry, vm_object_t *object, vm_pindex_t *pindex,
    vm_prot_t *out_prot, boolean_t *wired)

void
vm_map_lookup_done(vm_map_t map, vm_map_entry_t entry)
```

## 描述

`vm_map_lookup` 函数尝试在映射 `var_map` 中，针对给定虚拟地址 `vaddr`，假定发生了 `fault_type` 类型的页错误，查找对应的 `vm_object`、页索引和保护信息。

返回值保证有效，直到调用 `vm_map_lookup_done` 释放锁为止。

## 实现说明

`vm_map_lookup` 函数获取 `*var_map` 上的读锁，但不释放它。调用者应调用 `vm_map_lookup_done` 来释放此锁。

## 返回值

`vm_map_lookup` 函数返回 `KERN_SUCCESS`，并为假设的页错误适当地设置 `*object`、`*pindex`、`*out_prot` 和 `*out_entry` 参数。

## 参见

[vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
