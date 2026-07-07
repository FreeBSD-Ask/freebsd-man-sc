# vm_map_check_protection(9)

`vm_map_check_protection` — 检查 vm_map 的内存保护

## 名称

`vm_map_check_protection`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/vm_map.h>`

`boolean_t vm_map_check_protection(vm_map_t map, vm_offset_t start, vm_offset_t end, vm_prot_t protection)`

## 描述

`vm_map_check_protection()` 函数断言目标 `map` 允许从 `start` 到 `end` 的整个地址范围具有指定特权 `protection`。该区域必须是连续的；不允许有空洞。

## 实现说明

此代码不也不应检查区域内容是否可访问。例如，一个小文件可能映射到比其大得多的地址空间中。

## 返回值

`vm_map_check_protection()` 函数如果允许该特权则返回 TRUE；如果不允许或发生任何其他错误，则返回 FALSE。

## 参见

munmap(2), [vm_map(9)](vm_map.9.md), [vm_map_protect(9)](vm_map_protect.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
