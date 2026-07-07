# vm_map_remove(9)

`vm_map_remove` — 从映射中移除虚拟地址范围

## 名称

`vm_map_remove`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_remove(vm_map_t map, vm_offset_t start, vm_offset_t end)
```

## 描述

`vm_map_remove` 函数从目标 `map` 中移除由 `start` 和 `end` 界定的给定地址范围。

## 实现说明

这是 [vm_map_delete(9)](vm_map_delete.9.md) 的导出形式，可由 VM 子系统的消费者调用。

该函数调用 [vm_map_lock(9)](vm_map_lock.9.md) 在函数调用期间持有 `map` 上的锁。

## 返回值

`vm_map_remove` 始终返回 `KERN_SUCCESS`。

## 参见

[vm_map(9)](vm_map.9.md), [vm_map_delete(9)](vm_map_delete.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
