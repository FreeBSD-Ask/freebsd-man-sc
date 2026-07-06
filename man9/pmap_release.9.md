# pmap_release.9

`pmap_release` — 释放物理映射持有的资源

## 名称

`pmap_release`

## 概要

`#include <sys/param.h>`

`#include <vm/vm.h>`

`#include <vm/pmap.h>`

`Ft void Fn pmap_release pmap_t pmap`

## 描述

`pmap_release` 函数释放物理映射 `pmap` 持有的任何资源。当由相应函数 `pmap_pinit` 初始化的 pmap 被释放时，调用此函数。

## 实现说明

仅当 `pmap` 不再包含任何有效映射时才应调用此函数。

## 参见

[pmap(9)](pmap.9.md), [pmap_pinit(9)](pmap_pinit.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
