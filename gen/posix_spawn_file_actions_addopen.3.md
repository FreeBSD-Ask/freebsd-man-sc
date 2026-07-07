# posix_spawn_file_actions_addopen.3

`posix_spawn_file_actions_addopen` — 向 spawn 文件操作对象添加 open、dup2、close、closefrom 或 chdir/fchdir 操作

## 名称

`posix_spawn_file_actions_addopen`, `posix_spawn_file_actions_adddup2`, `posix_spawn_file_actions_addclose`, `posix_spawn_file_actions_addclosefrom_np`, `posix_spawn_file_actions_addchdir`, `posix_spawn_file_actions_addfchdir`

## 库

Lb libc

## 概要

`#include <spawn.h>`

```c
int
posix_spawn_file_actions_addopen(posix_spawn_file_actions_t *file_actions,
    int fildes, const char *restrict path, int oflag, mode_t mode)

int
posix_spawn_file_actions_adddup2(posix_spawn_file_actions_t *file_actions,
    int fildes, int newfildes)

int
posix_spawn_file_actions_addclose(posix_spawn_file_actions_t *file_actions,
    int fildes)

int
posix_spawn_file_actions_addclosefrom_np(
    posix_spawn_file_actions_t *file_actions, int from)

int
posix_spawn_file_actions_addchdir(
    posix_spawn_file_actions_t *restrict file_actions,
    const char *restrict path)

int
posix_spawn_file_actions_addfchdir(posix_spawn_file_actions_t *file_actions,
    int fildes)
```

## 描述

这些函数向 spawn 文件操作对象添加 open、dup2 或 close 操作。

spawn 文件操作对象的类型为 `posix_spawn_file_actions_t`（定义于

`#include <spawn.h>`

），用于指定一系列由 `posix_spawn` 或 `posix_spawnp` 操作执行的动作，以便根据父进程的打开文件描述符集合得到子进程的打开文件描述符集合。

spawn 文件操作对象在传递给 `posix_spawn` 或 `posix_spawnp` 时，指定了调用进程的打开文件描述符集合如何转换为生成进程可能打开的文件描述符集合。此转换如同在生成进程的上下文中（在执行新进程映像之前），按动作添加到对象中的顺序，恰好执行一次指定的动作序列；此外，在执行新进程映像时，该新集合中任何设置了 `FD_CLOEXEC` 标志的文件描述符都会被关闭（参见 `posix_spawn`）。

`posix_spawn_file_actions_addopen` 函数向 `file_actions` 所引用的对象添加一个 open 动作，使得在使用此文件操作对象生成新进程时，名为 `path` 的文件被打开（如同调用了

```c
open(path, oflag, mode)
```

且返回的文件描述符如果不等于 `fildes`，则被改为 `fildes`）。如果 `fildes` 已经是一个打开的文件描述符，它会在打开新文件之前被关闭。

`path` 所描述的字符串由 `posix_spawn_file_actions_addopen` 函数复制。

`posix_spawn_file_actions_adddup2` 函数向 `file_actions` 所引用的对象添加一个 dup2 动作，使得在使用此文件操作对象生成新进程时，文件描述符 `fildes` 被复制为 `newfildes`（如同调用了

```c
dup2(fildes, newfildes)
```

），不同之处在于即使 `fildes` 等于 `newfildes`，`newfildes` 的 `FD_CLOEXEC` 标志也会被清除。与 `dup2` 的这一差异对于将特定文件描述符传递给特定子进程很有用。

`posix_spawn_file_actions_addclose` 函数向 `file_actions` 所引用的对象添加一个 close 动作，使得在使用此文件操作对象生成新进程时，文件描述符 `fildes` 被关闭（如同调用了

```c
close(fildes)
```

）。

`posix_spawn_file_actions_addclosefrom_np` 函数添加一个 close 动作，关闭所有数值大于或等于参数 `from` 的文件描述符。对于每个打开的文件描述符，逻辑上执行 close 动作，遇到的任何可能错误都被忽略。

`posix_spawn_file_actions_addchdir` 和 `posix_spawn_file_actions_addfchdir` 函数向 `file_actions` 所引用的对象添加一个更改当前目录的动作，该动作按插入 `file_actions` 对象的顺序影响在操作之后执行的动作（以相对路径打开文件）。它还为生成的程序设置工作目录。`posix_spawn_file_actions_addchdir` 函数接受 `path` 作为要设置的工作目录，而 `posix_spawn_file_actions_addfchdir` 接受目录文件描述符。

## 返回值

成功完成时，这些函数返回零；否则返回一个错误号以指示错误。

## 错误

这些函数在以下情况失败：

**[`EBADF`]** `fildes` 或 `newfildes` 指定的值为负数。

**[`ENOMEM`]** 内存不足，无法添加到 spawn 文件操作对象。

## 参见

[close(2)](../sys/close.2.md), dup2(2), [open(2)](../sys/open.2.md), [posix_spawn(3)](posix_spawn.3.md), posix_spawn_file_actions_destroy(3), [posix_spawn_file_actions_init(3)](posix_spawn_file_actions_init.3.md), posix_spawnp(3)

## 标准

`posix_spawn_file_actions_addopen`、`posix_spawn_file_actions_adddup2` 和 `posix_spawn_file_actions_addclose` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")，但 `posix_spawn_file_actions_adddup2` 在 `fildes` 等于 `newfildes` 时的行为（清除 `FD_CLOEXEC`）例外。预计标准的未来更新将要求此行为。

`posix_spawn_file_actions_addclosefrom_np` 函数是非标准的，参照 glibc 提供的类似功能实现。

## 历史

`posix_spawn_file_actions_addopen`、`posix_spawn_file_actions_adddup2` 和 `posix_spawn_file_actions_addclose` 函数首次出现于 FreeBSD 8.0。`posix_spawn_file_actions_addchdir_np`、`posix_spawn_file_actions_addfchdir_np` 和 `posix_spawn_file_actions_addclosefrom_np` 函数首次出现于 FreeBSD 13.1。在 FreeBSD 16.0 中，`posix_spawn_file_actions_addchdir` 和 `posix_spawn_file_actions_addfchdir` 别名被添加到对应的带 `_np` 后缀的函数。

## 作者

Ed Schouten <ed@FreeBSD.org>
