# tcsetpgrp(3)

`tcsetpgrp` — 设置前台进程组 ID

## 名称

`tcsetpgrp` — 设置前台进程组 ID

## 库

Lb libc

## 概要

```c
#include <unistd.h>

int
tcsetpgrp(int fd, pid_t pgrp_id);
```

## 描述

如果进程有控制终端，`tcsetpgrp` 函数将与终端设备关联的前台进程组 ID 设置为 `pgrp_id`。与 `fd` 关联的终端设备必须是调用进程的控制终端，且该控制终端必须当前与调用进程的会话关联。`pgrp_id` 的值必须与同一会话中某个进程的进程组 ID 相同。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`tcsetpgrp` 函数在以下情况下会失败：

**[`EBADF`]** `fd` 参数不是有效的文件描述符。

**[`EINVAL`]** 指定了无效的 `pgrp_id` 值。

**[`ENOTTY`]** 调用进程没有控制终端，或 `fd` 所表示的文件不是控制终端，或控制终端不再与调用进程的会话关联。

**[`EPERM`]** `pgrp_id` 参数与同一会话中某个进程的进程组 ID 不匹配。

## 参见

[setpgid(2)](../sys/setpgid.2.md), [setsid(2)](../sys/setsid.2.md), [tcgetpgrp(3)](tcgetpgrp.3.md)

## 标准

`tcsetpgrp` 函数预期符合 -p1003.1-88 规范。
