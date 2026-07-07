# pmap_growkernel(9)

`pmap_growkernel` — 扩展内核虚拟地址（KVA）空间

## 名称

`pmap_growkernel`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft void Fn pmap_growkernel vm_offset_t addr`

## 描述

`pmap_growkernel` 函数将内核虚拟地址空间扩展到虚拟地址 `addr`。

如果需要，它会分配更多页表项。

## 参见

[pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
