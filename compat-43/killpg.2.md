# killpg.2

`killpg` — 向进程组发送信号

## 名称

`killpg`

## 库

Lb libc

## 概要

```c
#include <sys/types.h>
#include <signal.h>
```

```c
int
killpg(pid_t pgrp, int sig)
```

## 描述

`killpg` 函数向进程组 `pgrp` 发送信号 `sig`。信号列表参见 sigaction(2)。如果 `pgrp` 为 0，`killpg` 向发送进程所属的进程组发送信号。

发送进程必须能够 kill 接收进程组中的至少一个进程。

## 返回值

成功完成时，`killpg` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`killpg` 函数将失败且不发送信号，如果：

**[`EINVAL`]** `sig` 参数不是有效的信号编号。

**[`ESRCH`]** 在 `pgrp` 指定的进程组中找不到进程。

**[`EPERM`]** kill 对进程组中的所有进程都返回 `EPERM`。

## 参见

getpgrp(2), kill(2), sigaction(2)

## 历史

`killpg` 函数首次出现于 4.0BSD。
