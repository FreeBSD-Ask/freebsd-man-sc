# pmap_zero_page(9)

`pmap_zero_page` — 使用机器相关优化对页面进行零填充

## 名称

`pmap_zero_page`, `pmap_zero_area`

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
pmap_zero_page(vm_page_t m)

void
pmap_zero_page_area(vm_page_t m, int off, int size)
```

## 描述

`pmap_zero_page` 函数使用机器相关优化对整个页面进行零填充。`pmap_zero_page_area` 函数用于对页面的某个区域进行零填充。指定的范围不得跨越页面边界；它必须完全包含在单个页面内。

## 实现说明

FreeBSD 支持的每种架构都必须实现此函数。

## 参见

[bzero(3)](../man3/bzero.3.md), [pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
