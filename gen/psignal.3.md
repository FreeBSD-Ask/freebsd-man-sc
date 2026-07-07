# psignal(3)

`psignal` — 系统信号消息

## 名称

`psignal`, `psiginfo`, `strsignal`, `sys_siglist`, `sys_signame`, `sig2str`, `str2sig` — 系统信号消息

## 库

Lb libc

## 概要

```c
#include <signal.h>

void
psignal(int sig, const char *s);

void
psiginfo(const siginfo_t *si, const char *s);

extern const char * const sys_siglist[];
extern const char * const sys_signame[];
```

```c
#include <string.h>

char *
strsignal(int sig);

int
sig2str(int signum, char *str);

int
str2sig(char *str, int *pnum);
```

## 描述

`psignal` 和 `strsignal` 函数定位信号编号对应的描述性消息字符串。

`strsignal` 函数接受信号编号参数 `sig`，返回指向相应消息字符串的指针。

`psignal` 函数接受信号编号参数 `sig` 并将其写入标准错误。如果参数 `s` 非 `NULL` 且不指向空字符，则在消息字符串之前将 `s` 写入标准错误文件描述符，紧接着是一个冒号和一个空格。如果信号编号无法识别（[sigaction(2)](../sys/sigaction.2.md)），则产生字符串 “Unknown signal”。

`psiginfo` 函数类似于 `psignal`，不同之处在于信号编号信息取自 `si` 参数，该参数是一个 `siginfo_t` 结构。

消息字符串可以通过外部数组 `sys_siglist` 直接访问，按已识别的信号编号索引。外部数组 `sys_signame` 用法类似，包含信号的简短大写缩写，对于识别用户输入中的信号名称很有用。定义的变量 `NSIG` 包含 `sys_siglist` 和 `sys_signame` 中字符串的计数。

`sig2str` 函数将信号编号 `signum` 转换为信号名称（不带 “SIG” 前缀），并存储在 `str` 指定的位置，该位置应足够大以容纳名称和终止 `NUL` 字节。符号 `SIG2STR_MAX` 给出了所需的以字节为单位的最大大小。

`str2sig` 函数将信号名称 `str` 转换为信号编号，并存储在 `pnum` 引用的位置。`str` 中的名称可以是信号的名称（带或不带 “SIG” 前缀）或十进制数字。

## 返回值

`sig2str` 和 `str2sig` 成功时返回 0，转换失败时返回 -1。在后一种情况下，存储转换结果的内存保持不变。

## 参见

[sigaction(2)](../sys/sigaction.2.md), perror(3), [strerror(3)](strerror.3.md)

## 标准

`psignal` 和 `psiginfo` 函数由 IEEE Std 1003.1-2008 ("POSIX.1") 定义，而 `sig2str` 和 `str2sig` 函数由 -p1003.1-2024 定义。

## 历史

`psignal` 函数出现于 4.2BSD。`psiginfo` 函数出现于 FreeBSD 14.3、NetBSD 6.0 和 Dx 4.1。`sig2str` 和 `str2sig` 函数出现于 FreeBSD 15.0。

