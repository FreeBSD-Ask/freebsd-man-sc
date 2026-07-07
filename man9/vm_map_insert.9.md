# vm_map_insert(9)

`vm_map_insert` — 将一个对象插入到映射中

## 名称

`vm_map_insert`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_insert(vm_map_t map, vm_object_t object, vm_ooffset_t offset,
    vm_offset_t start, vm_offset_t end, vm_prot_t prot,
    vm_prot_t max, int cow)
```

## 描述

`vm_map_insert` 函数将整个 vm_object `object` 的映射插入到目标映射 `map` 中。

`offset` 参数指定 `object` 中开始映射的偏移量。对象的大小应与指定的地址范围匹配。

`start` 和 `end` 参数指定 `map` 地址空间中映射对象窗口的边界。

`cow` 参数指定应传播到新条目的标志，例如用于指示这是一个写时复制（copy-on-write）映射。

## 实现说明

此函数通过调用内部函数 `vm_map_entry_create` 隐式创建一个新的 `vm_map_entry`。

## 返回值

`vm_map_insert` 函数在映射可以成功创建时返回 `KERN_SUCCESS`。

否则，如果找不到范围的起始处，将返回 `KERN_INVALID_ADDRESS`；如果该范围是现有条目的一部分或与映射的末尾重叠，则返回 `KERN_NO_SPACE`。

## 参见

[vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
