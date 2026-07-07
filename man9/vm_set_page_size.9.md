# vm_set_page_size(9)

`vm_set_page_size` — 初始化系统页面大小

## 名称

`vm_set_page_size`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

void
vm_set_page_size(void)
```

## 描述

`vm_set_page_size` 函数初始化系统页面大小。如果 `vm_cnt.v_page_size`（参见 `#include <sys/vmmeter.h>`）等于 0，则使用 `PAGE_SIZE`；否则使用 `vm_cnt.v_page_size` 中存储的值。如果 `vm_cnt.v_page_size` 不是 2 的幂，系统将产生恐慌。

`vm_set_page_size` 必须在任何依赖页面大小的函数之前调用。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
