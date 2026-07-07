# vm_map_max(9)

`vm_map_max`, `vm_map_min`, `vm_map_pmap` — 返回映射属性

## 名称

`vm_map_max`, `vm_map_min`, `vm_map_pmap`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

vm_offset_t
vm_map_max(vm_map_t map)

vm_offset_t
vm_map_min(vm_map_t map)

pmap_t
vm_map_pmap(vm_map_t map)
```

## 描述

`vm_map_max` 函数返回映射 `map` 的上地址边界。

`vm_map_min` 函数返回映射 `map` 的下地址边界。

`vm_map_pmap` 函数返回与虚拟映射 `map` 关联的物理映射的指针。

## 参见

[pmap(9)](pmap.9.md), [vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
