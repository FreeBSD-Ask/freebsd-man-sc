# EVENTHANDLER.9

`EVENTHANDLER` — 内核事件处理函数

## 名称

`EVENTHANDLER`

## 概要

```c
#include <sys/eventhandler.h>

EVENTHANDLER_DECLARE(name, type)

EVENTHANDLER_DEFINE(name, func, arg, priority)

EVENTHANDLER_INVOKE(name, ...)

eventhandler_tag
EVENTHANDLER_REGISTER(name, func, arg, priority)

EVENTHANDLER_DEREGISTER(name, tag)

EVENTHANDLER_DEREGISTER_NOWAIT(name, tag)

EVENTHANDLER_LIST_DECLARE(name)

EVENTHANDLER_LIST_DEFINE(name)

EVENTHANDLER_DIRECT_INVOKE(name)

eventhandler_tag
eventhandler_register(struct eventhandler_list *list, const char *name,
    void *func, void *arg, int priority)

void
eventhandler_deregister(struct eventhandler_list *list, eventhandler_tag tag)

void
eventhandler_deregister_nowait(struct eventhandler_list *list, eventhandler_tag tag)

struct eventhandler_list *
eventhandler_find_list(const char *name)

void
eventhandler_prune_list(struct eventhandler_list *list)
```

## 描述

`EVENTHANDLER` 机制为内核子系统提供了一种注册对内核事件感兴趣的方式，并在这些事件发生时调用其回调函数。

回调函数按优先级顺序调用。每个回调相对于与某个事件关联的其他回调的相对优先级由参数 `priority` 给出，它是一个整数，范围从 `EVENTHANDLER_PRI_FIRST`（最高优先级）到 `EVENTHANDLER_PRI_LAST`（最低优先级）。如果处理程序没有特定的优先级，可以使用符号 `EVENTHANDLER_PRI_ANY`。

使用此子系统的正常方式是通过宏接口。对于高频事件，建议你额外使用 `EVENTHANDLER_LIST_DEFINE`，以便可以通过 `EVENTHANDLER_DIRECT_INVOKE` 直接调用事件处理程序（见下文）。这使得调用者无需对事件处理程序列表的全局列表进行锁定遍历。

`EVENTHANDLER_DECLARE` 此宏声明一个由参数 `name` 命名的事件处理程序，其回调函数类型为 `type`。

`EVENTHANDLER_DEFINE` 此宏使用 [SYSINIT(9)](sysinit.9.md) 向事件处理程序 `name` 注册回调函数 `func`。调用时，函数 `func` 将以参数 `arg` 作为其第一个参数调用，并通过宏 `EVENTHANDLER_INVOKE` 传入任何附加参数（见下文）。

`EVENTHANDLER_REGISTER` 此宏向事件处理程序 `name` 注册回调函数 `func`。调用时，函数 `func` 将以参数 `arg` 作为其第一个参数调用，并通过宏 `EVENTHANDLER_INVOKE` 传入任何附加参数（见下文）。`EVENTHANDLER_REGISTER` 返回一个 `eventhandler_tag` 类型的 cookie。

`EVENTHANDLER_DEREGISTER` 此宏从由参数 `name` 命名的事件处理程序中移除与标签 `tag` 关联的先前注册的回调。它会等待直到没有线程在运行此事件的处理程序后才返回，使得从此函数返回后立即卸载模块是安全的。

`EVENTHANDLER_DEREGISTER_NOWAIT` 此宏从由参数 `name` 命名的事件处理程序中移除与标签 `tag` 关联的先前注册的回调。返回时，可能仍有一个或多个线程在运行被移除的函数，但不会再进行新的调用。要从处理函数本身内部移除一个处理函数，请使用此版本的 deregister，以避免死锁。

`EVENTHANDLER_INVOKE` 此宏用于调用与事件处理程序 `name` 关联的所有回调。此宏是可变参数的。`name` 参数之后传递给宏的附加参数将作为每个已注册回调函数的第二个及后续参数传递。

`EVENTHANDLER_LIST_DEFINE` 此宏定义对由参数 `name` 命名的事件处理程序列表的引用。它使用 [SYSINIT(9)](sysinit.9.md) 初始化引用和事件处理程序列表。

`EVENTHANDLER_LIST_DECLARE` 此宏声明由参数 `name` 命名的事件处理程序列表。仅对于不在该列表定义同一编译单元中的 `EVENTHANDLER_DIRECT_INVOKE` 用户才需要此宏。

`EVENTHANDLER_DIRECT_INVOKE` 此宏调用为由参数 `name` 命名的列表注册的事件处理程序。此宏仅可用于通过 `EVENTHANDLER_LIST_DEFINE` 定义的列表。该宏是可变参数的，语义与 `EVENTHANDLER_INVOKE` 相同。

这些宏使用以下函数实现：

**`list`** 指向现有事件处理程序列表的指针，或 `NULL`。如果 `list` 为 `NULL`，则使用与参数 `name` 对应的事件处理程序列表。

**`name`** 事件处理程序列表的名称。

**`func`** 指向回调函数的指针。调用时，参数 `arg` 作为回调函数 `func` 的第一个参数传递。

**`priority`** 此回调在为此事件注册的所有回调中的相对优先级。有效值为 `EVENTHANDLER_PRI_FIRST` 到 `EVENTHANDLER_PRI_LAST` 范围内的值。

`eventhandler_register` `eventhandler_register` 函数用于向给定事件注册回调。此函数所需的参数如下：`eventhandler_register` 函数返回一个 `tag`，以后可用于 `eventhandler_deregister` 以移除特定的回调函数。

`eventhandler_deregister` `eventhandler_deregister` 函数从 `list` 指向的事件处理程序列表中移除与标签 `tag` 关联的回调。如果 `tag` 为 `NULL`，则移除该事件的所有回调函数。此函数在所有线程退出被移除的处理程序回调函数之前不会返回。此函数不能从事件处理程序回调内部安全调用。

`eventhandler_deregister_nowait` `eventhandler_deregister_nowait` 函数从 `list` 指向的事件处理程序列表中移除与标签 `tag` 关联的回调。此函数可从事件处理程序回调内部安全调用。

`eventhandler_find_list` `eventhandler_find_list` 函数返回与事件 `name` 对应的事件处理程序列表结构的指针。

`eventhandler_prune_list` `eventhandler_prune_list` 函数从事件列表 `list` 中移除所有已注销的回调。

## 返回值

宏 `EVENTHANDLER_REGISTER` 和函数 `eventhandler_register` 返回一个 `eventhandler_tag` 类型的 cookie，可在后续调用 `EVENTHANDLER_DEREGISTER` 或 `eventhandler_deregister` 时使用。

`eventhandler_find_list` 函数返回与参数 `name` 对应的事件处理程序列表的指针，如果未找到此类列表则返回 `NULL`。

## 历史

`EVENTHANDLER` 设施首次出现于 FreeBSD 4.0。

## 作者

本手册页由 Joseph Koshy <jkoshy@FreeBSD.org> 和 Matt Joras <mjoras@FreeBSD.org> 编写。
