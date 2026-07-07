# pmap_page_init(9)

`pmap_page_init` — 初始化 VM 页面的机器相关字段

## 名称

`pmap_page_init`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft void Fn pmap_page_init vm_page_t m`

## 描述

`pmap_page_init` 函数初始化 VM 页面结构的机器相关字段。此过程通常在将新页面添加到 VM 页面队列管理列表时使用。

## 参见

[pmap(9)](pmap.9.md), [pmap_pinit(9)](pmap_pinit.9.md)

## 作者

本手册页由 Hiten Pandya <hmp@FreeBSD.org> 编写。
