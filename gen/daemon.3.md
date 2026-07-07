# daemon(3)

`daemon` — 在后台运行

## 名称

`daemon`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
int
daemon(int nochdir, int noclose);

int
daemonfd(int chdirfd, int nullfd);
```

## 描述

`daemon` 函数用于希望从控制终端分离并作为系统守护进程在后台运行的程序。使用 [fork(2)](../sys/fork.2.md) 系统调用；关于 `fork` 之后（没有相应调用 exec 例程之一）的环境，参见下文的注意事项。

如果参数 `nochdir` 为零，`daemon` 将当前工作目录更改为根目录（**/**）。

如果参数 `noclose` 为零，`daemon` 将标准输入、标准输出和标准错误重定向到 **/dev/null**。

`daemonfd` 函数等同于 `daemon` 函数，不同之处在于其参数为当前工作目录的描述符和 **/dev/null** 的描述符。

如果 `chdirfd` 等于 (-1)，则不更改当前工作目录。

如果 `nullfd` 等于 (-1)，则不关闭标准输入、标准输出和标准错误的重定向。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`daemon` 和 `daemonfd` 函数可能失败并为库函数 [fork(2)](../sys/fork.2.md)、[open(2)](../sys/open.2.md) 和 [setsid(2)](../sys/setsid.2.md) 指定的任何错误设置 `errno`。

## 参见

[fork(2)](../sys/fork.2.md), [setsid(2)](../sys/setsid.2.md), [sigaction(2)](../sys/sigaction.2.md)

## 历史

`daemon` 函数首次出现于 4.4BSD。`daemonfd` 函数首次出现于 FreeBSD 12.0。

## 注意事项

在多线程程序中，`fork` 之后的子进程继承所有互斥锁和其他同步状态的副本，但只有调用线程存活。调用时由其他线程持有的任何锁将在子进程中永久保持获取状态，导致任何试图获取它们的代码死锁。在调用 [exec(3)](exec.3.md) 函数之一之前，子进程应仅限于异步信号安全的操作（参见 [sigaction(2)](../sys/sigaction.2.md)）。

除非 `noclose` 参数为非零，否则 `daemon` 将关闭前三个文件描述符并将其重定向到 **/dev/null**。通常，这些对应于标准输入、标准输出和标准错误。但是，如果这些文件描述符中的任何一个引用了其他内容，它们仍将被关闭，导致调用程序的行为不正确。如果在程序运行之前标准输入、标准输出或标准错误中的任何一个已被关闭，则可能发生这种情况。因此，使用 `daemon` 的程序应在打开任何文件或套接字之前调用 `daemon`，或者验证所获得的任何文件描述符的值大于 2。

`daemon` 函数在调用 [setsid(2)](../sys/setsid.2.md) 时临时忽略 `SIGHUP`，以防止父会话组领导者调用 [fork(2)](../sys/fork.2.md) 然后 [_exit(2)](../sys/_exit.2.md) 过早终止子进程。
