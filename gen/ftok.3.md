# ftok.3

`ftok` — 根据路径名创建 IPC 标识符

## 名称

`ftok`

## 库

Lb libc

## 概要

`#include <sys/ipc.h>`

```c
key_t
ftok(const char *path, int id);
```

## 描述

`ftok` 函数尝试根据现有文件的 `path` 和用户可选的 `id`，创建一个适用于 [msgget(2)](../sys/msgget.2.md)、[semget(2)](../sys/semget.2.md) 和 [shmget(2)](../sys/shmget.2.md) 函数的唯一键。

指定的 `path` 必须指向一个调用进程可访问的现有文件，否则调用将失败。另外请注意，给定相同的 `id`，指向文件的链接将返回相同的键。

## 返回值

如果 `path` 不存在或调用进程无法访问它，`ftok` 函数将返回 -1。

## 参见

[msgget(2)](../sys/msgget.2.md), [semget(2)](../sys/semget.2.md), [shmget(2)](../sys/shmget.2.md)

## 历史

`ftok` 函数起源于 System V，通常由使用 System V IPC 例程的程序使用。

## 作者

Thorsten Lockert <tholo@sigmasoft.com>

## 缺陷

返回的键是根据指定 `path` 的设备次设备号和 inode，结合给定 `id` 的低 8 位计算得出的。因此，该函数完全有可能返回重复的键。
