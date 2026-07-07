# pmap_quick_enter_page(9)

`pmap_quick_enter_page` — 管理快速、单页面内核地址空间映射

## 名称

`pmap_quick_enter_page`, `pmap_quick_remove_page`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft vm_offset_t Fn pmap_quick_enter_page vm_page_t m Ft void Fn pmap_quick_remove_page vm_offset_t kva`

## 描述

`pmap_quick_enter_page` 函数接受单个页面 `m`，并将此页面输入到内核虚拟地址（KVA）空间中的预分配地址。此函数用于仅在非常短的时间内使用的临时映射，例如对页面内容的复制操作。

`pmap_quick_remove_page` 函数删除先前由 `pmap_quick_enter_page` 在 `kva` 处创建的映射，使 `pmap_quick_enter_page` 使用的 KVA 帧可供重用。

在许多架构上，`pmap_quick_enter_page` 使用每 CPU 页帧。在这些情况下，它必须禁用本地 CPU 上的抢占。然后，相应的 `pmap_quick_remove_page` 调用会重新启用抢占。因此，机器无关代码在持有这些映射时睡眠或执行锁定操作是不安全的。当前实现仅保证调用线程有单个页面可用，因此对 `pmap_quick_enter_page` 的调用不能嵌套。

`pmap_quick_enter_page` 和 `pmap_quick_remove_page` 不会睡眠，并且 `pmap_quick_enter_page` 始终返回有效地址。在除自旋互斥锁之外的所有类型的锁下使用这些函数是安全的。在除主中断上下文之外的所有线程上下文中使用它们也是安全的。

映射处于活动状态时，页面*不得*被交换或以其他方式重用。它必须被锁定或持有，或者必须属于非受管区域（如 I/O 设备内存）。

## 返回值

`pmap_quick_enter_page` 函数返回映射到页面 `m` 的内核虚拟地址。

## 参见

[pmap(9)](pmap.9.md)

## 作者

本手册页由 Jason A Harmening <jah@FreeBSD.org> 编写。
