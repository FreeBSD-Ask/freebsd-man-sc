# vm\_fault\_prefault.9

`vm_fault_prefault` — 将页面错误聚集到进程的地址空间中

## 名称

`vm_fault_prefault`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`void vm_fault_prefault(pmap_t pmap, vm_offset_t addra, vm_map_entry_t entry)`

## 描述

`vm_fault_prefault()` 函数提供了一种将页面错误聚集到进程地址空间中的手段。它对物理映射 `pmap` 进行操作。`entry` 参数指定要预错误的条目；`addra` 参数指定进程虚拟地址空间中映射的起始位置。

它通常在第一次页面错误后由 `vm_fault()` 调用。它通过消除对 `vm_fault()` 的重复调用来使 execve(2) 系统调用受益，否则需要进行这些重复调用以将进程的可执行页面调入物理内存。

## 实现说明

这是一个机器无关函数，它调用机器相关的 [pmap_is_prefaultable(9)](pmap_is_prefaultable.9.md) 辅助函数来确定页面是否可以预错误到物理内存中。

## 参见

execve(2), [pmap_is_prefaultable(9)](pmap_is_prefaultable.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
