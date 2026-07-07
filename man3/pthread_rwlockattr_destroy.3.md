# pthread_rwlockattr_destroy(3)

`pthread_rwlockattr_destroy` — 销毁读写锁属性对象

## 名称

`pthread_rwlockattr_destroy`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_rwlockattr_destroy(pthread_rwlockattr_t *attr)
```

## 描述

`pthread_rwlockattr_destroy` 函数用于销毁先前通过 `pthread_rwlockattr_init` 创建的读写锁属性对象。

## 返回值

如果成功，`pthread_rwlockattr_destroy` 函数将返回零。否则将返回一个错误号以指示错误。

## 错误

`pthread_rwlockattr_destroy` 函数可能在以下情况失败：

**`[EINVAL]`** 由 `attr` 指定的值无效。

## 参见

[pthread_rwlockattr_init(3)](pthread_rwlockattr_init.3.md)

## 标准

`pthread_rwlockattr_destroy` 函数预期符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。

## 历史

`pthread_rwlockattr_destroy` 函数首次出现于 FreeBSD 3.0。
