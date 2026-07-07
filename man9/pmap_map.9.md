# pmap_map(9)

`pmap_map` — 将物理内存范围映射到内核虚拟地址（KVA）空间

## 名称

`pmap_map`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft vm_offset_t Fo pmap_map vm_offset_t *virt vm_paddr_t start vm_paddr_t end int prot Fc`

## 描述

`pmap_map` 函数将一系列物理地址从 `start` 到 `end` 映射到内核虚拟地址（KVA）空间，保护位为 `prot`。

在 `*virt` 中传递的值被视为映射开始的虚拟地址的提示。

## 实现说明

`prot` 参数目前被机器相关实现忽略。

可以支持物理到虚拟区域直接映射的架构可以返回该区域内的适当地址，而保持 `*virt` 不变。

## 返回值

如果映射成功创建，`pmap_map` 函数返回映射开始的虚拟地址；`*virt` 也将更新为映射区域之后的第一个可用地址。

如果函数不成功，则返回 `NULL`。

## 参见

[pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
