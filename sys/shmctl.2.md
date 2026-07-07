# shmctl(2)

`shmctl` — 共享内存控制

## 名称

`shmctl`

## 库

Lb libc

## 概要

```c
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>

int
shmctl(int shmid, int cmd, struct shmid_ds *buf);
```

## 描述

对 `shmid` 所标识的共享内存段执行 `cmd` 所指定的操作：

**`IPC_STAT`** 获取该段的 `struct shmid_ds`，并将其存储到 `buf` 所指向的内存中。

**`IPC_SET`** 将该段 `struct shmid_ds` 的 `shm_perm.uid`、`shm_perm.gid` 和 `shm_perm.mode` 成员更改为与 `buf` 所指向结构中的相应成员一致。调用进程的有效 uid 必须与 `shm_perm.uid` 或 `shm_perm.cuid` 匹配，否则必须具有超级用户权限。

**`IPC_RMID`** 从系统中移除该段。移除操作在所有已附加该段的进程退出后才会生效。要使操作成功，调用进程的有效 uid 必须与 `shm_perm.uid` 或 `shm_perm.cuid` 匹配，否则该进程必须具有超级用户权限。如果 `kern.ipc.shm_allow_removed` [sysctl(3)](../gen/sysctl.3.md) 变量设置为 0，则一旦执行了 IPC_RMID 操作，将不允许更多进程附加该段。

`shmid_ds` 结构定义如下：

```c
struct shmid_ds {
    struct ipc_perm shm_perm;   /* 操作权限结构 */
    size_t          shm_segsz;  /* 段大小（字节） */
    pid_t           shm_lpid;   /* 最后一次共享内存操作的进程 ID */
    pid_t           shm_cpid;   /* 创建者的进程 ID */
    int             shm_nattch; /* 当前附加数量 */
    time_t          shm_atime;  /* 最后一次 shmat() 的时间 */
    time_t          shm_dtime;  /* 最后一次 shmdt() 的时间 */
    time_t          shm_ctime;  /* 最后一次由 shmctl() 更改的时间 */
};
```

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`shmctl()` 系统调用将在以下情况下失败：

**[`EINVAL`]** 操作无效，或找不到与 `shmid` 对应的共享内存段。

**[`EPERM`]** 调用进程的有效 uid 与共享内存段所有者或创建者的 uid 不匹配。

**[`EACCES`]** 由于操作与共享内存段模式不匹配而拒绝权限。

## 参见

[shmat(2)](shmat.2.md), shmdt(2), [shmget(2)](shmget.2.md), [ftok(3)](../gen/ftok.3.md)
