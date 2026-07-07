# pmap_copy(9)

`pmap_copy` — 复制物理内存页面

## 名称

`pmap_copy`, `pmap_copy_page`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft void Fo pmap_copy pmap_t dst_pmap pmap_t src_pmap vm_offset_t dst_addr vm_size_t len vm_offset_t src_addr Fc Ft void Fn pmap_copy_page vm_page_t src vm_page_t dst`

## 描述

`pmap_copy` 函数将源物理映射 `src_pmap` 中由 `src_addr` 和 `len` 指定的范围复制到目标物理映射 `dst_pmap` 中的地址 `dst_addr` 处。

`pmap_copy_page` 函数通过将页面映射到内核虚拟地址空间（KVA）并使用 `bcopy` 复制页面，将物理页面 `src` 复制到物理页面 `dst`。

## 实现说明

`pmap_copy` 例程仅是建议性的，无需做任何事。实际实现它可能严重降低系统性能。

`pmap_copy_page` 例程仅对单个页面进行操作。

## 参见

bcopy(3), [pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
