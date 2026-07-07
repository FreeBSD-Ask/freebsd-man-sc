# membarrier(2)

`membarrier` — 内存屏障

## 名称

`membarrier`

## 库

Lb libc

## 概要

`#include <sys/membarrier.h>`

```c
int
membarrier(int cmd, unsigned flags, int cpu_id);
```

## 描述

`membarrier` 系统调用提供内存屏障，确保在同一地址空间中由不同线程或进程执行的内存访问之间的顺序。

可以指定以下 `cmd` 值：

**`MEMBARRIER_CMD_QUERY`** 查询支持的命令。返回内核支持的命令的位掩码。

**`MEMBARRIER_CMD_GLOBAL`** 为所有进程的所有线程发出内存屏障。

**`MEMBARRIER_CMD_SHARED`** 这是 `MEMBARRIER_CMD_GLOBAL` 的别名。

**`MEMBARRIER_CMD_GLOBAL_EXPEDITED`** 对所有注册了 `MEMBARRIER_CMD_REGISTER_GLOBAL_EXPEDITED` 的进程的所有运行中线程执行内存屏障。

**`MEMBARRIER_CMD_REGISTER_GLOBAL_EXPEDITED`** 注册进程以接收 `MEMBARRIER_CMD_GLOBAL_EXPEDITED` 内存屏障。

**`MEMBARRIER_CMD_PRIVATE_EXPEDITED`** 对属于与调用 `membarrier` 的线程相同进程的每个运行中线程执行内存屏障。

**`MEMBARRIER_CMD_REGISTER_PRIVATE_EXPEDITED`** 注册进程以接收 `MEMBARRIER_CMD_PRIVATE_EXPEDITED` 内存屏障。

**`MEMBARRIER_CMD_PRIVATE_EXPEDITED_SYNC_CORE`** 除了 `MEMBARRIER_CMD_PRIVATE_EXPEDITED` 提供的保证外，它还执行机器特定的序列化指令，确保目标 CPU 上所有可能的推测和乱序活动都被隔离。

**`MEMBARRIER_CMD_REGISTER_PRIVATE_EXPEDITED_SYNC_CORE`** 注册进程以接收 `MEMBARRIER_CMD_PRIVATE_EXPEDITED_SYNC_CORE` 内存屏障。

**`MEMBARRIER_CMD_GET_REGISTRATIONS`** 返回当前注册的接收屏障的位掩码。

以下 `cmd` 值为源兼容性而定义，但尚不支持：

**`MEMBARRIER_CMD_PRIVATE_EXPEDITED_RSEQ`**

**`MEMBARRIER_CMD_REGISTER_PRIVATE_EXPEDITED_RSEQ`**

`flags` 参数必须为 0。`cpu_id` 参数被忽略。

## 返回值

如果 `cmd` 为 `MEMBARRIER_CMD_QUERY`，返回支持的命令的位掩码。对于 `MEMBARRIER_CMD_GET_REGISTRATIONS` 命令，返回当前进程注册的位掩码。否则，成功时 `membarrier` 返回 0。出错时返回 -1，并设置 `errno` 以指示错误。

## 错误

`membarrier` 可能因以下错误而失败：

**[`EINVAL`]** `cmd` 未指定有效的命令。

**[`EINVAL`]** `flags` 不为 0。

**[`EPERM`]** 进程尝试使用 `MEMBARRIER_CMD_GLOBAL_EXPEDITED`、`MEMBARRIER_CMD_PRIVATE_EXPEDITED` 或 `MEMBARRIER_CMD_PRIVATE_EXPEDITED_SYNC_CORE`，但之前未通过相应的 `MEMBARRIER_CMD_REGISTER_*` `cmd` 注册使用。

## 标准

`membarrier` 系统调用起源于 Linux。此实现旨在与 Linux 实现源兼容。某些 `cmd` 和 `flags` 值目前不受 FreeBSD 支持。

## 历史

`membarrier` 函数引入于 FreeBSD 14.1。