# pmap_page_exists_quick(9)

`pmap_page_exists_quick` — 确定页面是否存在于物理映射中

## 名称

`pmap_page_exists_quick`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft bool Fn pmap_page_exists_quick pmap_t pmap vm_page_t m`

## 描述

`pmap_page_exists_quick` 函数用于快速确定页面 `m` 是否存在于物理映射 `pmap` 中。通常从 VM 分页代码中调用。

## 实现说明

上述使用的 PV 计数将来可能向上或向下调整；只需为 pmap 的一小部分子集返回 `true` 即可正确进行页面老化。

## 返回值

仅当物理映射 `pmap` 的 PV 条目是从页面 `m` 链接的前 16 个 PV 之一时，`pmap_page_exists_quick` 才返回 `true`。

## 参见

[pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
