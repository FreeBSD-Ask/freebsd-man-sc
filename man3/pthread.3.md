# pthread.3

`pthread` — POSIX 线程函数

## 名称

`pthread`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

## 描述

POSIX 线程是一组支持在同一进程中具有多个控制流（称为*线程*）的应用程序的函数。多线程用于提升程序性能。

POSIX 线程函数在本节中按以下分组进行总结：

- 线程例程
- 属性对象例程
- 互斥锁例程
- 条件变量例程
- 读写锁例程
- 线程特定上下文例程
- 清理例程

POSIX 线程函数的 FreeBSD 扩展在 [pthread_np(3)](pthread_np.3.md) 中总结。

### 线程例程

**Xo** Ft int Fo pthread_create `pthread_t *thread const pthread_attr_t *attr` `void **start_routinevoid * void *arg` Fc Xc 创建一个新的执行线程。

**Xo** Ft int Fn pthread_cancel pthread_t thread Xc 取消一个线程的执行。

**Xo** Ft int Fn pthread_detach pthread_t thread Xc 标记一个线程以便删除。

**Xo** Ft int Fn pthread_equal pthread_t t1 pthread_t t2 Xc 比较两个线程 ID。

**Xo** Ft void Fn pthread_exit void *value_ptr Xc 终止调用线程。

**Xo** Ft int Fn pthread_join pthread_t thread void **value_ptr Xc 使调用线程等待指定线程终止。

**Xo** Ft int Fn pthread_kill pthread_t thread int sig Xc 向指定线程发送信号。

**Xo** Ft int Fn pthread_once pthread_once_t *once_control void *init_routinevoid Xc 调用初始化例程一次。

**Xo** Ft pthread_t Fn pthread_self void Xc 返回调用线程的线程 ID。

**Xo** Ft int Fn pthread_setcancelstate int state int *oldstate Xc 设置当前线程的可取消状态。

**Xo** Ft int Fn pthread_setcanceltype int type int *oldtype Xc 设置当前线程的可取消类型。

**Xo** Ft void Fn pthread_testcancel void Xc 在调用线程中创建一个取消点。

**Xo** Ft void Fn pthread_yield void Xc 允许调度器运行其他线程而非当前线程。

### 属性对象例程

**Xo** Ft int Fn pthread_attr_destroy pthread_attr_t *attr Xc 销毁线程属性对象。

**Xo** Ft int Fo pthread_attr_getinheritsched `const pthread_attr_t *attr int *inheritsched` Fc Xc 从线程属性对象中获取继承调度属性。

**Xo** Ft int Fo pthread_attr_getschedparam `const pthread_attr_t *attr struct sched_param *param` Fc Xc 从线程属性对象中获取调度参数属性。

**Xo** Ft int Fn pthread_attr_getschedpolicy const pthread_attr_t *attr int *policy Xc 从线程属性对象中获取调度策略属性。

**Xo** Ft int Fn pthread_attr_getscope const pthread_attr_t *attr int *contentionscope Xc 从线程属性对象中获取竞争范围属性。

**Xo** Ft int Fn pthread_attr_getstacksize const pthread_attr_t *attr size_t *stacksize Xc 从线程属性对象中获取栈大小属性。

**Xo** Ft int Fn pthread_attr_getstackaddr const pthread_attr_t *attr void **stackaddr Xc 从线程属性对象中获取栈地址属性。

**Xo** Ft int Fn pthread_attr_getdetachstate const pthread_attr_t *attr int *detachstate Xc 从线程属性对象中获取分离状态属性。

**Xo** Ft int Fn pthread_attr_init pthread_attr_t *attr Xc 以默认值初始化线程属性对象。

**Xo** Ft int Fn pthread_attr_setinheritsched pthread_attr_t *attr int inheritsched Xc 在线程属性对象中设置继承调度属性。

**Xo** Ft int Fo pthread_attr_setschedparam `pthread_attr_t *attr const struct sched_param *param` Fc Xc 在线程属性对象中设置调度参数属性。

**Xo** Ft int Fn pthread_attr_setschedpolicy pthread_attr_t *attr int policy Xc 在线程属性对象中设置调度策略属性。

**Xo** Ft int Fn pthread_attr_setscope pthread_attr_t *attr int contentionscope Xc 在线程属性对象中设置竞争范围属性。

**Xo** Ft int Fn pthread_attr_setstacksize pthread_attr_t *attr size_t stacksize Xc 在线程属性对象中设置栈大小属性。

**Xo** Ft int Fn pthread_attr_setstackaddr pthread_attr_t *attr void *stackaddr Xc 在线程属性对象中设置栈地址属性。

**Xo** Ft int Fn pthread_attr_setdetachstate pthread_attr_t *attr int detachstate Xc 在线程属性对象中设置分离状态。

### 互斥锁例程

**Xo** Ft int Fn pthread_mutexattr_destroy pthread_mutexattr_t *attr Xc 销毁互斥锁属性对象。

**Xo** Ft int Fn pthread_mutexattr_getprioceiling const pthread_mutexattr_t *restrict attr int *restrict ceiling Xc 获取互斥锁属性对象的优先级上限属性。

**Xo** Ft int Fn pthread_mutexattr_getprotocol const pthread_mutexattr_t *restrict attr int *restrict protocol Xc 获取互斥锁属性对象的协议属性。

**Xo** Ft int Fn pthread_mutexattr_gettype const pthread_mutexattr_t *restrict attr int *restrict type Xc 获取指定互斥锁属性对象中的互斥锁类型属性。

**Xo** Ft int Fn pthread_mutexattr_init pthread_mutexattr_t *attr Xc 以默认值初始化互斥锁属性对象。

**Xo** Ft int Fn pthread_mutexattr_setprioceiling pthread_mutexattr_t *attr int ceiling Xc 设置互斥锁属性对象的优先级上限属性。

**Xo** Ft int Fn pthread_mutexattr_setprotocol pthread_mutexattr_t *attr int protocol Xc 设置互斥锁属性对象的协议属性。

**Xo** Ft int Fn pthread_mutexattr_settype pthread_mutexattr_t *attr int type Xc 设置创建互斥锁时使用的互斥锁类型属性。

**Xo** Ft int Fn pthread_mutex_destroy pthread_mutex_t *mutex Xc 销毁互斥锁。

**Xo** Ft int Fo pthread_mutex_init `pthread_mutex_t *mutex const pthread_mutexattr_t *attr` Fc Xc 以指定属性初始化互斥锁。

**Xo** Ft int Fn pthread_mutex_lock pthread_mutex_t *mutex Xc 锁定互斥锁并阻塞直至其可用。

**Xo** Ft int Fo pthread_mutex_timedlock `pthread_mutex_t *mutex const struct timespec *abstime` Fc Xc 锁定互斥锁并阻塞直至其可用或超时。

**Xo** Ft int Fn pthread_mutex_trylock pthread_mutex_t *mutex Xc 尝试锁定互斥锁，但如果互斥锁已被其他线程（包括当前线程）锁定，则不阻塞。

**Xo** Ft int Fn pthread_mutex_unlock pthread_mutex_t *mutex Xc 解锁互斥锁。

### 条件变量例程

**Xo** Ft int Fn pthread_condattr_destroy pthread_condattr_t *attr Xc 销毁条件变量属性对象。

**Xo** Ft int Fn pthread_condattr_init pthread_condattr_t *attr Xc 以默认值初始化条件变量属性对象。

**Xo** Ft int Fn pthread_cond_broadcast pthread_cond_t *cond Xc 唤醒当前在指定条件变量上阻塞的所有线程。

**Xo** Ft int Fn pthread_cond_destroy pthread_cond_t *cond Xc 销毁条件变量。

**Xo** Ft int Fn pthread_cond_init pthread_cond_t *cond const pthread_condattr_t *attr Xc 以指定属性初始化条件变量。

**Xo** Ft int Fn pthread_cond_signal pthread_cond_t *cond Xc 唤醒至少一个在指定条件变量上阻塞的线程。

**Xo** Ft int Fo pthread_cond_timedwait `pthread_cond_t *cond pthread_mutex_t *mutex` `const struct timespec *abstime` Fc Xc 解锁指定互斥锁，等待条件的时间不超过指定时长，然后重新锁定互斥锁。

**Xo** Ft int Fn pthread_cond_wait pthread_cond_t * pthread_mutex_t *mutex Xc 解锁指定互斥锁，等待条件，然后重新锁定互斥锁。

### 读写锁例程

**Xo** Ft int Fn pthread_rwlock_destroy pthread_rwlock_t *lock Xc 销毁读写锁对象。

**Xo** Ft int Fo pthread_rwlock_init `pthread_rwlock_t *lock const pthread_rwlockattr_t *attr` Fc Xc 初始化读写锁对象。

**Xo** Ft int Fn pthread_rwlock_rdlock pthread_rwlock_t *lock Xc 以读模式锁定读写锁，阻塞直至获得锁。

**Xo** Ft int Fn pthread_rwlock_tryrdlock pthread_rwlock_t *lock Xc 尝试以读模式锁定读写锁，如果锁不可用则不阻塞。

**Xo** Ft int Fn pthread_rwlock_trywrlock pthread_rwlock_t *lock Xc 尝试以写模式锁定读写锁，如果锁不可用则不阻塞。

**Xo** Ft int Fn pthread_rwlock_unlock pthread_rwlock_t *lock Xc 解锁读写锁。

**Xo** Ft int Fn pthread_rwlock_wrlock pthread_rwlock_t *lock Xc 以写模式锁定读写锁，阻塞直至获得锁。

**Xo** Ft int Fn pthread_rwlockattr_destroy pthread_rwlockattr_t *attr Xc 销毁读写锁属性对象。

**Xo** Ft int Fo pthread_rwlockattr_getpshared `const pthread_rwlockattr_t *attr int *pshared` Fc Xc 获取读写锁属性对象的进程共享设置。

**Xo** Ft int Fn pthread_rwlockattr_init pthread_rwlockattr_t *attr Xc 初始化读写锁属性对象。

**Xo** Ft int Fn pthread_rwlockattr_setpshared pthread_rwlockattr_t *attr int pshared Xc 设置读写锁属性对象的进程共享设置。

### 线程特定上下文例程

**Xo** Ft int Fn pthread_key_create pthread_key_t *key void *routinevoid * Xc 创建线程特定数据键。

**Xo** Ft int Fn pthread_key_delete pthread_key_t key Xc 删除线程特定数据键。

**Xo** Ft void * Fn pthread_getspecific pthread_key_t key Xc 获取指定键的线程特定值。

**Xo** Ft int Fn pthread_setspecific pthread_key_t key const void *value_ptr Xc 设置指定键的线程特定值。

### 清理例程

**Xo** Ft int Fo pthread_atfork `void *preparevoid` `void *parentvoid` `void *childvoid` Fc Xc 注册 fork 处理程序。

**Xo** Ft void Fn pthread_cleanup_pop int execute Xc 弹出调用线程取消清理栈顶的例程，并可选择调用它。

**Xo** Ft void Fn pthread_cleanup_push void *routinevoid * void *routine_arg Xc 将指定的取消清理处理程序压入调用线程的取消清理栈。

## 实现说明

当前 FreeBSD 的 POSIX 线程实现内置于 Lb libthr 库中。它包含线程安全版本的 Lb libc 函数以及线程函数。多线程应用程序与此库链接。

## 参见

libthr(3), [pthread_atfork(3)](pthread_atfork.3.md), [pthread_attr(3)](pthread_attr.3.md), [pthread_cancel(3)](pthread_cancel.3.md), [pthread_cleanup_pop(3)](pthread_cleanup_pop.3.md), [pthread_cleanup_push(3)](pthread_cleanup_push.3.md), [pthread_cond_broadcast(3)](pthread_cond_broadcast.3.md), [pthread_cond_destroy(3)](pthread_cond_destroy.3.md), [pthread_cond_init(3)](pthread_cond_init.3.md), [pthread_cond_signal(3)](pthread_cond_signal.3.md), [pthread_cond_timedwait(3)](pthread_cond_timedwait.3.md), [pthread_cond_wait(3)](pthread_cond_wait.3.md), pthread_condattr_destroy(3), pthread_condattr_init(3), [pthread_create(3)](pthread_create.3.md), [pthread_detach(3)](pthread_detach.3.md), [pthread_equal(3)](pthread_equal.3.md), [pthread_exit(3)](pthread_exit.3.md), [pthread_getspecific(3)](pthread_getspecific.3.md), [pthread_join(3)](pthread_join.3.md), [pthread_key_delete(3)](pthread_key_delete.3.md), [pthread_kill(3)](pthread_kill.3.md), [pthread_mutex_destroy(3)](pthread_mutex_destroy.3.md), [pthread_mutex_init(3)](pthread_mutex_init.3.md), [pthread_mutex_lock(3)](pthread_mutex_lock.3.md), [pthread_mutex_trylock(3)](pthread_mutex_trylock.3.md), [pthread_mutex_unlock(3)](pthread_mutex_unlock.3.md), pthread_mutexattr_destroy(3), pthread_mutexattr_getprioceiling(3), pthread_mutexattr_getprotocol(3), pthread_mutexattr_gettype(3), pthread_mutexattr_init(3), pthread_mutexattr_setprioceiling(3), pthread_mutexattr_setprotocol(3), pthread_mutexattr_settype(3), [pthread_np(3)](pthread_np.3.md), [pthread_once(3)](pthread_once.3.md), [pthread_rwlock_destroy(3)](pthread_rwlock_destroy.3.md), [pthread_rwlock_init(3)](pthread_rwlock_init.3.md), [pthread_rwlock_rdlock(3)](pthread_rwlock_rdlock.3.md), [pthread_rwlock_unlock(3)](pthread_rwlock_unlock.3.md), [pthread_rwlock_wrlock(3)](pthread_rwlock_wrlock.3.md), [pthread_rwlockattr_destroy(3)](pthread_rwlockattr_destroy.3.md), [pthread_rwlockattr_getpshared(3)](pthread_rwlockattr_getpshared.3.md), [pthread_rwlockattr_init(3)](pthread_rwlockattr_init.3.md), [pthread_rwlockattr_setpshared(3)](pthread_rwlockattr_setpshared.3.md), [pthread_self(3)](pthread_self.3.md), pthread_setcancelstate(3), pthread_setcanceltype(3), [pthread_setspecific(3)](pthread_setspecific.3.md), [pthread_testcancel(3)](pthread_testcancel.3.md)

## 标准

带有 `pthread_` 前缀且不含 `_np` 后缀、或带 `pthread_rwlock` 前缀的函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。

带有 `pthread_` 前缀和 `_np` 后缀的函数是 POSIX 线程的非可移植扩展。

带有 `pthread_rwlock` 前缀的函数是由 The Open Group 作为 -susv2 的一部分创建的扩展。
