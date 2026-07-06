# pmap_protect.9

`pmap_protect` — 设置物理页面保护

## 名称

`pmap_protect`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft void Fo pmap_protect pmap_t pmap vm_offset_t sva vm_offset_t eva vm_prot_t prot Fc`

## 描述

`pmap_protect` 函数将物理映射 `pmap` 中虚拟地址 `sva` 和 `eva` 之间所有物理页面的权限设置为 `prot`。

## 参见

[pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
