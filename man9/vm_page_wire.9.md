# vm_page_wire(9)

`vm_page_wire`, `vm_page_unwire`, `vm_page_unwire_noq` — 锁定和解锁页面

## 名称

`vm_page_wire`, `vm_page_unwire`, `vm_page_unwire_noq`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

void
vm_page_wire(vm_page_t m)

bool
vm_page_wire_mapped(vm_page_t m)

void
vm_page_unwire(vm_page_t m, int queue)

bool
vm_page_unwire_noq(vm_page_t m)
```

## 描述

`vm_page_wire` 和 `vm_page_wire_mapped` 函数锁定页面，防止其被页面守护进程回收或在包含它的对象被销毁时回收。两个函数都要求页面属于一个对象。`vm_page_wire_mapped` 函数供 [pmap(9)](pmap.9.md) 层在查找后使用。如果页面的映射正在被并发销毁，此函数可能失败，在这种情况下将返回 false。

`vm_page_unwire` 和 `vm_page_unwire_noq` 函数释放页面的锁定。`vm_page_unwire` 函数接受一个队列索引，并在释放最后一个锁定时将页面插入到相应的页面队列中。如果页面不属于任何对象且不存在对该页面的其他引用，`vm_page_unwire` 将释放该页面。`vm_page_unwire_noq` 释放锁定，如果是页面的最后一个锁定则返回 true。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
