# setpgid(2)

`setpgid`, `setpgrp` — 设置进程组

## 名称

`setpgid`, `setpgrp`

## 库

Lb libc

## 概要

```c
#include <unistd.h>

int
setpgid(pid_t pid, pid_t pgrp);

int
setpgrp(pid_t pid, pid_t pgrp);
```

## 描述

`setpgid()` 系统调用将指定进程 `pid` 的进程组设置为指定的 `pgrp`。如果 `pid` 为零，则该调用应用于当前进程。如果 `pgrp` 为零，则使用由 `pid` 指定的进程的进程 ID。

如果受影响的进程不是调用进程，则它必须是调用进程的子进程，且必须尚未执行 [exec(3)](../gen/exec.3.md) 操作，并且两个进程必须在同一会话中。请求的进程组 ID 必须已存在于调用者的会话中，或者必须等于目标进程 ID。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 兼容性

`setpgrp()` 系统调用与 `setpgid()` 相同，保留它是为了与历史版本的 BSD 保持调用约定兼容性。

## 错误

如果发生以下情况，`setpgid()` 系统调用将失败，且进程组不会被更改：

**[`EINVAL`]** 请求的进程组 ID 不合法。

**[`ESRCH`]** 请求的进程不存在。

**[`ESRCH`]** 目标进程不是调用进程，也不是调用进程的子进程。

**[`EACCES`]** 请求的进程是调用进程的子进程，但它已执行了 [exec(3)](../gen/exec.3.md) 操作。

**[`EPERM`]** 目标进程是会话组长。

**[`EPERM`]** 请求的进程组 ID 不在调用者的会话中，且不等于目标进程的进程 ID。

## 参见

[getpgrp(2)](getpgrp.2.md)

## 标准

`setpgid()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。
