# pthread_set_name_np.3

`pthread_get_name_np` — 设置和获取线程名称

## 名称

`pthread_get_name_np`, `pthread_getname_np`, `pthread_set_name_np`, `pthread_setname_np`

## 库

libpthread

## 概要

```c
#include <pthread_np.h>

void
pthread_get_name_np(pthread_t thread, char *name, size_t len)

int
pthread_getname_np(pthread_t thread, char *name, size_t len)

void
pthread_set_name_np(pthread_t thread, const char *name)

int
pthread_setname_np(pthread_t thread, const char *name)
```

## 描述

`pthread_set_name_np` 和 `pthread_setname_np` 函数将给定 `name` 的副本应用到给定 `thread`。

`pthread_get_name_np` 和 `pthread_getname_np` 函数获取与 `thread` 关联的 `name`。如果先前未对 `thread` 调用过 `pthread_set_name_np`，则 `name` 所指向的缓冲区将为空。

## 错误

`pthread_getname_np` 和 `pthread_setname_np` 将在以下情况失败：

**`[ESRCH]`** 在当前进程中找不到与给定的线程 ID `thread` 对应的线程。

由于 `pthread_get_name_np` 和 `pthread_set_name_np` 函数的调试性质，其内部可能出现的所有错误都会被静默忽略。

## 参见

thr_set_name(2), [pthread_np(3)](pthread_np.3.md)

## 标准

`pthread_set_name_np` 和 `pthread_get_name_np` 是非标准扩展。`pthread_setname_np` 和 `pthread_getname_np` 同样是非标准的，但被更多操作系统实现，因此事实上更具可移植性。

## 作者

本手册页由 Alexey Zelkin <phantom@FreeBSD.org> 和 Yuri Pankov <yuripv@yuripv.net> 编写。
