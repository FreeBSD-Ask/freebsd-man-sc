# setjmp(3)

`setjmp` — 非局部跳转

## 名称

`sigsetjmp`, `siglongjmp`, `setjmp`, `longjmp`, `_setjmp`, `_longjmp`, `longjmperror`

## 库

Lb libc

## 概要

`#include <setjmp.h>`

```c
int
sigsetjmp(sigjmp_buf env, int savemask);

void
siglongjmp(sigjmp_buf env, int val);

int
setjmp(jmp_buf env);

void
longjmp(jmp_buf env, int val);

int
_setjmp(jmp_buf env);

void
_longjmp(jmp_buf env, int val);

void
longjmperror(void);
```

## 描述

`sigsetjmp`、`setjmp` 和 `_setjmp` 函数将其调用环境保存到 `env` 中。这些函数均返回 0。

对应的 `longjmp` 函数会恢复最近一次调用相应 `setjmp` 函数时所保存的环境。随后它们返回，使得程序继续执行，就好像对相应 `setjmp` 调用的返回刚刚返回了由 `val` 指定的值，而不是 0。

成对的调用可以混合使用，即 `sigsetjmp` 和 `siglongjmp` 以及 `setjmp` 和 `longjmp` 组合可在同一程序中使用，但是单个调用不可混用，例如，传给 `setjmp` 的 `env` 参数不能传递给 `siglongjmp`。

在调用 `setjmp` 例程的例程返回之后，不能再调用 `longjmp` 例程。

所有可访问对象的值均为调用 `longjmp` 例程时的值，但不具有 `volatile` 类型且在 `setjmp` 调用与 `longjmp` 调用之间被修改过的自动存储期对象，其值是不确定的。

`setjmp`/`longjmp` 对会保存和恢复信号掩码，而 `_setjmp`/`_longjmp` 对仅保存和恢复寄存器集与栈。（参见 [sigprocmask(2)](../sys/sigprocmask.2.md)。）

如果参数 `savemask` 非零，则 `sigsetjmp`/`siglongjmp` 函数对会保存和恢复信号掩码，否则仅保存寄存器集与栈。

## 错误

如果 `env` 的内容已损坏，或者对应于一个已经返回的环境，`longjmp` 例程会调用 `longjmperror` 例程。如果 `longjmperror` 返回，程序将被中止（参见 [abort(3)](../man3/abort.3.md)）。`longjmperror` 的默认版本会向标准错误输出消息“`longjmp botch`”并返回。希望更优雅退出的用户程序应自行编写 `longjmperror` 的版本。

## 参见

[sigaction(2)](../sys/sigaction.2.md), [sigaltstack(2)](../sys/sigaltstack.2.md), [signal(3)](signal.3.md)

## 标准

`setjmp` 和 `longjmp` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`sigsetjmp` 和 `siglongjmp` 函数遵循 IEEE Std 1003.1-1988 ("POSIX.1")。

## 历史

`setjmp` 和 `longjmp` 函数首次出现于 Programmer's Workbench (PWB/UNIX)。
