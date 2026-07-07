# dllockinit(3)

`dllockinit` — 向动态链接器注册线程锁定方法

## 名称

`dllockinit`

## 库

Lb libc

## 概要

`#include <dlfcn.h>`

```c
void
dllockinit(void *context, void *(*lock_create)(void *context),
    void (*rlock_acquire)(void *lock), void (*wlock_acquire)(void *lock),
    void (*lock_release)(void *lock), void (*lock_destroy)(void *lock),
    void (*context_destroy)(void *context));
```

## 描述

由于动态链接器的增强，此接口已不再需要。它已被弃用，并将在未来的版本中移除。在当前版本中它仍然存在，但仅作为一个什么都不做的存根。

线程包可以在初始化时调用 `dllockinit` 来注册供动态链接器使用的锁定函数。这使得动态链接器能够防止多个线程同时进入其临界区。

`context` 参数指定用于创建锁的不透明上下文。动态链接器在创建所需的锁时会将其传递给 `lock_create` 函数。当动态链接器永久完成对锁定函数的使用时（例如，程序随后调用 `dllockinit` 注册新的锁定函数），它将调用 `context_destroy` 来销毁上下文。

`lock_create` 参数指定一个用于创建读写锁的函数。它必须返回指向新锁的指针。

`rlock_acquire` 和 `wlock_acquire` 参数分别指定为读取或写入而锁定锁的函数。`lock_release` 参数指定解锁锁的函数。这些函数中的每一个都接收指向锁的指针。

`lock_destroy` 参数指定销毁锁的函数。如果锁不需要销毁，它可以为 `NULL`。`context_destroy` 参数指定销毁上下文的函数。如果上下文不需要销毁，它可以为 `NULL`。

在调用 `dllockinit` 之前，动态链接器使用默认的锁定机制保护其临界区，该机制通过阻塞 `SIGVTALRM`、`SIGPROF` 和 `SIGALRM` 信号来工作。这对于许多应用程序级线程包来说已经足够，这些包通常使用这些信号之一来实现抢占。已通过 `dllockinit` 注册了自身锁定方法的应用程序可以通过以所有参数为 `NULL` 调用 `dllockinit` 来恢复默认锁定。

## 参见

[rtld(1)](../man1/rtld.1.md), [signal(3)](signal.3.md)

## 历史

`dllockinit` 函数首次出现于 FreeBSD 4.0。
