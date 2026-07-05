# osd.9

`osd` — 对象特定数据

## 名称

`osd`, `osd_register`, `osd_deregister`, `osd_set`, `osd_reserve`, `osd_set_reserved`, `osd_free_reserved`, `osd_get`, `osd_del`, `osd_call`, `osd_exit`

## 概要

```c
#include <sys/osd.h>
```

```c
typedef void *(osd_destructor_t)(void *value);

typedef int *(osd_method_t)(void *obj, void *data);

int
osd_register(u_int type, osd_destructor_t destructor,
    const osd_method_t *methods)

void
osd_deregister(u_int type, u_int slot)

int
osd_set(u_int type, struct osd *osd, u_int slot, void *value)

void **
osd_reserve(u_int slot)

int
osd_set_reserved(u_int type, struct osd *osd, u_int slot,
    void **rsv, void *value)

void
osd_free_reserved(void **rsv)

void *
osd_get(u_int type, struct osd *osd, u_int slot)

void
osd_del(u_int type, struct osd *osd, u_int slot)

int
osd_call(u_int type, u_int method, void *obj, void *data)

void
osd_exit(u_int type, struct osd *osd)
```

## 描述

`osd` 框架提供了一种机制，可以在运行时将任意数据动态关联到任何已适配为可使用 `osd` 的内核数据结构。所需的一次性修改涉及在内核数据结构中嵌入一个 `struct osd`。

一个额外的好处是，在对结构进行初始更改之后，所有后续对该结构使用 `osd` 都不涉及对结构布局的更改。推而广之，如果该数据结构是 ABI 的一部分，`osd` 提供了一种以保持 ABI 的方式扩展结构的方法。

嵌入的 `struct osd` 的细节与 `osd` 框架的使用者无关，不应直接操作。

与结构关联的数据由 `osd` 框架使用类型/槽标识符对来引用。类型在

```c
#include <sys/osd.h>
```

中静态定义，并为要注册的槽提供高级分组。槽标识符在使用 `osd_register` 注册数据类型时由框架动态分配，并在相应的 `osd_deregister` 调用之前保持有效。

### 函数

`osd_register` 函数向 `osd` 框架注册一个类型/槽标识符对，用于新的数据类型。该函数可能会休眠，因此不能从不可休眠的上下文中调用。`type` 参数指定从

```c
#include <sys/osd.h>
```

中定义的高级类型分组中分配槽标识符。`destructor` 参数指定一个可选的 `osd_destructor_t` 函数指针，该函数将在被注册类型的对象随后被 `osd_del` 函数销毁时调用。如果不需要析构函数，可以传递 NULL。`methods` 参数指定一个可选的 `osd_method_t` 函数指针数组，可随后由 `osd_call` 函数调用。如果不需要方法，可以传递 NULL。`methods` 参数目前仅在 OSD_JAIL 类型标识符下有用。

`osd_deregister` 函数注销先前注册的类型/槽标识符对。该函数可能会休眠，因此不能从不可休眠的上下文中调用。`type` 参数指定从

```c
#include <sys/osd.h>
```

中定义的高级类型分组中分配槽标识符。`slot` 参数指定要注销的槽标识符，应为注册数据类型时 `osd_register` 返回的值。

`osd_set` 函数将数据对象指针与内核数据结构的 `struct osd` 成员关联。`type` 参数指定从

```c
#include <sys/osd.h>
```

中定义的高级类型分组中分配槽标识符。`osd` 参数是指向内核数据结构 `struct osd` 的指针，`value` 指针将与之关联。`slot` 参数指定要将 `value` 指针分配到的槽标识符。`value` 参数指向要与 `osd` 关联的数据对象。

`osd_set_reserved` 函数与 `osd_set` 功能相同，但多了一个 `rsv` 参数，这是先前通过 `osd_reserve` 分配的内部使用内存。

`osd_get` 函数从指定的类型/槽标识符对返回与内核数据结构 `struct osd` 成员关联的数据指针。`type` 参数指定从

```c
#include <sys/osd.h>
```

中定义的高级类型分组中分配槽标识符。`osd` 参数是指向内核数据结构 `struct osd` 的指针，从中检索数据指针。`slot` 参数指定从中检索数据指针的槽标识符。

`osd_del` 函数从指定的类型/槽标识符对中移除与内核数据结构 `struct osd` 成员关联的数据指针。`type` 参数指定从

```c
#include <sys/osd.h>
```

中定义的高级类型分组中分配槽标识符。`osd` 参数是指向内核数据结构 `struct osd` 的指针，从中移除数据指针。`slot` 参数指定从中移除数据指针的槽标识符。如果在注册时指定了 `osd_destructor_t` 函数指针，则将调用析构函数并传递正在删除的类型/槽标识符对的数据指针。

`osd_call` 函数为指定 `obj` 和 `data` 指针上给定类型的所有当前已注册槽调用指定的 `osd_method_t` 函数指针。该函数可能会休眠，因此不能从不可休眠的上下文中调用。`type` 参数指定从

```c
#include <sys/osd.h>
```

中定义的高级类型分组中调用方法。`method` 参数指定传递给 `osd_register` 的 `osd_method_t` 数组的索引。`obj` 和 `data` 参数传递给每个槽的方法函数指针。

`osd_exit` 函数从指定内核数据结构 `struct osd` 成员的所有当前已注册槽中移除给定类型的所有数据对象指针。`type` 参数指定从

```c
#include <sys/osd.h>
```

中定义的高级类型分组中移除数据指针。`osd` 参数是指向内核数据结构 `struct osd` 的指针，从中移除所有当前已注册槽的所有数据对象指针。

## 实现说明

`osd` 使用二维矩阵（数组的数组）作为数据结构来管理与内核数据结构 `struct osd` 成员关联的外部数据。类型标识符用作外层数组的索引，槽标识符用作内层数组的索引。要设置或检索给定类型/槽标识符对的数据指针，`osd_set` 和 `osd_get` 执行相当于 array[type][slot] 的操作，这既是常数时间又很快。

如果首次对 `struct osd` 调用 `osd_set`，存储数据指针的数组将使用 [malloc(9)](malloc.9.md) 以 M_NOWAIT 动态分配到适合正在设置的槽标识符的大小。如果随后调用 `osd_set` 尝试设置数值上大于先前 `osd_set` 调用中使用的槽的槽标识符，则使用 realloc(9) 将数组增长到适当的大小以便可以使用该槽标识符。为最大化任何按顺序在多个不同槽标识符上调用 `osd_set` 的代码（例如在初始化阶段）的效率，应按从高到低的降序遍历槽标识符。这将导致仅一次 [malloc(9)](malloc.9.md) 调用来创建最大槽大小的数组，所有后续对 `osd_set` 的调用将在没有任何 realloc(9) 调用的情况下进行。

`osd_set` 有可能无法分配此数组。为确保此类分配成功，可以（在非阻塞上下文中）调用 `osd_reserve`，它将通过 [malloc(9)](malloc.9.md) 以 M_WAITOK 预分配内存。然后此预分配的内存传递给 `osd_set_reserved`，后者在必要时使用它，否则丢弃它。也可以通过调用 `osd_free_reserved` 显式丢弃内存。由于此方法总是分配内存（无论最终是否需要），应仅很少使用，例如在 `osd_set` 失败的不太可能发生的情况下。

`osd` API 面向存储指向给定 `osd` 类型标识符的相同底层数据结构类型指针的槽标识符。这不是必需的，例如 [khelp(9)](khelp.9.md) 在 OSD_KHELP 类型标识符下的槽中存储完全不同的数据类型。

### 锁

`osd` 内部使用 [mutex(9)](mutex.9.md)、[rmlock(9)](rmlock.9.md) 和 [sx(9)](sx.9.md) 锁的混合来保护其内部数据结构和状态。

同步对内核数据结构 `struct osd` 成员访问的责任留给使用该数据结构并调用 `osd` API 的子系统。

`osd_get` 仅在读取模式下获取 [rmlock(9)](rmlock.9.md)，因此在内核内大多数上下文（包括大多数快速路径）中使用都是安全的。

## 返回值

`osd_register` 返回新注册数据类型的槽标识符。

`osd_set` 和 `osd_set_reserved` 成功时返回零，如果指定的类型/槽标识符对触发了失败的内部 realloc(9)，则返回 ENOMEM（当 `rsv` 为非 NULL 时，`osd_set_reserved` 将始终成功）。

`osd_get` 返回指定类型/槽标识符对的数据指针，如果槽尚未初始化则返回 NULL。

`osd_reserve` 返回适合传递给 `osd_set_reserved` 或 `osd_free_reserved` 的指针。

`osd_call` 如果没有方法运行或每个槽的方法都成功运行则返回零。如果某个槽的方法返回非零值，`osd_call` 提前终止并将方法的错误返回给调用者。

## 参见

[khelp(9)](khelp.9.md)

## 历史

对象特定数据（OSD）设施首次出现在 FreeBSD 8.0 中。

## 作者

`osd` 设施由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。

本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 编写。
