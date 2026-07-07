# semctl(2)

`semctl` — 对信号量集执行控制操作

## 名称

`semctl`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/ipc.h>`

`#include <sys/sem.h>`

```c
int
semctl(int semid, int semnum, int cmd, ...);
```

## 描述

`semctl()` 系统调用对由 `semid` 指示的信号量集执行由 `cmd` 指示的操作。对于某些 `cmd` 值，需要第四个参数 `union semun arg`。对于使用 `arg` 参数的命令，`union semun` 必须定义如下：

```c
union semun {
        int     val;            /* SETVAL 的值 */
        struct  semid_ds *buf;  /* IPC_STAT 和 IPC_SET 的缓冲区 */
        u_short *array;         /* GETALL 和 SETALL 的数组 */
};
```

不可移植的软件可在包含 `sys/sem.h` 之前定义 `_WANT_SEMUN`，以使用系统提供的 `union semun` 定义。

各命令执行如下：

**`IPC_STAT`** 获取信号量集的 `struct semid_ds`，并将其存储到 `arg.buf` 所指向的内存中。

**`IPC_SET`** 将信号量集 `struct semid_ds` 的 `sem_perm.uid`、`sem_perm.gid` 和 `sem_perm.mode` 成员修改为与 `arg.buf` 所指向结构中的对应成员一致。调用进程的有效 uid 必须与 `sem_perm.uid` 或 `sem_perm.cuid` 匹配，或者具有超级用户特权。

**`IPC_RMID`** 立即从系统中移除该信号量集。调用进程的有效 uid 必须等于该信号量集的 `sem_perm.uid` 或 `sem_perm.cuid`，或者该进程必须具有超级用户特权。

**`GETVAL`** 返回信号量编号 `semnum` 的值。

**`SETVAL`** 将信号量编号 `semnum` 的值设置为 `arg.val`。任何进程中该信号量的未决 exit 时调整值均被清除。

**`GETPID`** 返回最后对信号量编号 `semnum` 执行操作的进程的 pid。

**`GETNCNT`** 返回等待信号量编号 `semnum` 的值变得大于其当前值的进程数。

**`GETZCNT`** 返回等待信号量编号 `semnum` 的值变为 0 的进程数。

**`GETALL`** 将集合中所有信号量的值获取到 `arg.array` 所指向的数组中。

**`SETALL`** 将集合中所有信号量的值设置为 `arg.array` 所指向数组中的值。任何进程中此集合中所有信号量的未决 exit 时调整值均被清除。

`struct semid_ds` 定义如下：

```c
struct semid_ds {
        struct  ipc_perm sem_perm;      /* 操作权限结构 */
        u_short sem_nsems;      /* 集合中信号量数量 */
        time_t  sem_otime;      /* 最后操作时间 */
        time_t  sem_ctime;      /* 最后修改时间 */
                                /* 时间以自 1970 年 1 月 1 日 */
                                /* GMT 00:00:00 起的秒数计量 */
};
```

## 返回值

成功时，当 `cmd` 为 `GETVAL`、`GETPID`、`GETNCNT` 或 `GETZCNT` 之一时，`semctl()` 返回对应的值；否则返回 0。失败时返回 -1，并设置 `errno` 以指示错误。

## 错误

`semctl()` 系统调用将在以下情况下失败：

**[`EINVAL`]** 没有信号量集对应于 `semid`。

**[`EINVAL`]** `semnum` 参数不在给定信号量集的有效信号量范围内。

**[`EPERM`]** 调用进程的有效 uid 与信号量集所有者或创建者的 uid 不匹配。

**[`EACCES`]** 由于操作与信号量集模式不匹配而拒绝权限。

**[`ERANGE`]** `SETVAL` 或 `SETALL` 试图将信号量设置为超出允许范围 [0 .. `SEMVMX`] 的值。

## 参见

[semget(2)](semget.2.md), [semop(2)](semop.2.md)

## 缺陷

`SETALL` 可能在返回错误之前已更新部分信号量元素。
