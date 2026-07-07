# siginterrupt(3)

`siginterrupt` — 允许信号中断系统调用

## 名称

`siginterrupt`

## 库

Lb libc

## 概要

`#include <signal.h>`

```c
int
siginterrupt(int sig, int flag)
```

## 描述

`siginterrupt` 函数用于更改系统调用被指定信号中断时的重启行为。如果 `flag` 为假（0），则系统调用在被指定信号中断且尚未传输数据时将被重启。系统调用重启自 4.2BSD 起就是默认行为，也是 FreeBSD 上 [signal(3)](signal.3.md) 的默认行为。

如果 `flag` 为真（1），则禁用系统调用重启。如果系统调用被指定信号中断且尚未传输数据，系统调用将返回 -1，并将全局变量 `errno` 设置为 `EINTR`。已开始传输数据的中断系统调用将返回实际传输的数据量。系统调用中断是 4.1BSD 和 AT&T System V UNIX 系统上的信号行为。

注意，新的 4.2BSD 信号处理语义在其他方面不做任何改变。最值得注意的是，信号处理程序始终保持安装状态，直到被后续的 [sigaction(2)](../sys/sigaction.2.md) 调用显式更改，且信号掩码按 [sigaction(2)](../sys/sigaction.2.md) 中的文档说明运作。程序可以在执行过程中根据需要频繁地在可重启和可中断的系统调用操作之间切换。

在信号处理程序执行期间发出 `siginterrupt` 调用，将使新动作在下一个被捕获的信号上生效。

## 注释

此库例程使用了 [sigaction(2)](../sys/sigaction.2.md) 系统调用的一个扩展，该扩展在 4.2BSD 中不可用，因此如果需要向后兼容则不应使用。

## 返回值

成功完成时，`siginterrupt` 函数返回 0；否则返回 -1 并设置全局变量 `errno` 以指示错误。

## 错误

`siginterrupt` 调用在以下情况失败：

**[`EINVAL`]** `sig` 参数不是有效的信号编号。

## 参见

[sigaction(2)](../sys/sigaction.2.md), [sigprocmask(2)](../sys/sigprocmask.2.md), [sigsuspend(2)](../sys/sigsuspend.2.md), [signal(3)](signal.3.md)

## 历史

`siginterrupt` 函数出现于 4.3BSD。
