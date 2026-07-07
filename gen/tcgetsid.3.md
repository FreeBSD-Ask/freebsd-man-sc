# tcgetsid(3)

`tcgetsid` — 获取与控制终端关联的会话 ID

## 名称

`tcgetsid`

## 库

Lb libc

## 概要

`#include <termios.h>`

```c
pid_t
tcgetsid(int fd);
```

## 描述

`tcgetsid` 函数返回由 `fd` 指定的控制终端的会话领导者的进程组 ID。

## 错误

如果发生错误，`tcgetsid` 返回 -1，并设置全局变量 `errno` 以指示错误，如下所示：

**[`EBADF`]** `fd` 参数不是有效的文件描述符。

**[`ENOTTY`]** 调用进程没有控制终端，或 `fd` 所表示的底层终端设备不是控制终端。

## 参见

[getsid(2)](../sys/getsid.2.md), [setsid(2)](../sys/setsid.2.md), [tcgetpgrp(3)](tcgetpgrp.3.md), [tcsetsid(3)](tcsetsid.3.md)

## 标准

`tcgetsid` 函数遵循 -xpg4.2。
