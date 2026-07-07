# refcount(9)

`refcount` — 管理简单的引用计数器

## 名称

`refcount`, `refcount_init`, `refcount_acquire`, `refcount_release`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/refcount.h>
```

```c
void
refcount_init(volatile u_int *count, u_int value)

u_int
refcount_load(volatile u_int *count)

u_int
refcount_acquire(volatile u_int *count)

bool
refcount_acquire_checked(volatile u_int *count)

bool
refcount_acquire_if_not_zero(volatile u_int *count)

bool
refcount_release(volatile u_int *count)

bool
refcount_release_if_last(volatile u_int *count)

bool
refcount_release_if_not_last(volatile u_int *count)
```

## 描述

`refcount` 函数提供了管理简单引用计数器的 API。调用者在无符号整数中提供计数器的存储。指向此整数的指针通过 `count` 传递。通常，计数器用于管理对象的生命周期，并作为对象的成员存储。

目前所有函数都实现为 static inline。

`refcount_init` 函数用于将计数器的初始值设置为 `value`。通常在创建引用计数对象时使用。

`refcount_load` 函数返回计数器值的快照。在缺少外部同步的情况下，此值可能立即变为过时。应使用 `refcount_load` 而不是依赖 `volatile` 限定符的属性。

`refcount_acquire` 函数用于获取新引用。它返回获取新引用之前的计数器值。调用者负责确保在获取新引用时持有有效引用。例如，如果对象存储在列表中且列表持有对该对象的引用，则持有保护该列表的锁就为获取新引用提供了足够的保护。

`refcount_acquire_checked` 变体执行与 `refcount_acquire` 相同的操作，但额外检查 `count` 值不会因操作而溢出。如果成功获取引用，则返回 `true`，如果由于溢出未获取，则返回 `false`。

`refcount_acquire_if_not_zero` 函数是 `refcount_acquire` 的另一种变体，它仅在已存在某些引用时获取引用。换句话说，`*count` 必须已大于零函数才能成功，此时返回值为 `true`，否则返回 `false`。

`refcount_release` 函数用于释放现有引用。如果释放的引用是最后一个引用，函数返回 true；否则返回 false。

`refcount_release_if_last` 和 `refcount_release_if_not_last` 函数是 `refcount_release` 的变体，它们分别在是和不是最后一个引用时才丢弃引用。换句话说，`refcount_release_if_last` 在 `*count` 等于 1 时返回 `true`，此时将其递减为零。否则，`*count` 不被修改，函数返回 `false`。类似地，`refcount_release_if_not_last` 在 `*count` 大于 1 时返回 `true`，此时 `*count` 被递减。否则，如果 `*count` 等于 1，引用不被释放，函数返回 `false`。

注意，这些例程不提供任何 CPU 间同步或数据保护来管理计数器。调用者负责任何包含对象的使用者所需的额外同步。此外，调用者还负责管理任何包含对象的生命周期，包括在释放最后一个引用时显式释放任何资源。

`refcount_release` 在释放引用之前无条件执行释放栅栏（参见 [atomic(9)](atomic.9.md)），该栅栏与在返回 `true` 值之前立即执行的获取栅栏同步。这确保了在最后一个引用被丢弃后由调用者执行的析构函数能看到对象生命周期内完成的所有更新。

## 返回值

`refcount_release` 函数在释放最后一个引用时返回 true，在释放任何其他引用时返回 false。

## 历史

这些函数在 FreeBSD 6.0 中引入。
