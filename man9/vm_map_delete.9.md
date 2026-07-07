# vm_map_delete(9)

`vm_map_delete` — 从映射中释放地址范围

## 名称

`vm_map_delete`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/vm_map.h>`

`int vm_map_delete(vm_map_t map, vm_offset_t start, vm_offset_t end)`

## 描述

`vm_map_delete()` 函数从 `map` 中释放由 `start` 和 `end` 界定的地址范围。

## 实现说明

此函数仅供 FreeBSD VM 内部使用。FreeBSD VM 使用者应改为调用 [vm_map_remove(9)](vm_map_remove.9.md) 函数。

## 返回值

`vm_map_delete()` 函数始终返回 `KERN_SUCCESS`。

## 参见

[vm_map(9)](vm_map.9.md), [vm_map_remove(9)](vm_map_remove.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
