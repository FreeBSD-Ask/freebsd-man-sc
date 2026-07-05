# pmap\_remove.9

`pmap_remove` — 从物理映射中移除页面

## 名称

`pmap_remove`, `pmap_remove_all`, `pmap_remove_pages`

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
pmap_remove(pmap_t pmap, vm_offset_t sva, vm_offset_t eva)

void
pmap_remove_all(vm_page_t m)

void
pmap_remove_pages(pmap_t pmap)
```

## 描述

`pmap_remove` 函数从物理映射 `pmap` 中移除介于 `sva` 和 `eva` 之间的地址范围。如果 `eva` 小于 `sva`，则结果未定义。假定 `sva` 和 `eva` 均为页对齐地址。

`pmap_remove_all` 从所有包含物理页 `m` 的物理映射中移除该物理页，并将修改位反映回相应的 pager。

`pmap_remove_pages` 函数从物理映射 `pmap` 中移除所有用户页面。该函数在进程退出时调用，以比调用 `pmap_remove` 更快地回收其地址空间。

## 参见

[pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
