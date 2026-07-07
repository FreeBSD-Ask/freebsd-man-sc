# msgget(2)

`msgget` — 获取消息队列

## 名称

`msgget`

## 库

Lb libc

## 概要

`#include <sys/msg.h>`

```c
int
msgget(key_t key, int msgflg);
```

## 描述

`msgget()` 函数返回与 `key` 关联的消息队列标识符。消息队列标识符是一个大于零的唯一整数。

当 `key` 等于 `IPC_PRIVATE`，或者 `key` 没有关联的消息队列标识符且 `msgflg` 中设置了 `IPC_CREAT` 位时，将创建一个新的消息队列。

如果创建了新的消息队列，与之关联的数据结构（`msqid_ds` 结构，参见 [msgctl(2)](msgctl.2.md)）将按如下方式初始化：

- `msg_perm.cuid` 和 `msg_perm.uid` 设置为调用进程的有效用户 ID。
- `msg_perm.gid` 和 `msg_perm.cgid` 设置为调用进程的有效组 ID。
- `msg_perm.mode` 设置为 `msgflg` 的低 9 位，这些位通过对以下常量进行按位或运算来设置：

  **`0400`** 用户读权限。

  **`0200`** 用户写权限。

  **`0040`** 组读权限。

  **`0020`** 组写权限。

  **`0004`** 其他用户读权限。

  **`0002`** 其他用户写权限。

- `msg_cbytes`、`msg_qnum`、`msg_lspid`、`msg_lrpid`、`msg_rtime` 和 `msg_stime` 设置为 0。
- `msg_qbytes` 设置为队列中字节数的系统范围最大值（`MSGMNB`）。
- `msg_ctime` 设置为当前时间。

## 返回值

成功完成时，返回一个正的消息队列标识符。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

**[`EACCES`]** `key` 已关联一个消息队列，但调用者没有权限访问它。

**[`EEXIST`]** `msgflg` 中同时设置了 `IPC_CREAT` 和 `IPC_EXCL`，且 `key` 已关联一个消息队列。

**[`ENOSPC`]** 无法创建新的消息队列，因为已达到系统中消息队列数量的限制。

**[`ENOENT`]** `msgflg` 中未设置 `IPC_CREAT`，且未找到与 `key` 关联的消息队列。

## 参见

[msgctl(2)](msgctl.2.md), [msgrcv(2)](msgrcv.2.md), [msgsnd(2)](msgsnd.2.md)

## 历史

消息队列出现于 AT&T System V UNIX 的第一个版本。
