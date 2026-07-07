# vm_page_dontneed(9)

`vm_page_dontneed` — 指示页面不再需要

## 名称

`vm_page_dontneed`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

void
vm_page_dontneed(vm_page_t m)
```

## 描述

`vm_page_dontneed` 函数通知 VM 系统给定页面不再需要。如果页面已在非活跃队列或缓存队列中，此函数不执行任何操作；否则停用该页面。

注意，`vm_page_dontneed` 不一定停用页面，而是实现了一种算法，试图防止小对象的页面被过快重用，以及大对象的页面在释放时将较小的对象从队列中冲刷出去。

## 参见

[vm_page_deactivate(9)](vm_page_deactivate.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
