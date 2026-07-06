# pmap_init.9

`pmap_init` — 初始化 pmap 子系统

## 名称

`pmap_init`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft void Fn pmap_init void`

## 描述

`pmap_init` 函数初始化 [pmap(9)](pmap.9.md) 子系统。它在系统初始化期间由 `vm_mem_init` 调用，以初始化 `pmap_init` 系统在物理和虚拟内存之间进行映射所需的任何结构。

## 参见

[pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
