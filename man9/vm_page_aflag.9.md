# vm\_page\_aflag.9

`vm_page_aflag_clear`, `vm_page_aflag_set`, `vm_page_reference` — 更改页面原子标志

## 名称

`vm_page_aflag_clear`, `vm_page_aflag_set`, `vm_page_reference`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

void
vm_page_aflag_clear(vm_page_t m, uint8_t bits)

void
vm_page_aflag_set(vm_page_t m, uint8_t bits)

void
vm_page_reference(vm_page_t m)
```

## 描述

`vm_page_aflag_clear` 原子地清除页面 `aflags` 上的指定位。

`vm_page_aflag_set` 原子地设置页面 `aflags` 上的指定位。

`vm_page_reference(m)` 调用等同于

```c
vm_page_aflag_set(m, PGA_REFERENCED);
```

并且是从第三方内核模块标记页面已被引用的推荐方式。

这些函数既不阻塞，也不要求在调用周围持有任何锁即可保证正确性。

函数参数如下：

**`m`** 更新其 `aflags` 的页面。

**`bits`** 在页面标志上设置或清除的位。

以下 `aflags` 可以被设置或清除：

**`PGA_REFERENCED`** 可以设置该位以指示页面最近被访问过。例如，[pmap(9)](pmap.9.md) 设置此位以反映页面映射的访问属性，该属性通常由处理器的内存管理单元在页面访问时更新。

**`PGA_WRITEABLE`** 页面可能存在可写映射。

`PGA_REFERENCED` 和 `PGA_WRITEABLE` 位仅对托管页面有效。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
