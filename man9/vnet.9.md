# VNET.9

`VNET` — 网络子系统虚拟化基础设施

## 名称

`VNET`

## 概要

```c
options VIMAGE
options VNET_DEBUG

#include <net/vnet.h>
```

### 常量与全局变量

```c
VNET_SETNAME
VNET_SYMPREFIX
extern struct vnet *vnet0;
```

### 变量声明

```c
VNET(name)
VNET_NAME(name)
VNET_DECLARE(type, name)
VNET_DEFINE(type, name)
VNET_DEFINE_STATIC(type, name)
```

```c
#define	V_name	VNET(name)
```

### 虚拟实例选择

```c
CRED_TO_VNET(struct ucred *)
TD_TO_VNET(struct thread *)
P_TO_VNET(struct proc *)
IS_DEFAULT_VNET(struct vnet *)
VNET_ASSERT(exp, msg)
CURVNET_SET(struct vnet *)
CURVNET_SET_QUIET(struct vnet *)
CURVNET_RESTORE()
VNET_ITERATOR_DECL(struct vnet *)
VNET_FOREACH(struct vnet *)
```

### 锁定

```c
VNET_LIST_RLOCK()
VNET_LIST_RUNLOCK()
VNET_LIST_RLOCK_NOSLEEP()
VNET_LIST_RUNLOCK_NOSLEEP()
```

### 启动与拆除函数

```c
struct vnet *
vnet_alloc(void)

void
vnet_destroy(struct vnet *)

VNET_SYSINIT(ident, enum sysinit_sub_id subsystem,
    enum sysinit_elem_order order, sysinit_cfunc_t func,
    const void *arg)

VNET_SYSUNINIT(ident, enum sysinit_sub_id subsystem,
    enum sysinit_elem_order order, sysinit_cfunc_t func,
    const void *arg)
```

### 事件处理器

```c
VNET_GLOBAL_EVENTHANDLER_REGISTER(const char *name, void *func,
    void *arg, int priority)

VNET_GLOBAL_EVENTHANDLER_REGISTER_TAG(eventhandler_tag tag,
    const char *name, void *func, void *arg, int priority)
```

## 描述

`VNET` 是一种用于虚拟化网络栈的技术名称。其基本思想是将全局资源（最显著的是变量）转变为每个网络栈独立的资源，并让函数、sysctl、事件处理器等在正确实例的上下文中访问和处理它们。每个（虚拟）网络栈附加到一个 *prison* 上，其中 `vnet0` 是基础系统的无限制默认网络栈。

`VNET_SETNAME` 和 `VNET_SYMPREFIX` 的全局定义与 kvm(3) 共享，用于出于调试原因访问内部实现。

### 变量声明

通过使用 `VNET_DEFINE` 宏而不是将变量写为 *type name* 来虚拟化变量。仍然可以使用静态初始化，例如：

```c
VNET_DEFINE(int, foo) = 1;
```

使用 static 关键字声明的变量可以使用 `VNET_DEFINE_STATIC` 宏，例如：

```c
VNET_DEFINE_STATIC(SLIST_HEAD(, bar), bars);
```

当虚拟化变量需要被引用时（例如使用 "TAILQ_HEAD_INITIALIZER()"），无法使用静态初始化。在这种情况下，必须使用基于 `VNET_SYSINIT` 的初始化函数。

外部变量必须使用 `VNET_DECLARE` 宏声明。在上述任一情况下，约定是定义另一个宏，然后在整个实现中使用它来访问该变量。变量名通常以 *V_* 为前缀以表示它是虚拟化的。`VNET` 宏随后将对该变量的访问转换为当前选定实例的副本（参见“虚拟实例选择”小节）：

```c
#define V_name VNET(name)
```

*注意：* 不要将此与 [VFS(9)](vfs.9.md) 使用的约定混淆。

`VNET_NAME` 宏返回在虚拟网络栈实例内存区域内的偏移量。

### 虚拟实例选择

当前虚拟网络栈指针存储在三个不同的位置，可以从这些位置获取：

- 一个 *prison*：为方便起见，提供了以下宏：

```c
(struct prison *)->pr_vnet
```

```c
CRED_TO_VNET(struct ucred *)
TD_TO_VNET(struct thread *)
P_TO_VNET(struct proc *)
```

- 一个 *socket*：

```c
(struct socket *)->so_vnet
```

- 一个 *interface*：

```c
(struct ifnet *)->if_vnet
```

此外，当前活动实例缓存在 "curthread->td_vnet" 中，通常仅通过 `curvnet` 宏访问。

要设置当前虚拟网络实例的正确上下文，请使用 `CURVNET_SET` 或 `CURVNET_SET_QUIET` 宏。如果内核编译时启用了 `options VNET_DEBUG`，`CURVNET_SET_QUIET` 版本不会记录 vnet 递归，因此只应在递归不可避免的已知情况下使用。这两个宏都会将先前的状态保存在栈上，并且必须使用 `CURVNET_RESTORE` 宏来恢复。

*注意：* 由于先前的状态保存在栈上，不能在同一块中多次调用 `CURVNET_SET`。

*注意：* 由于先前的状态保存在栈上，`CURVNET_RESTORE` 调用必须与 `CURVNET_SET` 调用在同一块中，或者在与外层块具有相同已保存实例视图的子块中。

*注意：* 由于每个宏都是一组操作，并且如前所述在定义时不能放入自己的块中，因此不能有条件地设置当前 vnet 上下文。以下方式*不*起作用：

```c
if (condition)
	CURVNET_SET(vnet);
```

以下方式也不起作用：

```c
if (condition) {
	CURVNET_SET(vnet);
}
CURVNET_RESTORE();
```

有时需要遍历所有虚拟实例，例如将全局状态更新到虚拟实例、为每个实例从 [callout(9)](callout.9.md) 运行函数等。对于这些情况，提供了 `VNET_ITERATOR_DECL` 和 `VNET_FOREACH` 宏。前者定义遍历循环的变量，后者遍历所有虚拟网络栈实例。关于如何安全地遍历所有虚拟实例的列表，请参见“锁定”小节。

`IS_DEFAULT_VNET` 宏提供了一种安全的方法来检查当前活动实例是否是基础系统的无限制默认网络栈（`vnet0`）。

`VNET_ASSERT` 宏提供了一种有条件添加断言的方法，这些断言仅在编译时启用了 `options VIMAGE` 并且同时启用了 `options VNET_DEBUG` 或 `options INVARIANTS` 时才激活。它使用与 [KASSERT(9)](kassert.9.md) 相同的语义。

### 锁定

对于公共访问虚拟网络栈实例列表（例如通过 `VNET_FOREACH` 宏），提供了读锁。使用宏来抽象出锁的实际类型。如果调用者在遍历列表时可能休眠，则必须使用 `VNET_LIST_RLOCK` 和 `VNET_LIST_RUNLOCK` 宏。否则，调用者可以使用 `VNET_LIST_RLOCK_NOSLEEP` 和 `VNET_LIST_RUNLOCK_NOSLEEP`。

### 启动与拆除函数

要启动或拆除虚拟网络栈实例，提供了内部函数 `vnet_alloc` 和 `vnet_destroy`，并由 jail 框架调用。它们运行公开提供的方法来处理网络栈的启动和拆除。

对于公共控制，系统启动接口已得到增强，不仅可以处理系统引导，还可以处理虚拟网络栈的启动和拆除。对于基础系统，`VNET_SYSINIT` 和 `VNET_SYSUNINIT` 宏看起来与没有虚拟网络栈时完全一样。事实上，如果编译时未启用 `options VIMAGE`，它们会被编译为标准的 `SYSINIT` 宏。除此之外，它们在启动时为每个虚拟网络栈运行，或者在关闭时以相反顺序运行。

### 事件处理器

事件处理器可以以两种方式处理：

- 在每个虚拟实例中保存返回的 *tag*，并在拆除时使用这些 tag 正确释放事件处理器，或者
- 使用一个将遍历所有虚拟网络栈实例的事件处理器。

对于第一种情况，可以直接使用普通的 [EVENTHANDLER(9)](eventhandler.9.md) 函数；对于第二种情况，提供了 `VNET_GLOBAL_EVENTHANDLER_REGISTER` 和 `VNET_GLOBAL_EVENTHANDLER_REGISTER_TAG` 宏。它们的区别在于 `VNET_GLOBAL_EVENTHANDLER_REGISTER_TAG` 接受一个额外的第一个参数，该参数在返回时将携带 `tag`。使用其中任一宏注册的事件处理器不会直接运行 `func`，而是 `func` 将由内部迭代器函数为每个 vnet 调用。这两个宏只能用于不接受额外参数的事件处理器，因为来自 EVENTHANDLER_INVOKE(9) 调用的可变参数将被忽略。

### Sysctl 处理

可以通过将 `CTLFLAG_VNET` 控制标志添加到宏的 ctlflags 位掩码来虚拟化 [sysctl(9)](sysctl.9.md)。

## 参见

[jail(2)](../man2/jail.2.md), [kvm(3)](../man3/kvm.3.md), [EVENTHANDLER(9)](eventhandler.9.md), [KASSERT(9)](kassert.9.md), [sysctl(9)](sysctl.9.md)

Marko Zec, Implementing a Clonable Network Stack in the FreeBSD Kernel, USENIX ATC'03, June 2003, Boston

## 历史

虚拟网络栈实现首次出现于 FreeBSD 8.0。

## 作者

`VNET` 框架由 Marko Zec 在萨格勒布大学设计并实现，由 FreeBSD 基金会和 NLnet 基金会赞助，后来由 Bjoern A. Zeeb（同样在 FreeBSD 基金会赞助下）和 Robert Watson 进行了扩展和改进。

本手册页由 Bjoern A. Zeeb（CK Software GmbH）编写，由 FreeBSD 基金会赞助。
