# vm\_page\_grab.9

`vm_page_grab` — 从对象中返回一个页面

## 名称

`vm_page_grab`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

vm_page_t
vm_page_grab(vm_object_t object, vm_pindex_t pindex, int allocflags)
```

## 描述

`vm_page_grab` 函数从给定对象返回 `pindex` 处的页面。如果页面存在且忙碌，`vm_page_grab` 将睡眠等待。如果页面不存在，则分配它。函数睡眠直到分配请求可以满足。

函数要求在入口处锁定 `object`，并在返回时保持锁定状态。如果 `vm_page_grab` 函数因任何原因睡眠，对象锁会被临时释放。

`vm_page_grab` 支持 [vm_page_alloc(9)](vm_page_alloc.9.md) 支持的所有标志。此外，`vm_page_grab` 还支持以下标志：

**`VM_ALLOC_IGN_SBUSY`** 在等待现有页面的忙碌状态清除时，仅测试独占忙碌；忽略共享忙碌计数。

## 返回值

`vm_page_grab` 始终返回该页面。

## 参见

[vm_page_alloc(9)](vm_page_alloc.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
