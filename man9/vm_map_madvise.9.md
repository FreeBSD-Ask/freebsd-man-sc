# vm_map_madvise(9)

`vm_map_madvise` — 将内存使用建议应用到映射条目

## 名称

`vm_map_madvise`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

int
vm_map_madvise(vm_map_t map, vm_offset_t start, vm_offset_t end,
    int behav)
```

## 描述

`vm_map_madvise` 函数将标志 `behav` 应用到 `map` 中 `start` 和 `end` 之间的条目。

建议分为影响 `vm_map_entry` 结构的建议和影响底层对象的建议两类。

`vm_map_madvise` 函数由 [madvise(2)](../sys/madvise.2.md) 系统调用使用。

## 返回值

`vm_map_madvise` 函数成功时返回 0。如果 `behav` 参数无法识别，则返回 `KERN_INVALID_ARGUMENT`。

## 参见

[madvise(2)](../sys/madvise.2.md), [vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
