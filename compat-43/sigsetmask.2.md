# sigsetmask.2

`sigsetmask` — 操作当前信号掩码

## 名称

`sigsetmask`, `sigblock`

## 库

Lb libc

## 概要

```c
#include <signal.h>
```

```c
int
sigsetmask(int mask)

int
sigblock(int mask)

int
sigmask(int signum)
```

## 描述

**此接口由** sigprocmask(2) **取代。**

`sigsetmask` 函数将当前信号掩码设置为指定的 `mask`。如果 `mask` 中对应的位为 1，则阻止相应信号的传递。`sigblock` 函数将指定 `mask` 中的信号添加到当前信号掩码，而非像 `sigsetmask` 那样覆盖它。`sigmask` 宏用于为给定的 `signum` 构造掩码。

系统会静默地禁止屏蔽 `SIGKILL` 或 `SIGSTOP`。

## 返回值

`sigblock` 和 `sigsetmask` 函数返回先前被屏蔽的信号集。

## 参见

kill(2), sigaction(2), sigprocmask(2), sigsuspend(2), [sigvec(2)](sigvec.2.md), sigsetops(3)

## 历史

`sigsetmask` 和 `sigblock` 函数首次出现于 4.2BSD，现已废弃。
