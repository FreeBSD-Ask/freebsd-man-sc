# semget(2)

`semget` — 获取信号量 ID

## 名称

`semget`

## 库

Lb libc

## 概要

`#include <sys/sem.h>`

```c
int
semget(key_t key, int nsems, int flag);
```

## 描述

根据 `key` 和 `flag` 的值，`semget()` 返回一个新建或已存在的信号量集的标识符。key 类似于文件名：它提供了一个命名 IPC 对象的句柄。指定 key 的方式有三种：

- 可以指定 IPC_PRIVATE，在这种情况下将创建一个新的 IPC 对象。
- 可以指定一个整数常量。如果不存在与 `key` 对应的 IPC 对象，且 `flag` 中设置了 IPC_CREAT 位，则会创建一个新的 IPC 对象。
- 可以使用 [ftok(3)](../gen/ftok.3.md) 函数从路径名生成一个 key。

新创建的 IPC 对象的模式通过将这些常量按位或到 `flag` 参数中来确定：

**`0400`** 用户读权限。

**`0200`** 用户修改权限。

**`0040`** 组读权限。

**`0020`** 组修改权限。

**`0004`** 其他用户读权限。

**`0002`** 其他用户修改权限。

如果正在创建一个新的信号量集，`nsems` 用于指示该集应包含的信号量数量。否则，`nsems` 可以指定为 0。

## 返回值

若成功，`semget()` 系统调用返回信号量集的 id；否则返回 -1，并设置 `errno` 以指示错误。

## 错误

`semget()` 系统调用在以下情况下会失败：

**[`EACCES`]** 访问权限失败。

**[`EEXIST`]** 指定了 IPC_CREAT 和 IPC_EXCL，且与 `key` 对应的信号量集已存在。

**[`EINVAL`]** 请求的信号量数量超过了系统规定的每个集合的最大值。

**[`EINVAL`]** 与 `key` 对应的信号量集已存在，且包含的信号量数量少于 `nsems`。

**[`EINVAL`]** 与 `key` 对应的信号量集不存在，且 `nsems` 为 0 或负数。

**[`ENOSPC`]** 可用的信号量不足。

**[`ENOSPC`]** 内核无法分配 `struct semid_ds`。

**[`ENOENT`]** 未找到与 `key` 对应的信号量集，且未指定 IPC_CREAT。

## 参见

[semctl(2)](semctl.2.md), [semop(2)](semop.2.md), [ftok(3)](../gen/ftok.3.md)
