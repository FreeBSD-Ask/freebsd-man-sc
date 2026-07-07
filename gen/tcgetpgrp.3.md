# tcgetpgrp(3)

`tcgetpgrp` — 获取前台进程组 ID

## 名称

`tcgetpgrp`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
pid_t
tcgetpgrp(int fd);
```

## 描述

`tcgetpgrp` 函数返回与终端设备关联的前台进程组的进程组 ID 值。如果没有前台进程组，`tcgetpgrp` 返回一个无效的进程 ID。

## 错误

如果发生错误，`tcgetpgrp` 返回 -1，并设置全局变量 `errno` 以指示错误，如下所示：

**[`EBADF`]** `fd` 参数不是有效的文件描述符。

**[`ENOTTY`]** 调用进程没有控制终端，或 `fd` 所表示的底层终端设备不是控制终端。

## 参见

[setpgid(2)](../sys/setpgid.2.md), [setsid(2)](../sys/setsid.2.md), [tcsetpgrp(3)](tcsetpgrp.3.md)

## 标准

`tcgetpgrp` 函数预期符合 -p1003.1-88 规范。
