# SYSINIT.9

`SYSINIT` — 动态内核初始化框架

## 名称

`SYSINIT`, `SYSUNINIT`

## 概要

```c
#include <sys/param.h>
#include <sys/kernel.h>

SYSINIT(uniquifier, enum sysinit_sub_id subsystem, enum sysinit_elem_order order,
    sysinit_cfunc_t func, const void *ident)
SYSUNINIT(uniquifier, enum sysinit_sub_id subsystem, enum sysinit_elem_order order,
    sysinit_cfunc_t func, const void *ident)
```

## 描述

`SYSUNINIT` 是一个用于调度初始化和拆卸例程执行的机制。这类似于 init 和 fini 例程，但增加了显式的排序元数据。它允许在内核以及内核模块（KLD）中对子系统初始化进行运行时排序。

`SYSINIT` 宏创建一个 `struct sysinit` 并将其存储在启动链接器集合中。`struct sysinit` 类型以及子系统标识符常量（`SI_SUB_*`）和初始化排序常量（`SI_ORDER_*`）定义于：

```c
#include <sys/kernel.h>
```

```c
struct sysinit {
	enum sysinit_sub_id subsystem;	/* 子系统标识符 */
	enum sysinit_elem_order	order;	/* 子系统内的初始化顺序 */
	SLIST_ENTRY(sysinit) next;	/* 单链表 */
	sysinit_cfunc_t func;		/* 函数 */
	const void	*udata;		/* 多路复用器/参数 */
};
```

`SYSINIT` 宏接受一个 `uniquifier` 参数来标识特定的函数分派数据，启动接口的 `subsystem` 类型，子系统内初始化的子系统元素 `order`，要调用的 `func` 函数，以及 `ident` 参数中指定的要传递给函数的数据。

`SYSUNINIT` 宏的行为与 `SYSINIT` 宏类似，不同之处在于它将数据添加到关闭链接器集合中。

内核的启动链接器集合在启动期间被扫描以构建已排序的初始化例程列表。然后按排序顺序执行初始化例程。`subsystem` 用作主键并按升序排序。`order` 用作次键并按升序排序。具有相同 `subsystem` 和 `order` 的两个例程的相对顺序是未定义的。

由引导加载程序与内核一起加载的模块的启动链接器集合在 `SI_SUB_KLD` 子系统初始化期间被扫描。这些模块的初始化例程被排序并合并到内核的启动例程列表中，并在启动期间与内核的初始化例程一起执行。注意，这会产生这样的效果：内核模块中任何计划早于 `SI_SUB_KLD` 的初始化例程在启动期间要到 `SI_SUB_KLD` 之后才会执行。

在运行时通过 kldload(2) 加载的内核模块的启动链接器集合在模块加载时被扫描、排序和执行。

内核模块的关闭链接器集合在内核模块卸载时被扫描、排序和执行。拆卸例程按初始化例程的相反顺序排序。内核和任何已加载模块的拆卸例程在关机期间**不会**被执行。

## 实例

此示例展示了在启动期间显示版权声明的 SYSINIT：

```c
static void
print_caddr_t(void *data)
{
	printf("%s", (char *)data);
}
SYSINIT(announce, SI_SUB_COPYRIGHT, SI_ORDER_FIRST, print_caddr_t,
    copyright);
```

## 参见

[kld(4)](../man4/kld.4.md), [DECLARE_MODULE(9)](declare_module.9.md), [DEV_MODULE(9)](dev_module.9.md), [DRIVER_MODULE(9)](driver_module.9.md), [MTX_SYSINIT(9)](mtx_pool.9.md), [SYSCALL_MODULE(9)](syscall_module.9.md)

## 历史

`SYSUNINIT` 框架首次出现于 FreeBSD 2.2。

## 作者

`SYSUNINIT` 框架由 Terrence Lambert <terry@FreeBSD.org> 编写。

本手册页由 Hiten Pandya <hmp@FreeBSD.org> 编写。
