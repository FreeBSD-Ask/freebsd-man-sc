# atomic(9)

`atomic_add` — 原子操作

## 名称

`atomic_add`, `atomic_clear`, `atomic_cmpset`, `atomic_fcmpset`, `atomic_fetchadd`, `atomic_interrupt_fence`, `atomic_load`, `atomic_readandclear`, `atomic_set`, `atomic_subtract`, `atomic_store`, `atomic_thread_fence`

## 概要

```c
#include <machine/atomic.h>
```

```c
void
atomic_add_[acq_|rel_]<type>(volatile <type> *p, <type> v)

void
atomic_clear_[acq_|rel_]<type>(volatile <type> *p, <type> v)

int
atomic_cmpset_[acq_|rel_]<type>(volatile <type> *dst, <type> old, <type> new)

int
atomic_fcmpset_[acq_|rel_]<type>(volatile <type> *dst, <type> *old, <type> new)

<type>
atomic_fetchadd_<type>(volatile <type> *p, <type> v)

void
atomic_interrupt_fence(void)

<type>
atomic_load_[acq_]<type>(const volatile <type> *p)

<type>
atomic_readandclear_<type>(volatile <type> *p)

void
atomic_set_[acq_|rel_]<type>(volatile <type> *p, <type> v)

void
atomic_subtract_[acq_|rel_]<type>(volatile <type> *p, <type> v)

void
atomic_store_[rel_]<type>(volatile <type> *p, <type> v)

<type>
atomic_swap_<type>(volatile <type> *p, <type> v)

int
atomic_testandclear_<type>(volatile <type> *p, u_int v)

int
atomic_testandset_<type>(volatile <type> *p, u_int v)

void
atomic_thread_fence_[acq|acq_rel|rel|seq_cst](void)
```

## 描述

原子操作通常用于实现引用计数，并作为互斥锁等同步原语的构建块。

所有这些操作在多线程和中断存在的情况下都以*原子方式*执行，这意味着从并发运行的线程和中断处理程序的角度来看，它们以不可分割的方式执行。

在 FreeBSD 支持的所有架构上，如果整数自然对齐且其大小不超过处理器的字长，则在缓存一致性内存中对整数的普通加载和存储本质上是原子的。然而，编译器可能会从程序中省略此类加载和存储，而原子操作始终会执行。

在缓存一致性内存上执行原子操作时，对同一位置的所有操作都是完全有序的。

对缓存一致性内存中的位置执行原子加载时，它读取的是由对该位置的每个字节的最后一次原子存储定义的整个值。原子加载绝不会返回凭空出现的值。对某个位置执行原子存储时，没有其他线程或中断处理程序会观察到*撕裂写入*或对该位置的部分修改。

除下文注明的例外情况外，这些操作的语义与同名的 C11 原子操作几乎相同。

### 类型

大多数原子操作作用于特定的 `type`。该类型在函数名中指示。与 C11 原子操作不同，FreeBSD 的原子操作作用于普通整数类型。可用类型有：

**`int`** 无符号整数

**`long`** 无符号长整数

**`ptr`** 指针大小的无符号整数

**`32`** 无符号 32 位整数

**`64`** 无符号 64 位整数

例如，原子地将两个整数相加的函数称为 `atomic_add_int`。

某些架构还提供对小于 "`int`" 类型的操作。

**`char`** 无符号字符

**`short`** 无符号短整数

**`8`** 无符号 8 位整数

**`16`** 无符号 16 位整数

这些类型不得用于与机器无关的代码中。

### 获取和释放操作

默认情况下，线程对不同内存位置的访问可能不会按*程序顺序*（即访问在源代码中出现的顺序）执行。为了优化程序的执行，编译器和处理器都可能重新排序线程的访问。然而，两者都确保其重新排序对线程本身不可见。否则，将违反单线程程序所期望的传统内存模型。尽管如此，多线程程序（如 FreeBSD 内核）中的其他线程可能会观察到这种重新排序。此外，在某些情况下，例如线程间同步的实现，任意重新排序可能导致程序执行不正确。为约束编译器和处理器可能对线程访问执行的重新排序，程序员可以使用具有*获取*（acquire）和*释放*（release）语义的原子操作。

内存上的原子操作最多有三种变体。第一种即*宽松*（relaxed）变体，执行操作时不施加任何对其他内存位置访问的顺序约束。此变体是默认的。第二种变体具有获取语义，第三种变体具有释放语义。

只有当原子操作执行从内存加载时，才能具有*获取*语义。当原子操作具有获取语义时，作为操作一部分执行的加载必须先完成，然后才能执行任何后续的加载或存储（按程序顺序）。相反，获取语义不要求先前的加载或存储在原子操作的加载执行之前完成。为表示获取语义，后缀 "`_acq`" 插入到函数名中紧靠 "`_`<`type`>" 后缀之前的位置。例如，要减去两个整数并确保从内存加载值先于任何后续加载和存储完成，使用 `atomic_subtract_acq_int`。

只有当原子操作执行存储到内存时，才能具有*释放*语义。当原子操作具有释放语义时，所有先前的加载或存储（按程序顺序）必须先完成，然后才能执行作为操作一部分执行的存储。相反，释放语义不要求原子操作的存储在执行任何后续加载或存储之前完成。为表示释放语义，后缀 "`_rel`" 插入到函数名中紧靠 "`_`<`type`>" 后缀之前的位置。例如，要加两个长整数并确保所有先前的加载和存储在存储结果之前完成，使用 `atomic_add_rel_long`。

当一个线程的释放操作与另一个线程的获取操作*同步*（通常意味着获取操作读取释放操作写入的值）时，释放线程先前所有存储的效果必须对获取线程后续的加载可见。此外，对释放线程可见的所有其他线程的存储效果也必须对获取线程可见。这些规则仅适用于同步的线程。其他线程可能以不同的顺序观察这些存储。

实际上，具有获取和释放语义的原子操作建立了单向的重新排序屏障，使同步原语的实现能够表达其顺序要求，而不会施加不必要的顺序。例如，对于由互斥锁保护的临界区，在锁定互斥锁时的获取操作和解锁互斥锁时的释放操作将防止任何加载或存储移出临界区。然而，它们不会阻止编译器或处理器将加载或存储移入临界区，这并不违反互斥锁的语义。

### 比较并交换的架构相关注意事项

`atomic_[f]cmpset_<type>` 操作，特别是那些没有明确指定内存顺序的操作，定义为宽松的。因此，线程对与原子操作位置不同的内存位置的访问可以相对于原子操作重新排序。

然而，**amd64** 和 **i386** 架构上的实现提供顺序一致语义。特别是，上述重新排序不会发生。

在 **arm64/aarch64** 架构上，操作可能包含组成部分加载的获取语义或组成部分存储的释放语义。这意味着，按程序顺序在原子操作之前对其他位置的访问，可能被观察为在作为原子操作一部分的加载之后执行（但由于释放语义，不会在操作的存储之后）。类似地，原子操作之后的访问可能被观察为在存储之前执行。

### 线程栅栏操作

或者，程序员可以使用原子线程栅栏操作来约束访问的重新排序。与其他原子操作不同，栅栏本身不访问内存。

当栅栏具有获取语义时，所有先前的加载（按程序顺序）必须先完成，然后才能执行任何后续加载或存储。因此，获取栅栏是加载操作的双向屏障。为表示获取语义，后缀 "`_acq`" 附加到函数名，例如 `atomic_thread_fence_acq`。

当栅栏具有释放语义时，所有先前的加载或存储（按程序顺序）必须先完成，然后才能执行任何后续存储操作。因此，释放栅栏是存储操作的双向屏障。为表示释放语义，后缀 "`_rel`" 附加到函数名，例如 `atomic_thread_fence_rel`。

虽然 `atomic_thread_fence_acq_rel` 实现了获取和释放语义，但它不是完整屏障。例如，栅栏之前的存储（按程序顺序）可能在栅栏之后的加载之后完成。相比之下，`atomic_thread_fence_seq_cst` 实现了完整屏障。加载和存储都不能在任何方向上跨越此屏障。

在 C11 中，当一个线程的释放栅栏与另一个线程的获取栅栏同步时，获取栅栏之前的原子加载（按程序顺序）读取释放栅栏之后的原子存储写入的值。相比之下，在 FreeBSD 中，由于普通自然对齐的加载和存储的原子性，栅栏也可以由普通的加载和存储同步。这简化了 FreeBSD 中某些同步原语的实现和使用。

由于编译器和处理器都无法预见哪个（原子）加载将读取（原子）存储写入的值，栅栏施加的顺序约束必须比获取加载和释放存储更具限制性。本质上，这就是栅栏是双向屏障的原因。

虽然栅栏比获取加载和释放存储施加更严格的顺序，但通过将访问与顺序分离，它们有时可以促进同步原语的更高效实现。例如，它们可用于避免执行内存屏障，直到内存访问表明满足某些条件。

### 中断栅栏操作

`atomic_interrupt_fence` 函数在其调用位置与在同一 CPU 上执行的任何中断处理程序之间建立顺序。它仿照类似的 C11 函数 `atomic_signal_fence`，并针对内核环境进行了适配。

### 多处理器

在多处理器系统中，内存上原子操作的原子性取决于底层架构对缓存一致性的支持。通常，FreeBSD 支持的所有架构都保证默认内存类型 `VM_MEMATTR_DEFAULT` 的缓存一致性。例如，amd64 和 i386 架构在写回内存上保证缓存一致性。然而，在某些架构上，可能并非在所有内存类型上都启用缓存一致性。要确定非默认内存类型是否启用了缓存一致性，请查阅架构文档。

### 语义

本节使用类似 C 的表示法描述每个操作的语义。

```c
*p += v;
```

```c
*p &= ~v;
```

```c
if (*dst == old) {
	*dst = new;
	return (1);
} else
	return (0);
```

**`atomic_add`**(p, v)

**`atomic_clear`**(p, v)

**`atomic_cmpset`**(dst, old, new)

某些架构不为 "`char`"、"`short`"、"`8`" 和 "`16`" 类型实现 `atomic_cmpset` 函数。

**`atomic_fcmpset`**(dst, *old, new)

在硬件中实现*比较并交换*（Compare And Swap）操作的架构上，功能可描述为

```c
if (*dst == *old) {
	*dst = new;
	return (1);
} else {
	*old = *dst;
	return (0);
}
```

在提供*加载链接/存储条件*（Load Linked/Store Conditional）原语的架构上，写入 `*dst` 也可能因多种原因失败，其中最重要的是其他 CPU 对 `*dst` 缓存行的并行写入。在这种情况下，`atomic_fcmpset` 函数也返回 `false`，尽管

```c
*old == *dst 。
```

某些架构不为 "`char`"、"`short`"、"`8`" 和 "`16`" 类型实现 `atomic_fcmpset` 函数。

```c
tmp = *p;
*p += v;
return (tmp);
```

**`atomic_fetchadd`**(p, v)

`atomic_fetchadd` 函数仅为 "`int`"、"`long`" 和 "`32`" 类型实现，目前没有任何带内存屏障的变体。

```c
return (*p);
```

```c
tmp = *p;
*p = 0;
return (tmp);
```

**`atomic_load`**(p)

**`atomic_readandclear`**(p)

`atomic_readandclear` 函数不为 "`char`"、"`short`"、"`ptr`"、"`8`" 和 "`16`" 类型实现，目前没有任何带内存屏障的变体。

```c
*p |= v;
```

```c
*p -= v;
```

```c
*p = v;
```

```c
tmp = *p;
*p = v;
return (tmp);
```

**`atomic_set`**(p, v)

**`atomic_subtract`**(p, v)

**`atomic_store`**(p, v)

**`atomic_swap`**(p, v)

`atomic_swap` 函数不为 "`char`"、"`short`"、"`ptr`"、"`8`" 和 "`16`" 类型实现，目前没有任何带内存屏障的变体。

```c
bit = 1 << (v % (sizeof(*p) * NBBY));
tmp = (*p & bit) != 0;
*p &= ~bit;
return (tmp);
```

**`atomic_testandclear`**(p, v)

```c
bit = 1 << (v % (sizeof(*p) * NBBY));
tmp = (*p & bit) != 0;
*p |= bit;
return (tmp);
```

**`atomic_testandset`**(p, v)

`atomic_testandset` 和 `atomic_testandclear` 函数仅为 "`int`"、"`long`"、"ptr"、"`32`" 和 "`64`" 类型实现，目前通常没有任何带内存屏障的变体，除了 `atomic_testandset_acq_long`。

"`64`" 类型目前在 arm、i386 和 powerpc 架构上的某些原子操作中未实现。

## 返回值

`atomic_cmpset` 函数返回比较操作的结果。`atomic_fcmpset` 函数在操作成功时返回 `true`。否则返回 `false` 并将 `*old` 设置为找到的值。`atomic_fetchadd`、`atomic_load`、`atomic_readandclear` 和 `atomic_swap` 函数返回指定地址处的值。`atomic_testandset` 和 `atomic_testandclear` 函数返回测试操作的结果。

## 实例

此示例使用 `atomic_cmpset_acq_ptr` 和 `atomic_set_ptr` 函数获取睡眠互斥锁并处理递归。由于 `struct mtx` 的 `mtx_lock` 成员是指针，因此使用 "`ptr`" 类型。

```c
/* 尝试获取 mtx_lock 一次。 */
#define _obtain_lock(mp, tid)						\
	atomic_cmpset_acq_ptr(&(mp)->mtx_lock, MTX_UNOWNED, (tid))
/* 获取睡眠锁，内联处理递归。 */
#define _get_sleep_lock(mp, tid, opts, file, line) do {			\
	uintptr_t _tid = (uintptr_t)(tid);				\
									\
	if (!_obtain_lock(mp, tid)) {					\
		if (((mp)->mtx_lock & MTX_FLAGMASK) != _tid)		\
			_mtx_lock_sleep((mp), _tid, (opts), (file), (line));\
		else {							\
			atomic_set_ptr(&(mp)->mtx_lock, MTX_RECURSE);	\
			(mp)->mtx_recurse++;				\
		}							\
	}								\
} while (0)
```

## 历史

`atomic_add`、`atomic_clear`、`atomic_set` 和 `atomic_subtract` 操作引入于 FreeBSD 3.0。最初，这些操作定义在 "`char`"、"`short`"、"`int`" 和 "`long`" 类型上。

`atomic_cmpset`、`atomic_load_acq`、`atomic_readandclear` 和 `atomic_store_rel` 操作添加于 FreeBSD 5.0。同时引入了获取和释放变体，并添加了对 "`8`"、"`16`"、"`32`"、"`64`" 和 "`ptr`" 类型的操作支持。

`atomic_fetchadd` 操作添加于 FreeBSD 6.0。

`atomic_swap` 和 `atomic_testandset` 操作添加于 FreeBSD 10.0。

`atomic_testandclear` 和 `atomic_thread_fence` 操作添加于 FreeBSD 11.0。

`atomic_load` 和 `atomic_store` 的宽松变体添加于 FreeBSD 12.0。

`atomic_interrupt_fence` 操作添加于 FreeBSD 13.0。
