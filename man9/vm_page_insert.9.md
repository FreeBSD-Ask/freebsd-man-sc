# vm\_page\_insert.9

`vm_page_insert`, `vm_page_remove` — 从对象中添加/移除页面

## 名称

`vm_page_insert`, `vm_page_remove`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

void
vm_page_insert(vm_page_t m, vm_object_t object, vm_pindex_t pindex)

void
vm_page_remove(vm_page_t m)
```

## 描述

`vm_page_insert` 函数将页面添加到给定对象的给定索引处。页面被添加到 VM 页哈希表和对象的页面列表中，但不更新硬件页表。对于用户页面，将在访问时通过页错误引入。如果页面是内核页面，调用者需要负责将页面添加到内核的 pmap 中。

如果页面标志中设置了 `PG_WRITEABLE`，则对象标志中设置 `OBJ_WRITEABLE` 和 `OBJ_MIGHTBEDIRTY`。

`vm_page_remove` 函数从其对象和 VM 页哈希表中移除给定页面。在调用此函数之前页面必须忙碌，否则系统将产生恐慌。页面的 pmap 条目不会被此函数移除。

`vm_page_insert` 的参数如下：

**`m`** 要添加到对象的页面。

**`object`** 页面应添加到的对象。

**`pindex`** 页面在对象中的索引位置。

`vm_page_remove` 的参数如下：

**`m`** 要移除的页面。

## 实现说明

VM 对象中页面的索引是同一对象中截断到页边界的字节索引。例如，如果页面大小为 4096 字节，对象中的地址为 81944，则页面索引为 20。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
