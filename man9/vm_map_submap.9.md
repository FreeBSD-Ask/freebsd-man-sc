# vm\_map\_submap.9

`vm_map_submap` — 创建从属映射

## 名称

`vm_map_submap`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_submap(vm_map_t map, vm_offset_t start, vm_offset_t end,
    vm_map_t submap)
```

## 描述

`vm_map_submap` 函数将映射 `map` 中由 `start` 和 `end` 界定的范围标记为由从属映射 `sub_map` 处理。

通常由内核内存分配器调用。

## 实现说明

此函数仅供内部使用。

两个映射都必须存在。该范围必须先前已通过 [vm_map_find(9)](vm_map_find.9.md) 创建。

在调用此函数之前，不得对此范围执行其他操作。在调用此函数之后，只能在此范围内执行 `vm_fault` 操作。

要移除子映射，必须首先从父 `map` 中移除该范围，然后销毁 `sub_map`。不建议使用此过程。

## 返回值

`vm_map_submap` 函数成功时返回 `KERN_SUCCESS`。

否则，如果调用者请求了写时复制标志，或为子映射指定的范围超出父映射的范围，或指定了 `NULL` 支持对象，则返回 `KERN_INVALID_ARGUMENT`。

## 参见

[vm_map(9)](vm_map.9.md), [vm_map_find(9)](vm_map_find.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
