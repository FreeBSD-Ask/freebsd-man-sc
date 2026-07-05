# pmap\_unwire.9

`pmap_unwire` — 解除一组虚拟页面的锁定属性

## 名称

`pmap_unwire`

## 概要

```c
#include <sys/param.h>
```

```c
#include <vm/vm.h>
```

```c
#include <vm/pmap.h>
```

```c
void
pmap_unwire(pmap_t pmap, vm_offset_t start, vm_offset_t end)
```

## 描述

`pmap_unwire` 函数移除物理映射 `pmap` 中从 `start` 到 `end` 的虚拟地址范围内每个虚拟到物理页面映射的锁定属性。该范围内的每个有效映射都必须已设置锁定属性。无效映射将被忽略，因为它们无法设置锁定属性。

## 注释

只有函数 [pmap_enter(9)](pmap_enter.9.md) 可用于设置虚拟到物理页面映射的锁定属性。

## 参见

[pmap(9)](pmap.9.md), [pmap_enter(9)](pmap_enter.9.md), [pmap_wired_count(9)](pmap_resident_count.9.md)

## 作者

本手册页由 Alan L. Cox <alc@rice.edu> 编写。
