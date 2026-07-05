# pthread_attr.3

`pthread_attr_init` — 线程属性操作

## 名称

`pthread_attr_init`, `pthread_attr_destroy`, `pthread_attr_setstack`, `pthread_attr_getstack`, `pthread_attr_setstacksize`, `pthread_attr_getstacksize`, `pthread_attr_setguardsize`, `pthread_attr_getguardsize`, `pthread_attr_setstackaddr`, `pthread_attr_getstackaddr`, `pthread_attr_setdetachstate`, `pthread_attr_getdetachstate`, `pthread_attr_setinheritsched`, `pthread_attr_getinheritsched`, `pthread_attr_setschedparam`, `pthread_attr_getschedparam`, `pthread_attr_setschedpolicy`, `pthread_attr_getschedpolicy`, `pthread_attr_setscope`, `pthread_attr_getscope`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

`Ft int Fn pthread_attr_init pthread_attr_t *attr Ft int Fn pthread_attr_destroy pthread_attr_t *attr Ft int Fn pthread_attr_setstack pthread_attr_t *attr void *stackaddr size_t stacksize Ft int Fn pthread_attr_getstack const pthread_attr_t * restrict attr void ** restrict stackaddr size_t * restrict stacksize Ft int Fn pthread_attr_setstacksize pthread_attr_t *attr size_t stacksize Ft int Fn pthread_attr_getstacksize const pthread_attr_t *restrict attr size_t *restrict stacksize Ft int Fn pthread_attr_setguardsize pthread_attr_t *attr size_t guardsize Ft int Fn pthread_attr_getguardsize const pthread_attr_t * restrict attr size_t * restrict guardsize Ft int Fn pthread_attr_setstackaddr pthread_attr_t *attr void *stackaddr Ft int Fn pthread_attr_getstackaddr const pthread_attr_t *attr void **stackaddr Ft int Fn pthread_attr_setdetachstate pthread_attr_t *attr int detachstate Ft int Fn pthread_attr_getdetachstate const pthread_attr_t *attr int *detachstate Ft int Fn pthread_attr_setinheritsched pthread_attr_t *attr int inheritsched Ft int Fn pthread_attr_getinheritsched const pthread_attr_t *restrict attr int *restrct inheritsched Ft int Fn pthread_attr_setschedparam pthread_attr_t *attr const struct sched_param *param Ft int Fn pthread_attr_getschedparam const pthread_attr_t *attr struct sched_param *param Ft int Fn pthread_attr_setschedpolicy pthread_attr_t *attr int policy Ft int Fn pthread_attr_getschedpolicy const pthread_attr_t *restrict attr int *restrict policy Ft int Fn pthread_attr_setscope pthread_attr_t *attr int contentionscope Ft int Fn pthread_attr_getscope const pthread_attr_t *restrict attr int *restrict contentionscope`

## 描述

线程属性用于为 `Fn pthread_create` 指定参数。一个属性对象可以在多次调用 `Fn pthread_create` 时使用，调用之间可对其修改或不修改。

`Fn pthread_attr_init` 函数以所有默认线程属性初始化 `attr`。

`Fn pthread_attr_destroy` 函数销毁 `attr`。

`Fn pthread_attr_set*` 系列函数设置与各函数名对应的属性。

`Fn pthread_attr_get*` 系列函数将与各函数名对应的属性值复制到第二个函数参数所指向的位置。

## 返回值

若成功，这些函数返回 0。否则返回一个错误号以指示错误。

## 错误

`Fn pthread_attr_init` 函数在以下情况下会失败：

**[Er** ENOMEM] 内存不足。

`Fn pthread_attr_destroy` 函数在以下情况下会失败：

**[Er** EINVAL] `attr` 的值无效。

`Fn pthread_attr_setstacksize` 和 `Fn pthread_attr_setstack` 函数在以下情况下会失败：

**[Er** EINVAL] `stacksize` 小于 `PTHREAD_STACK_MIN`。

`Fn pthread_attr_setdetachstate` 函数在以下情况下会失败：

**[Er** EINVAL] `detachstate` 的值无效。

`Fn pthread_attr_setinheritsched` 函数在以下情况下会失败：

**[Er** EINVAL] `attr` 的值无效。

`Fn pthread_attr_setschedparam` 函数在以下情况下会失败：

**[Er** EINVAL] `attr` 的值无效。

**[Er** ENOTSUP] `param` 的值无效。

`Fn pthread_attr_setschedpolicy` 函数在以下情况下会失败：

**[Er** EINVAL] `attr` 的值无效。

**[Er** ENOTSUP] `policy` 的值无效或不受支持。

`Fn pthread_attr_setscope` 函数在以下情况下会失败：

**[Er** EINVAL] `attr` 的值无效。

**[Er** ENOTSUP] `contentionscope` 的值无效或不受支持。

## 参见

[pthread_attr_affinity_np(3)](pthread_attr_affinity_np.3.md), [pthread_attr_get_np(3)](pthread_attr_get_np.3.md), [pthread_create(3)](pthread_create.3.md)

## 标准

`Fn pthread_attr_init`、`Fn pthread_attr_destroy`、`Fn pthread_attr_setstacksize`、`Fn pthread_attr_getstacksize`、`Fn pthread_attr_setstackaddr`、`Fn pthread_attr_getstackaddr`、`Fn pthread_attr_setdetachstate` 和 `Fn pthread_attr_getdetachstate` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。

`Fn pthread_attr_setinheritsched`、`Fn pthread_attr_getinheritsched`、`Fn pthread_attr_setschedparam`、`Fn pthread_attr_getschedparam`、`Fn pthread_attr_setschedpolicy`、`Fn pthread_attr_getschedpolicy`、`Fn pthread_attr_setscope` 和 `Fn pthread_attr_getscope` 函数遵循 -susv2 标准。
