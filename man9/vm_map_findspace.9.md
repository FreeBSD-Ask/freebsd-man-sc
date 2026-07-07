# vm_map_findspace(9)

`vm_map_findspace` — 在映射中查找空闲区域

## 名称

`vm_map_findspace`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_findspace(vm_map_t map, vm_offset_t start, vm_size_t length,
    vm_offset_t *addr)
```

## 描述

`vm_map_findspace` 函数尝试在 `map` 中为大小为 `length` 的对象在地址 `addr` 处查找具有足够空间的区域。

## 实现说明

调用者在调用此函数之前，有责任使用 [vm_map_lock(9)](vm_map_lock.9.md) 获取 `map` 上的锁。

此例程可以调用 [pmap_growkernel(9)](pmap_growkernel.9.md) 来扩展内核地址空间，但仅当映射在内核地址空间内创建，且 `kernel_map` 中剩余空间不足时才会如此。

## 返回值

`vm_map_findspace` 函数成功时返回值 0，`*addr` 将包含所找到区域中的第一个虚拟地址；否则返回值 1。

## 参见

[pmap_growkernel(9)](pmap_growkernel.9.md), [vm_map(9)](vm_map.9.md), [vm_map_entry_resize_free(9)](vm_map_entry_resize_free.9.md), [vm_map_lock(9)](vm_map_lock.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
