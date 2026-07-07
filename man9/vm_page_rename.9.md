# vm_page_rename(9)

`vm_page_rename` — 移动一个页面

## 名称

`vm_page_rename`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

void
vm_page_rename(vm_page_t m, vm_object_t new_object,
    vm_pindex_t new_pindex)
```

## 描述

`vm_page_rename` 函数从一个对象中移除页面，并将其添加到另一个对象的给定页面索引处。页面被添加到给定对象，并从当前关联的对象中移除。如果页面当前在缓存队列上，它将被停用，除非它被锁定或非托管，在这种情况下停用将失败。移动后整个页面被标记为脏。

`vm_page_rename` 的参数如下：

**`m`** 要移动的页面。

**`new_object`** 页面应插入的对象。

**`new_pindex`** 新页面应插入到 `new_object` 中的页面索引。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
