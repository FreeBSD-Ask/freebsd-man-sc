# pthread_np(3)

`pthread_np` — FreeBSD 对 POSIX 线程函数的扩展

## 名称

`pthread_np`

## 库

libpthread

## 概要

```c
#include <pthread_np.h>
```

## 描述

本手册页记录了对 POSIX 线程函数的扩展。这些扩展不一定能移植到其他操作系统。

POSIX 线程函数在本节中按以下分组进行汇总：

- 线程例程
- 属性对象例程
- mutex 例程

### 线程例程

```c
int
pthread_getaffinity_np(pthread_t td, size_t cpusetsize,
    cpuset_t *cpusetp);
```

获取指定线程的 CPU 亲和性。

```c
int
pthread_get_name_np(pthread_t thread, char *name, size_t len);
```

获取指定线程的名称。

```c
int
pthread_getname_np(pthread_t thread, char *name, size_t len);
```

获取指定线程的名称。

```c
int
pthread_getthreadid_np(void);
```

获取调用线程的整数 ID。

```c
int
pthread_main_np(void);
```

标识初始线程。

```c
int
pthread_multi_np(void);
```

将线程的调度模式设置为多线程。

```c
int
pthread_peekjoin_np(pthread_t thread, void **value_ptr);
```

查看指定线程的退出状态。

```c
int
pthread_resume_all_np(void);
```

恢复所有被挂起的线程。

```c
int
pthread_setaffinity_np(pthread_t td, size_t cpusetsize,
    const cpuset_t *cpusetp);
```

设置指定线程的 CPU 亲和性。

```c
int
pthread_set_name_np(pthread_t thread, char *name);
```

设置指定线程的名称。

```c
int
pthread_setname_np(pthread_t thread, char *name);
```

设置指定线程的名称。

```c
void
pthread_signals_block_np(void);
```

快速阻塞所有异步信号。

```c
int
pthread_single_np(void);
```

将线程的调度模式设置为单线程。

```c
int
pthread_suspend_np(pthread_t tid);
```

挂起指定的线程。

```c
int
pthread_suspend_all_np(void);
```

挂起所有活动线程。

```c
int
pthread_timedjoin_np(pthread_t thread, void **value_ptr,
    const struct timespec *abstime);
```

`pthread_join` 的带超时变体。

### 属性对象例程

```c
int
pthread_attr_get_np(pthread_t pid, pthread_attr_t *dst);
```

获取已存在线程的属性。

```c
int
pthread_attr_getaffinity_np(const pthread_attr_t *pattr,
    size_t cpusetsize, cpuset_t *cpusetp);
```

从线程属性对象获取 CPU 亲和性掩码。

```c
int
pthread_attr_setaffinity_np(pthread_attr_t *pattr,
    size_t cpusetsize, const cpuset_t *cpusetp);
```

为线程属性对象设置 CPU 亲和性掩码。

```c
int
pthread_attr_setcreatesuspend_np(pthread_attr_t *attr);
```

允许创建已挂起的线程。

### mutex 例程

```c
int
pthread_mutexattr_getkind_np(pthread_mutexattr_t attr);
```

已弃用，请改用 pthread_mutexattr_gettype(3)。

```c
int
pthread_mutexattr_setkind_np(pthread_mutexattr_t *attr);
```

已弃用，请改用 pthread_mutexattr_settype(3)。

## 参见

libthr(3), [pthread(3)](pthread.3.md), [pthread_affinity_np(3)](pthread_affinity_np.3.md), [pthread_attr_affinity_np(3)](pthread_attr_affinity_np.3.md), [pthread_attr_get_np(3)](pthread_attr_get_np.3.md), [pthread_attr_setcreatesuspend_np(3)](pthread_attr_setcreatesuspend_np.3.md), [pthread_getthreadid_np(3)](pthread_getthreadid_np.3.md), [pthread_join(3)](pthread_join.3.md), [pthread_main_np(3)](pthread_main_np.3.md), [pthread_multi_np(3)](pthread_multi_np.3.md), [pthread_mutexattr_getkind_np(3)](pthread_mutexattr_getkind_np.3.md), [pthread_resume_all_np(3)](pthread_resume_all_np.3.md), [pthread_resume_np(3)](pthread_resume_np.3.md), [pthread_set_name_np(3)](pthread_set_name_np.3.md), [pthread_signals_block_np(3)](pthread_signals_block_np.3.md), [pthread_suspend_all_np(3)](pthread_suspend_all_np.3.md), [pthread_suspend_np(3)](pthread_suspend_np.3.md), pthread_switch_add_np(3)

## 标准

所有这些函数都是对 POSIX 线程的不可移植扩展。
