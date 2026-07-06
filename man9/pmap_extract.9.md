# pmap_extract.9

`pmap_extract` — 将虚拟地址映射到物理页面

## 名称

`pmap_extract`, `pmap_extract_and_hold`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft vm_paddr_t Fn pmap_extract pmap_t pmap vm_offset_t va Ft vm_page_t Fn pmap_extract_and_hold pmap_t pmap vm_offset_t va vm_prot_t prot`

## 描述

`pmap_extract` 函数将虚拟地址映射到物理页面。在某些情况下，调用者可以改用 `pmap_extract_and_hold`，以确保返回的页面被持有。

`pmap_extract_and_hold` 函数将虚拟地址映射到物理页面，并仅在映射允许给定的页面保护时，原子地持有返回的页面供调用者使用。

## 实现说明

目前，不验证调用者请求的页面保护。

## 返回值

`pmap_extract` 函数将返回与物理映射 `pmap` 内虚拟地址 `va` 相关联的物理页面地址。如果映射不存在，或如果 `pmap` 参数为 `NULL`，则返回 `NULL`。

`pmap_extract_and_hold` 函数将返回与物理映射 `pmap` 内虚拟地址 `va` 相关联的 `vm_page_t`。如果映射不存在，则结果为无操作，并返回 `NULL`。

## 参见

[mutex(9)](mutex.9.md), [pmap(9)](pmap.9.md)

## 作者

`pmap_extract_and_hold` 函数由 Alan L. Cox <alc@imimic.com> 实现。本手册页由 Bruce M Simpson <bms@spc.org> 编写。
