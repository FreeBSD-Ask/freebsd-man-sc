# semop(2)

`semop` — 对信号量集的原子操作数组

## 名称

`semop`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/ipc.h>`

`#include <sys/sem.h>`

```c
int
semop(int semid, struct sembuf *array, size_t nops)
```

## 描述

`semop()` 系统调用对由 `semid` 指示的信号量集原子地执行由 `array` 指示的操作数组。`array` 的长度由 `nops` 指示。每个操作编码在 `struct sembuf` 中，其定义如下：

```c
struct sembuf {
        u_short sem_num;        /* 信号量编号 */
        short   sem_op;         /* 信号量操作 */
        short   sem_flg;        /* 操作标志 */
};
```

对于 `array` 中的每个元素，`sem_op` 和 `sem_flg` 确定要对集合中编号为 `sem_num` 的信号量执行的操作。值 `SEM_UNDO` 和 `IPC_NOWAIT` 可以*按位或*到 `sem_flg` 成员中，以修改给定操作的行为。

执行的操作根据 `sem_op` 的值而定：

- 当 `sem_op` 为正且进程有修改权限时，信号量的值增加 `sem_op` 的值。如果指定了 `SEM_UNDO`，信号量的退出调整值减少 `sem_op` 的值。`sem_op` 为正值通常对应于进程释放与信号量关联的资源。
- 当 `sem_op` 为负且进程有修改权限时，行为取决于信号量的当前值：
  - 如果信号量的当前值大于或等于 `sem_op` 的绝对值，则该值减少 `sem_op` 的绝对值。如果指定了 `SEM_UNDO`，信号量的退出调整值增加 `sem_op` 的绝对值。
  - 如果信号量的当前值小于 `sem_op` 的绝对值，则发生以下情况之一：
    - 如果指定了 `IPC_NOWAIT`，则 `semop()` 立即返回，返回值为 `EAGAIN`。
    - 否则，调用进程将休眠，直到满足以下条件之一：
      - 某个其他进程使用 [semctl(2)](semctl.2.md) 的 `IPC_RMID` 选项删除了信号量。在这种情况下，`semop()` 立即返回，返回值为 `EIDRM`。
      - 进程收到一个要捕获的信号。在这种情况下，进程将按 [sigaction(2)](sigaction.2.md) 定义的恢复执行。
      - 信号量的值大于或等于 `sem_op` 的绝对值。当此条件为真时，信号量的值减少 `sem_op` 的绝对值，信号量的退出调整值增加 `sem_op` 的绝对值。

  `sem_op` 为负值通常意味着进程正在等待资源变为可用。
- 当 `sem_op` 为零且进程有读权限时，将发生以下情况之一：
  - 如果信号量的当前值等于零，则 `semop()` 可以立即返回。
  - 如果指定了 `IPC_NOWAIT`，则 `semop()` 立即返回，返回值为 `EAGAIN`。
  - 否则，调用进程将休眠，直到满足以下条件之一：
    - 某个其他进程使用 [semctl(2)](semctl.2.md) 的 `IPC_RMID` 选项删除了信号量。在这种情况下，`semop()` 立即返回，返回值为 `EIDRM`。
    - 进程收到一个要捕获的信号。在这种情况下，进程将按 [sigaction(2)](sigaction.2.md) 定义的恢复执行。
    - 信号量的值变为零。

对于进程使用的每个信号量，内核维护一个“退出调整”值，如前所述。当进程退出时（无论是自愿还是非自愿），每个信号量的退出调整值都会加到信号量的值上。这可用于确保在进程意外终止时释放资源。

## 返回值

成功完成时，`semop()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`semop()` 系统调用将在以下情况下失败：

**[`EINVAL`]** 没有与 `semid` 对应的信号量集，或进程将超过系统定义的每进程 `SEM_UNDO` 结构数限制。

**[`EACCES`]** 由于操作与信号量集的模式不匹配而拒绝权限。

**[`EAGAIN`]** 信号量的值将导致进程休眠，且指定了 `IPC_NOWAIT`。

**[`E2BIG`]** 指定的操作过多。[`SEMOPM`]

**[`EFBIG`]** `sem_num` 不在集合的有效信号量范围内。

**[`EIDRM`]** 信号量集已从系统中移除。

**[`EINTR`]** `semop()` 系统调用被信号中断。

**[`ENOSPC`]** 系统 `SEM_UNDO` 池 [`SEMMNU`] 已满。

**[`ERANGE`]** 请求的操作将导致信号量的当前值 [`SEMVMX`] 或其退出调整值 [`SEMAEM`] 超过系统施加的限制。

## 参见

[semctl(2)](semctl.2.md), [semget(2)](semget.2.md), [sigaction(2)](sigaction.2.md)

## 缺陷

即使指定了 `IPC_NOWAIT`，`semop()` 系统调用也可能因等待内存而阻塞。
