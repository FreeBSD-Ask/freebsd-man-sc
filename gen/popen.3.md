# popen(3)

`popen` — 进程 I/O

## 名称

`popen`, `pclose`

## 库

Lb libc

## 概要

`#include <stdio.h>`

```c
FILE *
popen(const char *command, const char *type);

int
pclose(FILE *stream);
```

## 描述

`popen` 函数通过创建双向管道、fork 并调用 shell 来“打开”一个进程。在父进程中由先前 `popen` 调用打开的任何流都会在新的子进程中被关闭。历史上，`popen` 是用单向管道实现的；因此许多 `popen` 实现只允许 `type` 参数指定读取或写入，而不能同时指定两者。由于 `popen` 现在使用双向管道实现，`type` 参数可以请求双向数据流。`type` 参数是指向以空字符结尾的字符串的指针，必须为 `r`（读取）、`w`（写入）或 `r+`（读取和写入）。

可以在其后追加字母 `e`，以请求将底层文件描述符设置为 close-on-exec。

`command` 参数是指向以空字符结尾的字符串的指针，该字符串包含 shell 命令行。此命令使用 `-c` 标志传递给 **/bin/sh**；解释（如果有）由 shell 执行。

`popen` 的返回值在所有方面都是一个普通的标准 I/O 流，只是必须用 `pclose` 而非 `fclose` 来关闭。写入这样的流会写入命令的标准输入；命令的标准输出与调用 `popen` 的进程的标准输出相同，除非命令本身改变了它。相反，从“popened”流读取会读取命令的标准输出，而命令的标准输入与调用 `popen` 的进程的标准输入相同。

注意，输出 `popen` 流默认是全缓冲的。

`pclose` 函数等待关联的进程终止，并返回由 [wait4(2)](../sys/wait.2.md) 返回的命令退出状态。

## 返回值

如果 [fork(2)](../sys/fork.2.md) 或 [pipe(2)](../sys/pipe.2.md) 调用失败，或者无法分配内存，`popen` 函数返回 `NULL`。

如果 `stream` 未与“popened”命令关联、`stream` 已经“pclosed”，或者 [wait4(2)](../sys/wait.2.md) 返回错误，`pclose` 函数返回 -1。

## 错误

`popen` 函数不会可靠地设置 `errno`。

## 参见

[sh(1)](../man1/sh.1.md), [fork(2)](../sys/fork.2.md), [pipe(2)](../sys/pipe.2.md), [wait4(2)](../sys/wait.2.md), [fclose(3)](../stdio/fclose.3.md), [fflush(3)](../stdio/fflush.3.md), [fopen(3)](../stdio/fopen.3.md), [stdio(3)](../stdio/stdio.3.md), [system(3)](../stdlib/system.3.md)

## 历史

`popen` 和 `pclose` 函数出现于 Version 7 AT&T UNIX。

双向功能在 FreeBSD 2.2.6 中添加。

## 缺陷

由于为读取而打开的命令的标准输入与调用 `popen` 的进程共享其寻道偏移量，如果原始进程已执行了缓冲读取，则命令的输入位置可能不如预期。类似地，为写入而打开的命令的输出可能与原始进程的输出混杂在一起。后者可以通过在 `popen` 之前调用 [fflush(3)](../stdio/fflush.3.md) 来避免。

无法执行 shell 与 shell 无法执行命令或命令立即退出是无法区分的。唯一的提示是退出状态为 127。

`popen` 函数始终调用 [sh(1)](../man1/sh.1.md)，从不调用 [csh(1)](../man1/csh.1.md)。
