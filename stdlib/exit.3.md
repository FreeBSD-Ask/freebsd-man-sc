# exit(3)

`exit` — 执行正常的程序终止

## 名称

`exit`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
void
exit(int status);

void
_Exit(int status);
```

## 描述

`exit` 和 `_Exit` 函数终止进程。

在终止之前，`exit` 按所列顺序执行以下操作：

- 调用所有通过 __cxa_atexit(3) 函数注册的函数（通常是来自已加载动态对象的析构函数），以及通过 [atexit(3)](atexit.3.md) 函数注册的函数，调用顺序与注册顺序相反。
- 刷新所有打开的输出流。
- 关闭所有打开的流。

`_Exit` 函数终止时不调用通过 [atexit(3)](atexit.3.md) 函数注册的函数，可能执行也可能不执行上述其他操作。FreeBSD 实现的 `_Exit` 函数不调用通过 __cxa_atexit(3) 注册的析构函数，不刷新缓冲区，也不关闭流。

这两个函数都使 `status` 参数的低八位可供已调用 [wait(2)](../sys/wait.2.md) 系列函数的父进程使用。

C 标准（ISO/IEC 9899:1999 ("ISO C99")）定义了 `0`、`EXIT_SUCCESS` 和 `EXIT_FAILURE` 作为 `status` 的可能值。协作进程可以使用其他值；在可能被邮件传输代理调用的程序中，可以使用 [sysexits(3)](../man3/sysexits.3.md) 中描述的值向父进程提供更多信息。

完整的 `status` 值可作为 `siginfo_t` 结构的 `si_status` 成员，供 wait6(2) 和 [sigwaitinfo(2)](../sys/sigwaitinfo.2.md) 调用者以及 `SIGCHLD` 信号处理程序使用。

对 `exit` 函数的调用是串行化的。所有通过 [atexit(3)](atexit.3.md) 注册的函数在第一个调用 `exit` 的线程中执行。如果进程的任何其他线程在所有注册函数完成之前或进程终止之前调用 `exit`，该线程将被阻塞直到进程终止。进程的退出状态是第一个 `exit` 调用的 `status` 参数，该调用所在的线程继续执行 atexit 处理程序。

注意，如果通过 [atexit(3)](atexit.3.md) 注册的函数本身调用 `exit`，`exit` 不会采取任何措施来防止无限递归。此类函数必须改用 `_Exit`（尽管这也会产生其他可能不希望的副作用）。

## 返回值

`exit` 和 `_Exit` 函数永不返回。

## 参见

[_exit(2)](../sys/_exit.2.md), [abort2(2)](../sys/abort2.2.md), [wait(2)](../sys/wait.2.md), [at_quick_exit(3)](at_quick_exit.3.md), [atexit(3)](atexit.3.md), [intro(3)](../man3/intro.3.md), [quick_exit(3)](quick_exit.3.md), [sysexits(3)](../man3/sysexits.3.md), tmpfile(3)

## 标准

`exit` 和 `_Exit` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。

## 历史

`exit` 函数出现于 Version 1 AT&T UNIX。
