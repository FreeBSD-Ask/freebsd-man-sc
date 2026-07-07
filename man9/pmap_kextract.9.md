# pmap_kextract(9)

`pmap_kextract` — 从内核页表中提取物理地址

## 名称

`pmap_kextract`, `vtophys`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft vm_paddr_t Fo pmap_kextract vm_offset_t va Fc Ft vm_paddr_t Fo vtophys vm_offset_t va Fc`

## 描述

`pmap_kextract` 函数检索与给定内核虚拟地址 `va` 对应的底层物理内存地址。调用者负责确保 `va` 属于内核地址空间中的有效映射。返回的物理地址仅在映射保持稳定时有意义，因此调用者还必须对映射的生命周期有所了解或保证。例如，当 malloc 的对象可能被并发释放时，使用该对象的地址调用 `pmap_kextract` 是无效的。

与 [pmap_extract(9)](pmap_extract.9.md) 不同，`pmap_kextract` 可以从任何上下文中安全地调用；它没有内部锁定或睡眠。

`vtophys` 是 `pmap_kextract` 的别名，行为完全相同。

## 返回值

`pmap_kextract` 函数返回映射到内核虚拟地址 `va` 处的内存的物理地址。

`pmap_kextract` 通常不会失败。但是，如果为 `va` 提供了非法值，则该函数可能返回零、无效的非零值或调用 [panic(9)](panic.9.md)。

## 参见

[pmap(9)](pmap.9.md), [pmap_extract(9)](pmap_extract.9.md)

## 作者

本手册页由 Mina Galić <FreeBSD@igalic.co> 编写，基于 Bruce M Simpson <bms@spc.org> 编写的 [pmap_extract(9)](pmap_extract.9.md) 页面。
