# pthread_rwlock_destroy.3

`pthread_rwlock_destroy` — 销毁读写锁

## 名称

`pthread_rwlock_destroy`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_rwlock_destroy(pthread_rwlock_t *lock);
```

## 描述

`pthread_rwlock_destroy` 函数用于销毁此前由 `pthread_rwlock_init` 创建的读写锁。

## 返回值

如果成功，`pthread_rwlock_destroy` 函数将返回零。否则返回一个错误编号以指示错误。

## 错误

`pthread_rwlock_destroy` 函数在以下情况下将失败：

**`[EPERM]`** 调用者没有执行该操作的权限。

`pthread_rwlock_destroy` 函数在以下情况下可能失败：

**`[EBUSY]`** 系统检测到试图在 `lock` 引用的对象处于锁定状态时销毁该对象。

**`[EINVAL]`** 由 `lock` 指定的值无效。

## 参见

[pthread_rwlock_init(3)](pthread_rwlock_init.3.md)

## 标准

`pthread_rwlock_destroy` 函数预期遵循 Version 2 of the Single UNIX Specification (“SUSv2”) 标准。

## 历史

`pthread_rwlock_destroy` 函数首次出现于 FreeBSD 3.0。
