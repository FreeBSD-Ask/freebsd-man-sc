# kthread.9

`kthread_start` — 内核线程

## 名称

`kthread_start`, `kthread_shutdown`, `kthread_add`, `kthread_exit`, `kthread_resume`, `kthread_suspend`, `kthread_suspend_check`

## 概要

```c
#include <sys/kthread.h>

void
kthread_start(const void *udata)

void
kthread_shutdown(void *arg, int howto)

void
kthread_exit(void)

int
kthread_resume(struct thread *td)

int
kthread_suspend(struct thread *td, int timo)

void
kthread_suspend_check(void)
```

```c
#include <sys/unistd.h>

int
kthread_add(void (*func)(void *), void *arg, struct proc *procp,
    struct thread **newtdpp, int flags, int pages, const char *fmt, ...)

int
kproc_kthread_add(void (*func)(void *), void *arg, struct proc **procptr,
    struct thread **tdptr, int flags, int pages, char * procname,
    const char *fmt, ...)
```

## 描述

在 FreeBSD 8.0 中，较旧的 `kthread_*` 函数系列被重命名为 `kproc_*` 函数系列，因为它们以前命名错误，实际上产生的是内核进程。这个新的 `kthread_*` 函数系列被添加以产生真正的内核线程。有关重命名的调用，参见 [kproc(9)](kproc.9.md) 手册页。还请注意，`kproc_kthread_add` 函数出现在两个页面中，因为其功能是分开的。

`kthread_start` 函数用于启动 “内部” 守护进程，如 `bufdaemon` 和 `syncer`，旨在从 [SYSINIT(9)](SYSINIT.9.md) 调用。`udata` 参数实际上是指向 `struct kthread_desc` 的指针，描述应创建的内核线程：

```c
struct kthread_desc {
	char		*arg0;
	void		(*func)(void);
	struct thread	**global_threadpp;
};
```

`kthread_start` 使用结构成员如下：

**`arg0`** 用作线程名称的字符串。此字符串将被复制到新线程 `struct thread` 的 `td_name` 成员中。

**`func`** 此内核线程要运行的主函数。

**`global_threadpp`** 指向 `struct thread` 指针的指针，应更新为指向新创建线程的 `thread` 结构。如果此变量为 `NULL`，则忽略。该线程将是 `proc0`（PID 0）的子线程。

`kthread_add` 函数用于创建内核线程。新线程仅在内核模式下运行。它被添加到 `procp` 参数指定的进程，或者如果该参数为 `NULL`，则添加到 `proc0`。`func` 参数指定线程应执行的函数。`arg` 参数是一个任意指针，当新线程调用 `func` 时作为唯一参数传入。`newtdpp` 指针指向要更新为指向新创建线程的 `struct thread` 指针。如果此参数为 `NULL`，则忽略。`flags` 参数可设置为 `RFSTOPPED` 以使线程保持停止状态。调用者必须调用 `sched_add` 来启动线程。`pages` 参数指定新内核线程栈的大小（页）。如果为 0，则分配默认内核栈大小。其余参数构成 [printf(9)](printf.9.md) 参数列表，用于构建新线程的名称，并存储在新线程 `struct thread` 的 `td_name` 成员中。

`kproc_kthread_add` 函数与上述 `kthread_add` 函数非常相似，区别在于如果 kproc 尚不存在，则会创建它。此函数在 [kproc(9)](kproc.9.md) 手册页中有更好的文档。

`kthread_exit` 函数用于终止内核线程。它应由内核线程的主函数调用，而不是让主函数返回到其调用者。

`kthread_resume`、`kthread_suspend` 和 `kthread_suspend_check` 函数用于挂起和恢复内核线程。在其执行的主循环期间，希望允许自身被挂起的内核线程应调用 `kthread_suspend_check` 以检查是否被要求挂起。如果是，它将 msleep(9) 直到被告知恢复。一旦被告知恢复，它将返回，允许内核线程继续执行。其他两个函数用于通知内核线程挂起或恢复请求。`td` 参数指向要挂起或恢复的内核线程的 `struct thread`。对于 `kthread_suspend`，`timo` 参数指定等待内核线程确认挂起请求并自行挂起的超时时间。

`kthread_shutdown` 函数旨在注册为内核线程的关闭事件，这些线程需要在系统关闭期间自愿挂起以免干扰系统关闭活动。内核线程的实际挂起由 `kthread_suspend` 完成。

## 返回值

`kthread_add`、`kthread_resume` 和 `kthread_suspend` 函数成功时返回零，失败时返回非零。

## 实例

此示例演示了使用 `struct kthread_desc` 以及函数 `kthread_start`、`kthread_shutdown` 和 `kthread_suspend_check` 来运行 `bufdaemon` 进程。

```c
static struct thread *bufdaemonthread;
static struct kthread_desc buf_kp = {
	"bufdaemon",
	buf_daemon,
	&bufdaemonthread
};
SYSINIT(bufdaemon, SI_SUB_KTHREAD_BUF, SI_ORDER_FIRST, kthread_start,
    &buf_kp)
static void
buf_daemon()
{
	...
	/*
	 * 此进程需要在关闭同步之前挂起。
	 */
	EVENTHANDLER_REGISTER(shutdown_pre_sync, kthread_shutdown,
	    bufdaemonthread, SHUTDOWN_PRI_LAST);
	...
	for (;;) {
		kthread_suspend_check();
		...
	}
}
```

## 错误

`kthread_resume` 和 `kthread_suspend` 函数在以下情况下失败：

**[`EINVAL`]** `td` 参数未引用内核线程。

`kthread_add` 函数在以下情况下失败：

**[`ENOMEM`]** 无法分配线程栈的内存。

## 参见

[kproc(9)](kproc.9.md), [SYSINIT(9)](SYSINIT.9.md), wakeup(9)

## 历史

`kthread_start` 函数首次出现于 FreeBSD 2.2，当时创建的是整个进程。它在 FreeBSD 8.0 中被转换为创建线程。`kthread_shutdown`、`kthread_exit`、`kthread_resume`、`kthread_suspend` 和 `kthread_suspend_check` 函数引入于 FreeBSD 4.0，并在 FreeBSD 8.0 中转换为线程。`kthread_create` 调用在 FreeBSD 8.0 中重命名为 `kthread_add`。创建内核进程的旧功能重命名为 kproc_create(9)。在 FreeBSD 5.0 之前，`kthread_shutdown`、`kthread_resume`、`kthread_suspend` 和 `kthread_suspend_check` 函数分别命名为 `shutdown_kproc`、`resume_kproc`、`shutdown_kproc` 和 `kproc_suspend_loop`。
