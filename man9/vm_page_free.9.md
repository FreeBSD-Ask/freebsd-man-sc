# vm\_page\_free.9

`vm_page_free`, `vm_page_free_toq`, `vm_page_free_zero`, `vm_page_try_to_free` — 释放一个页面

## 名称

`vm_page_free`, `vm_page_free_toq`, `vm_page_free_zero`, `vm_page_try_to_free`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

void
vm_page_free(vm_page_t m)

void
vm_page_free_toq(vm_page_t m)

void
vm_page_free_zero(vm_page_t m)

int
vm_page_try_to_free(vm_page_t m)
```

## 描述

`vm_page_free_toq` 函数将页面移入空闲队列，并解除其与对象的关联。如果页面被持有、锁定、已空闲或其忙碌计数不为零，系统将产生恐慌。如果页面上设置了 `PG_ZERO` 标志，则将其放在空闲队列末尾；否则放在开头。

如果页面的对象类型为 `OBJT_VNODE` 且是与该对象关联的最后一个页面，则底层 vnode 可能被释放。

`vm_page_free` 和 `vm_page_free_zero` 函数都调用 `vm_page_free_toq` 来实际释放页面，但 `vm_page_free_zero` 设置 `PG_ZERO` 标志，而 `vm_page_free` 在调用 `vm_page_free_toq` 之前清除 `PG_ZERO` 标志。

`vm_page_try_to_free` 函数验证页面未被持有、锁定、忙碌或脏，如果是这样，则将页面标记为忙碌，丢弃页面上可能设置的任何保护，并释放它。

## 返回值

`vm_page_try_to_free` 如果能够释放页面则返回 1；否则返回 0。

## 参见

[vm_page_busy(9)](vm_page_busy.9.md), [vm_page_wire(9)](vm_page_wire.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
