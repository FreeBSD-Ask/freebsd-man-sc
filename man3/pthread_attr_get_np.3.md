# pthread_attr_get_np.3

`pthread_attr_get_np` — 获取已存在线程的属性

## 名称

`pthread_attr_get_np`

## 库

Lb libpthread

## 概要

`#include <pthread_np.h>`

`Ft int Fn pthread_attr_get_np pthread_t pid pthread_attr_t *dst`

## 描述

`Fn pthread_attr_get_np` 函数用于将指定线程的属性检索到现有的 `pthread_attr_t` 结构中。这些属性值是目标线程的当前值，但栈顶地址例外——如果它没有按架构要求正确对齐，则其值已在内部使用前经过了调整。

参数 `dst` 必须指向一个有效的属性对象（该对象此前已由 pthread_attr_init(3) 初始化，并且此后未被销毁）。在 `Fn pthread_attr_get_np` 调用成功后，可按 [pthread_attr(3)](pthread_attr.3.md) 中所述，通过相应的访问函数照常获取各个属性值。在 `Fn pthread_attr_get_np` 调用失败后，`dst` 所指向的对象保持不变，可以像此次失败的调用从未发生过一样继续使用。

## 返回值

若成功，`Fn pthread_attr_get_np` 函数返回 0。否则返回一个错误号以指示错误。

## 实例

以下函数获取由 `pid` 参数指定的线程的栈大小：

```sh
size_t
my_thread_stack_size(pthread_t tid)
{
	pthread_attr_t attr;
	size_t size;
	pthread_attr_init(&attr);
	pthread_attr_get_np(tid, &attr);
	pthread_attr_getstacksize(&attr, &size);
	pthread_attr_destroy(&attr);
	return (size);
}
```

## 错误

`Fn pthread_attr_get_np` 函数在以下情况下会失败：

**[Er** EINVAL] 某个参数的值无效。

**[Er** ESRCH] 找不到与给定线程 ID 对应的线程。

**[Er** ENOMEM] 没有足够的内存来分配属性对象实现所需的额外存储空间。

## 参见

[pthread_attr(3)](pthread_attr.3.md), pthread_attr_destroy(3), pthread_attr_getdetachstate(3), pthread_attr_getinheritsched(3), pthread_attr_getschedparam(3), pthread_attr_getschedpolicy(3), pthread_attr_getscope(3), pthread_attr_getstack(3), pthread_attr_getstackaddr(3), pthread_attr_getstacksize(3), pthread_attr_init(3), [pthread_np(3)](pthread_np.3.md)

## 作者

`Fn pthread_attr_get_np` 函数及本手册页由 Alexey Zelkin <phantom@FreeBSD.org> 编写，后者由 Olivier Certner <olce@FreeBSD.org> 修订。
