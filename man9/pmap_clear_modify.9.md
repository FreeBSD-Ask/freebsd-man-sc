# pmap_clear_modify(9)

`pmap_clear_modify` — 设置物理页面的信息

## 名称

`pmap_clear_modify`

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

```c
void
pmap_clear_modify(vm_page_t m)
```

## 描述

`pmap_clear_modify` 函数清除物理页面 `m` 上的“已修改”位。

## 参见

[pmap(9)](pmap.9.md), [pmap_is_modified(9)](pmap_is_modified.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
