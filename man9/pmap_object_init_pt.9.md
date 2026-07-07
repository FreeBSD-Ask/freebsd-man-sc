# pmap_object_init_pt(9)

`pmap_object_init_pt` — 为 VM 对象初始化页表

## 名称

`pmap_object_init_pt`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft void Fo pmap_object_init_pt pmap_t pmap vm_offset_t addr vm_object_t object vm_pindex_t pindex vm_size_t size int limit Fc`

## 描述

`pmap_object_init_pt` 函数将页表项预加载到指定的物理映射 `pmap` 中，用于给定 `object` 在虚拟地址 `addr` 处、`size` 字节范围内，从对象内的页索引 `pindex` 开始。创建映射时会注意映射位 `limit`。

## 实现说明

此函数并非架构的 [pmap(9)](pmap.9.md) 实现严格要求的，但如果实现，它确实提供了性能优势。

它旨在消除进程启动时以及调用 mmap(2) 之后立即产生的软故障风暴。

## 参见

[pmap(9)](pmap.9.md), [vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
