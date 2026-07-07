# vm_map_inherit(9)

`vm_map_inherit` — 为映射中的某个范围设置 fork 继承标志

## 名称

`vm_map_inherit`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_inherit(vm_map_t map, vm_offset_t start, vm_offset_t end,
    vm_inherit_t new_inheritance)
```

## 描述

`vm_map_inherit` 函数将目标 `map` 中从 `start` 到 `end` 范围的继承标志设置为 `new_inheritance` 的值。

`new_inheritance` 标志必须具有 `VM_INHERIT_NONE`、`VM_INHERIT_COPY` 或 `VM_INHERIT_SHARE` 中的一个值。这影响在关联进程 fork 时映射如何与子映射共享。

## 实现说明

`vm_map_inherit` 函数在函数执行期间使用 [vm_map_lock(9)](vm_map_lock.9.md) 获取 `map` 上的锁。

## 返回值

`vm_map_inherit` 函数在可以设置继承标志时返回 `KERN_SUCCESS`。否则，如果提供的标志无效，将返回 `KERN_INVALID_ARGUMENT`。

## 参见

[fork(2)](../man2/fork.2.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
