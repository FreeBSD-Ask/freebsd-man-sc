# abort2(2)

`abort2` — 终止进程并输出诊断信息

## 名称

`abort2`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
void
abort2(const char *why, int nargs, void **args);
```

## 描述

`abort2()` 系统调用使进程被杀死，并由内核将指定的诊断消息（带参数）传递给 syslogd(8) 守护进程。

`why` 参数指向一个以 `NUL` 结尾的字符串，用于指定程序终止的原因（最长 128 个字符）。`args` 数组包含若干指针，这些指针会以数值形式（使用内核的 `%p` [printf(9)](../man9/printf.9.md) 格式）记录到日志中。`nargs` 参数指定 `args` 中的指针数量（最多 16 个）。

`abort2()` 系统调用适用于进程无法继续执行、或因其他明确原因不应继续执行，且正常诊断通道无法可靠传递消息的情况。

## 返回值

`abort2()` 函数永远不会返回。

进程会被 `SIGABRT` 信号杀死；但如果传给 `abort2()` 的参数无效，则改用 `SIGKILL` 信号。

## 实例

```c
#include <stdlib.h>
if (weight_kg > max_load) {
	void *ptrs[3];
	ptrs[0] = (void *)(intptr_t)weight_kg;
	ptrs[1] = (void *)(intptr_t)max_load;
	ptrs[2] = haystack;
	abort2("Camel overloaded", 3, ptrs);
}
```

## 参见

[abort(3)](../man3/abort.3.md), [exit(3)](../man3/exit.3.md)

## 历史

`abort2()` 系统调用首次出现于 FreeBSD 7.0。

## 作者

`abort2()` 系统调用由 Poul-Henning Kamp <phk@FreeBSD.org> 设计，由 Wojciech A. Koszek <dunstan@freebsd.czest.pl> 实现。
