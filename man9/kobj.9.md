# kobj(9)

`kobj` — FreeBSD 的内核对象系统

## 名称

`kobj`

## 概要

```c
#include <sys/param.h>
#include <sys/kobj.h>
```

```c
void
kobj_class_compile(kobj_class_t cls)

void
kobj_class_compile_static(kobj_class_t cls, kobj_ops_t ops)

void
kobj_class_free(kobj_class_t cls)

kobj_t
kobj_create(kobj_class_t cls, struct malloc_type *mtype, int mflags)

void
kobj_init(kobj_t obj, kobj_class_t cls)

void
kobj_init_static(kobj_t obj, kobj_class_t cls)

void
kobj_delete(kobj_t obj, struct malloc_type *mtype)

DEFINE_CLASS(name, kobj_method_t *methods, size_t size)
```

## 描述

内核对象系统在 FreeBSD 内核中实现了一个面向对象编程系统。该系统基于以下概念：接口，即方法集的描述；类，即实现这些接口中某些方法的函数列表；以及对象，即将类与内存中的结构相结合。

方法使用动态方法分派算法调用，该算法设计为允许在运行时向系统引入新的接口和类。方法分派算法设计为既快速又健壮，且仅比直接函数调用略高一点开销，使内核对象适合性能关键的算法。

内核对象的合适用途是任何需要某种多态性的算法（即许多可以统一处理的不同对象）。对象的共同行为由合适的接口描述，每种不同类型的对象由合适的类实现。

创建内核对象最简单的方法是使用合适的类、malloc 类型和标志调用 `kobj_create`（有关 malloc 类型和标志的描述，参见 [malloc(9)](malloc.9.md)）。这将根据类指定的对象大小为对象分配内存，并通过将内存清零并安装指向类方法分派表的指针来初始化它。以这种方式创建的对象应通过调用 `kobj_delete` 来释放。

希望自己管理内存分配的客户端应使用指向对象内存和实现它的类的指针调用 `kobj_init` 或 `kobj_init_static`。也可以使用 `kobj_init` 和 `kobj_init_static` 来更改对象的类。这应谨慎进行，因为类必须就对象的布局达成一致。设备框架使用此功能将驱动程序与设备关联。

`kobj_class_compile`、`kobj_class_compile_static` 和 `kobj_class_free` 函数用于处理类描述以使方法分派高效。客户端通常不需要调用这些，因为类将在首次使用时自动编译。如果要在 [malloc(9)](malloc.9.md) 和 [mutex(9)](mutex.9.md) 初始化之前使用类，则应在类用于初始化任何对象之前，使用类和指向静态分配的 `kobj_ops` 结构的指针调用 `kobj_class_compile_static`。在这种情况下，也应使用 `kobj_init_static` 而不是 `kobj_init`。

要定义类，首先定义一个简单的 `kobj_method_t` 数组。类实现的每个方法都应使用 `KOBJMETHOD` 宏输入到表中，该宏接受方法名（包括其接口）和指向实现它的函数的指针。表应以两个零终止。然后可以使用 `DEFINE_CLASS` 宏来初始化 `kobj_class_t` 结构。`DEFINE_CLASS` 的 size 参数指定应为每个对象分配多少内存。

## 历史

此接口的一些概念首次出现在 FreeBSD 3.0 的 alpha 移植版使用的设备框架中，并在 FreeBSD 4.0 中更广泛地使用。

## 作者

本手册页由 Doug Rabson 编写。
