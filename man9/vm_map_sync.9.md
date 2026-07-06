# vm\_map\_sync.9

`vm_map_sync` — 将脏页推送到其 pager

## 名称

`vm_map_sync`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_sync(vm_map_t map, vm_offset_t start, vm_offset_t end,
    boolean_t syncio, boolean_t invalidate)
```

## 描述

`vm_map_sync` 函数强制将 `map` 中 `start` 到 `end` 范围内的所有脏缓存页推送到其底层 pager。

如果 `syncio` 为 `TRUE`，则同步写入脏页。

如果 `invalidate` 为 `TRUE`，则还会释放所有缓存页。

提供的范围必须是连续的，不得包含空洞。提供的范围不得包含任何子映射条目。

## 返回值

`vm_map_sync` 函数成功时返回 `KERN_SUCCESS`。

否则，如果函数遇到子映射条目，将返回 `KERN_INVALID_ADDRESS`；如果函数在提供的区域中遇到空洞，或找不到给定起始地址的条目，则返回 `KERN_INVALID_ARGUMENT`。

## 参见

[vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
