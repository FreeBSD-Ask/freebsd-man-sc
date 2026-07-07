# sem_destroy(3)

`sem_destroy` — 销毁一个未命名信号量

## 名称

`sem_destroy`

## 库

libc

## 概要

`#include <semaphore.h>`

```c
int
sem_destroy(sem_t *sem);
```

## 描述

`sem_destroy` 函数销毁 `sem` 所指向的未命名信号量。在成功调用 `sem_destroy` 之后， `sem` 将无法使用，直到通过再次调用 [sem_init(3)](sem_init.3.md) 重新初始化。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`sem_destroy` 函数在以下情况下会失败：

**`[EINVAL]`** `sem` 参数指向一个无效的信号量。

**`[EBUSY]`** 当前有线程阻塞在 `sem` 所指向的信号量上。

## 参见

[sem_init(3)](sem_init.3.md)

## 标准

`sem_destroy` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。

POSIX 未定义在有线程阻塞在 `sem` 上时调用 `sem_destroy` 的行为，但本实现保证在有线程阻塞在 `sem` 上时，会返回 -1 并将 `errno` 设置为 `EBUSY`。
