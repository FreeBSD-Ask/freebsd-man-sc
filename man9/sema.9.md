# sema(9)

`sema` — 内核计数信号量

## 名称

`sema`, `sema_init`, `sema_destroy`, `sema_post`, `sema_wait`, `sema_timedwait`, `sema_trywait`, `sema_value`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/lock.h>
```

```c
#include <sys/sema.h>
```

```c
void
sema_init(struct sema *sema, int value, const char *description)

void
sema_destroy(struct sema *sema)

void
sema_post(struct sema *sema)

void
sema_wait(struct sema *sema)

int
sema_timedwait(struct sema *sema, int timo)

int
sema_trywait(struct sema *sema)

int
sema_value(struct sema *sema)
```

## 描述

计数信号量提供了一种同步访问资源池的机制。与互斥锁不同，信号量没有所有者的概念，因此它们也可以在一个线程需要获取资源而另一个线程需要释放资源的情况下使用。每个信号量都有一个关联的整数值。发布（递增）总是成功，但等待（递减）只有在信号量的结果值大于或等于零时才能成功完成。

不应在互斥锁和条件变量足够的地方使用信号量。信号量是比互斥锁和条件变量更复杂的同步机制，效率也不如后者。

信号量通过 `sema_init` 创建，其中 `sema` 是指向 `struct sema` 空间的指针，`value` 是信号量的初始值，`description` 是指向描述信号量的以空字符结尾字符串的指针。信号量通过 `sema_destroy` 销毁。信号量通过 `sema_post` 发布（递增）。信号量通过 `sema_wait`、`sema_timedwait` 或 `sema_trywait` 等待（递减）。`sema_timedwait` 的 `timo` 参数指定在返回失败之前等待的最小时间（以 tick 为单位）。`sema_value` 用于读取信号量的当前值。

## 返回值

`sema_value` 函数返回信号量的当前值。

如果递减信号量会导致其值为负，`sema_trywait` 返回 0 表示失败。否则，返回非零值表示成功。

`sema_timedwait` 函数在等待信号量成功时返回 0；否则返回非零错误代码。

## 错误

`sema_timedwait` 函数在以下情况下会失败：

**[`EWOULDBLOCK`]** 超时已过。

## 参见

[condvar(9)](condvar.9.md), [locking(9)](locking.9.md), [mtx_pool(9)](mtx_pool.9.md), [mutex(9)](mutex.9.md), [rwlock(9)](rwlock.9.md), [sx(9)](sx.9.md)
