# pmap_is_modified(9)

`pmap_is_modified` — 返回有关物理页面的信息

## 名称

`pmap_is_modified`, `pmap_ts_modified`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft bool Fn pmap_is_modified vm_page_t m Ft int Fn pmap_ts_referenced vm_page_t m`

## 描述

`pmap_is_modified` 和 `pmap_ts_referenced` 函数返回有关物理页面的信息。

## 返回值

`pmap_is_modified` 函数返回物理页面 `m` 的"页面已修改"位的状态。

`pmap_ts_referenced` 函数返回页面 `m` 的引用位计数，并清除这些位。不必清除每个引用位，但当页面上没有剩余引用位设置时，必须返回 0。

## 参见

[pmap(9)](pmap.9.md), [pmap_clear_modify(9)](pmap_clear_modify.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
