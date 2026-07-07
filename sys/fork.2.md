# fork(2)

`fork` — 创建新进程

## 名称

`fork`, `_Fork`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
pid_t
fork(void);

pid_t
_Fork(void);
```

## 描述

`fork()` 函数用于创建新进程。新进程（子进程）是调用进程（父进程）的精确副本，但有以下不同：

- 子进程具有唯一的进程 ID。
- 子进程具有不同的父进程 ID（即父进程的进程 ID）。
- 子进程拥有父进程描述符的副本，但由 [kqueue(2)](kqueue.2.md) 返回的描述符不会从父进程继承。这些描述符引用相同的底层对象，因此文件对象中的文件指针在子进程和父进程之间共享，例如在子进程中对某个描述符调用 [lseek(2)](lseek.2.md) 可能影响父进程随后的 [read(2)](read.2.md) 或 [write(2)](write.2.md)。shell 也利用这种描述符复制机制为新建进程建立标准输入和输出，以及设置管道。任何标记了 close-on-fork 标志 `FD_CLOFORK` 的文件描述符（参见 `fcntl(2)` 和 `open(2)` 中的 `O_CLOFORK`）不会出现在子进程中，但在父进程中保持打开。
- 子进程的资源使用量被设置为 0；参见 `setrlimit(2)`。
- 所有间隔定时器都被清除；参见 `setitimer(2)`。
- 子进程的 robust mutex 列表（参见 `pthread_mutexattr_setrobust(3)`）会被清除。
- 通过 [pthread_atfork(3)](../man3/pthread_atfork.3.md) 函数建立的 atfork 处理程序会在父进程中 `fork()` 之前被调用，子进程创建之后在父进程和子进程中也会被调用。
- 子进程只有一个线程，对应父进程中的调用线程。如果进程拥有多个线程，其他线程持有的锁和其他资源不会被释放，因此在调用 [execve(2)](execve.2.md) 或类似函数之前，子进程中只能保证异步信号安全函数（参见 [sigaction(2)](sigaction.2.md)）可用。FreeBSD 的 `fork()` 实现在子进程中提供可用的 `malloc(3)` 和 `rtld(1)` 服务。

`fork()` 函数不是异步信号安全的，并且在父进程中创建一个取消点。它不能安全地从信号处理程序中使用，由 [pthread_atfork(3)](../man3/pthread_atfork.3.md) 建立的 atfork 处理程序也不需要是异步信号安全的。

`_Fork()` 函数创建新进程的方式与 `fork()` 类似，但它是异步信号安全的。`_Fork()` 不会调用 atfork 处理程序，也不会创建取消点。它可以安全地从信号处理程序中使用，但如果从多线程父进程派生，子进程中将没有用户空间服务（`malloc(3)` 或 `rtld(1)`）可用。

特别是，如果使用动态链接，子进程在 `_Fork()` 之后使用的所有动态符号必须预先解析。注意：可以通过向动态链接器指定 `LD_BIND_NOW` 环境变量全局进行解析，或者通过向静态链接器 [ld(1)](../man1/ld.lld.1.md) 传递 `-z` `now` 选项按二进制文件进行解析，也可以通过在 `_Fork()` 调用之前使用每个符号来强制绑定。这些方法都会微妙地改变生成二进制文件的 ABI。

## 返回值

成功完成时，`fork()` 和 `_Fork()` 向子进程返回值 0，向父进程返回子进程的进程 ID。否则，向父进程返回值 -1，不创建子进程，并设置全局变量 `errno` 以指示错误。

## 实例

以下示例展示了 `fork()` 在实践中的常见使用模式。

```c
#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int
main(void)
{
	pid_t pid;
	/*
	 * 如果子进程预期会使用 stdio(3)，则必须
	 * 在父进程和子进程之间同步重用的 I/O 流状态，
	 * 以避免重复输出和其他可能的问题。
	 */
	fflush(stdout);
	switch (pid = fork()) {
	case -1:
		err(1, "Failed to fork");
	case 0:
		printf("Hello from child process!\n");
		/*
		 * 由于我们写入了 stdout，子进程需要使用
		 * exit(3) 而不是 _exit(2)。这会导致
		 * 通过 atexit(3) 注册的处理程序被调用两次，
		 * 一次在父进程中，一次在子进程中。如果不希望
		 * 这种行为，可以考虑用 _exit(2) 或 _Exit(3)
		 * 终止子进程。
		 */
		exit(0);
	default:
		break;
	}
	printf("Hello from parent process (child's PID: %d)!\n", pid);
	return (0);
}
```

该程序的输出大致如下：

```sh
Hello from parent process (child's PID: 27804)!
Hello from child process!
```

## 错误

`fork()` 系统调用将在以下情况下失败且不创建子进程：

**[`EAGAIN`]** 将超过系统对执行中进程总数的限制。该限制由 [sysctl(3)](../gen/sysctl.3.md) MIB 变量 `KERN_MAXPROC` 给出。（对于超级用户以外的用户，该限制实际上比此值小 10。）

**[`EAGAIN`]** 用户不是超级用户，且将超过系统对单个用户执行中进程总数的限制。该限制由 [sysctl(3)](../gen/sysctl.3.md) MIB 变量 `KERN_MAXPROCPERUID` 给出。

**[`EAGAIN`]** 用户不是超级用户，且将超过对应于 `resource` 参数 `RLIMIT_NPROC` 的软资源限制（参见 [getrlimit(2)](getrlimit.2.md)）。

**[`ENOMEM`]** 没有足够的交换空间用于新进程。

## 参见

[execve(2)](execve.2.md), [rfork(2)](rfork.2.md), `setitimer(2)`, `setrlimit(2)`, [sigaction(2)](sigaction.2.md), [vfork(2)](vfork.2.md), [wait(2)](wait.2.md), [pthread_atfork(3)](../man3/pthread_atfork.3.md)

## 标准

`fork()` 和 `_Fork()` 函数遵循 -p1003.1-2024。

## 历史

`fork()` 函数出现于 Version 1 AT&T UNIX。`_Fork()` 函数出现于 FreeBSD 13.1。
