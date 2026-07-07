# filemon(4)

`filemon` — filemon 设备

## 名称

`filemon`

## 概要

`device filemon`

`#include <dev/filemon/filemon.h>`

## 描述

`filemon` 设备允许进程收集其子进程的文件操作数据。设备 **/dev/filemon** 响应两种 ioctl(2) 调用。

`filemon` 并非安全审计工具。许多系统调用不会被跟踪，使用非原生 ABI 的二进制程序可能无法被完整审计。其目的是通过高效且易于解析的格式审计进程，以确定它们的依赖关系。这样的一个例子是 [make(1)](../man1/make.1.md)，它使用此模块配合 **.MAKE.MODE=meta** 更智能地处理增量构建。

系统调用使用以下单字母表示：

**`A`** openat(2)。下一条日志条目可能缺少绝对路径或不准确。
**`C`** chdir(2)
**`D`** unlink(2)
**`E`** execve(2)
**`F`** fork(2), vfork(2)
**`L`** link(2), linkat(2), symlink(2)
**`M`** rename(2)
**`R`** open(2) 或 openat(2) 用于读取
**`W`** open(2) 或 openat(2) 用于写入
**`X`** _exit(2)

注意，`W` 记录之后的 `R` 可以表示一次以读/写方式进行的 open(2)，也可以是两次独立的 open(2) 调用，一次为 `R`，一次为 `W`。注意，仅成功的系统调用会被捕获。

## IOCTL

用户态程序通过若干 ioctl 与 `filemon` 驱动程序通信，如下所述。每个调用接受单个参数。

**`FILEMON_SET_FD`** 将内部跟踪缓冲区写入到所提供的已打开文件描述符。

**`FILEMON_SET_PID`** 要跟踪的子进程 ID。通常应在子进程中 fork(2) 之后、执行其他操作之前，由父进程在控制下完成。参见下文示例。

## 返回值

ioctl 函数成功时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

使用 `FILEMON_SET_FD` 的 ioctl 系统调用在以下情况下会失败：

**[Er** EEXIST] `filemon` 句柄已与某个文件描述符关联。

**[Er** EINVAL] 文件描述符类型无效，不能用于跟踪。

**[Er** EBADF] 文件描述符无效或未以写入方式打开。

使用 `FILEMON_SET_PID` 的 ioctl 系统调用在以下情况下会失败：

**[Er** ESRCH] 不存在具有指定进程 ID 的进程。

**[Er** EBUSY] 指定的进程 ID 已在被跟踪，且不是当前进程。

对 filemon 文件描述符的 close 系统调用可能在写入日志时遇到错误而以 write(2) 的错误失败。也可能在以下情况下失败：

**[Er** EFAULT] 被跟踪系统调用的参数使用了无效地址，导致该系统调用没有日志条目。

**[Er** ENAMETOOLONG] 被跟踪系统调用的参数过长，导致该系统调用没有日志条目。

## 文件

**/dev/filemon**

## 实例

```sh
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <sys/ioctl.h>
#include <dev/filemon/filemon.h>
#include <fcntl.h>
#include <err.h>
#include <errno.h>
#include <unistd.h>
static void
open_filemon(void)
{
	pid_t child, wait_rv;
	int fm_fd, fm_log;
	if ((fm_fd = open("/dev/filemon", O_RDWR | O_CLOEXEC)) == -1)
		err(1, "open(e"/dev/filemone", O_RDWR)");
	if ((fm_log = open("filemon.out",
	    O_CREAT | O_WRONLY | O_TRUNC | O_CLOEXEC, DEFFILEMODE)) == -1)
		err(1, "open(filemon.out)");
	if (ioctl(fm_fd, FILEMON_SET_FD, &fm_log) == -1)
		err(1, "Cannot set filemon log file descriptor");
	if ((child = fork()) == 0) {
		child = getpid();
		if (ioctl(fm_fd, FILEMON_SET_PID, &child) == -1)
			err(1, "Cannot set filemon PID");
		/* 在此执行某些操作。 */
	} else if (child == -1)
		err(1, "Cannot fork child");
	else {
		while ((wait_rv = wait(&child)) == -1 &&
		    errno == EINTR)
			;
		if (wait_rv == -1)
			err(1, "cannot wait for child");
		close(fm_fd);
	}
}
```

创建一个名为 `filemon.out` 的文件，并配置 `filemon` 设备将 `filemon` 缓冲区内容写入其中。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [ktrace(1)](../man1/ktrace.1.md), script(1), [truss(1)](../man1/truss.1.md), ioctl(2)

## 历史

`filemon` 设备出现于 FreeBSD 9.1。

## 缺陷

卸载模块可能导致系统 panic，因此需要使用 `kldunload -f`。
