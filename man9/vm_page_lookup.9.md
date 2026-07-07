# vm_page_lookup(9)

`vm_page_lookup` — 查找一个 VM 页面

## 名称

`vm_page_lookup`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

vm_page_t
vm_page_lookup(vm_object_t object, vm_pindex_t pindex)
```

## 描述

`vm_page_lookup` 函数根据 VM 对象和索引搜索 VM 页面。如果未找到页面，则返回 `NULL`。其参数如下：

**`object`** 要搜索的 VM 对象。

**`pindex`** 要搜索的页面索引。

## 返回值

成功时返回 `vm_page_t`；否则返回 `NULL`。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
