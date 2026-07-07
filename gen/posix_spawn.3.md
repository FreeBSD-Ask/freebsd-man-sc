# posix_spawn(3)

`posix_spawn` — 创建进程

## 名称

`posix_spawn`, `posix_spawnp` — 创建进程

## 库

Lb libc

## 概要

```c
#include <spawn.h>

int
posix_spawn(pid_t *restrict pid, const char *restrict path,
    const posix_spawn_file_actions_t *file_actions,
    const posix_spawnattr_t *restrict attrp,
    char *const argv[restrict], char *const envp[restrict]);

int
posix_spawnp(pid_t *restrict pid, const char *restrict file,
    const posix_spawn_file_actions_t *file_actions,
    const posix_spawnattr_t *restrict attrp,
    char *const argv[restrict], char *const envp[restrict]);
```

## 描述

`posix_spawn` 和 `posix_spawnp` 函数从指定的进程映像创建新进程（子进程）。新进程映像由一个称为新进程映像文件的常规可执行文件构造。

当 C 程序作为此调用的结果执行时，它作为 C 语言函数调用进入，如下所示：

```c
int main(int argc, char *argv[]);
```

其中 `argc` 是参数计数，`argv` 是指向参数本身的字符指针数组。此外，变量：

```c
extern char **environ;
```

指向指向环境字符串的字符指针数组。

参数 `argv` 是指向以空字符结尾的字符串的字符指针数组。该数组的最后一个成员是空指针，不计入 `argc`。这些字符串构成新进程映像可用的参数列表。`argv[0]` 中的值应指向与 `posix_spawn` 或 `posix_spawnp` 函数启动的进程映像相关联的文件名。

参数 `envp` 是指向以空字符结尾的字符串的字符指针数组。这些字符串构成新进程映像的环境。环境数组以空指针终止。

`posix_spawn` 的 `path` 参数是标识要执行的新进程映像文件的路径名。

`posix_spawnp` 的 `file` 参数用于构造标识新进程映像文件的路径名。如果 file 参数包含斜杠字符，则 file 参数用作新进程映像文件的路径名。否则，通过搜索作为环境变量 “`PATH`” 传递的目录来获取此文件的路径前缀。如果未指定此变量，则默认路径根据 `_PATH_DEFPATH` 定义设置：

```c
#include <paths.h>
```

该定义设置为 “`/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin`”。

如果 `file_actions` 是空指针，则在调用进程中打开的文件描述符在子进程中保持打开，但设置了 close-on-exec 标志 `FD_CLOEXEC` 的除外（参见 `fcntl`）。对于保持打开的文件描述符，相应打开文件描述的所有属性（包括文件锁，参见 `fcntl`）保持不变。

如果 `file_actions` 不是 NULL，则子进程中打开的文件描述符是调用进程中打开的文件描述符经过 `file_actions` 指向的 spawn 文件操作对象的修改，以及处理 spawn 文件操作后每个保持打开的文件描述符的 `FD_CLOEXEC` 标志。处理 spawn 文件操作的有效顺序为：

- 子进程的打开文件描述符集合最初与调用进程打开的集合相同。相应打开文件描述的所有属性（包括文件锁，参见 `fcntl`）保持不变。
- 子进程的信号掩码、信号默认动作以及有效用户和组 ID 按 `attrp` 引用的属性对象中的指定进行更改。
- 按 spawn 文件操作对象添加到自身的顺序执行 spawn 文件操作对象指定的文件操作。
- 任何设置了 `FD_CLOEXEC` 标志的文件描述符（参见 `fcntl`）都将关闭。

`posix_spawnattr_t` spawn 属性对象类型定义在：

```c
#include <spawn.h>
```

它包含以下定义的属性。

如果在 `attrp` 引用的对象的 spawn-flags 属性中设置了 `POSIX_SPAWN_SETPGROUP` 标志，且同一对象的 spawn-pgroup 属性非零，则子进程的进程组为 `attrp` 引用的对象的 spawn-pgroup 属性中指定的值。

作为特殊情况，如果在 `attrp` 引用的对象的 spawn-flags 属性中设置了 `POSIX_SPAWN_SETPGROUP` 标志，且同一对象的 spawn-pgroup 属性设置为零，则子进程位于一个新的进程组中，其进程组 ID 等于其进程 ID。

如果未在 `attrp` 引用的对象的 spawn-flags 属性中设置 `POSIX_SPAWN_SETPGROUP` 标志，新子进程继承父进程的进程组。

如果在 `attrp` 引用的对象的 spawn-flags 属性中设置了 `POSIX_SPAWN_SETSCHEDPARAM` 标志，但未设置 `POSIX_SPAWN_SETSCHEDULER`，则新进程映像最初具有调用进程的调度策略，以及 `attrp` 引用的对象的 spawn-schedparam 属性中指定的调度参数。

如果在 `attrp` 引用的对象的 spawn-flags 属性中设置了 `POSIX_SPAWN_SETSCHEDULER` 标志（无论 `POSIX_SPAWN_SETSCHEDPARAM` 标志的设置如何），则新进程映像最初具有 `attrp` 引用的对象的 spawn-schedpolicy 属性中指定的调度策略，以及同一对象的 spawn-schedparam 属性中指定的调度参数。

`attrp` 引用对象的 spawn-flags 属性中的 `POSIX_SPAWN_RESETIDS` 标志控制子进程的有效用户 ID。如果未设置此标志，子进程继承父进程的有效用户 ID。如果设置此标志，子进程的有效用户 ID 重置为父进程的实际用户 ID。在任一情况下，如果新进程映像文件的 set-user-ID 模式位已设置，则子进程的有效用户 ID 在新进程映像开始执行前变为该文件的所有者 ID。

`attrp` 引用对象的 spawn-flags 属性中的 `POSIX_SPAWN_RESETIDS` 标志也控制子进程的有效组 ID。如果未设置此标志，子进程继承父进程的有效组 ID。如果设置此标志，子进程的有效组 ID 重置为父进程的实际组 ID。在任一情况下，如果新进程映像文件的 set-group-ID 模式位已设置，则子进程的有效组 ID 在新进程映像开始执行前变为该文件的组 ID。

如果在 `attrp` 引用的对象的 spawn-flags 属性中设置了 `POSIX_SPAWN_SETSIGMASK` 标志，子进程最初具有 `attrp` 引用的对象的 spawn-sigmask 属性中指定的信号掩码。

如果在 `attrp` 引用的对象的 spawn-flags 属性中设置了 `POSIX_SPAWN_SETSIGDEF` 标志，则同一对象的 spawn-sigdefault 属性中指定的信号在子进程中设置为其默认动作。在父进程中设置为默认动作的信号在子进程中也设置为默认动作。

设置为被调用进程捕获的信号在子进程中设置为默认动作。

设置为被调用进程映像忽略的信号在子进程中设置为忽略，除非通过在 `attrp` 引用对象的 spawn-flags 属性中设置 `POSIX_SPAWN_SETSIGDEF` 标志并在 `attrp` 引用对象的 spawn-sigdefault 属性中指明该信号而另有指定。

可以通过在 spawn-flags 属性中指定 `POSIX_SPAWN_DISABLE_ASLR_NP` 标志来禁用新生成进程的地址空间布局随机化。此设置也会被子进程的未来子进程继承。更多细节参见 [procctl(2)](../sys/procctl.2.md)。

如果 `attrp` 指针的值为 NULL，则使用默认值。

除受 `attrp` 引用对象中设置的属性影响或受 `file_actions` 中指定的文件描述符操作影响外，所有进程属性在新进程映像中出现，如同调用了 `vfork` 创建子进程，然后子进程调用 `execve` 执行新进程映像。

本实现使用 `vfork`，因此调用 `posix_spawn` 或 `posix_spawnp` 时不运行 fork 处理程序。

## 返回值

成功完成后，`posix_spawn` 和 `posix_spawnp` 通过非 NULL `pid` 参数指向的变量将子进程的进程 ID 返回给父进程，并返回零作为函数返回值。否则，不创建子进程，不向 `pid` 指向的变量存储值，并返回错误号作为函数返回值以指示错误。如果 `pid` 参数是空指针，子进程的进程 ID 不返回给调用者。

## 错误

- 如果 `posix_spawn` 和 `posix_spawnp` 因任何会导致 `vfork` 或某个 `exec` 失败的原因而失败，则按 `vfork` 和 `exec` 所述返回错误值（或者，如果错误发生在调用进程成功返回之后，子进程以退出状态 127 退出）。
- 如果在 `attrp` 引用对象的 spawn-flags 属性中设置了 `POSIX_SPAWN_SETPGROUP`，且 `posix_spawn` 或 `posix_spawnp` 在更改子进程的进程组时失败，则按 `setpgid` 所述返回错误值（或者，如果错误发生在调用进程成功返回之后，子进程以退出状态 127 退出）。
- 如果在 `attrp` 引用对象的 spawn-flags 属性中设置了 `POSIX_SPAWN_SETSCHEDPARAM` 但未设置 `POSIX_SPAWN_SETSCHEDULER`，则如果 `posix_spawn` 或 `posix_spawnp` 因任何会导致 `sched_setparam` 失败的原因而失败，则按 `sched_setparam` 所述返回错误值（或者，如果错误发生在调用进程成功返回之后，子进程以退出状态 127 退出）。
- 如果在 `attrp` 引用对象的 spawn-flags 属性中设置了 `POSIX_SPAWN_SETSCHEDULER`，且如果 `posix_spawn` 或 `posix_spawnp` 因任何会导致 `sched_setscheduler` 失败的原因而失败，则按 `sched_setscheduler` 所述返回错误值（或者，如果错误发生在调用进程成功返回之后，子进程以退出状态 127 退出）。
- 如果 `file_actions` 参数不是 NULL，且指定了要执行的任何 dup2 或 open 操作，且如果 `posix_spawn` 或 `posix_spawnp` 因任何会导致 `dup2` 或 `open` 失败的原因而失败，则分别按 `dup2` 和 `open` 所述返回错误值（或者，如果错误发生在调用进程成功返回之后，子进程以退出状态 127 退出）。open 文件操作本身可能导致 `dup2` 所述的任何错误，以及 `open` 所述的错误。本实现忽略 `close` 的任何错误，包括试图关闭未打开的描述符。该忽略扩展到作为 `closefrom` 操作一部分执行的单个文件描述符 `close` 的任何错误。

## 参见

[close(2)](../sys/close.2.md), dup2(2), [execve(2)](../sys/execve.2.md), [fcntl(2)](../sys/fcntl.2.md), [open(2)](../sys/open.2.md), [procctl(2)](../sys/procctl.2.md), [sched_setparam(2)](../sys/sched_setparam.2.md), [sched_setscheduler(2)](../sys/sched_setscheduler.2.md), [setpgid(2)](../sys/setpgid.2.md), [vfork(2)](../sys/vfork.2.md), posix_spawn_file_actions_addchdir(3), posix_spawn_file_actions_addclose(3), posix_spawn_file_actions_addclosefrom_np(3), posix_spawn_file_actions_adddup2(3), posix_spawn_file_actions_addfchdir(3), [posix_spawn_file_actions_addopen(3)](posix_spawn_file_actions_addopen.3.md), posix_spawn_file_actions_destroy(3), [posix_spawn_file_actions_init(3)](posix_spawn_file_actions_init.3.md), posix_spawnattr_destroy(3), [posix_spawnattr_getexecfd_np(3)](posix_spawnattr_getexecfd_np.3.md), [posix_spawnattr_getflags(3)](posix_spawnattr_getflags.3.md), [posix_spawnattr_getpgroup(3)](posix_spawnattr_getpgroup.3.md), [posix_spawnattr_getprocdescp_np(3)](posix_spawnattr_getprocdescp_np.3.md), [posix_spawnattr_getschedparam(3)](posix_spawnattr_getschedparam.3.md), [posix_spawnattr_getschedpolicy(3)](posix_spawnattr_getschedpolicy.3.md), [posix_spawnattr_getsigdefault(3)](posix_spawnattr_getsigdefault.3.md), [posix_spawnattr_getsigmask(3)](posix_spawnattr_getsigmask.3.md), [posix_spawnattr_init(3)](posix_spawnattr_init.3.md), posix_spawnattr_setexecfd_np(3), posix_spawnattr_setflags(3), posix_spawnattr_setpgroup(3), posix_spawnattr_setprocdescp_np(3), posix_spawnattr_setschedparam(3), posix_spawnattr_setschedpolicy(3), posix_spawnattr_setsigdefault(3), posix_spawnattr_setsigmask(3)

## 标准

`posix_spawn` 和 `posix_spawnp` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准，但它们忽略 `close` 的所有错误。-p1003.1-2024 版本的标准不再要求这些函数因要关闭的文件描述符（通过 `posix_spawn_file_actions_addclose`）未打开而失败。

## 历史

`posix_spawn` 和 `posix_spawnp` 函数首次出现于 FreeBSD 8.0。

## 作者

Ed Schouten <ed@FreeBSD.org>

