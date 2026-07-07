# vm_map_init(9)

`vm_map_init` — 为进程零初始化 vm_map 结构

## 名称

`vm_map_init`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

void
vm_map_init(vm_map_t map, vm_offset_t min, vm_offset_t max)
```

## 描述

`vm_map_init` 函数通过将系统映射 `map` 的上下地址边界分别设置为 `max` 和 `min` 来初始化该映射。

它还初始化系统映射互斥锁。

## 实现说明

此例程仅供内部使用。它在系统早期初始化期间被调用。

## 参见

[vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
