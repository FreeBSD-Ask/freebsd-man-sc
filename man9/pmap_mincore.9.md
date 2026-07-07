# pmap_mincore(9)

`pmap_mincore` — 确定虚拟地址是否驻留在物理内存中

## 名称

`pmap_mincore`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft int Fn pmap_mincore pmap_t pmap vm_offset_t addr`

## 描述

`pmap_mincore` 函数确定物理映射 `pmap` 中虚拟地址 `addr` 处的页面是否驻留在物理内存中。它是 mincore(2) 系统调用使用的机器相关接口。

## 返回值

如果页面驻留在物理内存中，则返回一个标志掩码，其含义记录在 mincore(2) 中；否则返回 0。

`pmap` 必须存在且 `addr` 必须映射到 `pmap` 中。如果发生任何错误，机器相关实现应返回 0。

## 参见

mincore(2), [pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
