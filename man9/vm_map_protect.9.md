# vm\_map\_protect.9

`vm_map_protect` — 将保护位应用到虚拟内存区域

## 名称

`vm_map_protect`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_protect(vm_map_t map, vm_offset_t start, vm_offset_t end,
    vm_prot_t new_prot, vm_prot_t new_maxprot, int flags)
```

## 描述

`vm_map_protect` 函数设置映射 `map` 中由 `start` 和 `end` 界定的地址区域的保护位和最大保护位。

如果 `flags` 参数设置了 `VM_MAP_PROTECT_SET_PROT` 位，则有效保护设置为 `new_prot`。

如果 `flags` 参数设置了 `VM_MAP_PROTECT_SET_MAXPROT` 位，则最大保护设置为 `new_maxprot`。未包含在 `new_maxprot` 中的保护位将从现有条目中清除。

`new_prot` 和 `new_maxprot` 指定的值不允许包含范围内每个条目的现有 `max_protection` 中未设置的任何保护位。如果违反此条件，操作将失败。例如，这防止了将只读文件的共享映射从只读升级为读写。

指定的范围不得包含子映射。

## 实现说明

该函数通过调用 [vm_map_lock(9)](vm_map_lock.9.md) 在执行期间获取 `map` 上的锁。此外，映射上影响指定范围的任何正在进行的锁定操作都会导致 `vm_map_protect` 睡眠，等待其完成。

## 返回值

**`KERN_SUCCESS`** 指定的保护位设置成功。

**`KERN_INVALID_ARGUMENT`** 在范围内遇到子映射条目。

**`KERN_PROTECTION_FAILURE`** `new_prot` 或 `new_maxprot` 的值超过了范围内某个条目的 `max_protection`。

**`KERN_PROTECTION_FAILURE`** 映射不允许同时设置写和执行权限，但 `new_prot` 同时设置了 `VM_PROT_WRITE` 和 `VM_PROT_EXECUTE`。

**`KERN_RESOURCE_SHORTAGE`** 写时复制映射从只读转换为读写，但没有足够的交换空间来支持复制的页面。

**`KERN_OUT_OF_BOUNDS`** 请求同时更新新保护和新最大保护，但指定的 `new_prot` 不是 `new_maxprot` 的子集。

## 参见

[vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
