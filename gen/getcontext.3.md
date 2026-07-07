# getcontext.3

`getcontext` — 获取和设置用户线程上下文

## 名称

`getcontext`, `getcontextx`, `setcontext`

## 库

Lb libc

## 概要

`#include <ucontext.h>`

```c
int
getcontext(ucontext_t *ucp);

ucontext_t *
getcontextx(void);

int
setcontext(const ucontext_t *ucp);
```

## 描述

`getcontext()` 函数将当前线程的执行上下文保存到 `ucp` 所指向的结构中。保存的上下文之后可通过调用 `setcontext()` 来恢复。

`getcontextx()` 函数将当前执行上下文保存到新分配的 `ucontext_t` 结构中，该结构在成功时返回。如果架构定义了可存储在从 `ucontext_t` 引用的扩展块中的额外 CPU 状态，则可能为它们分配内存并存储其上下文。`getcontextx()` 函数返回的内存应使用 free(3) 释放。

`setcontext()` 函数将先前保存的线程上下文设为当前线程上下文，即当前上下文丢失且 `setcontext()` 不会返回。相反，执行在 `ucp` 指定的上下文中继续，`ucp` 必须先前已通过调用 `getcontext()`、[makecontext(3)](makecontext.3.md) 初始化，或作为参数传递给信号处理程序（参见 [sigaction(2)](../sys/sigaction.2.md)）。

如果 `ucp` 由 `getcontext()` 初始化，则执行继续，如同原始 `getcontext()` 调用刚刚（再次）返回。

如果 `ucp` 由 [makecontext(3)](makecontext.3.md) 初始化，执行继续调用指定给 [makecontext(3)](makecontext.3.md) 的函数。当该函数返回时，`ucp->uc_link` 决定接下来发生什么：如果 `ucp->uc_link` 为 `NULL`，进程退出；否则，隐式调用 `setcontext(ucp->uc_link)`。

如果 `ucp` 由信号处理程序的调用初始化，执行在线程被信号中断的位置继续。

## 返回值

如果成功，`getcontext()` 返回零且 `setcontext()` 不返回；否则返回 -1。`getcontextx()` 成功时返回指向已分配并初始化的上下文的指针，失败时返回 `NULL`。

## 错误

`getcontext()` 或 `setcontext()` 未定义错误。`getcontextx()` 可能在 `errno` 中返回以下错误：

**[ENOMEM]** 没有可用内存来分配上下文或某些扩展状态。

## 参见

[sigaction(2)](../sys/sigaction.2.md), [sigaltstack(2)](../sys/sigaltstack.2.md), [makecontext(3)](makecontext.3.md), [ucontext(3)](ucontext.3.md)

## 标准

`getcontext()` 和 `setcontext()` 函数符合 X/Open System Interfaces and Headers Issue 5 ("XSH5") 和 IEEE Std 1003.1-2001 ("POSIX.1")。`errno` 指示是对标准的扩展。

IEEE Std 1003.1-2004 ("POSIX.1") 修订版将 `getcontext()` 和 `setcontext()` 函数标记为过时，理由是可移植性问题，并建议改用 POSIX 线程。IEEE Std 1003.1-2008 ("POSIX.1") 修订版从规范中移除了这些函数。

## 历史

`getcontext()` 和 `setcontext()` 函数首次出现在 AT&T System V Release 4 UNIX 中。
