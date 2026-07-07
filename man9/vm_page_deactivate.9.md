# vm_page_deactivate(9)

`vm_page_deactivate` — 停用一个页面

## 名称

`vm_page_deactivate`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

void
vm_page_deactivate(vm_page_t m)
```

## 描述

`vm_page_deactivate` 函数将给定页面移动到非活跃队列，只要该页面是非托管的且未被锁定。

## 参见

[vm_page_wire(9)](vm_page_wire.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
