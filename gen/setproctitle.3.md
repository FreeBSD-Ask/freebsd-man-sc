# setproctitle(3)

`setproctitle` — 设置进程标题

## 名称

`setproctitle`, `setproctitle_fast` — 设置进程标题

## 概要

```c
#include <unistd.h>

void
setproctitle(const char *fmt, ...);

void
setproctitle_fast(const char *fmt, ...);
```

## 描述

`setproctitle` 库例程设置出现在 [ps(1)](../man1/ps.1.md) 命令中的进程标题。`setproctitle_fast` 变体针对高频更新进行了优化，但可能通过不更新程序参数的内核缓存而使 [ps(1)](../man1/ps.1.md) 命令稍慢。

标题由可执行文件的名称开始，后跟由 `fmt` 参数指定的 [printf(3)](../stdio/printf.3.md) 风格的参数扩展结果。如果 `fmt` 参数以 “-” 字符开头，则跳过可执行文件的名称。

如果 `fmt` 为 NULL，则恢复进程标题。

## 实例

将守护进程的标题设置为其活动状态：

```c
setproctitle("talking to %s", inet_ntoa(addr));
```

## 参见

[ps(1)](../man1/ps.1.md), [w(1)](../man1/w.1.md), kvm(3), kvm_getargv(3), [printf(3)](../stdio/printf.3.md), setprogname(3)

## 标准

`setproctitle` 函数本质上是非标准的。其他导致 [ps(1)](../man1/ps.1.md) 命令行改变的方法，包括覆盖 argv[0] 字符串，也本质上不可移植。如果存在操作系统提供的 `setproctitle`，优先使用它。

遗憾的是，其他版本的 `setproctitle` 可能存在其他调用约定，尽管作者尚未发现任何此类约定。本实现被认为是主流约定。

一般认为该实现与其他系统（包括 NetBSD 和 BSD/OS）兼容。

## 历史

`setproctitle` 函数首次出现于 FreeBSD 2.2。`setproctitle_fast` 函数首次出现于 FreeBSD 12。其他操作系统有类似的功能。

## 作者

Peter Wemm <peter@FreeBSD.org> 从 Eric Allman <eric@sendmail.org> 的 **Sendmail 8.7.3** 源代码中借鉴了此想法。

## 缺陷

切勿在不使用 `%s` 的情况下将带有用户 supplied 数据的字符串作为格式传递。攻击者可以在字符串中放入格式说明符来破坏栈，可能导致安全漏洞。即使字符串是使用类似 `snprintf` 的函数构建的也同样如此，因为生成的字符串可能仍包含用户提供的转换说明符，供后续 `setproctitle` 插值。

始终使用正确的安全写法：

```c
setproctitle("%s", string);
```
