# vm_map_wire(9)

`vm_map_wire`, `vm_map_unwire` — 管理虚拟内存映射中的页锁定

## 名称

`vm_map_wire`, `vm_map_unwire`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_wire(vm_map_t map, vm_offset_t start, vm_offset_t end, int flags)

int
vm_map_unwire(vm_map_t map, vm_offset_t start, vm_offset_t end, int flags)
```

## 描述

`vm_map_wire` 函数负责锁定映射 `map` 中 `start` 和 `end` 之间的页面。锁定的页面被固定在物理内存中，只要其锁定计数保持大于零，就不会被换出。

`vm_map_unwire` 函数执行相应的解锁操作。

`flags` 参数是一个位掩码，由以下标志组成：

如果设置了 `VM_MAP_WIRE_USER` 标志，函数在用户地址空间内操作。

如果设置了 `VM_MAP_WIRE_HOLESOK` 标志，可以在 `map` 地址空间内的任意范围上操作。

如果需要连续范围，调用者应通过指定 `VM_MAP_WIRE_NOHOLES` 标志明确表达其意图。

## 实现说明

两个函数都会尝试使用 [vm_map_lock(9)](vm_map_lock.9.md) 获取映射上的锁，并在调用期间持有该锁。如果检测到 `MAP_ENTRY_IN_TRANSITION`，将调用 `vm_map_unlock_and_wait` 直到映射再次可用。

映射在此期间可能已被其他消费者持有而发生变化，因此此接口的消费者应使用以下返回值检查此条件。

## 返回值

`vm_map_wire` 和 `vm_map_unwire` 函数具有相同的返回值。如果范围内的所有页面都成功[解除]锁定，函数返回 `KERN_SUCCESS`。

否则，如果指定的范围无效，或在设置 `MAP_ENTRY_IN_TRANSITION` 标志时映射发生了变化，则返回 `KERN_INVALID_ADDRESS`。

## 参见

[mlockall(2)](../man2/mlockall.2.md), [munlockall(2)](../man2/munlockall.2.md), [vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
