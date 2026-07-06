# pmap_is_prefaultable.9

`pmap_is_prefaultable` — 确定页面是否可以预故障

## 名称

`pmap_is_prefaultable`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft bool Fn pmap_is_prefaultable pmap_t pmap vm_offset_t va`

## 描述

`pmap_is_prefaultable` 函数提供了一种确定物理映射 `pmap` 中位于虚拟地址 `va` 处的页面是否可以预故障到主内存的方法。

这是一个由 [vm_fault_prefault(9)](vm_fault_prefault.9.md) 调用的辅助函数。

## 参见

[pmap(9)](pmap.9.md), [vm_fault_prefault(9)](vm_fault_prefault.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
