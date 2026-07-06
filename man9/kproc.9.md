# kproc.9

`kproc_start` — 内核进程

## 名称

`kproc_start`, `kproc_shutdown`, `kproc_create`, `kproc_exit`, `kproc_resume`, `kproc_suspend`, `kproc_suspend_check`

## 概要

```c
#include <sys/kthread.h>
```

```c
void
kproc_start(const void *udata)

void
kproc_shutdown(void *arg, int howto)

int
kproc_create(void (*func)(void *), void *arg,
    struct proc **newpp, int flags, int pages, const char *fmt, ...)

void
kproc_exit(int ecode)

int
kproc_resume(struct proc *p)

int
kproc_suspend(struct proc *p, int timo)

void
kproc_suspend_check(struct proc *p)

int
kproc_kthread_add(void (*func)(void *), void *arg,
    struct proc **procptr, struct thread **tdptr,
    int flags, int pages, char * procname, const char *fmt, ...)
```

## 描述

在 FreeBSD 8.0 中，`kthread*` 9 函数系列被重命名为 `kproc*` 9 函数系列，因为它们命名错误，实际上产生的是内核进程。添加了一个*不同*的 `kthread_*` 9 函数系列来产生*真正的*内核*线程*。有关这些调用的更多信息，请参见 [kthread(9)](kthread.9.md) 手册页。还请注意，`kproc_kthread_add` 9 函数出现在两个页面中，因为其功能是分开的。

`kproc_start` 函数用于启动“内部”守护进程，例如 `bufdaemon` 和 `syncer`，并旨在从 [SYSINIT(9)](sysinit.9.md) 调用。`udata` 参数实际上是指向 `struct kproc_desc` 的指针，它描述了应创建的内核进程：

```c
struct kproc_desc {
	char		*arg0;
	void		(*func)(void);
	struct proc	**global_procpp;
};
```

`kproc_start` 使用结构成员如下：

**`arg0`** 用作进程名称的字符串。此字符串将被复制到新进程 `struct proc` 的 `p_comm` 成员中。

**`func`** 此内核进程要运行的主函数。

**`global_procpp`** 指向 `struct proc` 指针的指针，该指针应更新为指向新创建进程的进程结构。如果此变量为 `NULL`，则被忽略。

`kproc_create` 函数用于创建内核进程。新进程与进程 0（`swapper` 进程）共享其地址空间，并仅在内核模式下运行。`func` 参数指定进程应执行的函数。`arg` 参数是一个任意指针，在新进程调用 `func` 时作为唯一参数传递。`newpp` 指针指向要更新为指向新创建进程的 `struct proc` 指针。如果此参数为 `NULL`，则被忽略。`flags` 参数指定 rfork(2) 中描述的一组标志。`pages` 参数指定新内核进程栈的页面大小。如果使用 0，则分配默认内核栈大小。其余参数形成 [printf(9)](printf.9.md) 参数列表，用于构建新进程的名称并存储在新进程 `struct proc` 的 `p_comm` 成员中。

`kproc_exit` 函数用于终止内核进程。它应由内核进程的主函数调用，而不是让主函数返回其调用者。`ecode` 参数指定进程的退出状态。退出时，函数 exit1(9) 将在进程句柄上发起对 wakeup(9) 的调用。

`kproc_resume`、`kproc_suspend` 和 `kproc_suspend_check` 函数用于挂起和恢复内核进程。在其执行的主循环期间，希望允许自身被挂起的内核进程应调用 `kproc_suspend_check`，将 `curproc` 作为唯一参数传入。此函数检查内核进程是否已被要求挂起。如果是，它将 tsleep(9) 直到被告知恢复。一旦被告知恢复，它将返回，允许内核进程继续执行。其他两个函数用于通知内核进程挂起或恢复请求。`p` 参数指向要挂起或恢复的内核进程的 `struct proc`。对于 `kproc_suspend`，`timo` 参数指定等待内核进程确认挂起请求并挂起自身的超时时间。

`kproc_shutdown` 函数旨在注册为需要在系统关闭期间自愿挂起以免干扰系统关闭活动的内核进程的关闭事件。内核进程的实际挂起通过 `kproc_suspend` 完成。

`kproc_kthread_add` 函数与上面的 `kproc_create` 函数非常相似，不同之处在于如果 kproc 已存在，则仅在现有进程上创建一个新线程（参见 [kthread(9)](kthread.9.md)）。`func` 参数指定进程应执行的函数。`arg` 参数是一个任意指针，在新进程调用 `func` 时作为唯一参数传递。`procptr` 指针指向 `struct proc` 指针，如果创建新进程，该位置将用新进程指针更新，如果不为 `NULL`，则必须包含已存在进程的进程指针。如果此参数指向 `NULL`，则创建新进程并更新该字段。如果不为 NULL，`tdptr` 指针指向 `struct thread` 指针，该位置将用新线程指针更新。`flags` 参数指定 rfork(2) 中描述的一组标志。`pages` 参数指定新内核线程栈的页面大小。如果使用 0，则分配默认内核栈大小。procname 参数是如果需要创建新进程时应给予新进程的名称。它*不是* printf 风格的格式说明符，而是简单字符串。其余参数形成 [printf(9)](printf.9.md) 参数列表，用于构建新线程的名称并存储在新线程 `struct thread` 的 `td_name` 成员中。

## 返回值

`kproc_create`、`kproc_resume` 和 `kproc_suspend` 函数成功时返回零，失败时返回非零。

## 实例

此示例演示了使用 `struct kproc_desc` 以及函数 `kproc_start`、`kproc_shutdown` 和 `kproc_suspend_check` 来运行 `bufdaemon` 进程。

```c
static struct proc *bufdaemonproc;
static struct kproc_desc buf_kp = {
	"bufdaemon",
	buf_daemon,
	&bufdaemonproc
};
SYSINIT(bufdaemon, SI_SUB_KTHREAD_BUF, SI_ORDER_FIRST, kproc_start,
    &buf_kp)
static void
buf_daemon()
{
	...
	/*
	 * 此进程需要在关闭同步之前被挂起。
	 */
	EVENTHANDLER_REGISTER(shutdown_pre_sync, kproc_shutdown,
	    bufdaemonproc, SHUTDOWN_PRI_LAST);
	...
	for (;;) {
		kproc_suspend_check(bufdaemonproc);
		...
	}
}
```

## 错误

`kproc_resume` 和 `kproc_suspend` 函数在以下情况下会失败：

**[Er** EINVAL] `p` 参数未引用内核进程。

`kproc_create` 函数在以下情况下会失败：

**[Er** EAGAIN] 将超过系统对执行中进程总数的限制。该限制由 sysctl(3) MIB 变量 `KERN_MAXPROC` 给出。

**[Er** EINVAL] 在 `flags` 参数中指定了 `RFCFDG` 标志。

## 参见

rfork(2), exit1(9), [kthread(9)](kthread.9.md), [SYSINIT(9)](sysinit.9.md), wakeup(9)

## 历史

`kproc_start` 函数首次出现在 FreeBSD 2.2 中。`kproc_shutdown`、`kproc_create`、`kproc_exit`、`kproc_resume`、`kproc_suspend` 和 `kproc_suspend_check` 函数在 FreeBSD 4.0 中引入。在 FreeBSD 5.0 之前，`kproc_shutdown`、`kproc_resume`、`kproc_suspend` 和 `kproc_suspend_check` 函数分别命名为 `shutdown_kproc`、`resume_kproc`、`shutdown_kproc` 和 `kproc_suspend_loop`。它们最初命名为 `kthread_*`，但在真正的 kthreads 可用后更改为 `kproc_*`。
