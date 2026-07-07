# setsid(2)

`setsid` — 创建会话并设置进程组 ID

## 名称

`setsid`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
pid_t
setsid(void);
```

## 描述

`setsid()` 系统调用创建一个新会话。调用进程是新会话的会话首领，是新进程组的进程组首领，且没有控制终端。调用进程是该会话或进程组中的唯一进程。

## 返回值

成功完成时，`setsid()` 系统调用返回新进程组的进程组 ID 值，该值与调用进程的进程 ID 相同。如果发生错误，`setsid()` 返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`setsid()` 系统调用将在以下情况下失败：

**[`EPERM`]** 调用进程已经是进程组首领，或调用进程以外的某个进程的进程组 ID 与调用进程的进程 ID 匹配。

## 参见

[setpgid(2)](setpgid.2.md), [tcgetpgrp(3)](../gen/tcgetpgrp.3.md), [tcsetpgrp(3)](../gen/tcsetpgrp.3.md)

## 标准

`setsid()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1") 规范。
