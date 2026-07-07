# vm_page_bits(9)

`vm_page_bits`, `vm_page_set_validclean`, `vm_page_clear_dirty`, `vm_page_set_invalid`, `vm_page_zero_invalid`, `vm_page_is_valid`, `vm_page_test_dirty`, `vm_page_dirty`, `vm_page_undirty` — 管理页面干净和脏位

## 名称

`vm_page_bits`, `vm_page_set_validclean`, `vm_page_clear_dirty`, `vm_page_set_invalid`, `vm_page_zero_invalid`, `vm_page_is_valid`, `vm_page_test_dirty`, `vm_page_dirty`, `vm_page_undirty`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

int
vm_page_bits(int base, int size)

void
vm_page_set_validclean(vm_page_t m, int base, int size)

void
vm_page_clear_dirty(vm_page_t m, int base, int size)

void
vm_page_set_invalid(vm_page_t m, int base, int size)

void
vm_page_zero_invalid(vm_page_t m, boolean_t setvalid)

int
vm_page_is_valid(vm_page_t m, int base, int size)

void
vm_page_test_dirty(vm_page_t m)

void
vm_page_dirty(vm_page_t m)

void
vm_page_undirty(vm_page_t m)
```

## 描述

`vm_page_bits` 计算 `base` 和 `size` 之间表示 `DEV_BSIZE` 范围字节的位。字节范围应在单个页面内，如果 `size` 为零，则不设置任何位。

`vm_page_set_validclean` 将 `base` 和 `size` 之间的字节范围标记为有效且干净。该范围应 `DEV_BSIZE` 对齐且不大于 `PAGE_SIZE`。如果未正确对齐，范围开头和结尾的 `DEV_BSIZE` 块的任何未对齐部分将被清零。

如果 `base` 为零且 `size` 为一页，则清除页映射中的修改位；同时清除 `VPO_NOSYNC` 标志。

`vm_page_clear_dirty` 清除页面中 `base` 和 `size` 之间的脏位。表示该范围的位通过调用 `vm_page_bits` 计算。

`vm_page_set_invalid` 清除页面中 `base` 和 `size` 之间表示 `DEV_BSIZE` 块的有效和脏标志中的位。这些位通过调用 `vm_page_bits` 计算。除了清除页面内的位之外，持有该页的对象中的生成号也会递增。

`vm_page_zero_invalid` 将页面中当前标记为无效的所有块清零。如果 `setvalid` 为 `TRUE`，则设置页面内的所有有效位。

在某些情况下（如 NFS），不能设置有效位以保持缓存一致性。

`vm_page_is_valid` 检查页面的 `base` 和 `size` 之间的所有 `DEV_BSIZE` 块是否有效。如果 `size` 为零且页面完全无效，`vm_page_is_valid` 将返回 `TRUE`，在其他所有情况下大小为零将返回 `FALSE`。

`vm_page_test_dirty` 检查页面是否通过其任何物理映射被修改过，如果是，则将整个页面标记为脏。调用 `vm_page_dirty` 来修改脏位。

`vm_page_dirty` 将整个页面标记为脏。预期页面当前不在缓存队列上。

`vm_page_undirty` 清除页面中的所有脏位。

## 注意

这些函数都不允许阻塞。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
