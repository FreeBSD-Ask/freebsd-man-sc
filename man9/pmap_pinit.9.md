# pmap_pinit(9)

`pmap_pinit` — 初始化 pmap 结构

## 名称

`pmap_pinit`, `pmap_pinit0`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft void Fn pmap_pinit pmap_t pmap Ft void Fn pmap_pinit0 pmap_t pm`

## 描述

`pmap_pinit` 函数初始化预分配并清零的结构 `pmap`，例如 `vmspace` 结构中的结构。

`pmap_pinit0` 函数初始化与进程 0（系统中创建的第一个进程）相关联的物理映射 `pm`。

## 参见

[pmap(9)](pmap.9.md), [pmap_growkernel(9)](pmap_growkernel.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
