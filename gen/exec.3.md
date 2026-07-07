# exec(3)

`execl` — 执行一个文件

## 名称

`execl`, `execlp`, `execle`, `exect`, `execv`, `execvp`, `execvpe`, `execvP`

## 库

libc

## 概要

`#include <unistd.h>`

```c
extern char **environ;

int
execl(const char *path, const char *arg, ..., NULL);

int
execlp(const char *file, const char *arg, ..., NULL);

int
execle(const char *path, const char *arg, ..., NULL, char *const envp[]);

int
exect(const char *path, char *const argv[], char *const envp[]);

int
execv(const char *path, char *const argv[]);

int
execvp(const char *file, char *const argv[]);

int
execvpe(const char *file, char *const argv[], char *const envp[]);

int
execvP(const char *file, const char *search_path, char *const argv[]);
```

## 描述

`exec` 系列函数用一个新的进程映像替换当前进程映像。本手册页中描述的函数是 [execve(2)](../sys/execve.2.md) 函数的前端。（有关当前进程替换的详细信息，请参见 [execve(2)](../sys/execve.2.md) 的手册页。）

这些函数的初始参数是要执行的文件的路径名。

`execl` 、 `execlp` 和 `execle` 函数中的 `const char *arg` 及后续省略号可视为 *arg0,* *arg1,* ..., *argn.* 它们共同描述了一个或多个指向以空字符结尾的字符串的指针列表，这些字符串表示被执行程序可用的参数列表。按照约定，第一个参数应指向与正在执行的文件相关联的文件名。参数列表*必须*以 `NULL` 指针终止。

`exect` 、 `execv` 、 `execvp` 、 `execvpe` 和 `execvP` 函数提供一个指向以空字符结尾的字符串的指针数组，这些字符串表示新程序可用的参数列表。按照约定，第一个参数应指向与正在执行的文件相关联的文件名。指针数组**必须**以 `NULL` 指针终止。

`execle` 、 `exect` 和 `execvpe` 函数还通过在终止参数列表的 `NULL` 指针或指向 argv 数组的指针之后跟随一个额外参数来指定被执行进程的环境。此额外参数是一个指向以空字符结尾的字符串的指针数组，并且*必须*以 `NULL` 指针终止。其他函数从当前进程的外部变量 `environ` 中获取新进程映像的环境。

这些函数中有些具有特殊语义。

如果指定的文件名不包含斜杠"`/`"字符，`execlp` 、 `execvp` 、 `execvpe` 和 `execvP` 函数将模拟 shell 搜索可执行文件的行为。对于 `execlp` 、 `execvp` 和 `execvpe` ，搜索路径是环境中由 `PATH` 变量指定的路径。如果未指定此变量，则默认路径根据以下定义中的 `_PATH_DEFPATH` 设置：

`#include <paths.h>`

即设置为 **/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin** 。对于 `execvP` ，搜索路径作为参数传递给该函数。此外，某些错误会被特殊处理。

如果错误是模糊的（为简单起见，此处将除 `ENOEXEC` 以外的所有错误视为模糊的，尽管只有关键错误 `EACCES` 真正模糊），这些函数的行为就如同它们对文件进行了 stat 以确定文件是否存在并具有适当的执行权限。如果是，它们会立即返回，并将全局变量 `errno` 恢复为 `execve` 所设置的值。否则，搜索将继续。如果搜索完成时既未成功执行 `execve` 也未因错误而终止，这些函数将返回，并根据是否找到至少一个具有适当执行权限的文件，将全局变量 `errno` 设置为 `EACCES` 或 `ENOENT` 。

如果文件头无法识别（尝试的 `execve` 返回 `ENOEXEC` ），这些函数将以文件路径作为第一个参数来执行 shell。（如果此尝试失败，则不再进一步搜索。）

`exect` 函数在启用程序跟踪设施的情况下执行文件（参见 [ptrace(2)](../sys/ptrace.2.md)）。

## 返回值

如果任何一个 `exec` 函数返回，说明发生了错误。返回值为 -1，并将全局变量 `errno` 设置为指示错误。

## 文件

**/bin/sh** shell。

## 兼容性

历史上，`execlp` 和 `execvp` 函数的默认路径为 **:/bin:/usr/bin** 。为增强系统安全性，该路径被更改以移除当前目录。

`execlp` 和 `execvp` 在尝试执行文件时发生错误的行为并非完全的历史做法，传统上未被文档记录，POSIX 标准也未指定。

传统上，`execlp` 和 `execvp` 函数忽略除上述错误以及 `ETXTBSY` （在睡眠数秒后重试）、 `ENOMEM` 和 `E2BIG` （返回）以外的所有错误。现在它们对 `ETXTBSY` 也返回，并更仔细地确定文件的存在性和可执行性。特别是，路径前缀中不可访问目录的 `EACCES` 不再与具有不适当执行权限的文件的 `EACCES` 相混淆。在 4.4BSD 中，它们对除 `EACCES` 、 `ENOENT` 、 `ENOEXEC` 和 `ETXTBSY` 以外的所有错误都返回。这不如传统的错误处理方式，因为它打破了对路径前缀错误的忽略，仅改善了不常见的模糊错误 `EFAULT` 和不常见错误 `EIO` 的处理。该行为更改为与 [sh(1)](../man1/sh.1.md) 的行为一致。

## 错误

`execl` 、 `execle` 、 `execlp` 、 `execvp` 、 `execvpe` 和 `execvP` 函数可能失败并设置 `errno` 为库函数 [execve(2)](../sys/execve.2.md) 和 malloc(3) 所指定的任何错误。

`exect` 和 `execv` 函数可能失败并设置 `errno` 为库函数 [execve(2)](../sys/execve.2.md) 所指定的任何错误。

## 参见

[sh(1)](../man1/sh.1.md), [execve(2)](../sys/execve.2.md), [fork(2)](../sys/fork.2.md), [ktrace(2)](../sys/ktrace.2.md), [ptrace(2)](../sys/ptrace.2.md), [environ(7)](../man7/environ.7.md)

## 标准

`execl` 、 `execv` 、 `execle` 、 `execlp` 和 `execvp` 函数遵循 -p1003.1-88 标准。`execvpe` 函数是一个 GNU 扩展。

## 历史

`exec` 函数出现于 Version 1 AT&T UNIX。`execl` 和 `execv` 函数出现于 Version 2 AT&T UNIX。`execlp` 、 `execle` 、 `execve` 和 `execvp` 函数出现于 Version 7 AT&T UNIX。`execvP` 函数首次出现于 FreeBSD 5.2。`execvpe` 函数首次出现于 FreeBSD 14.1。

## 缺陷

`execle` 、 `exect` 、 `execv` 、 `execvp` 、 `execvpe` 和 `execvP` 的 `argv` 和 `envp` 参数的类型是一个历史遗留问题，任何合理的实现都不应修改所提供的字符串。这些不合理的参数类型会引发 `const` 正确性分析器的误报。在 FreeBSD 上，可使用 `__DECONST` 宏来解决此限制。

由于 C 标准的一个巧合，在 FreeBSD 以外的平台上，`NULL` 的定义可能是无类型数字零，而非 `(void *)0` 表达式。为区分这两个概念，分别称其为"空指针常量"和"空指针"。在 FreeBSD 不支持的异构计算机架构上，空指针常量和空指针可能具有不同的表示。通常，本文档及其他文档中引用 `NULL` 值时，实际暗示的是空指针。例如，为了可移植到异构计算机架构上的非 FreeBSD 操作系统，在调用 `execl` 、 `execle` 和 `execlp` 时，可使用 `(char *)NULL` 代替 `NULL` 。
