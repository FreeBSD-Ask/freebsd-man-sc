# tcsetsid(3)

`tcsetsid` — 设置与控制终端关联的会话 ID

## 名称

`tcsetsid` — 设置与控制终端关联的会话 ID

## 库

Lb libc

## 概要

```c
#include <termios.h>

int
tcsetsid(int fd, pid_t pid);
```

## 描述

`tcsetsid` 函数将由 `pid` 标识的会话与由 `fd` 指定的控制终端关联。

本实现仅允许会话领导者自身更改控制终端。这意味着 `pid` 必须始终等于进程 ID。

不支持与已有关联会话的终端进行关联。反之，当会话已与不同终端关联时，也不支持将其关联到该终端。

## 错误

如果发生错误，`tcsetsid` 返回 -1，并设置全局变量 `errno` 以指示错误，如下所示：

**[`EBADF`]** `fd` 参数不是有效的文件描述符。

**[`ENOTTY`]** `fd` 所表示的文件描述符不是终端。

**[`EINVAL`]** `pid` 参数不等于调用进程的会话 ID。

**[`EPERM`]** 调用进程不是会话领导者。

**[`EPERM`]** 该会话已有关联的终端，或该终端已有关联的会话。

## 参见

[getsid(2)](../sys/getsid.2.md), [setsid(2)](../sys/setsid.2.md), [tcgetpgrp(3)](tcgetpgrp.3.md), [tcgetsid(3)](tcgetsid.3.md)

## 历史

`tcsetsid` 函数首次出现于 QNX。它不符合任何标准。
