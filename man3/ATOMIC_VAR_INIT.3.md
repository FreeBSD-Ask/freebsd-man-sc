# ATOMIC_VAR_INIT.3

`ATOMIC_VAR_INIT` — 类型通用的原子操作

## 名称

`ATOMIC_VAR_INIT`, `atomic_init`, `atomic_load`, `atomic_store`, `atomic_exchange`, `atomic_compare_exchange_strong`, `atomic_compare_exchange_weak`, `atomic_fetch_add`, `atomic_fetch_and`, `atomic_fetch_or`, `atomic_fetch_sub`, `atomic_fetch_xor`, `atomic_is_lock_free`

## 概要

`#include <stdatomic.h>`

```c
_Atomic(T) v = ATOMIC_VAR_INIT(c);
void atomic_init(_Atomic(T) *object, T value);
T atomic_load(_Atomic(T) *object);
T atomic_load_explicit(_Atomic(T) *object, memory_order order);
void atomic_store(_Atomic(T) *object, T desired);
void atomic_store_explicit(_Atomic(T) *object, T desired, memory_order order);
T atomic_exchange(_Atomic(T) *object, T desired);
T atomic_exchange_explicit(_Atomic(T) *object, T desired, memory_order order);
_Bool atomic_compare_exchange_strong(_Atomic(T) *object, T *expected, T desired);
_Bool atomic_compare_exchange_strong_explicit(_Atomic(T) *object, T *expected, T desired, memory_order success, memory_order failure);
_Bool atomic_compare_exchange_weak(_Atomic(T) *object, T *expected, T desired);
_Bool atomic_compare_exchange_weak_explicit(_Atomic(T) *object, T *expected, T desired, memory_order success, memory_order failure);
T atomic_fetch_add(_Atomic(T) *object, T operand);
T atomic_fetch_add_explicit(_Atomic(T) *object, T operand, memory_order order);
T atomic_fetch_and(_Atomic(T) *object, T operand);
T atomic_fetch_and_explicit(_Atomic(T) *object, T operand, memory_order order);
T atomic_fetch_or(_Atomic(T) *object, T operand);
T atomic_fetch_or_explicit(_Atomic(T) *object, T operand, memory_order order);
T atomic_fetch_sub(_Atomic(T) *object, T operand);
T atomic_fetch_sub_explicit(_Atomic(T) *object, T operand, memory_order order);
T atomic_fetch_xor(_Atomic(T) *object, T operand);
T atomic_fetch_xor_explicit(_Atomic(T) *object, T operand, memory_order order);
_Bool atomic_is_lock_free(const _Atomic(T) *object);
```

## 描述

头文件

```c
#include <stdatomic.h>
```

提供了类型通用的原子操作宏。多线程程序可借助原子操作在线程间共享变量，多数情况下无需获取锁即可修改这些变量。

原子变量通过 `_Atomic` 类型说明符声明。这类变量与其非原子版本在类型上不兼容。根据所用编译器的不同，原子变量可能是不透明的，因此只能借助本文描述的宏来操作。

`atomic_init` 宏使用值 `value` 初始化原子变量 `object`。声明原子变量时可通过 `ATOMIC_VAR_INIT` 进行初始化。

`atomic_load` 宏返回原子变量 `object` 的值。`atomic_store` 宏将原子变量 `object` 设置为期望的 `desired` 值。

`atomic_exchange` 宏结合了 `atomic_load` 与 `atomic_store` 的行为。它将原子变量 `object` 设置为期望的 `value`，并返回该原子变量的原始内容。

`atomic_compare_exchange_strong` 宏仅在原子变量等于 `expected` 值时，将 `desired` 值存入原子变量 `object`。成功时该宏返回 `true`；失败时 `desired` 值会被原子变量的当前值覆盖，并返回 `false`。`atomic_compare_exchange_weak` 宏与 `atomic_compare_exchange_strong` 行为一致，但即使原子变量 `object` 等于 `expected` 值，也允许失败。

`atomic_fetch_add` 宏将值 `operand` 加到原子变量 `object` 上，并返回该原子变量的原始内容。

`atomic_fetch_and` 宏对原子变量 `object` 与 `operand` 应用 *and* 运算符，将结果存入 `object`，并返回该原子变量的原始内容。

`atomic_fetch_or` 宏对原子变量 `object` 与 `operand` 应用 *or* 运算符，将结果存入 `object`，并返回该原子变量的原始内容。

`atomic_fetch_sub` 宏从原子变量 `object` 中减去值 `operand`，并返回该原子变量的原始内容。

`atomic_fetch_xor` 宏对原子变量 `object` 与 `operand` 应用 *xor* 运算符，将结果存入 `object`，并返回该原子变量的原始内容。

`atomic_is_lock_free` 宏返回原子变量 `object` 在执行原子操作时是否使用锁。

## 内存屏障

前述原子操作在实现上禁止编译器和执行处理器将附近的内存操作重排到原子操作前后。某些情况下，这种行为会导致性能下降。为缓解此问题，每个原子操作都有一个 `_explicit` 版本，允许配置重排行为。

这些 `_explicit` 宏的 `order` 参数可取以下值之一。

**`memory_order_relaxed`** 无任何内存排序。

**`memory_order_consume`** 执行 consume 操作。

**`memory_order_acquire`** Acquire 屏障。

**`memory_order_release`** Release 屏障。

**`memory_order_acq_rel`** Acquire 与 release 屏障。

**`memory_order_seq_cst`** 顺序一致的 acquire 与 release 屏障。

当 `order` 为 `memory_order_seq_cst` 时，前述非显式宏与对应的 `_explicit` 宏行为一致。

## 编译器支持

这些原子操作通常由编译器实现，因为它们必须以类型通用方式实现，并且常常需要使用特殊的硬件指令。由于该接口尚未被大多数编译器采纳，头文件

```c
#include <stdatomic.h>
```

在现有编译器内建功能之上实现了这些宏，以提供前向兼容性。

这意味着接口的某些方面（例如对不同屏障类型的支持）可能被忽略。使用 GCC 时，所有原子操作的执行效果等同于使用 `memory_order_seq_cst`。

ISO/IEC 9899:2011（"ISO C11"）允许直接使用语言内建操作符修改原子变量，而不必使用本接口提供的原子操作。这种行为无法在较老的编译器上模拟。为防止对这些变量的意外非原子访问，使用较老编译器时该头文件会将原子变量放入一个结构体中。

在不被 GCC 内建原子功能支持的架构上，这些宏可能会发出对回退例程的函数调用。这些回退例程仅在 CPU 支持时针对 32 位和 64 位数据类型实现。

## 参见

[pthread(3)](pthread.3.md), [atomic(9)](../man9/atomic.9.md)

## 标准

这些宏尝试遵循 ISO/IEC 9899:2011（"ISO C11"）。

## 历史

这些宏首次出现于 FreeBSD 10.0。

## 作者

Ed Schouten <ed@FreeBSD.org> David Chisnall <theraven@FreeBSD.org>
