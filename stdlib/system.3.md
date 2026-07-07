# system(3)

`system` — 将命令传递给 shell

## 名称

`system`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
int
system(const char *string);
```

## 描述

`system` 函数将参数 `string` 传递给命令解释器 [sh(1)](../man1/sh.1.md)。调用进程等待 shell 完成命令的执行，期间忽略 `SIGINT` 和 `SIGQUIT`，并阻塞 `SIGCHLD`。

如果 `string` 是 `NULL` 指针，当命令解释器 [sh(1)](../man1/sh.1.md) 可用时 `system` 将返回非零值，不可用时返回零。

## 返回值

`system` 函数返回 shell 的退出状态（由 [waitpid(2)](../sys/wait.2.md) 返回），或在调用 [fork(2)](../sys/fork.2.md) 或 [waitpid(2)](../sys/wait.2.md) 时发生错误时返回 -1。如果子进程执行 shell 失败，它将以退出码 127 终止，`system` 将返回相应的退出状态。

## 参见

[sh(1)](../man1/sh.1.md), [execve(2)](../sys/execve.2.md), [fork(2)](../sys/fork.2.md), [waitpid(2)](../sys/wait.2.md), [popen(3)](../gen/popen.3.md), [posix_spawn(3)](../gen/posix_spawn.3.md)

## 标准

`system` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")，并预期与 IEEE Std 1003.2 ("POSIX.2") 兼容。

## 安全考虑

`system` 函数容易被误用，从而使恶意用户能够运行任意命令，因为 [sh(1)](../man1/sh.1.md) 支持的所有元字符都会被解释执行。用户提供的参数在出现在 `string` 中之前，应始终经过仔细的清理。
