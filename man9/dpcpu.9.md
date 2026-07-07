# dpcpu(9)

`dpcpu` — 内核动态每 CPU 内存分配器

## 名称

`dpcpu`

## 概要

```c
#include <sys/pcpu.h>
```

### 每 CPU 变量的定义与声明

```c
DPCPU_DEFINE(type, name)
DPCPU_DEFINE_STATIC(type, name)
DPCPU_DECLARE(type, name)
```

### 当前 CPU 访问函数

```c
DPCPU_PTR(name)
DPCPU_GET(name)
DPCPU_SET(name, value)
```

### 指定 CPU 访问函数

```c
DPCPU_ID_PTR(cpu, name)
DPCPU_ID_GET(cpu, name)
DPCPU_ID_SET(cpu, name, value)
```

## 描述

`dpcpu` 为系统中每个 CPU 实例化一个全局变量实例。动态分配的每 CPU 变量使用 `DPCPU_DEFINE` 定义，它定义一个名为 `name`、类型为 `type` 的变量。可使用任意 C 类型，包括结构和数组。如果未提供初始化，则该变量的每个每 CPU 实例都会被零填充（即如同在 BSS 中分配）：

```c
DPCPU_DEFINE(int, foo_int);
```

也可在定义时静态初始化值，使每个每 CPU 实例以该值初始化：

```c
DPCPU_DEFINE(int, foo_int) = 1;
```

可定义为 `static` 的值必须使用 `DPCPU_DEFINE_STATIC`：

```c
DPCPU_DEFINE_STATIC(int, foo_int);
```

`DPCPU_DECLARE` 生成适合在头文件中使用的每 CPU 变量声明。

当前 CPU 的变量实例可通过 `DPCPU_PTR`（返回指向该每 CPU 实例的指针）、`DPCPU_GET`（获取该每 CPU 实例的值）和 `DPCPU_SET`（设置该每 CPU 实例的值）访问。

与特定 CPU 关联的变量实例可通过 `DPCPU_ID_PTR`、`DPCPU_ID_GET` 和 `DPCPU_ID_SET` 访问函数访问，这些函数接受一个额外的 CPU ID 参数 `cpu`。

### 同步

除了与全局变量相关的常规同步问题（可能涉及使用 [atomic(9)](atomic.9.md)、[mutex(9)](mutex.9.md) 或其他内核同步原语）之外，线程迁移还可能动态地改变线程在操作之间所访问的变量实例。因此，在推理和保护每 CPU 变量时需要额外小心。

例如，可使用 critical_section(9) 来保护访问，以防止在使用过程中被抢占和迁移。或者，可在一系列访问开始时缓存 CPU ID，并使用适当的同步使非原子序列在迁移存在时仍然安全。

```c
DPCPU_DEFINE_STATIC(int, foo_int);
DPCPU_DEFINE_STATIC(struct mutex, foo_lock);
void
foo_int_increment(void)
{
    int cpu, value;
    /* 作为原子访问是安全的。 */
    atomic_add_int(DPCPU_PTR(foo_int), 1);
    /*
     * 用临界区保护，可防止抢占和迁移。
     * 然而，从远程 CPU 实例访问并不安全，
     * 因为临界区仅防止来自当前 CPU 的并发访问。
     */
    critical_enter();
    value = DPCPU_GET(foo_int);
    value++;
    DPCPU_SET(foo_int, value);
    critical_exit();
    /*
     * 用每 CPU 互斥锁保护，可容忍迁移，
     * 但如果在读取 curcpu 之后发生迁移，
     * 可能会从多个 CPU 访问该变量。
     * 只要获取了正确的互斥锁，
     * 对每 CPU 变量的远程访问就是安全的。
     */
    cpu = curcpu;
    mtx_lock(DPCPU_ID_PTR(cpu, foo_lock));
    value = DPCPU_ID_GET(cpu, foo_int);
    value++;
    DPCPU_ID_SET(cpu, foo_int);
    mtx_unlock(DPCPU_ID_PTR(cpu, foo_lock));
}
```

## 参见

[atomic(9)](atomic.9.md), [critical_enter(9)](critical_enter.9.md), [mutex(9)](mutex.9.md)

## 历史

`DPGPU_ID_SET` 由 Jeff Roberson 在 FreeBSD 8.0 中首次引入。本手册页由 Robert N. M. Watson 编写。
