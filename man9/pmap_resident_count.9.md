# pmap\_resident\_count.9

`pmap_resident_count` — 返回页面驻留和锁定统计信息

## 名称

`pmap_resident_count`, `pmap_wired_count`

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
long
pmap_resident_count(pmap_t pmap)

long
pmap_wired_count(pmap_t pmap)
```

## 描述

`pmap_resident_count` 和 `pmap_wired_count` 宏允许 `pmap` 使用者从机器相关结构 `struct pmap` 的 `pm_stats` 成员中检索统计信息。

## 实现说明

这两个函数均定义为内联宏。它们所访问的成员类型为 `long`。

## 返回值

`pmap_resident_count` 返回物理映射 `pmap` 中当前驻留在主存中的页面数。

`pmap_wired_count` 返回物理映射 `pmap` 中当前锁定在主存中的页面数。

## 参见

[pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
