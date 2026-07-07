# makecontext(3)

`makecontext` — 修改和交换用户线程上下文

## 名称

`makecontext`, `swapcontext`

## 库

Lb libc

## 概要

```c
#include <ucontext.h>

void
makecontext(ucontext_t *ucp, void (*func)(void), int argc, ...);

int
swapcontext(ucontext_t *oucp, const ucontext_t *ucp);
```

## 描述

`makecontext()` 函数修改 `ucp` 所指向的用户线程上下文，该上下文必须先前已通过调用 [getcontext(3)](getcontext.3.md) 初始化，并已为其分配栈。上下文被修改为通过调用 `func()` 并使用所提供的参数来继续执行。`argc` 参数必须等于提供给 `makecontext()` 的 `int` 类型附加参数的数量，同时也等于 `func()` 的 `int` 类型参数的数量；否则，行为是未定义的。

`ucp->uc_link` 参数必须在调用 `makecontext()` 之前初始化，并决定 `func()` 返回时采取的操作：如果等于 `NULL`，进程退出；否则，隐式调用 `setcontext(ucp->uc_link)`。

`swapcontext()` 函数将当前线程上下文保存在 `*oucp` 中，并使 `*ucp` 成为当前活动上下文。

## 返回值

若成功，`swapcontext()` 返回零；否则返回 -1，并适当设置全局变量 `errno`。

## 错误

`swapcontext()` 函数在以下情况下会失败：

**`[ENOMEM]`** `ucp` 中没有足够的栈空间来完成操作。

## 参见

setcontext(3), [ucontext(3)](ucontext.3.md)

## 标准

`makecontext()` 和 `swapcontext()` 函数遵循 X/Open System Interfaces and Headers Issue 5 (XSH5) 和 IEEE Std 1003.1-2001 ("POSIX.1") 标准。

IEEE Std 1003.1-2004 ("POSIX.1") 修订版将 `makecontext()` 和 `swapcontext()` 函数标记为过时，指出可移植性问题并建议改用 POSIX 线程。IEEE Std 1003.1-2008 ("POSIX.1") 修订版从规范中删除了这些函数。

标准未明确定义通过 `makecontext()` 传递给 `func` 的整数参数的类型；可移植应用程序不应依赖于可能可以向函数传递指针参数这一实现细节。

## 历史

`makecontext()` 和 `swapcontext()` 函数首次出现在 AT&T System V Release 4 UNIX 中。
