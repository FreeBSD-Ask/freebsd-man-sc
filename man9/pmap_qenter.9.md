# pmap_qenter.9

`pmap_qenter` — 管理临时内核空间映射

## 名称

`pmap_qenter`, `pmap_qremove`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft void Fn pmap_qenter vm_offset_t sva vm_page_t *m int count Ft void Fn pmap_qremove vm_offset_t sva int count`

## 描述

`pmap_qenter` 函数接受一个包含 `count` 个指向已锁定页面 `*m` 的指针的线性数组，并将这些页面中的每一个从地址 `sva` 开始输入到内核虚拟地址（KVA）空间。如果可能，页面映射为不可执行。（例如，非 PAE i386 没有能力将页面映射为不可执行。）

`pmap_qremove` 函数从内核虚拟地址空间中拆除映射，从 `sva` 开始，共 `count` 个页面。

## 实现说明

`pmap_qenter` 函数用于不需要页面修改或引用计数的临时映射。旧映射直接被覆盖。页面*必须*被锁定到物理内存中。

相应的 `pmap_qremove` 函数用于删除此类临时映射。

## 参见

[pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
