# pthread_exit(3)

`pthread_exit` — 终止调用线程

## 名称

`pthread_exit`

## 库

libpthread

## 概要

```c
#include <pthread.h>

void
pthread_exit(void *value_ptr);
```

## 描述

`pthread_exit` 函数终止调用线程，并使值 `value_ptr` 可被任何成功汇合该终止线程的线程获取。所有已压入但尚未弹出的取消清理处理程序将按其压入的相反顺序弹出并执行。在所有取消清理处理程序执行完毕后，如果该线程拥有任何线程特定数据，将以未指定的顺序调用相应的析构函数。线程终止不会释放任何对应用程序可见的进程资源，包括但不限于互斥锁和文件描述符；也不会执行任何进程级别的清理操作，包括但不限于调用可能存在的 `atexit` 例程。

当最初调用 `main` 的线程以外的其他线程从用于创建它的启动例程返回时，会隐式调用 `pthread_exit`。该函数的返回值作为线程的退出状态。

如果在取消清理处理程序或析构函数中调用 `pthread_exit`，而该处理程序或析构函数是由于显式或隐式调用 `pthread_exit` 而被调用的，则 `pthread_exit` 的行为未定义。

线程终止后，对该线程的局部（自动）变量的访问结果未定义。因此，不应使用退出线程的局部变量的引用作为 `pthread_exit` 的 `value_ptr` 参数值。

最后一个线程终止后，进程将以退出状态 0 退出。该行为等同于实现在线程终止时以零参数调用 `exit`。

## 返回值

`pthread_exit` 函数无法返回其调用者。

## 错误

无。

## 参见

\_exit(2), exit(3), [pthread_cancel(3)](pthread_cancel.3.md), [pthread_create(3)](pthread_create.3.md), [pthread_join(3)](pthread_join.3.md)

## 标准

`pthread_exit` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
