# pthread_spin_lock(3)

`pthread_spin_lock` — 锁定或解锁自旋锁

## 名称

`pthread_spin_lock`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_spin_lock(pthread_spinlock_t *lock)

int
pthread_spin_trylock(pthread_spinlock_t *lock)

int
pthread_spin_unlock(pthread_spinlock_t *lock)
```

## 描述

`pthread_spin_lock` 函数将在 `lock` 当前未被其他线程持有时获取它。如果无法立即获取锁，它将自旋尝试获取锁（不会睡眠）直到锁可用。

`pthread_spin_trylock` 函数与 `pthread_spin_lock` 相同，区别在于如果无法立即获取 `lock`，将返回错误。

`pthread_spin_unlock` 函数将释放 `lock`，该锁必须先前已通过调用 `pthread_spin_lock` 或 `pthread_spin_trylock` 锁定。

## 返回值

如果成功，所有这些函数都将返回零。否则将返回一个错误号以指示错误。

这些函数都不会返回 `EINTR`。

## 错误

`pthread_spin_lock`、`pthread_spin_trylock` 和 `pthread_spin_unlock` 函数将在以下情况失败：

**`[EINVAL]`** 由 `lock` 指定的值无效或未初始化。

`pthread_spin_lock` 函数可能在以下情况失败：

**`[EDEADLK]`** 调用线程已持有该锁。

`pthread_spin_trylock` 函数将在以下情况失败：

**`[EBUSY]`** 另一个线程当前持有 `lock`。

`pthread_spin_unlock` 函数可能在以下情况失败：

**`[EPERM]`** 调用线程未持有 `lock`。

## 参见

pthread_spin_destroy(3), [pthread_spin_init(3)](pthread_spin_init.3.md)

## 历史

`pthread_spin_lock`、`pthread_spin_trylock` 和 `pthread_spin_unlock` 函数首次出现于 FreeBSD 5.2 的 libkse 中，以及 FreeBSD 5.3 的 libthr 中。

## 缺陷

`pthread_spin_lock`、`pthread_spin_trylock` 和 `pthread_spin_unlock` 的实现预期符合 IEEE Std 1003.2 ("POSIX.2") 规范。
