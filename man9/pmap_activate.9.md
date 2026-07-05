# pmap\_activate.9

`pmap_activate` — 激活物理映射

## 名称

`pmap_activate`

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
pmap_activate(struct thread *td)
```

## 描述

`pmap_activate` 函数为用户线程 `td` 激活物理映射。在访问线程的地址空间之前必须调用此函数。

## 参见

[pmap(9)](pmap.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
