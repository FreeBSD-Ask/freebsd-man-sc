# pmap(9)

`pmap` — 虚拟内存子系统的机器相关部分

## 名称

`pmap`

## 概要

```c
#include <sys/param.h>
```

```c
#include <vm/vm.h>
```

```c
#include <vm/pmap.h>
```

## 描述

`pmap` 模块是 FreeBSD VM（虚拟内存）子系统的机器相关部分。此处记录的每个函数都必须有自己的架构相关实现。

`pmap` 模块负责管理硬件相关对象，如页表、地址映射、TLB 等。

机器相关代码必须提供头文件

```c
#include <machine/pmap.h>
```

此文件包含 `pmap` 结构的定义：

```c
struct pmap {
        /* 内容由 pmap 实现定义。 */
};
typedef struct pmap *pmap_t;
```

此头文件还可以定义 `pmap` 实现使用的其他数据结构。

头文件

```c
#include <vm/pmap.h>
```

定义了用于跟踪 `pmap` 统计信息的结构（见下文）。此结构定义为：

```c
struct pmap_statistics {
        long        resident_count; /* 已映射页面的数量 */
        long        wired_count;    /* 已固定页面的数量 */
};
```

实现的 `struct pmap` 必须包含一个名为 `pm_stats` 的此结构实例，并且必须在每次相关 `pmap` 操作后由实现更新。

## 参见

[pmap_activate(9)](pmap_activate.9.md), [pmap_clear_modify(9)](pmap_clear_modify.9.md), [pmap_copy(9)](pmap_copy.9.md), pmap_copy_page(9), [pmap_enter(9)](pmap_enter.9.md), [pmap_extract(9)](pmap_extract.9.md), pmap_extract_and_hold(9), [pmap_growkernel(9)](pmap_growkernel.9.md), [pmap_init(9)](pmap_init.9.md), [pmap_is_modified(9)](pmap_is_modified.9.md), [pmap_is_prefaultable(9)](pmap_is_prefaultable.9.md), [pmap_kextract(9)](pmap_kextract.9.md), [pmap_map(9)](pmap_map.9.md), [pmap_mincore(9)](pmap_mincore.9.md), [pmap_object_init_pt(9)](pmap_object_init_pt.9.md), [pmap_page_exists_quick(9)](pmap_page_exists_quick.9.md), [pmap_page_init(9)](pmap_page_init.9.md), [pmap_pinit(9)](pmap_pinit.9.md), pmap_pinit0(9), [pmap_protect(9)](pmap_protect.9.md), [pmap_qenter(9)](pmap_qenter.9.md), pmap_qremove(9), [pmap_quick_enter_page(9)](pmap_quick_enter_page.9.md), pmap_quick_remove_page(9), [pmap_release(9)](pmap_release.9.md), [pmap_remove(9)](pmap_remove.9.md), pmap_remove_all(9), pmap_remove_pages(9), [pmap_resident_count(9)](pmap_resident_count.9.md), pmap_ts_referenced(9), [pmap_unwire(9)](pmap_unwire.9.md), pmap_wired_count(9), pmap_zero_area(9), [pmap_zero_page(9)](pmap_zero_page.9.md), [vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
