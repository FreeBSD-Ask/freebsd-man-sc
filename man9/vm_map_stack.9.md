# vm\_map\_stack.9

`vm_map_stack`, `vm_map_growstack` — 管理进程栈

## 名称

`vm_map_stack`, `vm_map_growstack`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_stack(vm_map_t map, vm_offset_t addrbos, vm_size_t max_ssize,
    vm_prot_t prot, vm_prot_t max, int cow)

int
vm_map_growstack(struct proc *p, vm_offset_t addr)
```

## 描述

`vm_map_stack` 函数为新进程映像映射进程栈。栈映射到 `map` 中的 `addrbos` 处，最大大小为 `max_ssize`。传入 `cow` 的写时复制标志也应用到新映射。保护位由 `prot` 和 `max` 提供。

通常由 [execve(2)](../man2/execve.2.md) 调用。

`vm_map_growstack` 函数负责将进程 `p` 的栈增长到所需地址 `addr`，类似于传统的 [sbrk(2)](../man2/sbrk.2.md) 调用。

## 实现说明

`vm_map_stack` 函数调用 [vm_map_insert(9)](vm_map_insert.9.md) 来创建其映射。

`vm_map_stack` 和 `vm_map_growstack` 函数在调用期间获取进程 `p` 上的进程锁。

## 返回值

`vm_map_stack` 函数在映射成功分配时返回 `KERN_SUCCESS`。

否则，如果映射栈会超过进程的 VMEM 资源限制，或指定的栈底地址超出映射范围，或该地址已有映射，或 `max_ssize` 无法在当前映射中容纳，则返回 `KERN_NO_SPACE`。

此函数其他可能的返回值记录在 [vm_map_insert(9)](vm_map_insert.9.md) 中。

`vm_map_growstack` 函数在 `addr` 已被映射或栈成功增长时返回 `KERN_SUCCESS`。

如果 `addr` 在栈范围之外，它也返回 `KERN_SUCCESS`；这样做是为了保持与先前位于 `vm_machdep.c` 文件中的已弃用 `grow` 函数的兼容性。

## 参见

[vm_map(9)](vm_map.9.md), [vm_map_insert(9)](vm_map_insert.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
