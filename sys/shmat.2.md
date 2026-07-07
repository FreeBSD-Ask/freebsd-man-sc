# shmat(2)

`shmat` — 附接或分离共享内存

## 名称

`shmat`, `shmdt`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/ipc.h>`

`#include <sys/shm.h>`

```c
void *
shmat(int shmid, const void *addr, int flag)

int
shmdt(const void *addr)
```

## 描述

`shmat()` 系统调用将由 `shmid` 标识的共享内存段附接到调用进程的地址空间。段附接的地址按以下方式确定：

- 如果 `addr` 为 0，段附接到内核选择的地址。
- 如果 `addr` 非零且 `flag` 中未指定 `SHM_RND`，段附接到指定地址。
- 如果指定了 `addr` 且指定了 `SHM_RND`，`addr` 向下舍入到 `SHMLBA` 的最近倍数。

如果指定了 `SHM_REMAP` 标志且传入的 `addr` 不为 `NULL`，则在附接段之前清除虚拟地址范围内的任何现有映射。如果未指定该标志，`addr` 不为 `NULL`，且虚拟地址范围包含一些预先存在的映射，`shmat()` 调用将失败。

`shmdt()` 系统调用将位于 `addr` 指定地址的共享内存段从调用进程的地址空间中分离。

## 返回值

成功时，`shmat()` 返回段附接的地址；否则返回 -1，并设置 `errno` 以指示错误。

成功完成时，`shmdt()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`shmat()` 系统调用将在以下情况下失败：

**[`EINVAL`]** 没有找到与 `shmid` 对应的共享内存段。

**[`EINVAL`]** `addr` 参数不是可接受的地址。

**[`ENOMEM`]** 指定的 `addr` 不能用于映射，例如由于可用空间量小于段大小，或因为范围内存在预先存在的映射且未提供 `SHM_REMAP` 标志。

**[`EMFILE`]** 由于达到了每进程 `kern.ipc.shmseg` [sysctl(3)](../gen/sysctl.3.md) 限制，附接共享内存段失败。

`shmdt()` 系统调用将在以下情况下失败：

**[`EINVAL`]** `addr` 参数不指向共享内存段。

## 参见

[shmctl(2)](shmctl.2.md), [shmget(2)](shmget.2.md)
