# execve(2)

`execve` — 执行文件

## 名称

`execve`, `fexecve`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
execve(const char *path, char *const argv[], char *const envp[]);

int
fexecve(int fd, char *const argv[], char *const envp[]);
```

## 描述

`execve()` 系统调用将调用进程转换为新进程。新进程由一个普通文件构造而成，该文件的名称由 `path` 指向，称为 *新进程文件*。`fexecve()` 系统调用等同于 `execve()`，不同之处在于要执行的文件由文件描述符 `fd` 而非 `path` 决定。该文件要么是可执行目标文件，要么是解释器的数据文件。可执行目标文件由一个标识头组成，其后是表示初始程序（text）和已初始化数据页面的数据页面。头可以指定额外的页面，用零数据初始化；参见 [elf(5)](../man5/elf.5.md) 和 [a.out(5)](../man5/a.out.5.md)。

解释器文件以如下形式的行开头：

**#!**
*interpreter*
[*arg*]

当对解释器文件执行 execve 时，系统实际上会对指定的 *interpreter* 执行 execve。如果指定了可选的 *arg*，它成为 *interpreter* 的第一个参数，而原本被 execve 的文件的名称成为第二个参数；否则，原本被 execve 的文件的名称成为第一个参数。原始参数向后移动成为后续参数。第零个参数设置为指定的 *interpreter*。

参数 `argv` 是一个指向以空字符结尾的字符指针数组的指针，该数组中的每个字符指针又指向一个以空字符结尾的字符串。这些字符串构成将提供给新进程的参数列表。数组中必须至少有一个参数；按照惯例，第一个元素应为被执行程序的名称（例如，`path` 的最后一个组件）。

参数 `envp` 也是一个指向以空字符结尾的字符指针数组的指针，该数组中的每个字符指针又指向以空字符结尾的字符串。指向此数组的指针通常存储在全局变量 `environ` 中。这些字符串向新进程传递信息，这些信息不是命令的直接参数（参见 [environ(7)](../man7/environ.7.md)）。

调用进程映像中打开的文件描述符在新进程映像中保持打开，除非设置了 close-on-exec 标志（参见 [close(2)](close.2.md) 和 [fcntl(2)](fcntl.2.md)）。保持打开的描述符不受 `execve()` 影响，但所有文件描述符上的 close-on-fork 标志 `FD_CLOFORK` 会被清除。如果在调用 `execve()` 时任何标准描述符（0、1 和/或 2）已关闭，且进程将因 set-id 语义而获得特权，这些描述符将被自动重新打开。任何程序，无论是否特权，都不应假设这些描述符在 `execve()` 调用期间会保持关闭。

在调用进程中设置为忽略的信号，在新进程中也被设置为忽略。在调用进程映像中设置为捕获的信号，在新进程映像中被设置为默认动作。阻塞的信号无论信号动作如何变化都保持阻塞。信号栈被重置为未定义状态（更多信息参见 [sigaction(2)](sigaction.2.md)）。

如果新进程映像文件的 set-user-ID 模式位被设置（参见 [chmod(2)](chmod.2.md)），新进程映像的有效用户 ID 设置为新进程映像文件的所有者 ID。如果新进程映像文件的 set-group-ID 模式位被设置，新进程映像的有效组 ID 设置为新进程映像文件的组 ID。（有效组 ID 是组列表的第一个元素。）新进程映像的实际用户 ID、实际组 ID 和其他组 ID 与调用进程映像保持相同。在所有 set-user-ID 和 set-group-ID 处理之后，有效用户 ID 被记录为保存的 set-user-ID，有效组 ID 被记录为保存的 set-group-ID。这些值可用于稍后更改有效 ID（参见 [setuid(2)](setuid.2.md)）。

如果相应文件系统启用了 `nosuid` 选项，或新进程文件是解释器文件，则不遵循 set-ID 位。如果有效 ID 发生更改，系统调用跟踪将被禁用。

新进程还从调用进程继承以下属性：

| 属性 | 参见 |
| --- | --- |
| 进程 ID | [getpid(2)](getpid.2.md) |
| 父进程 ID | getppid(2) |
| 进程组 ID | [getpgrp(2)](getpgrp.2.md) |
| 访问组 | [getgroups(2)](getgroups.2.md) |
| 工作目录 | [chdir(2)](chdir.2.md) |
| 根目录 | [chroot(2)](chroot.2.md) |
| 控制终端 | [termios(4)](../man4/termios.4.md) |
| 资源使用 | [getrusage(2)](getrusage.2.md) |
| 间隔定时器 | [getitimer(2)](getitimer.2.md) |
| 资源限制 | [getrlimit(2)](getrlimit.2.md) |
| 文件模式掩码 | [umask(2)](umask.2.md) |
| 信号掩码 | [sigaction(2)](sigaction.2.md), [sigprocmask(2)](sigprocmask.2.md) |

当程序因 `execve()` 系统调用的结果被执行时，其入口形式如下：

```c
main(argc, argv, envp)
int argc;
char **argv, **envp;
```

其中 `argc` 是 `argv` 中的元素数量（“参数计数”），`argv` 指向参数自身的字符指针数组。

`fexecve()` 忽略 `fd` 的文件偏移量。由于执行权限由 `fexecve()` 检查，文件描述符 `fd` 无需以 `O_EXEC` 标志打开。然而，如果要执行的文件拒绝向准备执行 exec 的进程授予读权限，则向 `fexecve()` 提供 `fd` 的唯一方法是在打开 `fd` 时使用 `O_EXEC` 标志。在执行解释型程序的情况下，可能需要不使用 `O_EXEC` 打开，因为如果不将 [fdescfs(4)](../man4/fdescfs.4.md) 以 `nodup` 选项挂载到 **/dev/fd**，解释器将无法获取用于读取脚本的描述符。注意，要执行的文件不能以写方式打开。

## 返回值

由于 `execve()` 系统调用用新进程映像覆盖当前进程映像，成功的调用没有进程可以返回。如果 `execve()` 确实返回到调用进程，则发生了错误；返回值将为 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`execve()` 系统调用在以下情况下会失败并返回到调用进程：

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOEXEC`]** 当调用解释型脚本时，第一行的长度（含 **#!** 前缀和终止换行符）超过 `MAXSHELLCMDLEN` 个字符。

**[`ENOENT`]** 新进程文件不存在。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EACCES`]** 拒绝对路径前缀某个组件的搜索权限。

**[`EACCES`]** 新进程文件不是普通文件。

**[`EACCES`]** 新进程文件模式拒绝执行权限。

**[`EINVAL`]** `argv` 未包含至少一个元素。

**[`ENOEXEC`]** 新进程文件具有适当的访问权限，但其头部中的魔数无效。

**[`ETXTBSY`]** 新进程文件是纯过程（共享文本）文件，且当前正被某个进程以写方式打开。

**[`ENOMEM`]** 新进程需要的虚拟内存超过所施加的最大值（[getrlimit(2)](getrlimit.2.md)）。

**[`E2BIG`]** 新进程参数列表的字节数大于系统施加的限制。此限制由 [sysctl(3)](../gen/sysctl.3.md) MIB 变量 `KERN_ARGMAX` 指定。

**[`EFAULT`]** 新进程文件的长度未达到其头部大小值所指示的长度。

**[`EFAULT`]** `path`、`argv` 或 `envp` 参数指向非法地址。

**[`EIO`]** 从文件系统读取时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

此外，`fexecve()` 在以下情况下会失败并返回到调用进程：

**[`EBADF`]** `fd` 参数不是为执行而打开的有效文件描述符。

## 参见

[ktrace(1)](../man1/ktrace.1.md), [_exit(2)](_exit.2.md), [fork(2)](fork.2.md), [open(2)](open.2.md), execl(3), [exit(3)](../stdlib/exit.3.md), [sysctl(3)](../gen/sysctl.3.md), [fdescfs(4)](../man4/fdescfs.4.md), [a.out(5)](../man5/a.out.5.md), [elf(5)](../man5/elf.5.md), [environ(7)](../man7/environ.7.md), [mount(8)](../man8/mount.8.md)

## 标准

`execve()` 系统调用遵循 IEEE Std 1003.1-2001 ("POSIX.1")，但在某些情况下重新打开描述符 0、1 和/或 2 的行为除外。标准的未来更新预期会要求此行为，它也可能成为非特权进程的默认行为。对执行解释型程序的支持是扩展。`fexecve()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`execve()` 系统调用出现于 Version 7 AT&T UNIX。`fexecve()` 系统调用出现于 FreeBSD 8.0。

## 注意事项

如果程序对非超级用户设置了 *setuid*，但在实际 *uid* 为 “root” 时执行，则该程序也具有超级用户的某些权限。

当通过 `fexecve()` 执行解释型程序时，内核向解释器提供 **/dev/fd/n** 作为第二个参数，其中 `n` 是传递给 `fexecve()` 的 `fd` 参数中的文件描述符。为使此构造正常工作，[fdescfs(4)](../man4/fdescfs.4.md) 文件系统应挂载到 **/dev/fd**。
