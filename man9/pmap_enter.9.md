# pmap_enter.9

`pmap_enter` — 将虚拟页面插入物理映射

## 名称

`pmap_enter`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft int Fo pmap_enter pmap_t pmap vm_offset_t va vm_page_t m vm_prot_t prot u_int flags int8_t psind Fc`

## 描述

`pmap_enter` 函数在物理映射 `pmap` 中创建从虚拟地址 `va` 到物理页面 `m` 的映射，保护属性为 `prot`。虚拟地址 `va` 处的任何先前映射都会被销毁。

`flags` 参数可具有以下值：

**`VM_PROT_READ`** 对给定虚拟地址的读访问触发了此调用。

**`VM_PROT_WRITE`** 对给定虚拟地址的写访问触发了此调用。

**`VM_PROT_EXECUTE`** 对给定虚拟地址的执行访问触发了此调用。

**`PMAP_ENTER_WIRED`** 映射应标记为已锁定。

**`PMAP_ENTER_NOSLEEP`** 此函数在创建映射期间不能睡眠。如果在不睡眠的情况下无法创建映射，则返回适当的 Mach VM 错误。

如果未指定 `PMAP_ENTER_NOSLEEP` 标志，则此函数必须在返回之前创建请求的映射。它不能失败。为了创建请求的映射，此函数可以销毁任何 pmap 中的任何非锁定映射。

`psind` 参数指定映射应使用的页面大小。支持的页面大小由全局数组 `pagesizes[]` 描述。通过传递等于所需页面大小的数组元素的索引来指定所需的页面大小。

当 `pmap_enter` 函数销毁或更新受管映射时（包括虚拟地址 `va` 处的现有映射），它会更新与先前映射的物理页面对应的 `vm_page` 结构。如果通过受管映射访问了物理页面，则会设置 `vm_page` 结构的 `PGA_REFERENCED` aflag。如果通过受管映射修改了物理页面，则会在 `vm_page` 结构上调用 `vm_page_dirty` 函数。

如果新映射是受管的且可写的，则必须为页面 `m` 设置 `PGA_WRITEABLE` aflag。如果实现可以确保先前映射的页面不存在其他可写的受管映射，则建议为已销毁的映射清除 `PGA_WRITEABLE`。

如果请求修改现有映射以使用不同的物理页面，则 `pmap_enter` 的实现必须在安装新映射之前使先前的映射无效。这确保了共享 pmap 的所有线程对映射保持一致的视图，这对于 CoW（写时复制）故障的正确处理是必要的。

如果页面 `m` 是受管的，则页面必须由调用者忙碌或所属对象必须被锁定。在后一种情况下，调用者必须指定 `PMAP_ENTER_NOSLEEP`。

`pmap_enter` 函数必须处理给定地址的多处理器 TLB 一致性。

## 注释

在 arm 和 i386 架构上，`pmap_enter` 函数的现有实现不完整，仅支持 `psind` 的值为 0。其他受支持的架构（amd64 除外）的 `pagesizes[]` 数组大小为 1。

## 返回值

如果成功，`pmap_enter` 函数返回 `KERN_SUCCESS`。如果指定了 `PMAP_ENTER_NOSLEEP` 标志且在不睡眠的情况下无法获取映射所需的资源，则返回 `KERN_RESOURCE_SHORTAGE`。

## 参见

[pmap(9)](pmap.9.md)

## 作者

本手册页最初由 Bruce M Simpson <bms@spc.org> 编写，然后由 Alan Cox <alc@FreeBSD.org> 和 Konstantin Belousov <kib@FreeBSD.org> 重写。
