# sigpause(2)

`sighold` — 传统的信号管理接口

## 名称

`sighold`, `sigignore`, `sigpause`, `sigrelse`, `sigset`

## 库

Lb libc

## 概要

```c
#include <signal.h>
```

```c
int
sighold(int sig)

int
sigignore(int sigmask)

int
sigrelse(int sig)

void (*)(int)
sigset(int sig, void (*disp)(int))

int
sigpause(int sigmask)
```

## 描述

**此接口由** sigsuspend(2) **和** sigaction(2) **取代。**

`sigset` 函数修改信号处置。`sig` 参数指定信号，可以是除 `SIGKILL` 和 `SIGSTOP` 之外的任何信号。`disp` 参数指定信号的处置，可以是 `SIG_DFL`、`SIG_IGN` 或信号处理程序的地址。如果使用 `sigset`，且 `disp` 为信号处理程序的地址，系统在执行信号处理程序之前将 `sig` 添加到调用进程的信号掩码中；当信号处理程序返回时，系统将调用进程的信号掩码恢复到信号传递之前的状态。此外，如果使用 `sigset`，且 `disp` 等于 `SIG_HOLD`，`sig` 将被添加到调用进程的信号掩码中，而 `sig` 的处置保持不变。如果使用 `sigset`，且 `disp` 不等于 `SIG_HOLD`，`sig` 将从调用进程的信号掩码中移除。

`sighold` 函数将 `sig` 添加到调用进程的信号掩码中。

`sigrelse` 函数将 `sig` 从调用进程的信号掩码中移除。

`sigignore` 函数将 `sig` 的处置设置为 `SIG_IGN`。

`xsi_sigpause` 函数将 `sig` 从调用进程的信号掩码中移除，并挂起调用进程直到收到信号。`xsi_sigpause` 函数在返回前将进程的信号掩码恢复到原始状态。

`sigpause` 函数将 `sigmask` 赋值给被屏蔽信号集，然后等待信号到达；返回时恢复被屏蔽信号集。`sigmask` 参数通常为 0，表示不屏蔽任何信号。

## 返回值

`sigpause` 和 `xsi_sigpause` 函数总是因被中断而终止，返回 -1，并将 `errno` 设置为 `EINTR`。

成功完成时，如果信号此前被屏蔽，`sigset` 返回 `SIG_HOLD`；如果未被屏蔽，则返回信号之前的处置。否则，返回 `SIG_ERR`，并设置 `errno` 以指示错误。

对于所有其他函数，成功完成时返回 0。否则，返回 -1，并设置 `errno` 以指示错误：

**[`EINVAL`]** `sig` 参数不是有效的信号编号。

**[`EINVAL`]** 对于 `sigset` 和 `sigignore` 函数，试图捕获或忽略 `SIGKILL` 或 `SIGSTOP`。

## 参见

kill(2), sigaction(2), sigblock(2), sigprocmask(2), sigsuspend(2), [sigvec(2)](sigvec.2.md)

## 标准

`sigpause` 函数为兼容历史 4.3BSD 应用程序而实现。AT&T System V UNIX 中存在一个同名但不兼容的接口，该接口使用单个信号编号而非掩码，后被复制到 IEEE Std 1003.1-2001 ("POSIX.1") 的 **X/Open System Interfaces** (XSI) 选项中。FreeBSD 以 `xsi_sigpause` 的名称实现该接口。`sighold`、`sigignore`、`sigrelse` 和 `sigset` 函数为兼容 **System V** 和 **XSI** 接口而实现。

## 历史

`sigpause` 函数出现于 4.2BSD，现已废弃。所有其他函数出现于 FreeBSD 8.1，在实现之前即被废弃。
